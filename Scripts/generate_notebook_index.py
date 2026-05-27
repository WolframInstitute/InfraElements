#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "Wiki"
MANIFEST = WIKI / "Notebooks" / "published.json"
OUT = WIKI / "Notebooks" / "Index.md"

BOOKS = [
    ("BookI", "Book I — plane geometry, congruence, parallels, Pythagorean theorem"),
    ("BookII", "Book II — geometric algebra"),
    ("BookIII", "Book III — circles"),
    ("BookIV", "Book IV — inscribed / circumscribed figures"),
    ("BookV", "Book V — theory of proportion (Eudoxus)"),
    ("BookVI", "Book VI — similar figures"),
    ("BookVII", "Book VII — elementary number theory"),
    ("BookVIII", "Book VIII — continued proportions"),
    ("BookIX", "Book IX — number theory, primes, perfect numbers"),
    ("BookX", "Book X — incommensurables"),
    ("BookXI", "Book XI — solid geometry"),
    ("BookXII", "Book XII — method of exhaustion"),
    ("BookXIII", "Book XIII — regular solids"),
]

ITEM = re.compile(r"^- \*\*\[([^\]]+)\]\(([^)]+)\)\*\*")
ID = re.compile(r"^(Def|Post|CN|Prop)([IVXLC]+)\.(.+)$")


def notebook_name(item_id):
    m = ID.match(item_id)
    if not m:
        return None
    kind, book, rest = m.groups()
    return f"Book{book}{kind}{rest.replace('.', '')}"


def items(book_dir):
    toc = WIKI / book_dir / f"{book_dir}.md"
    for line in toc.read_text().splitlines():
        m = ITEM.match(line)
        if m:
            yield m.group(1), m.group(2)


def main():
    published = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {}
    n_pub = 0
    n_all = 0
    out = [
        "# Notebooks",
        "",
        "Every Definition / Postulate / Common Notion / Proposition of Euclid's "
        "*Elements*, rendered as a Wolfram notebook (classical `GeometricScene` + "
        "infrageometric `InfraSceneViewer`). Each row links to the item's "
        "[construction page](../Elements.md) and, once published, its cloud notebook.",
        "",
    ]
    for book_dir, title in BOOKS:
        out.append(f"## {title}")
        out.append("")
        for item_id, target in items(book_dir):
            n_all += 1
            name = notebook_name(item_id)
            construction = f"../{book_dir}/{target}"
            url = published.get(name)
            if url:
                n_pub += 1
                out.append(f"- **{item_id}** — [construction]({construction}) · [notebook]({url})")
            else:
                out.append(f"- **{item_id}** — [construction]({construction}) · notebook pending")
        out.append("")
    OUT.write_text("\n".join(out))
    print(f"Wrote {OUT.relative_to(ROOT)}: {n_pub}/{n_all} notebooks published")


if __name__ == "__main__":
    main()
