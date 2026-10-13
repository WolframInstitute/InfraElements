# API requirements learned from the completed Elements notebooks

**[[ LLM Generated ]]**

The goal is a paired Euclidean and infrageometric construction for each item of the Elements.
The completed pilot covers Definitions I.15 and I.20, Postulates I.1 and I.3, and Proposition I.1 on three Large substrates.
The [verification bundle](../../Code/Artifacts/EuclidCompletedReview_LLM_261013/README.md) records the examples and their limits.

## Naming recommendation

Align names with SyntheticGeometry where the mathematical contracts agree.
Use an explicit correspondence table where they differ.
The current `InfraScene`, `InfraStep`, and `RandomInfraInstance` already make the scene workflow recognizable.
`InfraHalfLine`, `InfraInfiniteLine`, and `InfraRegularPolygon` are useful existing alignments.
Renaming `InfraSegment` to `InfraLine` would conflict with the former maximal-line meaning and obscure the current migration.

The largest missing vocabulary in this pilot is triangle/polygon boundaries, followed by the contract for circles in Euclid's proof.
Further names should follow those contracts.
No paclet rename or new public head is implemented by this refresh.

## What the pilot establishes

| Elements item | Checked result | Required distinction |
|---|---|---|
| Postulate I.1 | Four-hop shortest segments exist on all three graphs. | A path family can have several members. |
| Postulate I.3 | Separating band cycles exist at the tested centers and bands. | This does not establish a circle at every center and exact radius. |
| Definition I.15 | The selected cycles have unequal radii; exact shells have equal radii. | Connected boundary and equal-radius locus differ. |
| Definition I.20 | All three side-length classes have exact vertex examples. | Selected shortest legs often overlap. |
| Proposition I.1, side two | Exact-shell and selected band-cycle examples have equilateral apices on all three graphs. | The band-cycle examples also impose exact distance equalities. |
| Proposition I.1, side one | The mesh example succeeds; the square and hexagonal examples are empty. | Bipartite parity obstructs odd equilateral side lengths. |

These are checked instances on the seeded Large graphs, rather than general existence theorems.

In a bipartite graph, a pairwise distance is even exactly when its endpoints lie in the same part.
The sum of the three pairwise distances of any three vertices is therefore even.
For an equilateral triple of side length r the sum is 3r, so r is even.
Thus exact Euclid I.1 cannot hold for every given segment on the square or hexagonal substrate with hop distance.

## Proposed work, in order

### 1. State the Elements circle contract

Specify whether the adapted circle postulate asserts an exact distance locus, a separating cycle in a band, or both as distinct objects.
Keep `InfraShell` and `InfraCircle` separate while making their membership laws explicit.
For Proposition I.1, assert both apex distances equal AB; membership in two band cycles alone is insufficient.
The [circle-through item](../../../../SubProjectsMain/InfraGeometry/Work/Backlog/SyntheticCircleThrough.md) addresses prescribed-point cycle membership, but does not settle exact radii or existence for every base.

Acceptance: the circle postulate and Definition I.15 are stated without silently changing between distance locus and boundary cycle; odd-base failures stay visible.

### 2. Specify triangle and polygon boundary heads

Assess `InfraTriangle[ { p, q, c } ]` and `InfraPolygon[ points ]` as possible SyntheticGeometry-shaped tokens.
Specify whether their representatives admit any closed sequence of shortest legs or require a simple cycle through the corners in order.
Keep fillings separate.
Do not revive the former metric-regular `InfraPolygon` meaning without an explicit migration decision.
Reuse [polygon boundaries](../../../../SubProjectsMain/InfraGeometry/Work/Backlog/SyntheticPolygonBoundaries.md) and [triangle catalog](../../../../SubProjectsMain/InfraGeometry/Work/Backlog/SyntheticTriangleCatalog.md).

Acceptance: Definition I.20 distinguishes metric side equality, a simple boundary, and a chosen filling.

### 3. Sample a complete constrained construction efficiently

The scene engine enumerates each construction's pool with `All` before limiting branches.
The pilot therefore uses small geometric scales even on Large substrates.
A wider mesh circle band timed out in a bounded exploratory probe.
Limiting a circle to one selected member can also discard a member needed by a later apex constraint.

Assess lazy sampling and backtracking with explicit completeness information, reusing the existing [scene architecture](../../../../SubProjectsMain/InfraGeometry/Wiki/Concepts/SceneMultiway.md).
Distinguish no solution for selected representatives from no solution in the complete geometric family.

Acceptance: later constraints can be searched without eagerly enumerating every path or circle, and selected-branch failure is not reported as a nonexistence theorem.

### 4. Retain a repeatable paired notebook template

Keep the five refreshed notebooks as the review sample.
Retain the same three substrate columns, explicit parameters, exact empty cases, and saved figures beside executable scenes.
The viewer should eventually expose the failed step and distinguish empty from undecided constructions directly.
The [convention](../Concepts/NotebookConvention.md) and two checked scripts provide the local implementation.

After the circle and triangle contracts are reviewed, continue with Common Notion I.1 and Postulate I.2, then the next propositions in dependency order.
No additional Elements notebook is started by this refresh.

## See also

- [Current InfraGeometry subset](../Resources/InfraGeometry_LLM.md)
- [Synthetic geometry scope](../../../../SubProjectsMain/InfraGeometry/Wiki/Concepts/SyntheticGeometryScope.md)
- [Region filling](../../../../SubProjectsMain/InfraGeometry/Work/Backlog/SyntheticRegionFilling.md)
