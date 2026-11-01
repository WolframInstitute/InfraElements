# Book I, Proposition 1

**[[ LLM Generated ]]**

## Statement

To construct an equilateral triangle on a given finite straight line.

## Proof

Let *AB* be the given finite straight line. It is required to construct an equilateral triangle on the straight line *AB.*

Describe the circle *BCD* with center *A* and radius *AB.* Again describe the circle *ACE* with center *B* and radius *BA.* Join the straight lines *CA* and *CB* from the point *C* at which the circles cut one another to the points *A* and *B.*

Now, since the point *A* is the center of the circle *CDB,* therefore *AC* equals *AB.* Again, since the point *B* is the center of the circle *CAE,* therefore *BC* equals *BA.* But *AC* was proved equal to *AB,* therefore each of the straight lines *AC* and *BC* equals *AB.* And things which equal the same thing also equal one another, therefore *AC* also equals *BC.* Therefore the three straight lines *AC, AB,* and *BC* equal one another.

Therefore the triangle *ABC* is equilateral, and it has been constructed on the given finite straight line *AB.* Q.E.F.

## Setup

```wolfram
PacletDirectoryLoad @ FileNameJoin[ {
  NotebookDirectory[ ], "..", "..", "..",
  "InfraGeometry", "InfraGeometry", "InfraGeometry" } ];
Needs[ "WolframInstitute`InfraGeometry`" ];
```

## Geometric Scene

```wolfram
geometricSceneBookIProp1 = GeometricScene[ { BookIProp1`a, BookIProp1`b, BookIProp1`c }, {
  GeometricStep[ { Line[ { BookIProp1`a, BookIProp1`b } ] }, "Given segment AB" ],
  GeometricStep[ { Circle[ BookIProp1`a, EuclideanDistance[ BookIProp1`a, BookIProp1`b ] ] }, "Circle centered A, radius AB" ],
  GeometricStep[ { Circle[ BookIProp1`b, EuclideanDistance[ BookIProp1`a, BookIProp1`b ] ] }, "Circle centered B, radius AB" ],
  GeometricStep[ { BookIProp1`c \[Element] Circle[ BookIProp1`a, EuclideanDistance[ BookIProp1`a, BookIProp1`b ] ],
    BookIProp1`c \[Element] Circle[ BookIProp1`b, EuclideanDistance[ BookIProp1`a, BookIProp1`b ] ] }, "Apex C on both circles" ],
  GeometricStep[ { Triangle[ { BookIProp1`a, BookIProp1`b, BookIProp1`c } ] }, "Triangle ABC" ]
} ];
```

```wolfram
RandomInstance[ geometricSceneBookIProp1, RandomSeeding -> 0 ]
```

## Infrageometric Scene

The columns are the Large mesh, square grid, and hexagonal tiling. The first row uses exact equal-radius loci and a base of two hops. The second tests selected separating band cycles with the same exact apex conditions. The third uses exact loci and a base of one hop.

An empty construction is shown at its last completed step with the words "No exact apex". This is a failed construction on the stated data.

The exact construction preserves the equal-distance argument whenever an apex exists. Band-cycle intersection alone does not imply equal radii. On a bipartite graph an equilateral triangle with an odd side length is impossible.
The cycle bands are two to three hops on the mesh and square grid, and two to four on the hexagonal tiling.

```wolfram
infraSceneBookIProp1[ graph_Graph, kind : ( "Exact" | "Cycle" | "Odd" ) : "Exact",
    band : { _Integer, _Integer } : { 2, 3 } ] :=
  With[
    { center = First @ GraphCenter[ graph ], radius = If[ kind === "Odd", 1, 2 ] },
    { endpoint = First @ Keys @ Select[
        AssociationThread[ VertexList[ graph ], GraphDistance[ graph, center ] ], # == radius & ] },
    InfraScene[ { pBookIProp1, qBookIProp1, sBookIProp1, circleABookIProp1, circleBBookIProp1, BookIProp1`c, tBookIProp1 }, {
      InfraStep[ { pBookIProp1 == InfraPoint[ center ] }, "Point A" ],
      InfraStep[ { qBookIProp1 == InfraPoint[ endpoint ] }, "Point B" ],
      InfraStep[ { sBookIProp1 == InfraSegment[ pBookIProp1, qBookIProp1, "Branches" -> 1 ] }, "Given segment AB" ],
      InfraStep[ { circleABookIProp1 == If[ kind === "Cycle",
        InfraCircle[ pBookIProp1, band, "Branches" -> 1 ], InfraShell[ pBookIProp1, radius ] ] },
        If[ kind === "Cycle", "A separating cycle about A", "Points at exactly AB from A" ] ],
      InfraStep[ { circleBBookIProp1 == If[ kind === "Cycle",
        InfraCircle[ qBookIProp1, band, "Branches" -> 1 ], InfraShell[ qBookIProp1, radius ] ] },
        If[ kind === "Cycle", "A separating cycle about B", "Points at exactly AB from B" ] ],
      InfraStep[ { BookIProp1`c == InfraIntersection[ circleABookIProp1, circleBBookIProp1 ],
        InfraDistance[ pBookIProp1, BookIProp1`c ] == radius,
        InfraDistance[ qBookIProp1, BookIProp1`c ] == radius }, "An apex satisfying the exact equalities" ],
      InfraStep[ { tBookIProp1 == InfraSegment[ pBookIProp1, qBookIProp1, BookIProp1`c, pBookIProp1,
        "Branches" -> 1 ] }, "Equilateral boundary ABC" ]
    } ] ]
```

```wolfram
SeedRandom[ 0 ];
GraphicsGrid[ Map[
  kind |-> MapThread[
    { name, band } |-> With[
      { graph = ( SeedRandom[ 0 ]; InfraSubstrate[ name, "Large", "KeepCoordinates" -> True ] ) },
      { scene = infraSceneBookIProp1[ graph, kind, band ] },
      { instance = RandomInfraInstance[ scene, graph, "NextVertexFunction" -> Identity ] },
      { partial = If[ instance === { }, RandomInfraInstance[ scene, graph, "Steps" -> 5,
          "NextVertexFunction" -> Identity ], instance ], center = First @ GraphCenter[ graph ] },
      { window = MinMax /@ Transpose[ GraphEmbedding[ graph ][[
          VertexIndex[ graph, # ] & /@ VertexList @ NeighborhoodGraph[ graph, center, 8 ] ]] ] },
      { picture = InfraSubstrateHighlight[ graph, Join[ {
          If[ kind === "Cycle", InfraWalk[ Append[ #, First[ # ] ] & @ InfraSceneInstance[ partial, circleABookIProp1 ] ],
            InfraDensity[ graph, InfraSceneInstance[ partial, circleABookIProp1 ] ] ] -> StandardOrange,
          If[ kind === "Cycle", InfraWalk[ Append[ #, First[ # ] ] & @ InfraSceneInstance[ partial, circleBBookIProp1 ] ],
            InfraDensity[ graph, InfraSceneInstance[ partial, circleBBookIProp1 ] ] ] -> StandardGreen,
          InfraWalk[ InfraSceneInstance[ partial, sBookIProp1 ] ] -> StandardBlue,
          InfraSceneInstance[ partial, pBookIProp1 ] -> StandardRed,
          InfraSceneInstance[ partial, qBookIProp1 ] -> StandardRed },
          If[ instance === { }, { }, {
            InfraWalk[ InfraSceneInstance[ instance, tBookIProp1 ] ] -> StandardBlue,
            InfraSceneInstance[ instance, BookIProp1`c ] -> StandardPurple } ] ], PlotRange -> window ] },
      If[ instance === { }, Show[ picture, Epilog -> Text[ "No exact apex", Scaled[ { 0.5, 0.06 } ] ] ], picture ] ],
    { { "SquareMeshGraph", "SquareGridGraph", "HexagonalTilingGraph" }, { { 2, 3 }, { 2, 3 }, { 2, 4 } } } ],
  { "Exact", "Cycle", "Odd" } ] ]
```

## Interactive construction

```wolfram
SeedRandom[ 0 ];
With[
  { graph = InfraSubstrate[ "SquareGridGraph", "Large", "KeepCoordinates" -> True ] },
  InfraSceneViewer[ infraSceneBookIProp1[ graph ], graph ] ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/propI1.html

## Dependencies

- [Postulate 1](BookIPost1.nb) — To draw a straight line from any point to any point.
- [Postulate 3](BookIPost3.nb) — To describe a circle with any center and radius.
- [Definition 15](BookIDef15.nb) — A circle is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure equal one another.
- [Definition 20](BookIDef20.nb) — Of trilateral figures, an equilateral triangle is that which has its three sides equal, an isosceles triangle that which has two of its sides alone equal, and a scalene triangle that which has its three sides unequal.
- [Common Notion 1](BookICN1.nb) — Things which equal the same thing also equal one another.
