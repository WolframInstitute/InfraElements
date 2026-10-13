# SyntheticGeometry — Wolfram Language reference summary

Frozen local reference so future sessions never have to re-scrape. Source tutorial: <https://reference.wolfram.com/language/tutorial/SyntheticGeometry.html>.

Companion: [InfraGeometry](InfraGeometry_LLM.md) — the current graph-side subset used by the completed notebooks. The [SyntheticInfrageometry reference](SyntheticInfrageometry.md) is historical.

## 1. Overview

The Wolfram Language SyntheticGeometry framework provides **symbolic representation of synthetic (coordinate-independent) geometry scenes** suitable for **automated geometric reasoning, conjecture finding, and proof-by-instance**. A scene is described by named symbolic points (and optional scalar quantities), a list of hypotheses (regions, equations, geometric assertions), and optional conclusions; instances with explicit coordinates can be sampled by `RandomInstance`, properties solved with `GeometricSolveValues`, and theorems automatically discovered with `FindGeometricConjectures`.

The framework is fundamentally **2D** — most synthetic primitives are 2D-only. A few helpers like `Midpoint` work in arbitrary dimensions. Framework introduced in Wolfram Language 12.0 (2019); updated through 14.1 (2024).

## 2. Core symbols

### 2.1 `GeometricScene` — <https://reference.wolfram.com/language/ref/GeometricScene.html>

Symbolic 2D geometric scene; can hold multiple instances of the same abstract scene.

```
GeometricScene[{p1, p2, ...}, {hyp1, hyp2, ...}]
GeometricScene[{{p1, p2, ...}, {k1, k2, ...}}, hyps]                 (* with scalar quantities *)
GeometricScene[{{p1 -> {x1, y1}, ...}, {k1 -> v1, ...}}, hyps]       (* specific instance *)
GeometricScene[params, hyps, {con1, con2, ...}]                       (* with conclusions *)
GeometricScene[{{{p1->{x1,y1},...},{k1->v1,...}}, ...}, hyps]         (* multi-instance *)
GeometricScene[{scene1, scene2, ...}]                                 (* combine instances *)
```

Subvalue properties: `"AlgebraicFormulation"`, `"Conclusions"`, `"Graphics"`, `"GraphicsList"`, `"Hypotheses"`, `"Instances"`, `"Parameters"`, `"Points"`, `"Properties"`, `"Quantities"`.

Options (geometry-specific): `UnconstrainedParameters`, `GeometricStylingRules`, `PlotTheme`; inherits all `Graphics` options.

```wolfram
(* Symbolic scene: triangle with a 30 deg angle *)
scene = GeometricScene[ { a, b, c },
  { Triangle[ { a, b, c } ], PlanarAngle[ { a, b, c } ] == 30 Degree } ]
RandomInstance[ scene ]

(* Right triangle, unknown hypotenuse *)
scene = GeometricScene[ { { a, b, c }, { h } },
  { Triangle[ { a, b, c } ],
    GeometricAssertion[ { Line[ { a, b } ], Line[ { b, c } ] }, "Perpendicular" ],
    EuclideanDistance[ a, b ] == 3, EuclideanDistance[ b, c ] == 4,
    EuclideanDistance[ a, c ] == h } ]
GeometricSolveValues[ scene, h ]   (* {5} *)
```

### 2.2 `RandomInstance` — <https://reference.wolfram.com/language/ref/RandomInstance.html>

Finds an explicit-coordinate instance of a scene satisfying all hypotheses; assumes general position + nondegeneracy. Option `RandomSeeding -> Automatic | seed`.

```
RandomInstance[expr]
RandomInstance[expr, n]
```

```wolfram
RandomInstance[ scene, 4 ]
RandomInstance[ scene, RandomSeeding -> 12345 ]
```

### 2.3 `FindGeometricConjectures` — <https://reference.wolfram.com/language/ref/FindGeometricConjectures.html>

Discovers conjectures empirically from sampled instances. If no instances are supplied, `RandomInstance` is used internally.

```
FindGeometricConjectures[scene]
FindGeometricConjectures[{scene1, scene2, ...}]
FindGeometricConjectures[scenes, patt]
FindGeometricConjectures[scenes, patt, n]
```

Option `Method`; seed via `Method -> {"RandomInstance", RandomSeeding -> seed}`. Pattern examples: `GeometricAssertion[_, "Perpendicular"]`, `_ == Midpoint[{_, _}]`. Retrieve with `scene["Conclusions"]`.

```wolfram
(* Thales's theorem *)
scene = GeometricScene[ { a, b, c, o },
  { Triangle[ { a, b, c } ], CircleThrough[ { a, b, c }, o ],
    o \[Element] Line[ { a, c } ] } ];
FindGeometricConjectures[ scene ]
(* discovers GeometricAssertion[{Line[{a,b}], Line[{b,c}]}, "Perpendicular"] *)
```

Other doc-demonstrated theorems: Pappus's hexagon, Kosnita's, Finsler–Hadwiger, Brahmagupta's.

### 2.4 `GeometricAssertion` — <https://reference.wolfram.com/language/ref/GeometricAssertion.html>

Inert symbolic assertion used as a hypothesis in `GeometricScene`. The dual evaluating function is `GeometricTest`.

```
GeometricAssertion[obj, prop]
GeometricAssertion[{obj1, obj2, ...}, prop]
GeometricAssertion[objs, prop1, prop2, ...]
```

Predicates / relations supported:

| Group | Values |
|---|---|
| Polygon predicates | `"Clockwise"`, `"Convex"`, `"Counterclockwise"`, `"Cyclic"`, `"Equiangular"`, `"Equilateral"`, `"Parallelogram"`, `"Rectangle"`, `"Regular"`, `"Simple"` |
| Line predicates | `"Horizontal"`, `"Vertical"`, `"Leftward"`, `"Rightward"`, `"Upward"`, `"Downward"` |
| Containment | `{"Inside", circle}`, `{"Outside", circle}` |
| Point relations | `"Clockwise"`, `"Collinear"`, `"Counterclockwise"`, `"CyclicallyOrdered"`, `"Distinct"`, `{"EqualAngles", pt}` |
| Line relations | `"Antiparallel"`, `"Concurrent"`, `{"Concurrent", pt}`, `"MatchingParallel"`, `"Nondegenerate"`, `"Parallel"`, `"Perpendicular"` |
| Object relations | `"Congruent"`, `"PairwiseTangent"`, `{"SameSide", line}`, `"Similar"`, `"Tangent"`, `{"Tangent", pt}` |
| Two-list relation | `{"OppositeSides", line}` |

```wolfram
GeometricAssertion[ Triangle[ { a, b, c } ], "Equilateral" ]
GeometricAssertion[ { Line[ { a, b } ], Line[ { c, d } ] }, "Perpendicular" ]
GeometricAssertion[ { a, b, c }, "Collinear" ]
```

### 2.5 `GeometricTest` — <https://reference.wolfram.com/language/ref/GeometricTest.html>

Evaluates the same predicate/relation vocabulary to `True`/`False` or symbolic conditions.

```wolfram
GeometricTest[ { { 0, 0 }, { 1, 1 }, { 2, 2 } }, "Collinear" ]   (* True *)
GeometricTest[ { a, b, c }, "Collinear" ]                         (* condition *)
```

### 2.6 `GeometricSolveValues` — <https://reference.wolfram.com/language/ref/GeometricSolveValues.html>

```
GeometricSolveValues[scene, expr]
GeometricSolveValues[scene, {expr1, expr2, ...}]
```

For numeric instances, numeric output; for abstract scenes, symbolic (coordinates via `Indexed`). May return multiple sign branches.

### 2.7 `GeometricStep` — <https://reference.wolfram.com/language/ref/GeometricStep.html>

```
GeometricStep[{hyp1, hyp2, ...}]
GeometricStep[hyps, label]
```

Each step is satisfied in order; earlier-introduced points/scalars are fixed in later steps. Adds an **interactive setter menu** to the displayed scene (this is the analogue of `InfraSceneViewer` from the SyntheticInfrageometry paclet — both are mandatory in every per-item notebook of this project).

**Pitfall:** adding constraints to objects *after* the step that introduces them can render the scene unsatisfiable.

### 2.8 `GeometricStylingRules` — <https://reference.wolfram.com/language/ref/GeometricStylingRules.html>

Option to `GeometricScene`. Rules with LHS `"PointStyle"`, `"StylingPatterns"`, `"ConclusionStyle"`. Default conclusion highlight is orange.

### 2.9 `UnconstrainedParameters` — <https://reference.wolfram.com/language/ref/UnconstrainedParameters.html>

Option; values `None | All | {p1, p2, ...}`. Lets named points roam freely.

### 2.10 `GeometricTransformation` — <https://reference.wolfram.com/language/ref/GeometricTransformation.html>

```
GeometricTransformation[g, tfun]
GeometricTransformation[g, m]            (* point r -> m.r *)
GeometricTransformation[g, {m, v}]       (* affine: r -> m.r + v *)
GeometricTransformation[g, {t1, t2, ...}] (* multiple copies *)
```

A rendering construct, not a symbolic-constraint object. `Normal` applies it. Composition: `GeometricTransformation[GeometricTransformation[g, m1], m2] === GeometricTransformation[g, m2.m1]`. There is **no** `GeometricTransformationFunction` symbol — transformation functions are produced by `AffineTransform`, `RotationTransform`, `TranslationTransform`, `ReflectionTransform`, `ScalingTransform`, `ShearingTransform`.

## 3. Primitives & constructions recognised in `GeometricScene`

### 3.1 Primitive objects

| Primitive | Meaning |
|---|---|
| `Point[p]` | Point set |
| `Line[{p1, p2, ...}]` | Line segment(s) |
| `InfiniteLine[{p, q}]`, `InfiniteLine[p, v]` | Infinite line |
| `HalfLine[{p, q}]`, `HalfLine[p, v]` | Ray |
| `Circle[p, r]` | Circle |
| `Disk[p, r]` | Filled disk |
| `Triangle[{p, q, r}]` | Filled triangle |
| `Polygon[{p1, p2, ...}]` | Simple polygon |
| `Parallelogram[pt, {v1, v2}]` | Parallelogram |
| `Rectangle[pt1, pt2]` | Rectangle |
| `RegularPolygon[n]` | Regular polygon |

### 3.2 Constructions

| Construction | Notes |
|---|---|
| `AngleBisector[{q1, p, q2}]` | InfiniteLine; options `"Interior"`/`"Exterior"`. **2D only.** |
| `PerpendicularBisector[{p, q}]` | InfiniteLine; passes through `Midpoint[{p, q}]`. **2D only.** |
| `Midpoint[{p, q}]` | Any dimension; returns coords or `Point` matching input form. |
| `CircleThrough[{p1, ...}]`, `CircleThrough[pts, q]`, `CircleThrough[pts, q, r]` | Circle through points (with optional centre / radius). |
| `CircularArcThrough[{p1, ...}]` | Arc through points. |
| `InfiniteLineThrough[{p1, ...}]` | Line through unordered points (implies collinearity). |
| `Circumsphere[{p1, p2, p3}]` | Circumscribed circle (in 2D). |
| `Insphere[{p1, p2, p3}]` | Inscribed circle. |
| `TriangleCenter[tri, type]`, `TriangleConstruct[tri, type]` | See below. |
| `RegionBoundary`, `RegionCentroid`, `RegionNearest[reg, p]` | Generic region accessors. |

**`TriangleConstruct` types** (URL <https://reference.wolfram.com/language/ref/TriangleConstruct.html>):

- *Points/centres:* `"Centroid"`, `"Circumcenter"`, `"Incenter"`, `"Orthocenter"`, `"NinePointCenter"`, `"SymmedianPoint"`, `{"Excenter", p}`, `{"Foot", p}`, `{"Midpoint", p}`, `{"AngleBisectingCevianEndpoint", p}`, `{"SymmedianEndpoint", p}`, `{"CevianEndpoint", center, p}`.
- *Lines:* `{"Altitude", p}`, `{"AngleBisector", p}`, `{"AngleBisectingCevian", p}`, `"Boundary"`, `{"Cevian", center, p}`, `"EulerLine"`, `{"ExteriorAngleBisector", p}`, `{"Median", p}`, `{"OppositeSide", p}`, `{"PerpendicularBisector", p}`, `{"Symmedian", p}`.
- *Circles:* `"Circumcircle"`, `{"Excircle", p}`, `"Incircle"`, `"NinePointCircle"`.
- *Triangles:* `"AntimedialTriangle"`, `"MedialTriangle"`, `"Triangle"`.

Useful identities (from docs):
- `TriangleConstruct[{a,b,c}, "AngleBisector"]` ≡ `AngleBisector[{a,b,c}]`
- `TriangleConstruct[{a,b,c}, "PerpendicularBisector"]` ≡ `PerpendicularBisector[{a,c}]`
- `TriangleCenter[{a,b,c}, "Midpoint"]` ≡ `Midpoint[{a,c}]`
- `TriangleCenter[{a,b,c}]` ≡ `RegionCentroid[Triangle[{a,b,c}]]`
- `TriangleConstruct[{a,b,c}, "Incircle"]` ≡ `Circle[TriangleCenter[{a,b,c}, "Incenter"], TriangleMeasurement[{a,b,c}, "Inradius"]]`

### 3.3 Measurements

`ArcLength`, `Area`, `EuclideanDistance`, `Perimeter`, `PlanarAngle[{p, q, r}]` or `PlanarAngle[p -> {q1, q2}]` (specs `"Interior"`, `"Exterior"`, `"FullExterior"`, `"Clockwise"`, `"Counterclockwise"`), `PolygonAngle[poly, p]`, `RegionDistance`, `SignedRegionDistance`, `RegionMeasure`, `TriangleMeasurement[tri, type]` (`"Area"`, `"Circumradius"`, `"Inradius"`, `{"Exradius", p}`, `"Perimeter"`, `"Semiperimeter"`, `{"InteriorAngle", p}`, `{"ExteriorAngle", p}`, `{"FullExteriorAngle", p}`, `{"Height", p}`, `"NinePointRadius"`).

### 3.4 Hypothesis syntax

| Form | Meaning |
|---|---|
| `p \[Element] reg` or `RegionMember[reg, p]` | Point in region |
| `x1 == x2 == ...` | Equality |
| `x > y`, etc. | Inequality |
| `GeometricAssertion[objs, prop]` | Named assertion |
| `GeometricStep[hyps, label]` | Construction step |

## 4. Idioms

```wolfram
(* Declare points *)
GeometricScene[ { a, b, c }, { Triangle[ { a, b, c } ] } ]

(* Add scalars *)
GeometricScene[ { { a, b, c }, { h } },
  { Triangle[ { a, b, c } ], EuclideanDistance[ a, c ] == h } ]

(* Random instance *)
RandomInstance[ scene, 4 ]
RandomInstance[ scene, RandomSeeding -> 1 ]

(* Stepwise construction *)
GeometricScene[ { a, b, c },
  { GeometricStep[ { Line[ { a, b } ] }, "Given segment" ],
    GeometricStep[ { Circle[ a, EuclideanDistance[ a, b ] ],
                     Circle[ b, EuclideanDistance[ a, b ] ] }, "Construct circles" ],
    GeometricStep[ { c \[Element] Circle[ a, EuclideanDistance[ a, b ] ],
                     c \[Element] Circle[ b, EuclideanDistance[ a, b ] ],
                     Triangle[ { a, b, c } ] }, "Equilateral triangle" ] } ]

(* Find conjectures *)
FindGeometricConjectures[ scene ]
FindGeometricConjectures[ scene, GeometricAssertion[ _, "Perpendicular" ] ]
scene[ "Conclusions" ]

(* Solve *)
GeometricSolveValues[ scene, h ]

(* Polynomial constraints *)
scene[ "AlgebraicFormulation" ]

(* Test directly *)
GeometricTest[ { p1, p2, p3 }, "Collinear" ]
```

## 5. Limitations and pitfalls

- **2D only for most synthetic primitives.** `AngleBisector`, `PerpendicularBisector`, the entire `GeometricScene` framework, and `TriangleConstruct` outputs are 2D. From the docs: *"PerpendicularBisector only works in 2D"*; *"AngleBisector only works in 2D"*. `Midpoint` is the notable exception (any dimension).
- **General-position assumption.** `RandomInstance` assumes points are in general position and regions nondegenerate; degenerate configurations are avoided unless explicitly forced.
- **Conjectures are empirical.** `FindGeometricConjectures` produces *conjectures*, not proved theorems — they hold across sampled instances.
- **Symbolic scenes don't render.** From `GeometricScene` docs: *"Geometric scenes with symbolic points do not format; geometric scenes where all points have numerical values format graphically."* Use `RandomInstance` to render.
- **`GeometricStep` ordering matters.** Constraints added to objects after the step in which they were introduced can make the scene unsatisfiable.
- **Multi-instance `FindGeometricConjectures`** requires all `scene_i` to share the same list of points, quantities, and hypotheses.
- **`CircleThrough` returns unevaluated** if points are not explicit (fine inside `GeometricScene`).
- **`GeometricSolveValues` may return multiple sign-branches** — for generic triangles, only one branch matches the actual numeric instance.
- **Nonexistent symbols.** `GeometricTransformationFunction`, `Conic`, `Parabola`, `Ellipse`, `Hyperbola`, `PointFigure` have no reference pages (404). For non-circular conics use analytic forms (`Ellipsoid`, `ImplicitRegion`); transformation *functions* come from `AffineTransform` and friends.
- **`ImplicitRegion` is analytic, not synthetic.** It's not in the `GeometricScene` vocabulary; the tutorial implicitly contrasts the two.

## 6. Examples relevant to Euclid's Elements

### Equilateral triangle (Euclid I.1)

```wolfram
GeometricScene[ { a, b, c },
  { GeometricStep[ { Line[ { a, b } ] }, "Segment AB" ],
    GeometricStep[ { Circle[ a, EuclideanDistance[ a, b ] ],
                     Circle[ b, EuclideanDistance[ a, b ] ] }, "Two circles" ],
    GeometricStep[ { c \[Element] Circle[ a, EuclideanDistance[ a, b ] ],
                     c \[Element] Circle[ b, EuclideanDistance[ a, b ] ],
                     Triangle[ { a, b, c } ] }, "Equilateral triangle ABC" ] } ]
```

### Perpendicular bisector

```wolfram
PerpendicularBisector[ { p, q } ]                          (* InfiniteLine *)
TriangleConstruct[ { a, b, c }, { "PerpendicularBisector", a } ]
(* Three perpendicular bisectors of a triangle meet at the circumcenter. *)
```

### Angle bisector

```wolfram
AngleBisector[ { q1, p, q2 } ]                             (* interior, InfiniteLine *)
AngleBisector[ { q1, p, q2 }, "Exterior" ]
```

### Circle through given points

```wolfram
CircleThrough[ { p1, p2, p3 } ]
CircleThrough[ { p1, p2 }, q ]                             (* given centre *)
CircleThrough[ { p1, p2 }, q, r ]                          (* centre + radius *)
```

### Point on intersection of two circles

```wolfram
c \[Element] Circle[ a, r ]
c \[Element] Circle[ b, r ]
```

### Thales's theorem (Euclid III.31)

```wolfram
scene = GeometricScene[ { a, b, c, o },
  { Triangle[ { a, b, c } ], CircleThrough[ { a, b, c }, o ],
    o \[Element] Line[ { a, c } ] } ];
FindGeometricConjectures[ scene ]
(* GeometricAssertion[{Line[{a,b}], Line[{b,c}]}, "Perpendicular"] *)
```

### Pythagoras-style solve

```wolfram
scene = GeometricScene[ { { a, b, c }, { h } },
  { Triangle[ { a, b, c } ],
    GeometricAssertion[ { Line[ { a, b } ], Line[ { b, c } ] }, "Perpendicular" ],
    EuclideanDistance[ a, b ] == 3,
    EuclideanDistance[ b, c ] == 4,
    EuclideanDistance[ a, c ] == h } ];
GeometricSolveValues[ scene, h ]   (* {5} *)
```

### Concurrence / collinearity / tangency assertions

```wolfram
GeometricAssertion[ { c1, c2, c3 }, "PairwiseTangent" ]
GeometricAssertion[ { l1, l2, l3 }, { "Concurrent", p } ]
GeometricAssertion[ { p1, p2, p3 }, "Collinear" ]
```

## 7. Related reference pages

| Symbol | URL |
|---|---|
| GeometricScene | https://reference.wolfram.com/language/ref/GeometricScene.html |
| RandomInstance | https://reference.wolfram.com/language/ref/RandomInstance.html |
| FindGeometricConjectures | https://reference.wolfram.com/language/ref/FindGeometricConjectures.html |
| GeometricAssertion | https://reference.wolfram.com/language/ref/GeometricAssertion.html |
| GeometricTest | https://reference.wolfram.com/language/ref/GeometricTest.html |
| GeometricSolveValues | https://reference.wolfram.com/language/ref/GeometricSolveValues.html |
| GeometricStep | https://reference.wolfram.com/language/ref/GeometricStep.html |
| GeometricStylingRules | https://reference.wolfram.com/language/ref/GeometricStylingRules.html |
| UnconstrainedParameters | https://reference.wolfram.com/language/ref/UnconstrainedParameters.html |
| GeometricTransformation | https://reference.wolfram.com/language/ref/GeometricTransformation.html |
| Triangle / Polygon / Circle / Disk / Line | (same site, `/ref/<Name>.html`) |
| InfiniteLine / HalfLine / Point | (same) |
| CircleThrough / CircularArcThrough / InfiniteLineThrough | (same) |
| Midpoint / PerpendicularBisector / AngleBisector | (same) |
| TriangleCenter / TriangleConstruct / TriangleMeasurement | (same) |
| PlanarAngle / Parallelogram / Rectangle / RegularPolygon | (same) |
| RegionMember / ImplicitRegion | (same) |

**Confirmed not to exist on the doc site:** `GeometricTransformationFunction`, `Conic`, `Parabola`, `Ellipse`, `Hyperbola`, `PointFigure`.

## 8. Mental model

Think of `GeometricScene` as a constraint system over symbolic points and scalars:

- *primitives* (Circle, Triangle, Polygon, InfiniteLine, …) act as both diagram objects and nondegeneracy constraints;
- *constructions* (PerpendicularBisector, AngleBisector, Midpoint, TriangleConstruct, CircleThrough, …) act as derived objects that automatically carry their defining constraints;
- *assertions* (`GeometricAssertion`, `==`, `\[Element]`, inequalities) act as logical constraints;
- *conclusions* act as goal statements (either manually given or discovered).

```
declare points/scalars
  -> assemble hypotheses (primitives + constructions + assertions + steps)
    -> RandomInstance (visualise/sample)
    -> FindGeometricConjectures (auto-discover theorems)
    -> GeometricSolveValues (solve quantities)
    -> GeometricTest / GeometricAssertion (named property language)
```
