# Book I, Proposition 1

[LLM Generated]

## Statement

To construct an equilateral triangle on a given finite straight line.

## Proof

Let *AB* be the given finite straight line. It is required to construct an equilateral triangle on the straight line *AB.*

Describe the circle *BCD* with center *A* and radius *AB.* Again describe the circle *ACE* with center *B* and radius *BA.* Join the straight lines *CA* and *CB* from the point *C* at which the circles cut one another to the points *A* and *B.*

Now, since the point *A* is the center of the circle *CDB,* therefore *AC* equals *AB.* Again, since the point *B* is the center of the circle *CAE,* therefore *BC* equals *BA.* But *AC* was proved equal to *AB,* therefore each of the straight lines *AC* and *BC* equals *AB.* And things which equal the same thing also equal one another, therefore *AC* also equals *BC.* Therefore the three straight lines *AC, AB,* and *BC* equal one another.

Therefore the triangle *ABC* is equilateral, and it has been constructed on the given finite straight line *AB.* Q.E.F.

## Geometric Scene

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

## Infrageometric Scene

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
Needs[ "WolframInstitute`InfraGeometry`" ];
SeedRandom[ 0 ];
InfraSceneViewer[ infraSceneBookIProp1[ # ], # ] & @
  MeshConnectivityGraph @ DiscretizeRegion[ Rectangle[ ], MaxCellMeasure -> 0.005 ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/propI1.html

## Dependencies

- [Postulate 1](BookIPost1.nb) — To draw a straight line from any point to any point.
- [Postulate 3](BookIPost3.nb) — To describe a circle with any center and radius.
- [Definition 15](BookIDef15.nb) — A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure equal one another.
- [Definition 20](BookIDef20.nb) — Of trilateral figures, an equilateral triangle is that which has its three sides equal, an isosceles triangle that which has two of its sides alone equal, and a scalene triangle that which has its three sides unequal.
- [Common Notion 1](BookICN1.nb) — Things which equal the same thing also equal one another.
