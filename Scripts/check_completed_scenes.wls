root = ParentDirectory @ DirectoryName @ ExpandFileName[ $InputFileName ];
PacletDirectoryLoad[ FileNameJoin[ { root, "..", "..", "InfraGeometry", "InfraGeometry", "InfraGeometry" } ] ];
Needs[ "WolframInstitute`InfraGeometry`" ];

items = { "BookIPost1", "BookIPost3", "BookIDef15", "BookIDef20", "BookIProp1" };
Do[
  codeBlocks = StringCases[ Import[ FileNameJoin[ { root, "Wiki", "Notebooks", item <> ".md" } ], "Text" ],
    RegularExpression[ "(?s)```wolfram[ ]*\\n(.*?)\\n```" ] -> "$1" ];
  Scan[ ToExpression, Select[ codeBlocks, StringContainsQ[ #, ":=" ] & ] ], { item, items } ];

checks = <| |>;
records = <| |>;
Do[
  SeedRandom[ 0 ];
  graph = InfraSubstrate[ name, "Large", "KeepCoordinates" -> True ];
  band = If[ name === "HexagonalTilingGraph", { 2, 4 }, { 2, 3 } ];
  center = First @ GraphCenter[ graph ];
  distances = AssociationThread[ VertexList[ graph ], GraphDistance[ graph, center ] ];
  record = <| "Vertices" -> VertexCount[ graph ], "Edges" -> EdgeCount[ graph ], "Center" -> center,
    "Bipartite" -> BipartiteGraphQ[ graph ], "CycleBand" -> band |>;

  instance = TimeConstrained[ RandomInfraInstance[ infraSceneBookIPost1[ graph ], graph, "NextVertexFunction" -> Identity ], 30, $TimedOut ];
  path = InfraSceneInstance[ instance, sBookIPost1 ];
  checks[ name <> ": PostI.1 shortest segment" ] = ListQ[ path ] && Length[ path ] - 1 == 4 &&
    AllTrue[ Partition[ path, 2, 1 ], EdgeQ[ graph, UndirectedEdge @@ # ] & ];

  instance = TimeConstrained[ RandomInfraInstance[ infraSceneBookIPost3[ graph, band ], graph, "NextVertexFunction" -> Identity ], 30, $TimedOut ];
  circle = InfraSceneInstance[ instance, circleBookIPost3 ];
  closedCircle = Append[ circle, First[ circle ] ];
  radialDistances = distances /@ circle;
  checks[ name <> ": PostI.3 band cycle" ] = ListQ[ circle ] && Length[ circle ] >= 3 &&
    DuplicateFreeQ[ circle ] && AllTrue[ Partition[ closedCircle, 2, 1 ], EdgeQ[ graph, UndirectedEdge @@ # ] & ] &&
    Min[ radialDistances ] >= First[ band ] && Max[ radialDistances ] <= Last[ band ];
  checks[ name <> ": PostI.3 separates center" ] =
    Max[ distances /@ VertexComponent[ VertexDelete[ graph, DeleteDuplicates[ circle ] ], center ] ] <= Last[ band ];
  record[ "CycleRadiusRange" ] = MinMax[ radialDistances ];

  Do[
    instance = TimeConstrained[ RandomInfraInstance[ infraSceneBookIDef15[ graph, kind, band ], graph,
      "NextVertexFunction" -> Identity ], 30, $TimedOut ];
    radii = GraphDistance[ graph, InfraSceneInstance[ instance, oBookIDef15 ], # ] & /@
      InfraSceneInstance[ instance, { uBookIDef15, vBookIDef15 } ];
    checks[ name <> ": DefI.15 " <> kind <> " radii" ] = If[ kind === "Cycle", Less @@ radii, radii === { 2, 2 } ];
    record[ "Definition15" <> kind <> "Radii" ] = radii,
    { kind, { "Cycle", "Shell" } } ];
  shell = Keys @ Select[ distances, # == 2 & ];
  checks[ name <> ": exact shell parity" ] = ! BipartiteGraphQ[ graph ] || EdgeCount[ Subgraph[ graph, shell ] ] == 0;

  triangleRecords = <| |>;
  Do[
    instance = TimeConstrained[ RandomInfraInstance[ infraSceneBookIDef20[ graph, kind ], graph,
      "NextVertexFunction" -> Identity ], 30, $TimedOut ];
    points = InfraSceneInstance[ instance, { pBookIDef20, qBookIDef20, BookIDef20`c } ];
    lengths = GraphDistance[ graph, #1, #2 ] & @@@ Subsets[ points, { 2 } ];
    boundary = InfraSceneInstance[ instance, tBookIDef20 ];
    expected = Switch[ kind, "Equilateral", { 2, 2, 2 }, "Isosceles", { 2, 3, 3 }, "Scalene", { 3, 4, 5 } ];
    checks[ name <> ": DefI.20 " <> kind <> " side lengths" ] = Sort[ lengths ] === expected;
    checks[ name <> ": DefI.20 " <> kind <> " shortest legs" ] = First[ boundary ] === Last[ boundary ] &&
      Length[ boundary ] - 1 == Total[ lengths ] && AllTrue[ Partition[ boundary, 2, 1 ], EdgeQ[ graph, UndirectedEdge @@ # ] & ];
    triangleRecords[ kind ] = <| "SideLengths" -> lengths, "SimpleSelectedBoundary" -> DuplicateFreeQ[ Most[ boundary ] ] |> ,
    { kind, { "Equilateral", "Isosceles", "Scalene" } } ];
  record[ "Definition20" ] = triangleRecords;

  propositionRecords = <| |>;
  Do[
    scene = infraSceneBookIProp1[ graph, kind, band ];
    instance = TimeConstrained[ RandomInfraInstance[ scene, graph, "NextVertexFunction" -> Identity ], 30, $TimedOut ];
    checks[ name <> ": PropI.1 " <> kind <> " decided" ] = instance === { } || MatchQ[ instance, _InfraSceneInstance ];
    If[ MatchQ[ instance, _InfraSceneInstance ],
      points = InfraSceneInstance[ instance, { pBookIProp1, qBookIProp1, BookIProp1`c } ];
      lengths = GraphDistance[ graph, #1, #2 ] & @@@ Subsets[ points, { 2 } ];
      checks[ name <> ": PropI.1 " <> kind <> " equality" ] = SameQ @@ lengths;
      propositionRecords[ kind ] = <| "Result" -> "Solved", "SideLengths" -> lengths |>,
      propositionRecords[ kind ] = <| "Result" -> If[ instance === { }, "Empty", "Unresolved" ] |> ];
    If[ kind === "Exact", checks[ name <> ": PropI.1 even example exists" ] = MatchQ[ instance, _InfraSceneInstance ] ];
    If[ kind === "Odd" && BipartiteGraphQ[ graph ], checks[ name <> ": PropI.1 odd parity obstruction" ] = instance === { } ],
    { kind, { "Exact", "Cycle", "Odd" } } ];
  record[ "Proposition1" ] = propositionRecords;
  records[ name ] = record;
  Print[ { name, propositionRecords, triangleRecords } ],
  { name, { "SquareMeshGraph", "SquareGridGraph", "HexagonalTilingGraph" } } ];

report = TestReport[ KeyValueMap[ { key, value } |-> VerificationTest[ value, True, TestID -> key ], checks ] ];
output = <| "Date" -> "2026-10-13", "WolframVersion" -> $Version, "PacletVersion" -> "2.7.1",
  "TestsSucceeded" -> report[ "TestsSucceededCount" ], "TestsFailed" -> report[ "TestsFailedCount" ],
  "Checks" -> checks, "Substrates" -> records |>;
Export[ FileNameJoin[ { root, "Code", "Artifacts", "EuclidCompletedReview_LLM_261013", "SceneVerification.json" } ], output, "RawJSON" ];
Print[ KeyTake[ output, { "TestsSucceeded", "TestsFailed" } ] ];
If[ report[ "TestsFailedCount" ] > 0, Exit[ 1 ] ];
