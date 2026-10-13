# DependencyGraph

Auto-extracted directed dependency graph over the 606 Definitions, Postulates, Common Notions, and Propositions in D. Joyce's edition of Euclid's *Elements*.

Source of edges: every clickable Markdown link inside the `## Statement` and `## Proof` sections of the per-item MDs under [`Wiki/Book*/`](../). Those links are the marginal references that D. Joyce attached to each proposition's proof, faithfully preserved by [`Scripts/scrape_djoyce.py`](../../Scripts/scrape_djoyce.py).

## Files

| File | Format | Use |
|---|---|---|
| [`DependencyGraph.m`](DependencyGraph.m) | Wolfram `Association` | Load in any notebook with `Get[ "…/DependencyGraph.m" ]`. |
| [`DependencyGraph.json`](DependencyGraph.json) | JSON | For non-Wolfram consumers. |

Both files are **auto-generated**; never edit them by hand. Rebuild:

```bash
.venv/bin/python Scripts/extract_dependencies.py
```

## Schema

Each top-level entry is keyed by the canonical item id (`DefI.1`, `PostI.3`, `CNI.1`, `PropI.1`, `DefX.II.3`, `PropXIII.18`, …) and maps to an `Association` of the form

```wolfram
<|
  "Kind"         -> "Prop",                (* "Def" | "Post" | "CN" | "Prop" *)
  "Book"         -> "I",                   (* Roman numeral *)
  "Group"        -> Null,                  (* "I"/"II"/"III" for Book X def groups, Null otherwise *)
  "Num"          -> 1,
  "File"         -> "Wiki/BookI/PropI.1.md",
  "Statement"    -> "To construct an equilateral triangle on a given finite straight line.",
  "Dependencies" -> { "PostI.3", "PostI.1", "DefI.15", "CNI.1", "DefI.20" },
  "UsedIn"       -> { "PropI.10", "PropI.11", "PropI.2", "PropI.9", "PropXI.22", "PropXIII.13" }
|>
```

- `"Dependencies"`: items this one **directly cites in its statement or proof**. These edges drive the topological order in which per-item notebooks are generated.
- `"UsedIn"`: inverse of `Dependencies` (computed automatically; not parsed from Guide narrative, which is unreliable).

## Stats at the time of generation

```
items:        606
edges:        2193
layers:       33 (max depth = 32)
sources:      147   (items with no dependencies — definitions, postulates, common notions, and Layer-0 definitions)
sinks:        1     (the deepest proposition in the DAG)
```

Top-10 most-depended-on items (highest in-degree):

| Item | Incoming | Statement (truncated) |
|---|---|---|
| `PropX.11` | 58 | *If four magnitudes are proportional, …* |
| `PropV.11` | 50 | *Ratios which are the same with the same ratio …* |
| `PropVI.1` | 50 | *Triangles and parallelograms which are under the same height …* |
| `PropI.3`  | 47 | *To cut off from the greater of two given unequal straight lines …* |
| `PropI.4`  | 42 | *If two triangles have two sides equal …* |
| `PropI.31` | 40 | *To draw a straight line through a given point parallel …* |
| `CNI.1`    | 35 | *Things which equal the same thing also equal one another.* |
| `PropX.13` | 33 | *If two magnitudes are commensurable, …* |
| `PropI.11` | 32 | *To draw a straight line at right angles …* |
| `PropX.6`  | 31 | *If two magnitudes have to one another the ratio …* |

## Known limitations

- **D. Joyce's marginal references are not always exhaustive.** A proof may rely on an item without an explicit marginal link. The extracted graph is therefore a *lower bound* on actual mathematical dependencies. Manual patches (added during notebook generation in Phase E) should land in a separate `Wiki/Resources/DependencyGraphPatches.m` file rather than editing the generated `.m` / `.json`.
- **134 propositions have no incoming edges** in the current DAG (no later proposition cites them). They are valid leaves; many are concluding lemmas or culminating theorems (e.g. `PropII.10`, …, `PropII.14`). Don't mistake them for orphans.
- **Book VI is partially covered on the source site.** Only 4 of the 11 declared definitions and 33 of the 37 declared propositions actually exist as HTML pages. The DAG includes only what was scraped.
- **Definitions occasionally cite definitions in their `## Statement`.** The extractor pulls links from both `## Statement` and `## Proof` for this reason.

## Visualisation

The notebook source [`Wiki/Notebooks/DependencyGraph.md`](../Notebooks/DependencyGraph.md) loads `DependencyGraph.m`, builds a Wolfram `Graph[…]` with a layered layout, and highlights sources / sinks / the topological ordering used to schedule per-item notebook generation.

## Implementation notes

- Edges are extracted by `re.findall(r"\[([^\]]*)\]\(([^)]+)\)", section)` over the `## Statement` and `## Proof` sections only — Guide narrative is ignored to keep the graph focused on what the proof actually invokes.
- Cross-book links (`../BookXI/PropXI.1.md`) are resolved to canonical item ids by file-system lookup.
- The extractor exits non-zero on any unresolved link target or detected cycle. Cycles would indicate either a bug in the scrape or an error in D. Joyce's marginal references; either way it's something to surface, not silently accept.
