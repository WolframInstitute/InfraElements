# SyntheticInfrageometry — paclet API summary

Frozen local reference for the **SyntheticInfrageometry** paclet (v0.12.9). Future sessions should rely on this MD rather than re-scan the paclet codebase.

Paclet location (development): `/Users/pavel/Library/CloudStorage/Dropbox-WolframInstitute/Pavel Hajek/Infrageometry/FromPavel/SyntheticInfrageometry/SyntheticInfrageometry/`.

Companion: [SyntheticGeometry.md](SyntheticGeometry.md) — the classical-side framework used in tandem in every per-item notebook.

## 1. Overview

**SyntheticInfrageometry** is an axiomatic geometry framework for graphs and hypergraphs that models the geometric intuitions an "infra-observer" (constrained to walk on discrete vertices) would develop. It implements infra-geometric primitives (points, lines, circles, shells, balls, ellipses, …) as graph-metric constructs and studies branching constructions, coordinate systems, homotopy, and metric axioms. ~7,800 lines of Wolfram Language code across 35 kernel files with comprehensive `VerificationTest` suites.

**Motivation:** explore what continuous geometric concepts emerge from discrete substrates (Wolfram Physics Project's hypergraph rewriting framework).

## 2. Loading

From a local dev checkout:

```wolfram
PacletDirectoryLoad[ "/Users/pavel/Library/CloudStorage/Dropbox-WolframInstitute/Pavel Hajek/Infrageometry/FromPavel/SyntheticInfrageometry" ];
Needs[ "WolframInstitute`SyntheticInfrageometry`" ]
```

After loading, all exported symbols are available without prefix.

## 3. Public API by module

### `InfraPoint` — vertices and point constructions

- `InfraPoint[v]` — unary (single vertex); `InfraPoint[{v1,…,vk}]` — multi-realisation (set of vertices)
- `FindInfraPoint[graph]` — discover a vertex; optional `n` count, `UpTo[n]`, `All`; options: `"From"` (`All`, `"Center"`, `"Periphery"`), `"Distance"` (exact / range), `"MaxCliques"`
- `FindInfraMidpoint[graph, segment]` — vertex at metric centre of walk(s); `Method`: `"Metric"` (strict midpoint) | `"Embedding"` (coord space); option `"Tolerance"`
- `FindInfraGoldenSection[graph, segment]` — vertex S satisfying `AB/AS == AS/SB`
- `FindInfraReflection[graph, x, a]` — reflection of x through a (betweenness + equidistance)
- `CompleteInfraEquilateralTriangle[graph, p1, p2]` — equidistant apex (Euclid I.1 synthetic form)
- `FindInfraCommonPoint[graph, lines]` — vertex on all listed lines/segments
- `FindClosestInfraPoint[graph, line, point]` — closest point on line to point (metric argmin)
- `SelectInfraPoint[graph, vertices]` — select one from bundle using centrality/peripherality metrics
- `InfraReachableQ[graph, p1, p2]` — connectivity test between points

### `InfraSegment` — geodesic paths

- `InfraSegment[{path}]` — single geodesic; `InfraSegment[{path1,…,pathk}]` — multi
- `FindInfraSegment[graph, p1, p2]` — geodesic; `n / UpTo[n] / All`; options: `Properties` (edge filters), `Method` (`"Exhaustive"`, `"Greedy"`)
- `ExtendInfraSegment[graph, a, b, c, d]` — synthetic extension (Tarski A4): find x with `B(a,b,x) ∧ d(b,x)==d(c,d)`
- `InfraSegmentQ[graph, segment]` — is segment a geodesic?
- `InfraPathQ[graph, walk]` — is walk simple (no repeated vertices)?
- `UniqueInfraSegmentQ[graph, u, v]` — unique geodesic?

### `InfraPath` — walks (not necessarily geodesic)

- `InfraPath[{walk}]`; `InfraPath[{walk1,…,walkk}]`
- `FindInfraPath[graph, p1, p2, kspec]` — walk with length constraint; `kspec`: `k` (≤k), `{k}` (==k), `{kmin,kmax}`, `Infinity`; options: `Properties`, `Method`
- `ExtendInfraPath[graph, path]` — extend until stuck; options `"Direction"` (`"BothSides"`, `"Forward"`, `"Backward"`), `"Length"`
- `ConcatenateInfraPath[path1, path2]` — join compatible walks

### `InfraLoop` — closed walks

- `InfraLoop[{walk}]` — closed walk wrapper; open walks auto-closed

### `InfraString` — cyclic equivalence classes

- `InfraString[{walk}]` — closed walk modulo cyclic rotation (canonical form: lex-least rotation of the open interior)

### `InfraLine` — maximal geodesics

- `FindInfraLine[graph, p1, p2]` — maximal geodesic through p1 and p2; options: `"Maximality"` (`"Extension"`, `"Diameter"`), `"Direction"` (`"BothSides"`, `"Forward"`, `"Backward"`), `Method`
- `FindInfraParallel[graph, line, p]` — parallel lines through p (constant distance to line)
- `FindInfraPerpendicular[graph, line, point]` — perpendicular lines at point; options: `Method` (`"Metric"`, `"Projection"`, `"Coordinate"`, `"Arclength"`, `"Alexandrov"`), `"Radius"`
- `FindInfraCommonLine[graph, vertices]` — line containing all vertices
- `InfraLineQ[graph, segment]` — maximal geodesic predicate
- `InfraParallelQ[graph, l1, l2]` — constant-distance predicate
- `InfraPerpendicularQ[graph, l1, l2]` — perpendicularity predicate at common vertex
- `PencilDirections[graph, O]` — canonical directions (maximal geodesics through O, one per projective class)
- `PencilCardinality[graph, O]` — count of distinct direction classes
- `LineCount[graph]` — total number of distinct maximal geodesics

### `InfraShell` — metric level sets

- `InfraShell[{set}]` — vertices at fixed distance from centre; `InfraShell[center, radius]` — scene-DSL constructor
- `FindInfraShell[graph, c, r]` — level set `{v : d(c,v)==r}`; r can be scalar or `{rmin,rmax}` (tolerance band); options: `Properties` (`"Separating"`, `"Connected"`), `Method`
- `FindInfraOsculatingShell[graph, path, i, k]` — osculating shell at position i, window size k
- `FindInfraShellParameters[graph, vertexSet]` — recover `{center, radius}` pairs
- `InfraShellQ[graph, vertexSet]` — is a metric shell?
- `SeparatesQ[graph, vertexSet, u, v]` — vertex set disconnects u from v?

### `InfraBall` — closed metric balls

- `InfraBall[{ball}]` — closed ball `{v : d(c,v)≤r}`; `InfraBall[center, radius]` — scene constructor
- `FindInfraBall[graph, c, r]` — compute closed ball
- `InfraBallQ[graph, vertexSet]` — predicate

### `InfraCircle` — separating cycles

- `InfraCircle[{cycle}]` — shortest cycle in level surface (open vertex sequence); `InfraCircle[center, radius]` — scene constructor
- `FindInfraCircle[graph, c, r]` — separating cycle; options: `Properties` (default `{"Separating", "Shortest"}`)
- `FindInfraCycle[graph, n]` / `FindInfraCycle[graph, {k}, n]` / `FindInfraCycle[graph, {kMin,kMax}, n]`
- `InfraCircleQ[graph, cycle]` — predicate

### `InfraPolygon` — regular cycles

- `InfraPolygon[{cycle}]` — multi-realisation cycle; `["Length"]` returns vertex count
- `FindInfraRegularPolygon[graph, As, n]` — length-n cycle where k-diagonal distances match pattern `As`
- `InfraRegularPolygonQ[graph, cycle, As]`

### `InfraEllipticShell` / `InfraQuadric` / `InfraEllipse` — bi-focal / multi-focal objects

- `InfraEllipticShell[{set}]` — `{v : d(p1,v)+d(p2,v)==c}`; `FindInfraEllipticShell[graph, {p1,p2}, c]`
- `FindInfraQuadric[graph, {p1,…,pk}, c]` — `{v : sum_i d(p_i,v)≤c}` (solid ellipsoid); weighted version (hyperboloid)
- `InfraEllipse[{cycle}]` — shortest cycle in elliptic level surface; `FindInfraEllipse[graph, {p1,p2}, c]`
- `InfraEllipseQ`, `InfraEllipticShellQ` — predicates

### `InfraPlane` — bisecting hyperplanes

- `InfraPlane[{set}]` — bisector `{v : d(p1,v)==d(p2,v)}`; `InfraPlane[p1, p2]` or `InfraPlane[p1, p2, {lo,hi}]` — scene constructors
- `FindInfraBisectingHyperplane[graph, p1, p2]` — slab variant by positional `{lo,hi}`; options: `Properties`, `Method`

### `InfraRay` — half-lines

- `InfraRay[{ray}]` — pointed half-line `{O,…,w}` where w is inextensible
- `FindInfraRay[graph, O, v]` — ray from O in direction of v (half of maximal geodesic line)

### `InfraPolyline` — piecewise geodesics

- `InfraPolyline[{poly}]` — `poly = {seg1,…,segk}`, list of unary `InfraSegment[{path_i}]`; consecutive legs share endpoint
- `FindInfraPolylineSubdivision[graph, path]` — fewest geodesic legs; option `"MaxLength"`
- `InfraPolylineQ[graph, poly]`

### `InfraRevolution` — rotational objects

- `InfraObject[vs]` — wraps any vertex set as a single geometric object
- `InfraRevolution[axis, profile]` — scene DSL constructor
- `FindInfraRevolution[graph, axis, profile]` — rotational set around axis; profile: numeric (constant), list, `Association`, or callable; options: `"Form"` (`"Solid"`, `"Surface"`), `Method` (`"Voronoi"`, `"PerpendicularBisector"`)
- `FindInfraCylinder[graph, axis, r]` / `FindInfraCone[graph, axis, slope]`
- `InfraRevolutionQ[graph, vs, axis, profile]`

### `EuclideanSpace` — metric geometry in Euclidean frame

- `InfraScalarProduct[graph, o, u, v]` — base-point scalar product; `Method`: `"Alexandrov"` (law of cosines, optionally curved M_k²) | `"Parallelogram"` (polarisation via linear combination)
- `FindInfraLinearCombination[graph, o, {{λ1,u1},…}]` — vertex realising `sum_i λ_i u_i`; options: `"ScaleMethod"`, `"SumMethod"`
- `InfraAngle[graph, {q1,p,q2}]` — angle at p; `Method`: `"Arclength"` (synthetic radian via arc deletion), `"Alexandrov"` (law of cosines, optionally M_k²)

### `InfraCurveGeometry` — discrete curvature

- `TurningAngles[graph, path]` — list of exterior angles `π - InfraAngle` at interior vertices
- `TotalCurvature[graph, path]` / `TotalAbsoluteCurvature[graph, path]` — sums of (|·|) turning angles
- `TurningNumber[graph, cycle]` — `TotalCurvature / (2π)`

### `AlexandrovGeometry` — curvature bounds

- `ComparisonTriangle[a,b,c]` — Euclidean `Triangle` in R²; with `"Curvature" -> k` returns `InfraComparisonTriangle[…]` for M_k²
- `CATInequalityQ[graph, {p,q,r}, k]` — CAT(k) thinness test; `Method`: `"ApexSide"` (default), `"TwoRays"`
- `InfraCurvature[graph, v]` — local Alexandrov upper-curvature bound; option `"Radius"`

### `PathSpace` — metrics on path bundles

- `SelectInfraPath[graph, paths]` — select one path via centrality; options: `"From"`, `"Distance"`, `"Metric"` (`"Hausdorff"`, `"Frechet"`, `"MeanFrechet"`), `"MaxCliques"`
- `SelectInfraCycle[graph, cycles]` — `"From"` extras: `"ShortestCircumference"`, `"LongestCircumference"`
- `EmbeddingClosest[graph, bundle, ref]` — filter by Hausdorff distance to reference
- `GeodesicSprayGraph[graph, c]` — BFS DAG rooted at c
- `PathSubgraph[graph, u, v]` — union of all shortest u-v paths; capped variant `PathSubgraph[graph, u, v, k]`

### `Homotopy` — path equivalence

- `InfraHomotopy[{chain}]` — homotopy chain via elementary moves
- `FindInfraHomotopyRepresentative[graph, obj]` — shortest walk in homotopy class
- `FindInfraHomotopy[graph, a, b]` / `HomotopicQ[graph, a, b]` / `NullHomotopicQ[graph, cycle]`
- `HomotopyMoveType` / `HomotopyMoveTypes` — classify move(s) as `"Contract"`, `"Extend"`, `"Lateral"`

### `MetricAlgebra` — graph-metric structure

- `MetricInterval[graph, u, v]` — all geodesics `{w : d(u,w)+d(w,v)==d(u,v)}`
- `GeodesicMultiplicity[graph, u, v]` — count distinct geodesics
- `GeodesicMultiplicityMatrix[graph]` — `{D, M}` (distance, multiplicity)
- `MedianVertices[graph, vs]`
- `FindGeodesicConvexHull[graph, S]` / `GeodesicallyConvexQ[graph, S]` (Method `"Strong"`/`"Weak"`)

### `InfraTopology` — topological/order structure

- `InfraTopologicalSpace[graph, topo]` — Hasse-diagram wrapper of specialisation preorder; convenience `"Topology" -> {"Ball", r}`; accessors `["Graph"]`, `["Topology"]`
- `InfraBallTopology[graph, r]` — Hasse diagram of r-ball specialisation
- `InfraTopologicalGraph[graph, r]` — InfraTopologicalSpace overlaid
- `InfraSet[vs]` — topological set wrapper; `["Vertices"]`, `["Length"]`
- `InfraSetClosure / InfraSetInterior / InfraSetBoundary / InfraSetNeighborhood[ts, s]`
- `ContinuousMapQ[f, s1, s2]`

### `Coordinatization` — embedding and coordinate systems

- `ResistanceCoordinates[graph]` — resistance-matching spectral embedding (φ_i/√λ_i satisfies `||Φ(u)-Φ(v)||² == EffectiveResistance`); options `"Rescaling"` (`"ResistanceMatching"`, `"None"`, `"Diffusion" -> t`), `"Dimension"`, `"Origin"`
- `FindInfraRadarBasis[graph, n, m]` — up to n resolving sets of size m
- `InfraRadarBasisQ[graph, basis]` — unique distance vector per vertex?
- `RadarCoordinates[graph, basis, vertex]` — distance vector to basis; option `"InfraPointAggregation"` (`Min`, `Mean`, `Max`)
- `OrthogonalCoordinates[graph, c, {a1,a2,…}, v]` — Z-valued displacement on axes; option `"SelectCoordinate"`
- `FindInfraOrthogonalFrame[graph, c, axisLength]` — mutually perpendicular `InfraSegment` axes through c
- `FindInfraSpanningAxes[graph, n]` — n longest well-separated geodesics

### `TarskiGeometry` — Tarski axioms

- `BetweennessQ[graph, u, w, v]` — does w lie on a geodesic from u to v?
- `EquidistanceQ[graph, a, b, c, d]` — is `d(a,b)==d(c,d)`?
- `TarskiStructure[graph]` — memoised bundle: `"Vertices"`, `"VertexIndex"`, `"Distances"`, `"Betweenness"`, `"Equidistance"`, `"Diameter"`
- `TarskiBetweennessTensor`, `TarskiEquidistanceClasses`
- Per-axiom tests `TarskiCongruenceReflexivityQ`, …, `TarskiContinuityQ` (always False on finite graphs), `TarskiAxiomQ[graph]` (full `Association`)
- `FindTarskiCounterexample[graph, predQ]`

### `ProjectiveGeometry` — direction and incidence

- `SameDirectionQ`, `CollinearQ`, `ConcurrentQ`, `UniquePencilQ`, `UniqueCollinearQ`, `UniqueConcurrentQ`
- Whitehead axioms: `WhiteheadW1Q` (≥3 vertices per line?), `WhiteheadW2Q` (geodetic?), `WhiteheadW3Q` (intersection property, O(n⁴))
- `ProjectivePlaneGraphQ`

### `GraphEnumeration` — systematic graph construction

- `EnumerateGraphs[…]` — enumerate by properties (under development)

### `ExampleGraphs` — predefined families (use these in DiscreteEuclid notebooks)

- `PunchHole[g, r]` — remove closed r-ball around random vertex; `PunchHole[g, c -> r]` — explicit centre
- `TorusTessellation["Rectangular", {m, n}]` — `{4,4}`-tiling on Z_m × Z_n
- `TorusTessellation["Triangular", {m, n}]` — `{3,6}`-tiling (6-regular) — **used in DiscreteEuclid `$DiscreteEuclidGraphs`**
- `TorusTessellation["Hexagonal", {m, n}]` — `{6,3}`-tiling (3-regular)

### `InfraScene` — declarative construction language (primary interface)

- `InfraScene[{p, q, …}, {hypotheses}]` — scene object with objects and construction rules
- `FindInfraScene[scene, graph]` — enumerate all instances satisfying scene; options `"PruneProbability"`, `"Branches"`
- `InfraInstance[Association]` — wrapper for resolved bindings
- `InfraGeometricStep[construction]` — explicit step directive (analogue of `GeometricStep`)
- `InfraDistance[p, q]` — symbolic distance in scene (resolved to `GraphDistance`); option `"Aggregation"` (`Min`, `Max`, `Mean`, …)
- `InfraIntersection[objs]` / `InfraUnion[objs]` — symbolic vertex-set operations
- Symbolic predicate forms: `InfraPathQ`, `InfraSegmentQ`, `InfraShellQ`, `InfraCircleQ`, `InfraLineQ`, `InfraParallelQ`, `InfraIntersectQ`, `InfraPlaneQ`, `InfraRevolutionQ`

### `InfraSceneVisualization` — static rendering

- `InfraSceneHighlight[graph, objects]` — diffuse rendering of multi-realisations; each object auto-classified by type; options `"OpacityRange"`, `"ThicknessRange"`, `"PointSizeRange"` (use `None` to skip), plus `HighlightGraph` options
- Per-object palette: `$InfraPointColor` (red), `$InfraSegmentColor` (orange), `$InfraLineColor` (dark orange), `$InfraShellColor` (green), `$InfraBallColor` (light green), `$InfraPlaneColor` (purple), `$InfraCircleColor` (teal), `$InfraRayColor` (light orange), `$InfraPathColor` (tan), `$InfraObjectColor` (light blue), `$InfraTopologyColor` (light purple)

### `InfraSceneInteractive` — interactive viewers (**primary visualisation in DiscreteEuclid notebooks**)

- `InfraSceneViewer[scene, graph]` — **full scene instance browser; the analogue of `GeometricStep`'s built-in stepper**
- `PointViewer[graph]` — point-selection interface
- `SegmentViewer[graph]` — segment-discovery interface
- `ShellViewer[graph]` — shell explorer
- `CircleViewer[graph]` — cycle explorer

### `InfraEquality`

- `InfraEqualQ[a, b]` — extensional equality of `Infra*` wrappers (ignores wrapper realisations, compares underlying vertex sets)

## 4. Wrapper / multi-realisation semantics

All `Infra*` wrappers support **multi-realisation** via auto-flatten:

```wolfram
InfraPoint[{InfraPoint[{1}], InfraPoint[{2}]}] === InfraPoint[{1, 2}]
```

Finders return lists of unary wrappers; wrap with the head to collapse:

```wolfram
results = FindInfraPoint[ g, All ]
(* {InfraPoint[{v1}], InfraPoint[{v2}], ...} *)
InfraPoint @ results
(* InfraPoint[{v1, v2, ...}] *)
```

The "diffuse picture" signature: each construction step branches; rendering shades each graph element by candidate count.

## 5. Scene DSL example

```wolfram
scene = InfraScene[
  { p, q, s },
  {
    p == InfraPoint[ ],
    q == InfraPoint[ ],
    s == InfraSegment[ p, q ],
    InfraDistance[ p, q ] >= 3
  }
];
instances = FindInfraScene[ scene, PetersenGraph[ ] ];
```

For DiscreteEuclid notebooks, scenes use the `Find…` family directly inside hypotheses where they help (e.g. `c == CompleteInfraEquilateralTriangle[ graph, a, b ]`), and the **interactive viewer**:

```wolfram
InfraSceneViewer[ scene, graph ]
```

## 6. Loading and dependencies

Self-contained: no other paclets required. Built-in Wolfram Language 14.3+ graph functions only (`GraphDistance`, `FindPath`, `NeighborhoodGraph`, `Subgraph`, `FindCycle`, `TransitiveReductionGraph`, …) plus standard numerics.

## 7. Test files as documentation

`Tests/*.wlt` contain `VerificationTest`s — the by-example docs:

| File | Topic |
|---|---|
| `InfraPrimitivesTests.wlt` | wrapper semantics, auto-flatten, `FindInfraCycle` |
| `InfraSceneTests.wlt` | scene construction, `InfraDistance`, `InfraShell`/`Plane` constructors |
| `InfraBallTests.wlt` | balls on `PathGraph`, `CycleGraph`, `CompleteGraph`, `StarGraph` |
| `InfraLineTests.wlt` | maximal geodesics, parallels, perpendiculars, pencil directions |
| `InfraCircleTests.wlt` | separating cycles, level sets, shortest cycles, null-homotopy |
| `HomotopyTests.wlt` | path equivalence, homotopy chains, null-homotopic cycles |
| `TarskiGeometryTests.wlt` | betweenness, equidistance, axiom verification |
| `EuclideanSpaceTests.wlt` | angles, scalar products, curvature |
| `AlexandrovGeometryTests.wlt` | comparison triangles, CAT(k) |
| `CoordinatizationTests.wlt` | radar bases, resistance coords, orthogonal frames |
| `InfraTopologyTests.wlt` | ball topology, set closure / interior / boundary |
| `PathSpaceTests.wlt` | path selection, Hausdorff distance, geodesic spray graphs |

Representative test:

```wolfram
VerificationTest[
  FindInfraBall[ PathGraph[ Range[ 5 ] ], 3, 1 ],
  InfraBall[ { { 2, 3, 4 } } ],
  TestID -> "FindInfraBall-PathGraph-interior-r1"
]
```

## 8. Quick-start examples

Find all geodesics in a grid:

```wolfram
FindInfraSegment[ GridGraph[ { 3, 3 } ], 1, 9, All ]
```

Equilateral-triangle apex (Euclid I.1):

```wolfram
CompleteInfraEquilateralTriangle[ TorusTessellation[ "Triangular", { 10, 10 } ], 13, 17 ]
```

Multi-realisation circle visualisation:

```wolfram
g = GridGraph[ { 4, 4 } ];
InfraSceneHighlight[ g, FindInfraCircle[ g, 8, 1, All ], "OpacityRange" -> { 0.2, 1 } ]
```

Test axioms:

```wolfram
TarskiAxiomQ @ GridGraph[ { 3, 3 } ]
(* <| "A1" -> True, "A2" -> True, … |> *)
```

## 9. Complexity caveats

Some predicates are computationally expensive — `WhiteheadW3Q`, `CATInequalityQ`, `TarskiFiveSegmentsQ` are O(n⁴); `TarskiFiveSegmentsQ` is O(n⁸) without `"MaxTuples"`. Cap with `"MaxTuples"` where available when graphs are large.
