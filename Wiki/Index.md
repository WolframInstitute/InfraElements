# Wiki Index

Knowledge base for **InfraElements** — an infrageometric version of Euclid's *Elements*.

The wiki mirrors D. Joyce's edition of Euclid's *Elements* (http://aleph0.clarku.edu/~djoyce/java/elements/toc.html). Each Book has its own folder with one Markdown file per Definition / Postulate / Common Notion / Proposition (statement + proof + guide), plus a Book-level TOC.

All articles are **draft** until reviewed.

## Status & Log
- [Status](Status.md) — current state
- [Activity Log](Log.md) — what happened and when

## Code

- Infrageometric primitives come from the `SyntheticInfrageometry` paclet (`InfraPoint`, `InfraLine`, `InfraCircle`, `InfraAngle`) — see [`SyntheticInfrageometry.md`](Resources/SyntheticInfrageometry.md).
- [`Code/Tools.wl`](../Code/Tools.wl) — shared utilities
- [`Scripts/scrape_djoyce.py`](../Scripts/scrape_djoyce.py) — re-runnable scraper that builds Wiki/BookI/ … Wiki/BookXIII/ from D. Joyce's HTML edition

## Plans

(none yet)

## Concepts

- [Notebook convention](Concepts/NotebookConvention.md) — the locked template every per-item notebook follows (structure, naming, primitives, generation pipeline)

## Resources

- [SyntheticGeometry](Resources/SyntheticGeometry.md) — Wolfram Language `GeometricScene` framework (classical side)
- [SyntheticInfrageometry](Resources/SyntheticInfrageometry.md) — `SyntheticInfrageometry` paclet API v0.12.9 (discrete side)
- [DependencyGraph](Resources/DependencyGraph.md) — auto-extracted DAG of 606 items / 2193 edges, 33 layers; drives topological order of per-item notebook generation

## Euclid's Elements

- [Elements](Elements.md) — the 13 books, one page per Definition / Postulate / Common Notion / Proposition (Joyce's text + proof + guide)
- [Notebooks](Notebooks/Index.md) — every item as a Wolfram notebook, by book, with cloud links
- [BookIProp1](Notebooks/BookIProp1.md) — reference notebook source (equilateral triangle)
- [DependencyGraph](Notebooks/DependencyGraph.md) — visualise + topologically sort the dependency DAG

## Tour

Interactive guided walk through the project — say **"start tour"** to begin.
