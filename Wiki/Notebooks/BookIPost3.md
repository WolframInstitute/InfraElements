# Book I, Postulate 3

**[[ LLM Generated ]]**

## Statement

To describe a circle with any center and radius.

## Setup

```wolfram
PacletDirectoryLoad @ FileNameJoin[ {
  NotebookDirectory[ ], "..", "..", "..",
  "InfraGeometry", "InfraGeometry", "InfraGeometry" } ];
Needs[ "WolframInstitute`InfraGeometry`" ];
```

## Geometric Scene

```wolfram
geometricSceneBookIPost3 = GeometricScene[ { BookIPost3`a, BookIPost3`b }, {
  GeometricStep[ { Line[ { BookIPost3`a, BookIPost3`b } ] }, "Radius AB" ],
  GeometricStep[ { Circle[ BookIPost3`a, EuclideanDistance[ BookIPost3`a, BookIPost3`b ] ] },
    "Circle with center A and radius AB" ]
} ];
```

```wolfram
RandomInstance[ geometricSceneBookIPost3, RandomSeeding -> 0 ]
```

## Infrageometric Scene

The columns are the Large mesh, square grid, and hexagonal tiling. The radial band is two to three hops on the mesh and square grid, and two to four on the hexagonal tiling.

This is a band version of the postulate. It neither makes every radius equal to AB nor requires the given radius point to lie on the selected cycle.

```wolfram
infraSceneBookIPost3[ graph_Graph, band : { _Integer, _Integer } : { 2, 3 } ] :=
  With[
    { center = First @ GraphCenter[ graph ] },
    { endpoint = First @ Keys @ Select[
        AssociationThread[ VertexList[ graph ], GraphDistance[ graph, center ] ], # == 2 & ] },
    InfraScene[ { pBookIPost3, qBookIPost3, sBookIPost3, circleBookIPost3 }, {
      InfraStep[ { pBookIPost3 == InfraPoint[ center ] }, "Center A" ],
      InfraStep[ { qBookIPost3 == InfraPoint[ endpoint ] }, "Radius point B" ],
      InfraStep[ { sBookIPost3 == InfraSegment[ pBookIPost3, qBookIPost3, "Branches" -> 1 ] }, "Radius AB" ],
      InfraStep[ { circleBookIPost3 == InfraCircle[ pBookIPost3, band, "Branches" -> 1 ] },
        "A shortest separating cycle in the prescribed radial band" ]
    } ] ]
```

```wolfram
SeedRandom[ 0 ];
GraphicsGrid[ {
  MapThread[
    { name, band } |-> With[
      { graph = ( SeedRandom[ 0 ]; InfraSubstrate[ name, "Large", "KeepCoordinates" -> True ] ) },
      { scene = infraSceneBookIPost3[ graph, band ] },
      { instance = RandomInfraInstance[ scene, graph, "NextVertexFunction" -> Identity ] },
      { center = First @ GraphCenter[ graph ] },
      { window = MinMax /@ Transpose[ GraphEmbedding[ graph ][[
          VertexIndex[ graph, # ] & /@ VertexList @ NeighborhoodGraph[ graph, center, 8 ] ]] ] },
      InfraSubstrateHighlight[ graph, {
        InfraWalk[ Append[ #, First[ # ] ] & @ InfraSceneInstance[ instance, circleBookIPost3 ] ] -> StandardBlue,
        InfraWalk[ InfraSceneInstance[ instance, sBookIPost3 ] ] -> StandardOrange,
        InfraSceneInstance[ instance, pBookIPost3 ] -> StandardRed,
        InfraSceneInstance[ instance, qBookIPost3 ] -> StandardOrange
      }, PlotRange -> window ] ],
    { { "SquareMeshGraph", "SquareGridGraph", "HexagonalTilingGraph" }, { { 2, 3 }, { 2, 3 }, { 2, 4 } } } ]
} ]
```

## Interactive construction

```wolfram
SeedRandom[ 0 ];
With[
  { graph = InfraSubstrate[ "SquareGridGraph", "Large", "KeepCoordinates" -> True ] },
  InfraSceneViewer[ infraSceneBookIPost3[ graph ], graph ] ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/post3.html

## Dependencies

- *(none — a foundational postulate)*
