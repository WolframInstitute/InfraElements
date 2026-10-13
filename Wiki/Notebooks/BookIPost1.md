# Book I, Postulate 1

**[[ LLM Generated ]]**

## Statement

To draw a straight line from any point to any point.

## Setup

```wolfram
PacletDirectoryLoad @ FileNameJoin[ {
  NotebookDirectory[ ], "..", "..", "..", "SubProjectsMain",
  "InfraGeometry", "InfraGeometry", "InfraGeometry" } ];
Needs[ "WolframInstitute`InfraGeometry`" ];
```

## Geometric Scene

```wolfram
geometricSceneBookIPost1 = GeometricScene[ { BookIPost1`a, BookIPost1`b }, {
  GeometricStep[ { Line[ { BookIPost1`a, BookIPost1`b } ] }, "Straight line from A to B" ]
} ];
```

```wolfram
RandomInstance[ geometricSceneBookIPost1, RandomSeeding -> 0 ]
```

## Infrageometric Scene

A shortest path joins the given vertices. Several shortest paths can join the same pair.

The columns below are the Large mesh, square grid, and hexagonal tiling, in that order. All three constructions use hop distance; the embedding is used only for drawing.

```wolfram
infraSceneBookIPost1[ graph_Graph ] :=
  With[
    { center = First @ GraphCenter[ graph ] },
    { endpoint = First @ Keys @ Select[
        AssociationThread[ VertexList[ graph ], GraphDistance[ graph, center ] ], # == 4 & ] },
    InfraScene[ { pBookIPost1, qBookIPost1, sBookIPost1 }, {
      InfraStep[ { pBookIPost1 == InfraPoint[ center ] }, "Point A" ],
      InfraStep[ { qBookIPost1 == InfraPoint[ endpoint ] }, "Point B" ],
      InfraStep[ { sBookIPost1 == InfraSegment[ pBookIPost1, qBookIPost1, "Branches" -> 1 ] }, "A shortest segment AB" ]
    } ] ]
```

```wolfram
SeedRandom[ 0 ];
GraphicsGrid[ {
  Map[
    name |-> With[
      { graph = ( SeedRandom[ 0 ]; InfraSubstrate[ name, "Large", "KeepCoordinates" -> True ] ) },
      { scene = infraSceneBookIPost1[ graph ] },
      { instance = RandomInfraInstance[ scene, graph, "NextVertexFunction" -> Identity ] },
      { center = First @ GraphCenter[ graph ] },
      { window = MinMax /@ Transpose[ GraphEmbedding[ graph ][[
          VertexIndex[ graph, # ] & /@ VertexList @ NeighborhoodGraph[ graph, center, 8 ] ]] ] },
      InfraSubstrateHighlight[ graph, {
        InfraWalk[ InfraSceneInstance[ instance, sBookIPost1 ] ] -> StandardBlue,
        InfraSceneInstance[ instance, pBookIPost1 ] -> StandardRed,
        InfraSceneInstance[ instance, qBookIPost1 ] -> StandardOrange
      }, PlotRange -> window ] ],
    { "SquareMeshGraph", "SquareGridGraph", "HexagonalTilingGraph" } ]
} ]
```

## Interactive construction

```wolfram
SeedRandom[ 0 ];
With[
  { graph = InfraSubstrate[ "SquareGridGraph", "Large", "KeepCoordinates" -> True ] },
  InfraSceneViewer[ infraSceneBookIPost1[ graph ], graph ] ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/post1.html

## Dependencies

- *(none — a foundational postulate)*
