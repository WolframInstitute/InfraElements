# Status

## Current state

Wiki initialized. D. Joyce's edition of Euclid's *Elements* fully scraped into per-Book Markdown.

### Coverage

| Book | Definitions | Postulates | Common Notions | Propositions |
|---|---|---|---|---|
| I | 23 | 5 | 5 | 48 |
| II | 2 | — | — | 14 |
| III | 11 | — | — | 37 |
| IV | 7 | — | — | 16 |
| V | 18 | — | — | 25 |
| VI | 4* | — | — | 33* |
| VII | 22 | — | — | 39 |
| VIII | — | — | — | 27 |
| IX | — | — | — | 36 |
| X | 4 + 6 + 6 (groups I/II/III) | — | — | 115 |
| XI | 28 | — | — | 39 |
| XII | — | — | — | 18 |
| XIII | — | — | — | 18 |

*Book VI is partially present on D. Joyce's site: only 4 of the listed 11 definitions and 33 of the 37 propositions actually have pages. We scraped what exists.

### Wolfram code

- An early `Code/DiscreteEuclid*.wl` sketch (graph points/lines/distance/circles, equilateral-triangle construction, Voronoi) was **removed** during the rename to InfraElements — it duplicated the `SyntheticInfrageometry` paclet primitives the notebooks actually use.
- Infrageometric primitives now come from the `SyntheticInfrageometry` paclet (`InfraPoint`, `InfraLine`, `InfraCircle`, `InfraAngle`).
- `Code/Tools.wl` — shared utilities.

## In progress

- **Per-item notebooks (SyntheticGeometry + SyntheticInfrageometry).** Plan approved (`~/.claude/plans/0-great-now-we-glistening-crystal.md`). Reference resource MDs, dependency DAG, notebook setup, and the first example notebook source (`Wiki/Notebooks/PropI.1.md`) are written.
- **Next:** generate `Notebooks/PropI.1.nb`, smoke-test, get user acknowledgment, then walk the DAG in topological order (one commit per notebook to `WolframInstitute/InfraElements`).

## Blockers

- **Wolfram MCP kernel unresponsive** during this session — likely wedged after interrupted heavy `CompleteInfraEquilateralTriangle` / `InfraSceneViewer` calls on large graphs (triangular torus 100 vertices, rectangle mesh). The `.nb` generation step needs a healthy kernel. Recommended: restart the Wolfram MCP, then run `wolframscript -file Scripts/generate_notebooks.wls` (or the single-file pipeline) to build `Notebooks/PropI.1.nb`. Consider smaller default graphs in the notebook setup if the paclet finders are too slow at these sizes.
