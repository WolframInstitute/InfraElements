# Book I, Definition 15

**[[ LLM Generated ]]**

## Statement

A *circle* is a plane figure contained by one line such that all the straight lines falling upon it from one point among those lying within the figure equal one another.

## Setup

```wolfram
PacletDirectoryLoad @ FileNameJoin[ {
  NotebookDirectory[ ], "..", "..", "..", "SubProjectsMain",
  "InfraGeometry", "InfraGeometry", "InfraGeometry" } ];
Needs[ "WolframInstitute`InfraGeometry`" ];
```

## Geometric Scene

```wolfram
geometricSceneBookIDef15 = GeometricScene[ { BookIDef15`a, BookIDef15`b, BookIDef15`c }, {
  GeometricStep[ { Circle[ BookIDef15`a, 2 ] }, "Circle with center A" ],
  GeometricStep[ { BookIDef15`b \[Element] Circle[ BookIDef15`a, 2 ], Line[ { BookIDef15`a, BookIDef15`b } ] }, "A radius" ],
  GeometricStep[ { BookIDef15`c \[Element] Circle[ BookIDef15`a, 2 ], Line[ { BookIDef15`a, BookIDef15`c } ] },
    "Another radius, equal to the first" ]
} ];
```

```wolfram
RandomInstance[ geometricSceneBookIDef15, RandomSeeding -> 0 ]
```

## Infrageometric Scene

The columns are the Large mesh, square grid, and hexagonal tiling. The first row shows a separating cycle with two unequal radii. The second shows two equal radii to the exact distance shell.

A connected boundary and an equal-radius locus are distinct graph constructions. On the square and hexagonal graphs an exact shell has no edges.
The cycle bands are two to three hops on the mesh and square grid, and two to four on the hexagonal tiling.

```wolfram
infraSceneBookIDef15[ graph_Graph, kind : ( "Cycle" | "Shell" ) : "Cycle",
    band : { _Integer, _Integer } : { 2, 3 } ] :=
  With[
    { center = First @ GraphCenter[ graph ] },
    InfraScene[ { oBookIDef15, circleBookIDef15, uBookIDef15, vBookIDef15, rBookIDef15, sBookIDef15 }, {
      InfraStep[ { oBookIDef15 == InfraPoint[ center ] }, "Center A" ],
      InfraStep[ { circleBookIDef15 == If[ kind === "Cycle",
          InfraCircle[ oBookIDef15, band, "Branches" -> 1 ], InfraShell[ oBookIDef15, 2 ] ] },
        If[ kind === "Cycle", "A separating boundary cycle", "The exact equal-radius locus" ] ],
      InfraStep[ { uBookIDef15 == InfraRegionNearest[ circleBookIDef15, oBookIDef15 ] }, "A nearest boundary point" ],
      InfraStep[ { rBookIDef15 == InfraSegment[ oBookIDef15, uBookIDef15, "Branches" -> 1 ] }, "A shortest radius" ],
      InfraStep[ { vBookIDef15 == InfraIntersection[ circleBookIDef15, circleBookIDef15 ],
        If[ kind === "Cycle", InfraDistance[ oBookIDef15, vBookIDef15 ] > InfraDistance[ oBookIDef15, uBookIDef15 ],
          InfraGeometricAssertion[ { uBookIDef15, vBookIDef15 }, "Distinct" ] ] },
        If[ kind === "Cycle", "A boundary point with a longer radius", "Another point with the same radius" ] ],
      InfraStep[ { sBookIDef15 == InfraSegment[ oBookIDef15, vBookIDef15, "Branches" -> 1 ] }, "The second radius" ]
    } ] ]
```

```wolfram
SeedRandom[ 0 ];
GraphicsGrid[ Map[
  kind |-> MapThread[
    { name, band } |-> With[
      { graph = ( SeedRandom[ 0 ]; InfraSubstrate[ name, "Large", "KeepCoordinates" -> True ] ) },
      { instance = RandomInfraInstance[ infraSceneBookIDef15[ graph, kind, band ], graph, "NextVertexFunction" -> Identity ] },
      { center = First @ GraphCenter[ graph ] },
      { window = MinMax /@ Transpose[ GraphEmbedding[ graph ][[
          VertexIndex[ graph, # ] & /@ VertexList @ NeighborhoodGraph[ graph, center, 8 ] ]] ] },
      InfraSubstrateHighlight[ graph, {
        If[ kind === "Cycle", InfraWalk[ Append[ #, First[ # ] ] & @ InfraSceneInstance[ instance, circleBookIDef15 ] ],
          InfraDensity[ graph, InfraSceneInstance[ instance, circleBookIDef15 ] ] ] -> StandardBlue,
        InfraWalk[ InfraSceneInstance[ instance, rBookIDef15 ] ] -> StandardOrange,
        InfraWalk[ InfraSceneInstance[ instance, sBookIDef15 ] ] -> StandardGreen,
        InfraSceneInstance[ instance, oBookIDef15 ] -> StandardRed
      }, PlotRange -> window ] ],
    { { "SquareMeshGraph", "SquareGridGraph", "HexagonalTilingGraph" }, { { 2, 3 }, { 2, 3 }, { 2, 4 } } } ],
  { "Cycle", "Shell" } ] ]
```

## Interactive construction

```wolfram
SeedRandom[ 0 ];
With[
  { graph = InfraSubstrate[ "SquareGridGraph", "Large", "KeepCoordinates" -> True ] },
  InfraSceneViewer[ infraSceneBookIDef15[ graph ], graph ] ]
```

## Source

D. Joyce, *Euclid's Elements*, http://aleph0.clarku.edu/~djoyce/java/elements/bookI/defI15.html

## Dependencies

- *(none — a foundational definition)*
