# InfraGeometry: current Elements subset

**[[ LLM Generated ]]**

The completed Elements notebooks were migrated to InfraGeometry 2.7.1 on 2026-10-13.
The former [SyntheticInfrageometry reference](SyntheticInfrageometry.md) documents version 0.12.9 and is historical.

| Classical construction | Current graph construction | Contract |
|---|---|---|
| `GeometricScene` | `InfraScene` | Declare objects, constructors, and assertions. |
| `GeometricStep` | `InfraStep` | Labeled construction steps. |
| `RandomInstance` | `RandomInfraInstance` | Select an admissible graph-scene binding. |
| Bound points | `InfraSceneInstance[ instance, key ]` | Read a bound vertex, walk, or set. |
| `Point` | `InfraPoint[ vertex ]` | A fixed vertex. |
| Finite `Line` | `InfraSegment[ p, q ]` | The family of shortest paths. |
| `Circle` | `InfraCircle[ center, band ]` | Shortest separating band cycles; exact equal radii are not implied. |
| Exact radius equation | `InfraShell[ center, radius ]` | The graph distance level set. |
| Intersection point | `InfraIntersection[ first, second ]` | A point in the selected supports' intersection. |
| Triangle boundary | `InfraSegment[ p, q, c, p ]` | Closed shortest legs; overlaps are possible. |
| `EuclideanDistance` | `InfraDistance` | Ambient hop distance in these examples. |

`InfraSceneViewer` provides the live step browser.
`InfraSubstrateHighlight` displays the checked static representatives.
Style point sets as vertex densities and selected paths as `InfraWalk`.
A sampled circle is an open cyclic vertex order; close it explicitly when drawing it as a walk.

The notebook setup registers the sibling InfraGeometry checkout before `Needs`.
At this refresh the machine's installed version was 2.6.2, so the checked 2.7.1 source is required for the amended API.
The build record gives its exact source directory.

## See also

- [Notebook convention](../Concepts/NotebookConvention.md)
- [Current comparison](../../../../SubProjectsMain/InfraGeometry/ResearchNotebooks/SyntheticGeometryComparison_LLM.md)
- [Verified completed subset](../../Code/Artifacts/EuclidCompletedReview_LLM_261013/README.md)
- [Requirements learned from Euclid](../Plans/EuclidAPIRequirements_LLM.md)
