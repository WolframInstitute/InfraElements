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

- **Per-item notebooks (SyntheticGeometry + SyntheticInfrageometry).** First batch generated, smoke-tested, and **deployed to Wolfram Cloud** (public): `BookIPost1`, `BookIPost3`, `BookIDef15`, `BookIDef20` (the four geometric foundations of I.1), alongside the reference `BookIProp1` and the meta `DependencyGraph`. Cloud URLs at `https://www.wolframcloud.com/obj/hajek_pavel/InfraElements/<name>.nb`; manifest in [`Wiki/Notebooks/published.json`](Notebooks/published.json); index regenerated ([`Wiki/Notebooks/Index.md`](Notebooks/Index.md), 5/614 per-item notebooks published).
- Both the classical `GeometricScene`/`RandomInstance` and the infrageometric `InfraScene`/`FindInfraScene` sides of all four were verified to resolve on a Euclidean mesh before deploy (no workarounds).
- **Next:** `CNI.1` (deferred — a pure equality axiom with no construction; decide statement-only vs. an infra equal-magnitude illustration), then `PostI.2` and the proposition chain `PropI.2`, `PropI.3`, … in DAG topological order.

## Blockers

- *(cleared)* The prior "Wolfram MCP kernel unresponsive" blocker no longer applies: the kernel is healthy, and notebook **generation** (Markdown→`.nb`) and **publishing** (`CopyFile` to `CloudObject`) need neither the paclet nor heavy evaluation. Three issues found and fixed en route: (1) the installed `SyntheticInfrageometry` paclet was a stale 0.12.10 lacking `InfraTriangle` — rebuilt from the dev checkout and reinstalled (`CreatePacletArchive` + `PacletInstall[…, ForceVersionInstall -> True]`); (2) `Scripts/generate_notebooks.wls` was converting the human-facing `Index.md` TOC into a notebook — now excluded; (3) `Scripts/publish_notebooks.wls` computed the repo root as `Scripts/` — fixed to `ParentDirectory[ExpandFileName[DirectoryName[…]]]`.
