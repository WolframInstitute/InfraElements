# Per-item notebook convention

The completed pilot is Book I Definitions 15 and 20, Postulates 1 and 3, and Proposition 1.
The user requested the 2026-10-13 refresh of these five only.

## Source and structure

Existing sources stay in `Wiki/Notebooks/Book<Roman><Kind><Num>.md`; generated notebooks stay in `Notebooks/` with the same stem.
The Markdown is authoritative; rebuild a notebook instead of editing its cells.
The user explicitly requested edits to these existing sources.
New reader-facing documents carry `_LLM`.
Generated notebooks have a Title followed immediately by the Subtitle `[[ LLM Generated ]]`.

The sections are Statement, Proof (propositions only), Setup, Geometric Scene, Infrageometric Scene, Interactive construction, Source, and Dependencies.
Preserve Joyce's statement and proof verbatim.
Short mathematical explanations are allowed beside comparisons and failed constructions.
Defined functions carry the item suffix.
Classical points use an item context, for example ``BookIProp1`a``, so displayed labels stay short and notebooks can share a kernel.

## Substrates and examples

The comparison columns are always the Large `SquareMeshGraph`, `SquareGridGraph`, and `HexagonalTilingGraph`, constructed with `InfraSubstrate` and `"KeepCoordinates" -> True`.
Seed each graph and sample.
Choose anchors from `GraphCenter` and explicit graph-distance conditions.
Use hop distance on all three; coordinates only draw and clip the figures.
Use chained `With`, `GraphicsGrid`, Standard colors, and `InfraSubstrateHighlight`.
Explain row and column meanings immediately before the figure.

## Current scene API

The refreshed notebooks target InfraGeometry 2.7.1.
Use `InfraStep`, `RandomInfraInstance`, `InfraSceneInstance`, and construction-specific samplers.
The May 2026 calls `FindInfraPoint`, `FindInfraScene`, `InfraGeometricStep`, and `InfraTriangle` are obsolete.
The [historical reference](../Resources/SyntheticInfrageometry.md) is retained; use the [current subset](../Resources/InfraGeometry_LLM.md).

Construct fixed points with `p == InfraPoint[ vertex ]`.
Use `InfraSegment[ p, q ]` for shortest paths and `InfraSegment[ p, q, c, p ]` for a closed sequence of shortest legs.
Keep construction families separate from their selected representatives.
The pilot uses `"Branches" -> 1` on path and circle constructions for small reproducible examples; this is not a claim about every representative.
Provide a runnable `InfraSceneViewer` cell beside the evaluated static comparisons.

## Mathematical distinctions

- An exact radius locus is `InfraShell[ center, radius ]`.
- `InfraCircle[ center, band ]` supplies shortest separating band cycles, whose radii can differ.
- The tested cycle bands are `{2, 3}` on the mesh and square grid and `{2, 4}` on the hexagonal tiling.
- A sampled circle is an open cyclic vertex order. Append its first vertex before drawing it as an `InfraWalk`, or its closing edge is missing.
- Closed shortest triangle legs can overlap or repeat vertices. They need not give a simple boundary or a filled region.
- An empty apex family is a valid failed construction. Display the last completed step and identify the failure.
- Keep exact distance equalities in Proposition I.1. Intersecting band cycles alone do not imply equilateral side lengths.
- A sampled success is an instance, not a general theorem.

## Build and verification

Keep one commit per completed per-item notebook. Extend the collection in dependency order, and never disguise a failed construction as a successful Euclidean analogue.

`Scripts/refresh_completed_notebooks.wls` rebuilds and evaluates only the five completed items, or the named subset of those five.
It preserves earlier local notebooks in `Notebooks/Archive/2026-10-13-before-refresh/`.
The built-in Markdown importer supplies prose and structure; fenced Wolfram code is restored verbatim to avoid corruption of escaped characters.
Definition/setup cells are initialized and code boxes post-processed.
The build embeds classical and static graph outputs, saves previews, and records messages, timeouts, and unresolved calls.
Live viewer cells are retained; their interaction is not claimed by the batch check.

`Scripts/check_completed_scenes.wls` checks paths, separating cycles, radial distances, triangle side lengths, and exact/empty apex cases.
The records and inspected figures live in [EuclidCompletedReview](../../Code/Artifacts/EuclidCompletedReview_LLM_261013/README.md).
Use this local batch fallback when the available Wolfram connector cannot access the filesystem, after checking license headroom.
The local refresh does not republish cloud notebooks.

## See also

- [Euclid API requirements](../Plans/EuclidAPIRequirements_LLM.md)
- [Dependency graph](../Resources/DependencyGraph.md)
- [Synthetic geometry](../Resources/SyntheticGeometry.md)
