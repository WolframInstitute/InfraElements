# InfraElements

## Related repos

This repo vendors no git submodules.
The sibling repos are **not** cloned into this tree and must never be — a vendored copy
goes stale and then two versions of the same paclet disagree. Read them in place at the
paths below.

| Paclet | Repo, relative to this one | Paclet dir inside it |
|---|---|---|
| Infrageometry | `../../SubProjectsMain/Infrageometry/` | `Infrageometry/Infrageometry/` |
| SyntheticInfrageometry | `../../SubProjectsMain/SyntheticInfrageometry/` | `SyntheticInfrageometry/SyntheticInfrageometry/` |
| InfraAnalysis | `../../SubProjectsOther/InfraAnalysis/` | `InfraAnalysis/InfraAnalysis/` |
| InfraCausality | `../../SubProjectsOther/InfraCausality/` | `InfraCausality/InfraCausality/` |
| InfraGaugeTheory | `../../SubProjectsOther/InfraGaugeTheory/` | `InfraGaugeTheory/` |
| InfraUniverseRegistry | `../InfraUniverseRegistry/` | — *scripts only, no paclet* |

To use another paclet, prefer the **installed** copy — all of them are in
`~/Library/Wolfram/Paclets/Repository/`, so a plain load works with no path at all:

```wolfram
Needs["WolframInstitute`Infrageometry`"]
```

Reach for a dev checkout only when you need changes that are not published yet, and then
point at the sibling path rather than copying it here:

```wolfram
PacletDirectoryLoad @ FileNameJoin[ { $repoRoot, "..", "..", "SubProjectsMain", "Infrageometry", "Infrageometry" } ]
```

An infrageometric version of Euclid's *Elements*.

## Source attribution (authoritative)

The wiki under `Wiki/Book*/` is built **verbatim** from D. Joyce's HTML edition of Euclid's *Elements*:

> **D. Joyce, *Euclid's Elements*** — http://aleph0.clarku.edu/~djoyce/java/elements/toc.html

Statements / proofs / guides come from this source. The scraper [`Scripts/scrape_djoyce.py`](Scripts/scrape_djoyce.py) is the rebuild tool; raw HTML is cached in `Resources/djoyce_raw/`.

## Reference resources (read these before writing notebooks)

- [`Wiki/Resources/SyntheticGeometry.md`](Wiki/Resources/SyntheticGeometry.md) — the built-in Wolfram `GeometricScene` framework (classical-side API). Every per-item notebook uses `GeometricScene` + `GeometricStep` for the classical illustration.
- [`Wiki/Resources/SyntheticInfrageometry.md`](Wiki/Resources/SyntheticInfrageometry.md) — the `SyntheticInfrageometry` paclet API (discrete-side, v0.12.9). Notebooks use `InfraScene` + the interactive `InfraSceneViewer[scene, graph]` as the primary visualisation, with a secondary static `InfraSceneHighlight` cell.
- [`Wiki/Resources/DependencyGraph.md`](Wiki/Resources/DependencyGraph.md) — the auto-extracted dependency DAG over Definitions / Postulates / Common Notions / Propositions. Drives the topological order of notebook generation.
- [`Wiki/Concepts/NotebookConvention.md`](Wiki/Concepts/NotebookConvention.md) — **the locked template every per-item notebook follows.** Read this before creating any notebook. Covers file/symbol naming, the markdown section structure, the allowed infrageometric primitives (`InfraPoint`, `InfraCircle`, `InfraLine`, `InfraAngle` only), the Euclidean-mesh graph, and the generation pipeline. The reference implementation is [`Wiki/Notebooks/BookIProp1.md`](Wiki/Notebooks/BookIProp1.md).

Generate notebooks with `wolframscript -file Scripts/generate_notebooks.wls` (the pipeline — heading shift, definition-based initialization cells, preserved code formatting — is baked into that script).

## Project goals

1. Understand the mathematical structure of an infrageometric Euclid's Elements
2. Develop computational tools in Wolfram Language
3. Visualize and verify results computationally

## Code structure

- `Code/Tools.wl` — shared general utilities
- Infrageometric primitives come from the `SyntheticInfrageometry` paclet (`InfraPoint`, `InfraLine`, `InfraCircle`, `InfraAngle`); notebooks load the paclet rather than a local core file.

Additional topic scopes follow the same pattern:
- `Code/<Topic>.wl` — core functions
- `Code/<Topic>Visualization.wl` — visualization
- `Code/<Topic>Experiment.wl` — experiments
- `Code/<Topic>Test.wl` — tests (VerificationTest + TestReport)

Notebooks: `<Topic>1.nb` per topic, `Test1.nb` for tests.

## Resources

`Resources/` — reference papers and community notebooks, named as `Author_Year_Title.pdf` or `.nb`

## MCP usage

- **Official Wolfram MCP** — primary server for all evaluation, notebook
  generation (Markdown pipeline), and computation.
- **arxiv-latex-mcp** — preferred for reading papers. LaTeX source gives
  exact equations and definitions for Wolfram implementations. Fall back to
  arxiv MCP PDF reading only if LaTeX source is unavailable.
- **Unofficial Wolfram MCP** (if installed) — use for LSP features only:
  `hover_info` (type signatures), `find_definition`, `find_references`,
  `get_diagnostics` (errors/warnings), `document_symbols` (file outline).
  Do not use its notebook-manipulation tools; use the Markdown pipeline instead.

## Loading code

```wolfram
dir = DirectoryName @ $InputFileName;  (* in .wl scripts *)
(* or *)
dir = NotebookDirectory[];             (* in notebooks *)

Get @ FileNameJoin[{dir, "Code", "Tools.wl"}]
Needs[ "WolframInstitute`SyntheticInfrageometry`" ]
```

## Knowledge Base (Wiki)

`Wiki/` is a plain-markdown knowledge base. It mirrors D. Joyce's edition of Euclid's *Elements* (http://aleph0.clarku.edu/~djoyce/java/elements/toc.html).

### Structure

```
Wiki/
  Index.md, Status.md, Log.md
  Concepts/, Resources/, Plans/, Notebooks/
  BookI/ ... BookXIII/
    BookI.md              — TOC: list of defs/postulates/CNs/propositions with statements + links
    DefI.1.md, DefI.2.md  — one file per Definition
    PostI.1.md            — one file per Postulate (Book I only)
    CNI.1.md              — one file per Common Notion (Book I only)
    PropI.1.md, PropI.2.md — one file per Proposition
```

Each Def/Post/CN/Prop file follows:

```markdown
# Proposition I.1

## Statement
...verbatim from D. Joyce...

## Proof
...verbatim from D. Joyce...

## Guide
...verbatim from D. Joyce...

## See also
- [Book I TOC](BookI.md)
- ...cross-links to related propositions...
```

### Maintenance rules

After every substantial step, the LLM:
1. Creates or updates relevant articles in `Wiki/`
2. Updates `Wiki/Index.md`
3. Updates `Wiki/Status.md`
4. Appends to `Wiki/Log.md`
5. Adds cross-links in `See also` sections

### Resources

`Wiki/Resources/` holds summaries with download URLs and a `## Recover` section.
`Resources/` (gitignored) holds actual binary files.
Rebuild via `Scripts/recover_resources.sh`.

### Guided Tour

Say "start tour" for an interactive walk through the project.

