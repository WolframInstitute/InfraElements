# Book I, Postulate 1

[LLM Generated]

## Statement

To draw a straight line from any point to any point.

## Geometric Scene

```wolfram
geometricSceneBookIPost1 = GeometricScene[
  { a, b },
  {
    GeometricStep[ { Line[ { a, b } ] }, "Straight line from A to B" ]
  }
];
```

```wolfram
RandomInstance[ geometricSceneBookIPost1, RandomSeeding -> 0 ]
```

## Infrageometric Scene

```wolfram
infraSceneBookIPost1[ graph_Graph ] := Module[
  { centre, a, b },
  centre = First @ FindInfraPoint[ graph, "From" -> "Center" ];
  { a, b } = FindInfraPoint[ graph, 2, "From" -> ( centre -> { 0, Quotient[ GraphDiameter @ graph, 4 ] } ) ];
  InfraScene[
    { p, q, s },
    {
      InfraGeometricStep[ { p == a }, "Point A" ],
      InfraGeometricStep[ { q == b }, "Point B" ],
      InfraGeometricStep[ { s == InfraSegment[ p, q ] }, "Straight line from A to B" ]
    }
  ]
];
```

```wolfram
Needs[ "WolframInstitute`SyntheticInfrageometry`" ];
SeedRandom[ 0 ];
InfraSceneViewer[ infraSceneBookIPost1[ # ], # ] & @
  MeshConnectivityGraph @ DiscretizeRegion[ Rectangle[ ], MaxCellMeasure -> 0.005 ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/post1.html

## Dependencies

- *(none — a foundational postulate)*
