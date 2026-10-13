# Book I, Definition 20

**[[ LLM Generated ]]**

## Statement

Of trilateral figures, an *equilateral triangle* is that which has its three sides equal, an *isosceles triangle* that which has two of its sides alone equal, and a *scalene triangle* that which has its three sides unequal.

## Setup

```wolfram
PacletDirectoryLoad @ FileNameJoin[ {
  NotebookDirectory[ ], "..", "..", "..", "SubProjectsMain",
  "InfraGeometry", "InfraGeometry", "InfraGeometry" } ];
Needs[ "WolframInstitute`InfraGeometry`" ];
```

## Geometric Scene

```wolfram
geometricSceneBookIDef20[ kind_String ] :=
  With[
    { lengths = Switch[ kind, "Equilateral", { 2, 2, 2 }, "Isosceles", { 2, 3, 3 }, "Scalene", { 4, 3, 5 } ] },
    { ab = lengths[[ 1 ]], ac = lengths[[ 2 ]], bc = lengths[[ 3 ]] },
    GeometricScene[ { BookIDef20`a, BookIDef20`b, BookIDef20`c }, {
      GeometricStep[ {
        Triangle[ { BookIDef20`a, BookIDef20`b, BookIDef20`c } ],
        EuclideanDistance[ BookIDef20`a, BookIDef20`b ] == ab,
        EuclideanDistance[ BookIDef20`a, BookIDef20`c ] == ac,
        EuclideanDistance[ BookIDef20`b, BookIDef20`c ] == bc
      }, kind ]
    } ] ]
```

```wolfram
GraphicsRow[ ( kind |-> RandomInstance[ geometricSceneBookIDef20[ kind ], RandomSeeding -> 0 ][ "Graphics" ] ) /@
  { "Equilateral", "Isosceles", "Scalene" } ]
```

## Infrageometric Scene

The columns are the Large mesh, square grid, and hexagonal tiling. The rows are equilateral, isosceles, and scalene.

The classification uses the three endpoint distances. Three shortest legs give an ordered closed boundary; the legs can overlap, and no filled triangle is supplied.

```wolfram
infraSceneBookIDef20[ graph_Graph, kind : ( "Equilateral" | "Isosceles" | "Scalene" ) : "Equilateral" ] :=
  With[
    { center = First @ GraphCenter[ graph ], lengths = Switch[ kind,
        "Equilateral", { 2, 2, 2 }, "Isosceles", { 2, 3, 3 }, "Scalene", { 4, 3, 5 } ] },
    { endpoint = First @ Keys @ Select[
        AssociationThread[ VertexList[ graph ], GraphDistance[ graph, center ] ], # == First[ lengths ] & ] },
    InfraScene[ { pBookIDef20, qBookIDef20, BookIDef20`c, tBookIDef20 }, {
      InfraStep[ { pBookIDef20 == InfraPoint[ center ] }, "Vertex A" ],
      InfraStep[ { qBookIDef20 == InfraPoint[ endpoint ] }, "Vertex B" ],
      InfraStep[ { BookIDef20`c == InfraIntersection[
        InfraShell[ pBookIDef20, lengths[[ 2 ]] ], InfraShell[ qBookIDef20, lengths[[ 3 ]] ] ] }, "Vertex C with prescribed side lengths" ],
      InfraStep[ { tBookIDef20 == InfraSegment[ pBookIDef20, qBookIDef20, BookIDef20`c, pBookIDef20,
        "Branches" -> 1 ] }, "Three shortest legs forming a closed boundary" ]
    } ] ]
```

```wolfram
SeedRandom[ 0 ];
GraphicsGrid[ Map[
  kind |-> Map[
    name |-> With[
      { graph = ( SeedRandom[ 0 ]; InfraSubstrate[ name, "Large", "KeepCoordinates" -> True ] ) },
      { instance = RandomInfraInstance[ infraSceneBookIDef20[ graph, kind ], graph, "NextVertexFunction" -> Identity ] },
      { center = First @ GraphCenter[ graph ] },
      { window = MinMax /@ Transpose[ GraphEmbedding[ graph ][[
          VertexIndex[ graph, # ] & /@ VertexList @ NeighborhoodGraph[ graph, center, 8 ] ]] ] },
      InfraSubstrateHighlight[ graph, {
        InfraWalk[ InfraSceneInstance[ instance, tBookIDef20 ] ] -> StandardBlue,
        InfraSceneInstance[ instance, pBookIDef20 ] -> StandardRed,
        InfraSceneInstance[ instance, qBookIDef20 ] -> StandardOrange,
        InfraSceneInstance[ instance, BookIDef20`c ] -> StandardGreen
      }, PlotRange -> window ] ],
    { "SquareMeshGraph", "SquareGridGraph", "HexagonalTilingGraph" } ],
  { "Equilateral", "Isosceles", "Scalene" } ] ]
```

## Interactive construction

```wolfram
SeedRandom[ 0 ];
With[
  { graph = InfraSubstrate[ "SquareGridGraph", "Large", "KeepCoordinates" -> True ] },
  InfraSceneViewer[ infraSceneBookIDef20[ graph ], graph ] ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/defI20.html

## Dependencies

- *(none — a foundational definition)*
