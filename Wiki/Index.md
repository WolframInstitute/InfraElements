# Wiki Index

Knowledge base for **InfraElements** — an infrageometric version of Euclid's *Elements*.

The wiki mirrors D. Joyce's edition of Euclid's *Elements* (http://aleph0.clarku.edu/~djoyce/java/elements/toc.html). Each Book has its own folder with one Markdown file per Definition / Postulate / Common Notion / Proposition (statement + proof + guide), plus a Book-level TOC.

All articles are **draft** until reviewed.

## Status & Log
- [Status](Status.md) — current state
- [Activity Log](Log.md) — what happened and when

## Code

- Infrageometric primitives come from `InfraGeometry` — see the [current Elements subset](Resources/InfraGeometry_LLM.md).
- [`Code/Tools.wl`](../Code/Tools.wl) — shared utilities
- [`Scripts/scrape_djoyce.py`](../Scripts/scrape_djoyce.py) — re-runnable scraper that builds Wiki/BookI/ … Wiki/BookXIII/ from D. Joyce's HTML edition

## Plans

- [Euclid API requirements](Plans/EuclidAPIRequirements_LLM.md) — naming, circles, simple triangle boundaries, and scene sampling, learned from the five completed notebooks.

## Concepts

- [Notebook convention](Concepts/NotebookConvention.md) — paired scenes on three Large substrates, explicit failures, and the verified selected-subset build

## Resources

- [SyntheticGeometry](Resources/SyntheticGeometry.md) — Wolfram Language `GeometricScene` framework (classical side)
- [InfraGeometry](Resources/InfraGeometry_LLM.md) — current 2.7.1 API used by the completed pilot
- [SyntheticInfrageometry](Resources/SyntheticInfrageometry.md) — historical v0.12.9 reference
- [DependencyGraph](Resources/DependencyGraph.md) — auto-extracted DAG of 606 items / 2193 edges, 33 layers; drives topological order of per-item notebook generation

## Euclid's Elements

- [Elements](Elements.md) — the 13 books, one page per Definition / Postulate / Common Notion / Proposition (Joyce's text + proof + guide)
- [Notebooks](Notebooks/Index.md) — every item as a Wolfram notebook, by book, with cloud links
- [BookIProp1](Notebooks/BookIProp1.md) — reference notebook source (equilateral triangle)
- [DependencyGraph](Notebooks/DependencyGraph.md) — visualise + topologically sort the dependency DAG
- [Completed notebook review](../Code/Artifacts/EuclidCompletedReview_LLM_261013/README.md) — five refreshed local notebooks, figures, and verification

## Tour

Interactive guided walk through the project — say **"start tour"** to begin.
