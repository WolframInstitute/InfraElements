# Per-item notebook convention

The template every Definition / Postulate / Common Notion / Proposition notebook follows. Locked in with `BookIProp1` (equilateral triangle). Reproduce it for every other item.

## Naming

- **File** (source and `.nb`): `Book<Roman><Kind><Num>` — **dot-free**. Examples: `BookIProp1`, `BookIDef15`, `BookIPost1`, `BookICN1`. Book X definition groups: `BookXDefII3` (group roman + number).
- **Source** lives at `Wiki/Notebooks/<name>.md`; the generated notebook at `Notebooks/<name>.nb` (gitignored).
- **Symbols defined inside a notebook carry the item as a suffix** so notebooks sharing a kernel never collide: `geometricSceneBookIProp1`, `infraSceneBookIProp1`. camelCase — underscores are illegal in Wolfram symbol names (`_` is the pattern blank). If a real separator is ever wanted, use a context mark (`` BookIProp1`geometricScene ``), not an underscore.

## Markdown structure

```markdown
# Book <Roman>, <Kind> <Num>

[LLM Generated]

## Statement

<pure statement, verbatim from D. Joyce — no extra prose>

## Proof

<pure proof, verbatim — propositions only; no marginal-reference clutter>

## Geometric Scene

<code only>

## Infrageometric Scene

<code only>

## Source

D. Joyce, *Euclid's Elements*, <link to the item's source HTML>

## Dependencies

- [<Kind> <Num>](Book<Roman><Kind><Num>.nb) — <that item's statement>
- ...
```

Rules:
- `[LLM Generated]` sits directly under the title.
- **Only Statement and Proof carry prose** — both verbatim from D. Joyce. Every other section is code only (no explanatory paragraphs, no comparison essays).
- **Dependencies link to the corresponding notebooks** (`Book…Kind…Num.nb`, sibling files in `Notebooks/`) and append each dependency's statement after an em dash. Dependency list comes from `Wiki/Resources/DependencyGraph.m`.

## Cell hierarchy (applied by the generator)

- The `#` title becomes a **Section** cell.
- Every `##` heading becomes a **Subsection** cell.
- ` ```wolfram ` fences become **Input** cells; untagged fences become **CodeText**.
- **Definition cells become initialization cells** — a cell is init iff it contains `:=` or is a single-statement `name = …` assignment. Calling/display cells (ending in a bare expression like `InfraSceneViewer[…]` or `RandomInstance[…]`) stay normal.
- Code formatting is preserved as written (no `ToBoxes` reformatting).

## Geometric Scene section

Classical Wolfram `GeometricScene` with stepwise `GeometricStep` (its built-in interactive stepper is the classical viewer), then a display cell.

```wolfram
geometricSceneBookIProp1 = GeometricScene[
  { a, b, c },
  {
    GeometricStep[ { Line[ { a, b } ] }, "Given segment AB" ],
    GeometricStep[ { Circle[ a, EuclideanDistance[ a, b ] ] }, "Circle centred A, radius AB" ],
    GeometricStep[ { Circle[ b, EuclideanDistance[ a, b ] ] }, "Circle centred B, radius AB" ],
    GeometricStep[ { c \[Element] Circle[ a, EuclideanDistance[ a, b ] ], c \[Element] Circle[ b, EuclideanDistance[ a, b ] ] }, "Apex C on both circles" ],
    GeometricStep[ { Triangle[ { a, b, c } ] }, "Triangle ABC" ]
  }
];
```

```wolfram
RandomInstance[ geometricSceneBookIProp1, RandomSeeding -> 0 ]
```

## Infrageometric Scene section

A scene-building **function of the graph** (init cell), then a single **calling cell** that loads the paclet, seeds, and applies the function directly to the graph (no intermediate `mesh` variable, no separate setup cell).

```wolfram
infraSceneBookIProp1[ graph_Graph ] := Module[
  { centre, a, b, r },
  centre = First @ FindInfraPoint[ graph, "From" -> "Center" ];
  { a, b } = FindInfraPoint[ graph, 2, "From" -> ( centre -> { 0, Quotient[ GraphDiameter @ graph, 4 ] } ) ];
  r = InfraDistance[ graph, a, b ];
  InfraScene[
    { p, q, s, cA, cB, c, t },
    {
      InfraGeometricStep[ { p == a }, "Point A" ],
      InfraGeometricStep[ { q == b }, "Point B" ],
      InfraGeometricStep[ { s == InfraSegment[ p, q ] }, "Given segment AB" ],
      InfraGeometricStep[ { cA == InfraCircle[ p, r ] }, "Circle centred A, radius AB" ],
      InfraGeometricStep[ { cB == InfraCircle[ q, r ] }, "Circle centred B, radius AB" ],
      InfraGeometricStep[ { c == InfraIntersection[ cA, cB ] }, "Apex C where the circles meet" ],
      InfraGeometricStep[ { t == InfraTriangle[ { p, q, c } ] }, "Triangle ABC" ]
    }
  ]
];
```

```wolfram
Needs[ "WolframInstitute`SyntheticInfrageometry`" ];
SeedRandom[ 0 ];
InfraSceneViewer[ infraSceneBookIProp1[ # ], # ] & @
  MeshConnectivityGraph @ DiscretizeRegion[ Rectangle[ ], MaxCellMeasure -> 0.005 ]
```

The calling cell only does `Needs` — paclet **installation** is not a notebook concern. The cloud install lines live in the top-level [`README.md`](../../README.md) (Paclets section); the kernel that evaluates/publishes the notebooks is expected to have the paclet installed already.

## Rules for the infrageometric construction

- **Allowed primitives: `InfraPoint`, `InfraSegment`, `InfraCircle`, `InfraLine`, `InfraAngle`, and the figure primitives `InfraTriangle` / `InfraPolygon`** (geodesic-sided; `InfraSegment` is the analogue of the classical given `Line[{a,b}]`, `InfraTriangle`/`InfraPolygon` of `Triangle`/`Polygon`). Do **not** use `InfraShell`, `InfraBall`, `CompleteInfraEquilateralTriangle`, or other paclet objects. (`InfraIntersection` is the scene combinator that produces a point from two circles; `InfraDistance` and the built-in `GraphCenter` / `GraphDiameter` are fine for radii / vertex selection.)
- **Correspond to the classical scene, object-for-object, respecting infra reality.** The infrageometric scene mirrors the classical `GeometricScene` step list: the same given figure (classical `Line[{a,b}]` ↔ `InfraSegment[p,q]`), the same circles, the same apex, the same result figure (classical `Triangle[{a,b,c}]` ↔ `InfraTriangle[{p,q,c}]`). The one infra-reality difference: the initial points are *found* individually (`FindInfraPoint`) before the segment is drawn, so the classical's single "given segment" step becomes "Point A", "Point B", "Given segment AB". Requires `SyntheticInfrageometry` ≥ 0.12.10.
- **Graph:** the Euclidean mesh `MeshConnectivityGraph @ DiscretizeRegion[ Rectangle[ ], MaxCellMeasure -> 0.005 ]`, applied via a pure function — don't bind it to a variable.
- **Initial points** are selected with the paclet's `FindInfraPoint` (not hand-rolled `GraphCenter`/`Select`): the centre via `FindInfraPoint[graph, "From" -> "Center"]`, then the initial vertices from the ball of radius `diameter/4` around it via `FindInfraPoint[graph, n, "From" -> (centre -> {0, Quotient[GraphDiameter@graph, 4]})]`. All initial data therefore lie within `diameter/4` of a centre point. (`FindInfraPoint` samples randomly — reproducible under the `SeedRandom[0]` in the calling cell.)
- **`InfraSceneViewer`** is the primary infrageometric visualisation (the analogue of `GeometricStep`'s stepper). No static `InfraSceneHighlight`, no per-graph labels, no explicit `Style`/colour overrides.
- **Use labeled steps.** Express the construction as `InfraGeometricStep[ { hypotheses }, "label" ]` blocks (mirroring the classical `GeometricStep` sequence) so the viewer shows a labeled step-through. Requires `SyntheticInfrageometry` ≥ 0.12.10.
- **One object per step.** Construct a single object per step where possible — don't build two objects in the same `GeometricStep` / `InfraGeometricStep` (e.g. the two circles of I.1 go in separate steps). A single object constrained several ways (e.g. an apex lying on two circles) is still one step.
- **All randomness seeded** (`SeedRandom[0]`, and `RandomSeeding -> 0` on `RandomInstance`).
- **No hacky workarounds.** If a construction can't be built cleanly (e.g. two infracircles don't intersect, so there's no apex), stop and surface it — don't paper over it.

## Working rules

- **One commit per notebook.** Each generated per-item notebook is its own commit on the `WolframInstitute/InfraElements` private repo.
- **Topological order.** A notebook only invokes definitions/constructions whose own notebooks already exist (or live in `Code/`). The dependency DAG ([DependencyGraph](../Resources/DependencyGraph.md)) enforces this ordering.
- **All randomness seeded.** `SeedRandom[0]`, and `RandomSeeding -> 0` on `RandomInstance`, for reproducibility.
- **No hacky workarounds.** If a construction can't be built cleanly (e.g. an item has no discrete analogue, or two infracircles don't intersect so there's no apex), stop and log it in [`Status.md`](../Status.md) as a blocker — don't paper over it.

## Generating the `.nb`

Single source, via the Wolfram MCP pipeline embedded in `Scripts/generate_notebooks.wls`, or batch:

```bash
wolframscript -file Scripts/generate_notebooks.wls
```

## See also

- [DependencyGraph](../Resources/DependencyGraph.md) — supplies dependency edges and statements; sets the topological order for generating notebooks
- [SyntheticGeometry](../Resources/SyntheticGeometry.md) — classical framework API
- [SyntheticInfrageometry](../Resources/SyntheticInfrageometry.md) — paclet API
