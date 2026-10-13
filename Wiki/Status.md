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
- The five completed notebooks now use the sibling `InfraGeometry` 2.7.1 checkout and its amended scene API.
- `Code/Tools.wl` — shared utilities.

## In progress

- **2026-10-13 local refresh:** only the five existing per-item notebooks, `BookIPost1`, `BookIPost3`, `BookIDef15`, `BookIDef20`, and `BookIProp1`, were updated. Each has its classical construction and evaluated graph comparisons on the Large mesh, square grid, and hexagonal tiling. Joyce's text and dependencies are preserved; the dependency notebook is untouched.
- Ten static/classical outputs render without messages, timeouts, or unresolved calls. All 57 mathematical checks pass. Viewer inputs remain runnable, with live interaction left for front-end review. [Verification and notebooks](../Code/Artifacts/EuclidCompletedReview_LLM_261013/README.md).
- The older first batch remains published in Wolfram Cloud; this local refresh has **not** been republished. The existing [manifest](Notebooks/published.json) and cloud links still describe that earlier version.
- **Learned requirements:** exact radius loci differ from separating band cycles; shortest triangle legs often overlap; odd equilateral side lengths are impossible on bipartite substrates; eager scene enumeration limits scale. [Proposed work and naming assessment](Plans/EuclidAPIRequirements_LLM.md).
- **Next:** review the circle and triangle contracts from this pilot, then resume `CNI.1`, `PostI.2`, and the proposition chain in dependency order. No new per-item notebook has been started.

## Blockers

- No execution blocker remains for the refreshed pilot. The mathematical limits above are explicit and are not patched into false Euclidean claims.

## Historical resolved blockers

- *(cleared)* The prior "Wolfram MCP kernel unresponsive" blocker no longer applies: the kernel is healthy, and notebook **generation** (Markdown→`.nb`) and **publishing** (`CopyFile` to `CloudObject`) need neither the paclet nor heavy evaluation. Three issues found and fixed en route: (1) the installed `SyntheticInfrageometry` paclet was a stale 0.12.10 lacking `InfraTriangle` — rebuilt from the dev checkout and reinstalled (`CreatePacletArchive` + `PacletInstall[…, ForceVersionInstall -> True]`); (2) `Scripts/generate_notebooks.wls` was converting the human-facing `Index.md` TOC into a notebook — now excluded; (3) `Scripts/publish_notebooks.wls` computed the repo root as `Scripts/` — fixed to `ParentDirectory[ExpandFileName[DirectoryName[…]]]`.
