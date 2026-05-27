# Book I, Postulate 3

[LLM Generated]

## Statement

To describe a circle with any center and radius.

## Geometric Scene

```wolfram
geometricSceneBookIPost3 = GeometricScene[
  { a, b },
  {
    GeometricStep[ { Line[ { a, b } ] }, "Radius AB" ],
    GeometricStep[ { Circle[ a, EuclideanDistance[ a, b ] ] }, "Circle with center A and radius AB" ]
  }
];
```

```wolfram
RandomInstance[ geometricSceneBookIPost3, RandomSeeding -> 0 ]
```

## Infrageometric Scene

```wolfram
infraSceneBookIPost3[ graph_Graph ] := Module[
  { centre, a, b, r },
  centre = First @ FindInfraPoint[ graph, "From" -> "Center" ];
  { a, b } = FindInfraPoint[ graph, 2, "From" -> ( centre -> { 0, Quotient[ GraphDiameter @ graph, 4 ] } ) ];
  r = InfraDistance[ graph, a, b ];
  InfraScene[
    { p, q, s, cir },
    {
      InfraGeometricStep[ { p == a }, "Center A" ],
      InfraGeometricStep[ { q == b }, "Radius point B" ],
      InfraGeometricStep[ { s == InfraSegment[ p, q ] }, "Radius AB" ],
      InfraGeometricStep[ { cir == InfraCircle[ p, r ] }, "Circle with center A and radius AB" ]
    }
  ]
];
```

```wolfram
Needs[ "WolframInstitute`SyntheticInfrageometry`" ];
SeedRandom[ 0 ];
InfraSceneViewer[ infraSceneBookIPost3[ # ], # ] & @
  MeshConnectivityGraph @ DiscretizeRegion[ Rectangle[ ], MaxCellMeasure -> 0.005 ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/post3.html

## Dependencies

- *(none — a foundational postulate)*
