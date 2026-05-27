# Book I, Definition 15

[LLM Generated]

## Statement

A *circle* is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure equal one another.

## Geometric Scene

```wolfram
geometricSceneBookIDef15 = GeometricScene[
  { a, b, c },
  {
    GeometricStep[ { Circle[ a, EuclideanDistance[ a, b ] ] }, "Circle with center A" ],
    GeometricStep[ { Line[ { a, b } ] }, "A radius to the boundary" ],
    GeometricStep[ { c \[Element] Circle[ a, EuclideanDistance[ a, b ] ], Line[ { a, c } ] }, "Another radius, equal to the first" ]
  }
];
```

```wolfram
RandomInstance[ geometricSceneBookIDef15, RandomSeeding -> 0 ]
```

## Infrageometric Scene

```wolfram
infraSceneBookIDef15[ graph_Graph ] := Module[
  { centre, r, b1, b2 },
  centre = First @ FindInfraPoint[ graph, "From" -> "Center" ];
  r = Quotient[ GraphDiameter @ graph, 4 ];
  { b1, b2 } = FindInfraPoint[ graph, 2, "From" -> ( centre -> { r, r } ) ];
  InfraScene[
    { o, cir, u, rad1, v, rad2 },
    {
      InfraGeometricStep[ { o == centre }, "Center" ],
      InfraGeometricStep[ { cir == InfraCircle[ o, r ] }, "Circle: the boundary line" ],
      InfraGeometricStep[ { u == b1 }, "A boundary point" ],
      InfraGeometricStep[ { rad1 == InfraSegment[ o, u ] }, "A radius" ],
      InfraGeometricStep[ { v == b2 }, "Another boundary point" ],
      InfraGeometricStep[ { rad2 == InfraSegment[ o, v ] }, "Another radius, equal to the first" ]
    }
  ]
];
```

```wolfram
Needs[ "WolframInstitute`SyntheticInfrageometry`" ];
SeedRandom[ 0 ];
InfraSceneViewer[ infraSceneBookIDef15[ # ], # ] & @
  MeshConnectivityGraph @ DiscretizeRegion[ Rectangle[ ], MaxCellMeasure -> 0.005 ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/defI15.html

## Dependencies

- *(none — a foundational definition)*
