"""Scrape D. Joyce's edition of Euclid's Elements into per-Book Markdown.

Source: http://aleph0.clarku.edu/~djoyce/java/elements/toc.html

Pipeline:
  1. Download all 13 Book overview pages.
  2. Parse each overview page to extract (kind, number, href) tuples for
     definitions, postulates, common notions, and propositions.
  3. Download each unique HTML page (cached in Resources/djoyce_raw/).
  4. Parse each page into one or more `<div class="theorem">` blocks plus
     a shared Guide section.
  5. Match items to theorem blocks by header text and write one MD file per
     definition / postulate / common notion / proposition.
  6. Build a per-Book TOC MD listing all entries with statements and links.

Each MD file follows:

    # Definition I.1
    ## Statement
    ...
    ## Proof          (propositions only)
    ...
    ## Guide
    ...
    ## See also
    - [Book I TOC](BookI.md)
"""

import os
import re
import sys
import time
import urllib.request
import urllib.parse
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

BASE_URL = "http://aleph0.clarku.edu/~djoyce/java/elements/"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_ROOT / "Resources" / "djoyce_raw"
WIKI_DIR = PROJECT_ROOT / "Wiki"

BOOKS = [
    ("I", "BookI", "bookI"),
    ("II", "BookII", "bookII"),
    ("III", "BookIII", "bookIII"),
    ("IV", "BookIV", "bookIV"),
    ("V", "BookV", "bookV"),
    ("VI", "BookVI", "bookVI"),
    ("VII", "BookVII", "bookVII"),
    ("VIII", "BookVIII", "bookVIII"),
    ("IX", "BookIX", "bookIX"),
    ("X", "BookX", "bookX"),
    ("XI", "BookXI", "bookXI"),
    ("XII", "BookXII", "bookXII"),
    ("XIII", "BookXIII", "bookXIII"),
]


def fetch(url: str, dest: Path) -> str:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return dest.read_text(encoding="utf-8", errors="replace")
    print(f"  download  {url}", file=sys.stderr)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read()
    text = raw.decode("utf-8", errors="replace")
    dest.write_text(text, encoding="utf-8")
    time.sleep(0.2)
    return text


def fetch_toc() -> str:
    return fetch(BASE_URL + "toc.html", RAW_DIR / "toc.html")


def fetch_book_overview(book_url_seg: str) -> str:
    url = f"{BASE_URL}{book_url_seg}/{book_url_seg}.html"
    return fetch(url, RAW_DIR / book_url_seg / f"{book_url_seg}.html")


def parse_overview(book_roman: str, book_url_seg: str, html: str):
    """Return list of (kind, number, href, group_label) for this book's overview.

    kind is one of {"Def", "Post", "CN", "Prop"}.
    href is the relative HTML filename inside the book folder (may contain #anchor).
    group_label is None for most books, or "I"/"II"/"III" for Book X definition groups.
    """
    soup = BeautifulSoup(html, "html5lib")
    items = []
    current_group = None  # for Book X: tracks "Definitions I/II/III"

    # Walk through the document in order, watching for <h3> group headers
    # and links inside <dt>/<dd>.
    for node in soup.find_all(["h3", "a"]):
        if node.name == "h3":
            text = node.get_text(" ", strip=True)
            m = re.match(r"^Definitions\s+(I+|IV|V)$", text)
            if m:
                current_group = m.group(1)
                continue
            # Plain "Propositions" or "Definitions" resets group
            current_group = None
            continue

        # node.name == "a"
        href = node.get("href", "").strip()
        if not href:
            continue
        # Strip surrounding quotes (shouldn't happen with bs4 but safe)
        if "/" in href:
            continue
        # Drop fragment if present (Book X uses defX.I.html#1 etc.)
        href_clean = href.split("#")[0]
        if not href_clean.endswith(".html"):
            continue
        text = node.get_text(" ", strip=True)
        m = re.match(r"^(Definition|Postulate|Common\s+[nN]otion|Proposition)\s+([0-9]+)", text)
        if not m:
            continue
        kind_word, num = m.group(1), int(m.group(2))
        if kind_word.lower().startswith("common"):
            kind = "CN"
        else:
            kind = {"Definition": "Def", "Postulate": "Post",
                    "Proposition": "Prop"}[kind_word]
        items.append((kind, num, href_clean, current_group if kind == "Def" else None))
    return items


def fetch_item_page(book_url_seg: str, href: str) -> str:
    url = f"{BASE_URL}{book_url_seg}/{href}"
    return fetch(url, RAW_DIR / book_url_seg / href)


def clean_html_text(node) -> str:
    """Convert a bs4 node to Markdown-ish text, preserving italics and links."""
    parts = []
    for child in node.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif isinstance(child, Tag):
            name = child.name.lower()
            if name in ("i", "em"):
                parts.append("*" + clean_html_text(child).strip() + "*")
            elif name in ("b", "strong"):
                parts.append("**" + clean_html_text(child).strip() + "**")
            elif name == "a":
                inner = clean_html_text(child).strip()
                href = child.get("href", "")
                if href and not href.startswith("#"):
                    parts.append(f"[{inner}]({href})")
                else:
                    parts.append(inner)
            elif name == "br":
                parts.append("\n")
            elif name == "p":
                parts.append("\n\n" + clean_html_text(child).strip())
            elif name in ("ul", "ol"):
                for li in child.find_all("li", recursive=False):
                    parts.append("\n- " + clean_html_text(li).strip())
                parts.append("\n")
            elif name == "li":
                parts.append(clean_html_text(child))
            elif name == "table":
                parts.append("\n\n" + render_table(child) + "\n\n")
            elif name == "img":
                alt = child.get("alt", "")
                src = child.get("src", "")
                parts.append(f"![{alt}]({src})")
            elif name == "applet":
                img = child.find("img")
                if img is not None:
                    parts.append(f"![{img.get('alt', '')}]({img.get('src', '')})")
            elif name == "script":
                continue
            elif name in ("div", "span", "center", "font", "td", "tr", "th"):
                parts.append(clean_html_text(child))
            elif name in ("h1", "h2", "h3", "h4", "h5", "h6"):
                level = int(name[1])
                parts.append("\n\n" + "#" * (level + 2) + " " + clean_html_text(child).strip() + "\n\n")
            else:
                parts.append(clean_html_text(child))
    return "".join(parts)


def render_table(table) -> str:
    rows = []
    for tr in table.find_all("tr"):
        cells = [clean_html_text(td).strip().replace("\n", " ") for td in tr.find_all(["td", "th"])]
        rows.append(" | ".join(cells))
    return "\n".join(rows)


def collapse_whitespace(s: str) -> str:
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r" *\n *", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def rewrite_links(md: str, book_url_seg: str) -> str:
    """Rewrite intra-djoyce links to wiki-relative paths."""
    def repl(match):
        text, href = match.group(1), match.group(2)
        if href.startswith("http"):
            return match.group(0)
        # Preserve fragment so we can resolve Book X defX.I.html#3
        fragment = None
        if "#" in href:
            href, fragment = href.split("#", 1)
        if not href.endswith(".html"):
            if fragment:
                return f"[{text}]({href}#{fragment})"
            return f"[{text}]({href})"
        # Cross-book link: "../bookXI/propXI1.html"
        m = re.match(r"^\.\./([A-Za-z0-9]+)/([A-Za-z0-9.]+)\.html$", href)
        if m:
            other_seg, fname = m.group(1), m.group(2)
            wiki_name = filename_to_wiki(fname, other_seg, fragment)
            if wiki_name is None:
                return text
            book_folder = seg_to_book_folder(other_seg)
            return f"[{text}](../{book_folder}/{wiki_name}.md)"
        # Same-book link
        m = re.match(r"^([A-Za-z0-9.]+)\.html$", href)
        if m:
            fname = m.group(1)
            wiki_name = filename_to_wiki(fname, book_url_seg, fragment)
            if wiki_name is None:
                return text
            return f"[{text}]({wiki_name}.md)"
        return match.group(0)

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", repl, md)


def seg_to_book_folder(seg: str) -> str:
    for roman, folder, s in BOOKS:
        if s == seg:
            return folder
    return seg.capitalize()


def seg_to_roman(seg: str) -> str:
    for roman, folder, s in BOOKS:
        if s == seg:
            return roman
    return seg


def filename_to_wiki(fname: str, book_url_seg: str, fragment=None):
    """Convert a djoyce HTML basename (+fragment) to its wiki MD basename (no .md).

    Examples:
      defI1            -> DefI.1
      defI15           -> DefI.15 (first def on a multi-def page)
      propI1           -> PropI.1
      post1            -> PostI.1
      cn               -> CNI.1     (default to first)
      cn   + #5        -> CNI.5
      defX.I           -> DefX.I.1  (default to first def in group)
      defX.II + #3     -> DefX.II.3
    """
    roman = seg_to_roman(book_url_seg)
    # Postulate: post1, post2, ...
    m = re.match(r"^post(\d+)$", fname)
    if m:
        return f"Post{roman}.{m.group(1)}"
    # Common notions
    if fname == "cn":
        n = fragment if fragment and fragment.isdigit() else "1"
        return f"CN{roman}.{n}"
    # Book X definition groups: defX.I, defX.II, defX.III
    m = re.match(r"^def([IVX]+)\.([IVX]+)$", fname)
    if m:
        prefix_roman, group_label = m.group(1), m.group(2)
        n = fragment if fragment and fragment.isdigit() else "1"
        return f"Def{prefix_roman}.{group_label}.{n}"
    # Definition: defI1, defI15
    m = re.match(r"^def([IVX]+)(\d+)$", fname)
    if m:
        prefix_roman, num_part = m.group(1), m.group(2)
        return f"Def{prefix_roman}.{num_part}"
    # Proposition: propI1, propII3
    m = re.match(r"^prop([IVX]+)(\d+)$", fname)
    if m:
        prefix_roman, num_part = m.group(1), m.group(2)
        return f"Prop{prefix_roman}.{num_part}"
    return None


KIND_LABEL = {
    "Def": "Definition",
    "Post": "Postulate",
    "CN": "Common Notion",
    "Prop": "Proposition",
}


def _is_guide_marker(node) -> bool:
    """True if `node` is an h2/h3 introducing a Guide section.

    Two variants on djoyce:
      <a name=guide><h2>Guide</h2></a>     (most pages)
      <a name=guide><h3><img alt=Guide ...></h3></a>  (Book X pages)
    """
    if not isinstance(node, Tag):
        return False
    if node.name not in ("h2", "h3"):
        return False
    text = node.get_text(" ", strip=True).lower()
    if text == "guide":
        return True
    img = node.find("img")
    if img is not None and (img.get("alt", "").lower() == "guide"):
        return True
    return False


def _node_is_guide_anchor(node) -> bool:
    """An <a name=guide> wrapping a guide marker counts as a guide anchor."""
    if not isinstance(node, Tag):
        return False
    if node.name == "a" and node.get("name") == "guide":
        return True
    return False


def extract_theorem_blocks(html: str):
    """Walk the page body and split into per-theorem sections.

    Returns (blocks, shared_guide_md) where:
      blocks = [(header, statement_md, inline_body_md, own_guide_md), ...]
        - inline_body_md  = content inside the <div class="theorem"> after statement
                            (this is the proof body for propositions)
        - own_guide_md    = Guide content found AFTER this theorem div but BEFORE
                            the next theorem div (per-definition Guide, as on Book X)
      shared_guide_md = Guide content found after the LAST theorem div until footer.
                        Use this when own_guide_md is empty for an item.
    """
    soup = BeautifulSoup(html, "html5lib")
    body = soup.body or soup

    # Flatten body's descendants we care about, in document order.
    # We collect top-level theorem divs and inter-section content.
    theorem_divs = body.find_all("div", class_="theorem")

    blocks = []
    for i, thdiv in enumerate(theorem_divs):
        h1 = thdiv.find("h1")
        header = h1.get_text(" ", strip=True) if h1 else ""
        stmt_div = thdiv.find("div", class_="statement")
        statement_md = clean_html_text(stmt_div) if stmt_div else ""
        # Inline body inside the theorem div, after the statement div
        body_parts = []
        after_stmt = False
        for child in thdiv.children:
            if isinstance(child, Tag) and child is stmt_div:
                after_stmt = True
                continue
            if not after_stmt:
                continue
            if isinstance(child, Tag) and child.name == "h1":
                continue
            if isinstance(child, NavigableString):
                body_parts.append(str(child))
            elif isinstance(child, Tag):
                body_parts.append(clean_html_text(child))
        inline_body_md = "".join(body_parts)

        # Trailing content: walk forward from this theorem div until the next
        # theorem div or end of body / footer.
        next_thdiv = theorem_divs[i + 1] if i + 1 < len(theorem_divs) else None
        own_guide_parts = []
        in_guide = False
        cur = thdiv.next_sibling
        while cur is not None:
            if cur is next_thdiv:
                break
            if isinstance(cur, Tag):
                if cur.get("id") == "footer":
                    break
                if cur.name == "script":
                    cur = cur.next_sibling
                    continue
                # Check whether this node contains the next theorem div as a descendant
                # (shouldn't happen with djoyce's flat structure, but be safe)
                if next_thdiv is not None and isinstance(cur, Tag) and next_thdiv in cur.descendants:
                    # Walk inside this node
                    pass
                # Detect guide marker anywhere in this node
                if in_guide or _is_guide_marker(cur):
                    in_guide = True
                    if _is_guide_marker(cur):
                        # skip the heading itself
                        cur = cur.next_sibling
                        continue
                    own_guide_parts.append(clean_html_text(cur))
                else:
                    # Check if this is an anchor <a name=guide> wrapping a guide marker
                    if _node_is_guide_anchor(cur):
                        in_guide = True
                        # don't include the anchor text itself, just continue
                        cur = cur.next_sibling
                        continue
                    # Pre-Guide content (could be a 'just' div, more <p>, etc.)
                    # We treat pre-Guide trailing content as part of the proof body
                    # by appending to inline_body_md after the loop.
                    own_guide_parts.append(("__pre__", clean_html_text(cur)))
            elif isinstance(cur, NavigableString):
                if in_guide:
                    own_guide_parts.append(str(cur))
                else:
                    own_guide_parts.append(("__pre__", str(cur)))
            cur = cur.next_sibling

        # Separate pre-Guide trailing content (treat as proof continuation)
        # from the Guide content itself.
        proof_extra_pieces = [p[1] for p in own_guide_parts if isinstance(p, tuple) and p[0] == "__pre__"]
        guide_pieces = [p for p in own_guide_parts if not isinstance(p, tuple)]
        proof_extra = "".join(proof_extra_pieces)
        own_guide_md = "".join(guide_pieces)

        blocks.append((header, statement_md, inline_body_md + proof_extra, own_guide_md))

    # For shared-guide pages: when only the last block has a guide and earlier
    # blocks have empty own_guide_md, treat that last guide as "shared".
    shared_guide_md = ""
    if blocks:
        non_empty_guides = [b for b in blocks if b[3].strip()]
        if len(non_empty_guides) == 1 and blocks[-1][3].strip():
            shared_guide_md = blocks[-1][3]

    return blocks, shared_guide_md


def md_filename_for(book_roman: str, kind: str, num, group_label=None) -> str:
    """E.g., (I, Def, 1) -> 'DefI.1', (X, Def, 1, 'I') -> 'DefX.I.1'."""
    if group_label:
        return f"{kind}{book_roman}.{group_label}.{num}"
    return f"{kind}{book_roman}.{num}"


def display_label(book_roman: str, kind: str, num, group_label=None) -> str:
    """E.g., (I, Def, 1) -> 'I.1', (X, Def, 1, 'I') -> 'X.I.1'."""
    if group_label:
        return f"{book_roman}.{group_label}.{num}"
    return f"{book_roman}.{num}"


def write_item_md(book_folder: str, book_roman: str, kind: str, num,
                  statement_md: str, proof_md: str, guide_md: str,
                  source_url: str, shared_with=None, group_label=None):
    """Write a single MD file for one definition / postulate / CN / proposition."""
    title = f"{KIND_LABEL[kind]} {display_label(book_roman, kind, num, group_label)}"
    fname = md_filename_for(book_roman, kind, num, group_label) + ".md"
    out = WIKI_DIR / book_folder / fname

    parts = [f"# {title}", ""]
    parts.append("## Statement")
    parts.append("")
    parts.append(collapse_whitespace(statement_md))
    parts.append("")
    if proof_md.strip():
        parts.append("## Proof")
        parts.append("")
        parts.append(collapse_whitespace(proof_md))
        parts.append("")
    if guide_md.strip():
        parts.append("## Guide")
        parts.append("")
        if shared_with:
            parts.append(f"*Note: in D. Joyce's edition the Guide is shared with {shared_with}.*")
            parts.append("")
        parts.append(collapse_whitespace(guide_md))
        parts.append("")
    parts.append("## See also")
    parts.append("")
    parts.append(f"- [{book_folder} TOC]({book_folder}.md)")
    parts.append(f"- [Source HTML]({source_url})")
    parts.append("")

    text = "\n".join(parts)
    # Link rewriting happens in a per-book post-pass (needs book_url_seg).
    out.write_text(text, encoding="utf-8")


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    WIKI_DIR.mkdir(parents=True, exist_ok=True)

    fetch_toc()

    all_book_items = {}  # book_roman -> list of (kind, num, href)
    for book_roman, book_folder, book_url_seg in BOOKS:
        print(f"=== Book {book_roman} ===", file=sys.stderr)
        html = fetch_book_overview(book_url_seg)
        items = parse_overview(book_roman, book_url_seg, html)
        all_book_items[book_roman] = items
        print(f"  {len(items)} items in overview", file=sys.stderr)

    # Step 2: download each unique href page per book
    for book_roman, book_folder, book_url_seg in BOOKS:
        items = all_book_items[book_roman]
        unique_hrefs = []
        seen = set()
        for kind, num, href, group_label in items:
            if href not in seen:
                seen.add(href)
                unique_hrefs.append(href)
        for href in unique_hrefs:
            fetch_item_page(book_url_seg, href)

    # Step 3: parse each page and write MDs
    for book_roman, book_folder, book_url_seg in BOOKS:
        items = all_book_items[book_roman]
        # Group items by href
        by_href = {}
        for kind, num, href, group_label in items:
            by_href.setdefault(href, []).append((kind, num, group_label))

        # Build TOC entries (kind, num, group_label, statement) for this book
        toc_entries = []

        for href, members in by_href.items():
            page = (RAW_DIR / book_url_seg / href).read_text(encoding="utf-8", errors="replace")
            blocks, shared_guide_md = extract_theorem_blocks(page)
            source_url = f"{BASE_URL}{book_url_seg}/{href}"

            if len(members) == 1 and len(blocks) == 1:
                (kind, num, group_label) = members[0]
                header, statement_md, body_md, own_guide_md = blocks[0]
                guide_md = own_guide_md or shared_guide_md
                write_item_md(book_folder, book_roman, kind, num,
                              statement_md, body_md if kind == "Prop" else "",
                              guide_md, source_url, group_label=group_label)
                toc_entries.append((kind, num, group_label, collapse_whitespace(statement_md)))
                continue

            # Multi-item, single-block case: split numbered list inside statement.
            if len(blocks) == 1 and len(members) > 1:
                header, statement_md, body_md, own_guide_md = blocks[0]
                guide_for_all = own_guide_md or shared_guide_md
                soup = BeautifulSoup(page, "html5lib")
                thdiv = soup.find("div", class_="theorem")
                if thdiv is None:
                    continue
                stmt = thdiv.find("div", class_="statement")
                parts = []
                if stmt is not None:
                    for p in stmt.find_all("p"):
                        txt = clean_html_text(p).strip()
                        m = re.match(r"^(\d+)\.\s*(.*)$", txt, re.S)
                        if m:
                            parts.append((int(m.group(1)), m.group(2)))
                members_sorted = sorted(members, key=lambda kn: kn[1])
                shared_label = ", ".join(
                    f"{KIND_LABEL[k]} {display_label(book_roman, k, n, g)}"
                    for k, n, g in members_sorted)
                for (kind, num, group_label) in members_sorted:
                    stmt_text = next((s for (n, s) in parts if n == num), "")
                    if not stmt_text and parts:
                        stmt_text = parts[0][1]
                    write_item_md(book_folder, book_roman, kind, num,
                                  stmt_text, "", guide_for_all, source_url,
                                  shared_with=shared_label, group_label=group_label)
                    toc_entries.append((kind, num, group_label, collapse_whitespace(stmt_text)))
                continue

            # Multi-block case: page has multiple <div class="theorem">.
            members_sorted = sorted(members, key=lambda kn: kn[1])
            block_index = {}
            for header, statement_md, body_md, own_guide_md in blocks:
                m = re.match(r"^(Definition|Postulate|Common Notion|Proposition)\s+(\d+)", header)
                if m:
                    block_index[int(m.group(2))] = (statement_md, body_md, own_guide_md)
            shared_label = ", ".join(
                f"{KIND_LABEL[k]} {display_label(book_roman, k, n, g)}"
                for k, n, g in members_sorted)
            for (kind, num, group_label) in members_sorted:
                trio = block_index.get(num)
                if trio is None:
                    continue
                statement_md, body_md, own_guide_md = trio
                guide_md = own_guide_md or shared_guide_md
                # When a per-block guide exists, there's no "shared with" caveat.
                shared_note = None
                if not own_guide_md and shared_guide_md and len(members_sorted) > 1:
                    shared_note = shared_label
                write_item_md(book_folder, book_roman, kind, num,
                              statement_md,
                              body_md if kind == "Prop" else "",
                              guide_md, source_url,
                              shared_with=shared_note,
                              group_label=group_label)
                toc_entries.append((kind, num, group_label, collapse_whitespace(statement_md)))

        # Rewrite internal links in every MD file for this book
        for md_path in (WIKI_DIR / book_folder).glob("*.md"):
            if md_path.name == f"{book_folder}.md":
                continue
            content = md_path.read_text(encoding="utf-8")
            content = rewrite_links(content, book_url_seg)
            md_path.write_text(content, encoding="utf-8")

        # Write per-book TOC
        write_book_toc(book_folder, book_roman, toc_entries)


def write_book_toc(book_folder: str, book_roman: str, entries):
    toc_path = WIKI_DIR / book_folder / f"{book_folder}.md"
    # Sort by kind order, then group_label, then number
    kind_order = {"Def": 0, "Post": 1, "CN": 2, "Prop": 3}
    group_order = {None: 0, "I": 1, "II": 2, "III": 3, "IV": 4}
    entries_sorted = sorted(
        entries,
        key=lambda e: (kind_order.get(e[0], 99), group_order.get(e[2], 99),
                       e[1] if isinstance(e[1], int) else 0))

    lines = []
    lines.append(f"# Book {book_roman}")
    lines.append("")
    lines.append(f"D. Joyce's edition: <{BASE_URL}book{book_roman}/book{book_roman}.html>")
    lines.append("")

    # by (kind, group_label)
    sections = {}
    for kind, num, group_label, stmt in entries_sorted:
        sections.setdefault((kind, group_label), []).append((num, stmt))

    section_titles = [
        ("Def", None, "Definitions"),
        ("Def", "I", "Definitions I"),
        ("Def", "II", "Definitions II"),
        ("Def", "III", "Definitions III"),
        ("Post", None, "Postulates"),
        ("CN", None, "Common Notions"),
        ("Prop", None, "Propositions"),
    ]

    for kind, group_label, title in section_titles:
        key = (kind, group_label)
        if key not in sections:
            continue
        lines.append(f"## {title}")
        lines.append("")
        for num, stmt in sections[key]:
            fname = md_filename_for(book_roman, kind, num, group_label)
            label = display_label(book_roman, kind, num, group_label)
            stmt_short = stmt.replace("\n", " ").strip()
            lines.append(f"- **[{kind}{label}]({fname}.md)** — {stmt_short}")
        lines.append("")

    lines.append("## See also")
    lines.append("")
    lines.append("- [Wiki Index](../Index.md)")
    lines.append("")

    toc_path.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
    print("Done.", file=sys.stderr)
