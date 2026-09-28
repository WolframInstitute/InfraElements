# Book I, Definition 20

[LLM Generated]

## Statement

Of trilateral figures, an *equilateral triangle* is that which has its three sides equal, an *isosceles triangle* that which has two of its sides alone equal, and a *scalene triangle* that which has its three sides unequal.

## Geometric Scene

```wolfram
geometricSceneBookIDef20 = GeometricScene[
  { a, b, c },
  {
    GeometricStep[ { Triangle[ { a, b, c } ] }, "Trilateral figure ABC" ]
  }
];
```

```wolfram
RandomInstance[ geometricSceneBookIDef20, RandomSeeding -> 0 ]
```

## Infrageometric Scene

```wolfram
infraSceneBookIDef20[ graph_Graph ] := Module[
  { centre, a, b, c },
  centre = First @ FindInfraPoint[ graph, "From" -> "Center" ];
  { a, b, c } = FindInfraPoint[ graph, 3, "From" -> ( centre -> { 0, Quotient[ GraphDiameter @ graph, 4 ] } ) ];
  InfraScene[
    { p, q, s, t },
    {
      InfraGeometricStep[ { p == a }, "Vertex A" ],
      InfraGeometricStep[ { q == b }, "Vertex B" ],
      InfraGeometricStep[ { s == c }, "Vertex C" ],
      InfraGeometricStep[ { t == InfraTriangle[ { p, q, s } ] }, "Trilateral figure ABC" ]
    }
  ]
];
```

```wolfram
Needs[ "WolframInstitute`InfraGeometry`" ];
SeedRandom[ 0 ];
InfraSceneViewer[ infraSceneBookIDef20[ # ], # ] & @
  MeshConnectivityGraph @ DiscretizeRegion[ Rectangle[ ], MaxCellMeasure -> 0.005 ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/defI20.html

## Dependencies

- *(none — a foundational definition)*
