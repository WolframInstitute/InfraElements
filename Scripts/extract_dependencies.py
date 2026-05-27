"""Build the DAG of references between Definitions, Postulates, Common Notions
and Propositions of Euclid's Elements as scraped from D. Joyce's edition.

The authoritative source of edges is the markdown links already inside each
per-item MD's `## Proof` section (and the `## Statement` section for
definitions, which sometimes cite earlier definitions). These were preserved
verbatim by `Scripts/scrape_djoyce.py`.

Emits two artifacts:
  Wiki/Resources/DependencyGraph.m     -- Wolfram Association, `Get`-loadable
  Wiki/Resources/DependencyGraph.json  -- same data, JSON-encoded

And prints sanity stats (item count, edge count, layered topo sort, top-10
most-depended-on items). Exits non-zero if:
  - a dependency id resolves to no existing MD file
  - the graph has a cycle
"""

import json
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = PROJECT_ROOT / "Wiki"
RESOURCES_OUT = WIKI_DIR / "Resources"
BOOK_FOLDERS = [
    "BookI", "BookII", "BookIII", "BookIV", "BookV", "BookVI",
    "BookVII", "BookVIII", "BookIX", "BookX", "BookXI", "BookXII", "BookXIII",
]

# An item id is one of: DefI.1, DefX.II.3, PostI.1, CNI.1, PropI.1, PropXIII.18.
ITEM_RE = re.compile(r"^(Def|Post|CN|Prop)([IVX]+)(?:\.([IVX]+))?\.(\d+)$")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")


def parse_item_id(name: str):
    m = ITEM_RE.match(name)
    if not m:
        return None
    kind, book, group, num = m.group(1), m.group(2), m.group(3), int(m.group(4))
    return {"Kind": kind, "Book": book, "Group": group, "Num": num}


def file_to_item_id(file_path: Path) -> str:
    """Wiki/BookI/PropI.1.md -> PropI.1"""
    return file_path.stem


def split_sections(md_text: str) -> dict:
    """Return dict like {"Statement": "...", "Proof": "...", "Guide": "..."}."""
    sections = {}
    current = None
    buf = []
    for line in md_text.splitlines():
        m = SECTION_RE.match(line)
        if m:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = m.group(1).strip()
            buf = []
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def resolve_link_target(href: str, source_file: Path) -> str | None:
    """Convert an `[label](Foo.md)` href into a canonical item id, or None.

    Handles same-book (Foo.md) and cross-book (../BookIII/Foo.md) forms.
    """
    if href.startswith("http") or href.startswith("#"):
        return None
    href = href.split("#")[0]
    if not href.endswith(".md"):
        return None
    target = (source_file.parent / href).resolve()
    # Item id is the file stem
    if not target.exists():
        return None
    item_id = target.stem
    if parse_item_id(item_id) is None:
        return None
    return item_id


def extract_links_from(md_text: str, source_file: Path) -> list:
    targets = []
    for label, href in LINK_RE.findall(md_text):
        resolved = resolve_link_target(href, source_file)
        if resolved is None:
            continue
        targets.append(resolved)
    return targets


def first_statement_line(stmt_md: str) -> str:
    """Compress the statement to a single line for the index / TOC."""
    txt = re.sub(r"\s+", " ", stmt_md or "").strip()
    return txt


def topo_layers(adj_out: dict, nodes: list) -> list:
    """Return list of layers (lists of node ids), Layer 0 = sources.

    A source is a node with no outgoing dependencies (the leaves of the
    "depends-on" graph). We treat dependencies as edges going *up* in the
    layering: an item with no dependencies sits at Layer 0; an item that
    depends only on Layer 0 sits at Layer 1; etc.
    """
    depth = {}
    pending = deque()
    for n in nodes:
        if not adj_out.get(n):
            depth[n] = 0
            pending.append(n)

    inv_in = defaultdict(list)
    for u, deps in adj_out.items():
        for v in deps:
            inv_in[v].append(u)

    while pending:
        n = pending.popleft()
        for parent in inv_in.get(n, []):
            deps = adj_out.get(parent, [])
            if not deps:
                continue
            if all(d in depth for d in deps):
                d = max(depth[x] for x in deps) + 1
                if parent not in depth or depth[parent] != d:
                    depth[parent] = d
                    pending.append(parent)

    max_d = max(depth.values()) if depth else -1
    layers = [[] for _ in range(max_d + 1)]
    for n in nodes:
        if n in depth:
            layers[depth[n]].append(n)
    for layer in layers:
        layer.sort()
    return layers, depth


def detect_cycle(adj_out: dict, nodes: list) -> list | None:
    """Return a cycle (list of node ids) if one exists, else None."""
    WHITE, GREY, BLACK = 0, 1, 2
    color = {n: WHITE for n in nodes}
    stack = []
    found = []

    def dfs(u):
        color[u] = GREY
        stack.append(u)
        for v in adj_out.get(u, []):
            if v not in color:
                continue
            if color[v] == GREY:
                idx = stack.index(v)
                found.extend(stack[idx:] + [v])
                return True
            if color[v] == WHITE:
                if dfs(v):
                    return True
        color[u] = BLACK
        stack.pop()
        return False

    for n in nodes:
        if color[n] == WHITE:
            if dfs(n):
                return found
    return None


def wolfram_serialize(value) -> str:
    if isinstance(value, dict):
        body = ", ".join(
            f'"{k}" -> {wolfram_serialize(v)}' for k, v in value.items()
        )
        return f"<| {body} |>"
    if isinstance(value, list):
        body = ", ".join(wolfram_serialize(v) for v in value)
        return f"{{ {body} }}"
    if isinstance(value, bool):
        return "True" if value else "False"
    if value is None:
        return "Null"
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        return f'"{escaped}"'
    raise TypeError(f"Cannot serialize {type(value)}")


def main():
    md_files = []
    for book in BOOK_FOLDERS:
        book_dir = WIKI_DIR / book
        if not book_dir.is_dir():
            continue
        for f in sorted(book_dir.glob("*.md")):
            if f.name == f"{book}.md":
                continue
            md_files.append(f)

    items = {}  # item_id -> info dict
    for f in md_files:
        item_id = file_to_item_id(f)
        info = parse_item_id(item_id)
        if info is None:
            continue
        text = f.read_text(encoding="utf-8")
        sections = split_sections(text)
        stmt = first_statement_line(sections.get("Statement", ""))
        # Truncate to keep the .m file readable
        if len(stmt) > 400:
            stmt = stmt[:397] + "..."
        deps = []
        # Look in Proof and Statement; Statement for cross-references in defs,
        # Proof for the marginal references on propositions.
        for sec_name in ("Statement", "Proof"):
            if sec_name in sections:
                for tgt in extract_links_from(sections[sec_name], f):
                    if tgt != item_id and tgt not in deps:
                        deps.append(tgt)
        items[item_id] = {
            "Kind": info["Kind"],
            "Book": info["Book"],
            "Group": info["Group"],
            "Num": info["Num"],
            "File": str(f.relative_to(PROJECT_ROOT)),
            "Statement": stmt,
            "Dependencies": deps,
        }

    # Validate that every dep id resolves
    unknown = set()
    for item_id, info in items.items():
        for d in info["Dependencies"]:
            if d not in items:
                unknown.add((item_id, d))
    if unknown:
        print("ERROR: dependency targets not found:", file=sys.stderr)
        for src, dst in sorted(unknown):
            print(f"  {src} -> {dst}", file=sys.stderr)
        sys.exit(1)

    # Compute UsedIn (inverse of Dependencies)
    used_in = defaultdict(list)
    for item_id, info in items.items():
        for d in info["Dependencies"]:
            used_in[d].append(item_id)
    for item_id in items:
        items[item_id]["UsedIn"] = sorted(used_in.get(item_id, []))

    # Build adjacency for cycle / topo
    adj_out = {k: list(v["Dependencies"]) for k, v in items.items()}
    nodes = list(items.keys())
    cycle = detect_cycle(adj_out, nodes)
    if cycle is not None:
        print("ERROR: dependency graph contains a cycle:", file=sys.stderr)
        print(" -> ".join(cycle), file=sys.stderr)
        sys.exit(1)

    layers, depth = topo_layers(adj_out, nodes)

    # Emit .m
    RESOURCES_OUT.mkdir(parents=True, exist_ok=True)
    m_path = RESOURCES_OUT / "DependencyGraph.m"
    m_path.write_text(
        "(* Auto-generated by Scripts/extract_dependencies.py. Do not edit by hand. *)\n"
        "(* Source of edges: markdown links inside ## Proof / ## Statement sections of *)\n"
        "(* per-item MDs under Wiki/Book*/, themselves scraped from D. Joyce's edition: *)\n"
        "(* http://aleph0.clarku.edu/~djoyce/java/elements/toc.html *)\n\n"
        + wolfram_serialize(items)
        + "\n",
        encoding="utf-8",
    )

    json_path = RESOURCES_OUT / "DependencyGraph.json"
    json_path.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # Stats
    n_items = len(items)
    n_edges = sum(len(v["Dependencies"]) for v in items.values())
    in_degree = Counter()
    for v in items.values():
        for d in v["Dependencies"]:
            in_degree[d] += 1
    top10 = in_degree.most_common(10)
    print(f"items:        {n_items}")
    print(f"edges:        {n_edges}")
    print(f"layers:       {len(layers)} (max depth = {len(layers) - 1})")
    print(f"sources (Layer 0): {len(layers[0]) if layers else 0}")
    if layers:
        print(f"sinks (Layer {len(layers) - 1}): {len(layers[-1])}")
    print()
    print("top-10 most-depended-on:")
    for item_id, count in top10:
        kind = items[item_id]["Kind"]
        stmt = items[item_id]["Statement"]
        short = stmt if len(stmt) <= 80 else stmt[:77] + "..."
        print(f"  {item_id:14s} (in={count:3d}, kind={kind:4s})  {short}")

    # Items with no incoming edges that are NOT in the source layer
    # (sanity: these might be unreferenced — useful to flag)
    unreferenced_props = [
        n for n in nodes
        if items[n]["Kind"] == "Prop" and in_degree.get(n, 0) == 0
    ]
    print()
    print(f"propositions never referenced by another item: {len(unreferenced_props)}")
    if unreferenced_props[:5]:
        print(f"  e.g. {', '.join(unreferenced_props[:5])}")

    # Sanity check on PropI.1
    pi1 = items.get("PropI.1")
    if pi1 is not None:
        expected = {"PostI.1", "PostI.3", "DefI.15", "DefI.20", "CNI.1"}
        found = set(pi1["Dependencies"])
        missing = expected - found
        extra = found - expected
        print()
        print(f"PropI.1 dependencies: {sorted(found)}")
        if missing:
            print(f"  expected but missing: {sorted(missing)}", file=sys.stderr)
        if extra:
            print(f"  extra (not in expected set): {sorted(extra)}")


if __name__ == "__main__":
    main()
