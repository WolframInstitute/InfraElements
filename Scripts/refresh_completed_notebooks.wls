root = ParentDirectory @ DirectoryName @ ExpandFileName[ $InputFileName ];
pacletRoot = FileNameJoin[ { root, "..", "..", "InfraGeometry", "InfraGeometry", "InfraGeometry" } ];
PacletDirectoryLoad[ pacletRoot ];
Needs[ "WolframInstitute`InfraGeometry`" ];

notebookDirectory = FileNameJoin[ { root, "Notebooks" } ];
artifactDirectory = FileNameJoin[ { root, "Code", "Artifacts", "EuclidCompletedReview_LLM_261013" } ];
archiveDirectory = FileNameJoin[ { notebookDirectory, "Archive", "2026-10-13-before-refresh" } ];
Scan[ directory |-> If[ ! DirectoryQ[ directory ], CreateDirectory[ directory, CreateIntermediateDirectories -> True ] ],
  { artifactDirectory, archiveDirectory } ];

Unprotect[ NotebookDirectory ];
NotebookDirectory[ ] := notebookDirectory <> $PathnameSeparator;
Protect[ NotebookDirectory ];

completedItems = { "BookIPost1", "BookIPost3", "BookIDef15", "BookIDef20", "BookIProp1" };
requestedItems = Rest[ $ScriptCommandLine ];
items = If[ requestedItems === { }, completedItems, Select[ completedItems, MemberQ[ requestedItems, # ] & ] ];

boxify[ code_String ] :=
  If[ StringContainsQ[ code, { "Graphics", "InfraSubstrateHighlight", "InfraSceneViewer", "RandomInstance" } ], code,
    Quiet @ Check[ ToBoxes @ ToExpression[ code, StandardForm, Defer ], code ] ]

normalize[ expression_Notebook, codeBlocks_List ] :=
  Module[ { codeIndex = 0, converted, cleaned },
    converted = First[ expression ] /. Cell[ BoxData[ _ ], "Input", options___ ] :>
      With[ { code = codeBlocks[[ ++codeIndex ]] },
        Cell[ BoxData[ boxify[ code ] ], "Input", options,
          If[ StringContainsQ[ code, { ":=", "Needs[", "geometricScene" ~~ ___ ~~ " =" } ],
            InitializationCell -> True, Sequence[ ] ] ] ];
    converted = converted /. {
      Cell[ content_, "Chapter", options___ ] :> Cell[ content, "Section", options ],
      Cell[ content_, "Program", options___ ] :> Cell[ content, "CodeText", options ] };
    cleaned = DeleteCases[ converted, cell_Cell /; ! FreeQ[ cell, "[[ LLM Generated ]]" ] ];
    Notebook[ Insert[ cleaned, Cell[ "[[ LLM Generated ]]", "Subtitle" ], 2 ],
      TaggingRules -> { "Source" -> "Wiki/Notebooks/" <> item <> ".md", "InfraGeometryVersion" -> "2.7.1" } ] ]

evaluateCell[ Cell[ CellGroupData[ inner_List, state___ ], options___ ] ] :=
  Cell[ CellGroupData[ evaluateCell /@ inner, state ], options ]

evaluateCell[ cell : Cell[ BoxData[ code_ ], "Input", options___ ] ] :=
  Module[ { result, image, outputBoxes, messages = { }, index, input, held },
    inputCount++;
    index = inputCount;
    held = ToExpression[ BoxData[ code ], StandardForm, HoldComplete ];
    input = cell;
    If[ ! FreeQ[ held, InfraSceneViewer ],
      AppendTo[ cellResults, <| "Input" -> index, "Kind" -> "InteractiveViewer", "Evaluated" -> False |> ];
      Return[ input ] ];
    Internal`HandlerBlock[
      { "Message", If[ TrueQ[ Last[ # ] ], AppendTo[ messages, ToString[ #, InputForm ] ] ] & },
      result = TimeConstrained[ ReleaseHold[ held ], 90, $TimedOut ];
      If[ result =!= Null && result =!= $TimedOut,
        image = TimeConstrained[ UsingFrontEnd @ Rasterize[ result, "Image", ImageResolution -> 110 ], 120, $TimedOut ];
        outputBoxes = TimeConstrained[ UsingFrontEnd @ ToBoxes[ result ], 60, $TimedOut ] ] ];
    AppendTo[ cellResults, <| "Input" -> index, "Head" -> ToString[ Head[ result ], InputForm ],
      "Messages" -> DeleteDuplicates[ messages ], "TimedOut" -> ( result === $TimedOut || image === $TimedOut || outputBoxes === $TimedOut ),
      "UnresolvedCalls" -> ! FreeQ[ result, _RandomInstance | _RandomInfraInstance | _InfraSubstrateHighlight | $Failed ],
      "Image" -> If[ ImageQ[ image ], item <> "-" <> ToString[ index ] <> ".png", Null ] |> ];
    If[ ImageQ[ image ], Export[ FileNameJoin[ { artifactDirectory, item <> "-" <> ToString[ index ] <> ".png" } ], image ] ];
    Which[
      result === Null, input,
      result === $TimedOut || outputBoxes === $TimedOut, input,
      True, Cell[ CellGroupData[ { input, Cell[ BoxData[ outputBoxes ], "Output" ] }, Open ] ] ]
  ]

evaluateCell[ cell_ ] := cell

verification = <| "Date" -> "2026-10-13", "WolframVersion" -> $Version,
  "PacletSource" -> ExpandFileName[ pacletRoot ], "PacletVersion" -> "2.7.1", "Items" -> <| |> |>;

Do[
  Print[ "Building ", item ];
  sourceFile = FileNameJoin[ { root, "Wiki", "Notebooks", item <> ".md" } ];
  outputFile = FileNameJoin[ { notebookDirectory, item <> ".nb" } ];
  archiveFile = FileNameJoin[ { archiveDirectory, item <> ".nb" } ];
  If[ FileExistsQ[ outputFile ] && ! FileExistsQ[ archiveFile ], CopyFile[ outputFile, archiveFile ] ];
  markdown = Import[ sourceFile, "Text" ];
  codeBlocks = StringCases[ markdown, RegularExpression[ "(?s)```wolfram[ ]*\\n(.*?)\\n```" ] -> "$1" ];
  notebook = normalize[ ImportString[ markdown, { "Markdown", "Notebook" } ], codeBlocks ];
  inputCount = 0;
  cellResults = { };
  evaluated = ReplacePart[ notebook, 1 -> ( evaluateCell /@ First[ notebook ] ) ];
  Export[ outputFile, ExportString[ evaluated, "NB" ], "Text" ];
  verification[ "Items" ][ item ] = cellResults;
  Export[ FileNameJoin[ { artifactDirectory, "Verification.json" } ], verification, "RawJSON" ];
  Print[ { item, "Inputs" -> inputCount, "Outputs" -> Count[ cellResults, KeyValuePattern[ "Image" -> _String ] ],
    "Messages" -> Total[ Length @ Lookup[ #, "Messages", { } ] & /@ cellResults ],
    "Timeouts" -> Count[ cellResults, KeyValuePattern[ "TimedOut" -> True ] ] } ],
  { item, items } ];

If[ ! FreeQ[ Values[ verification[ "Items" ] ], KeyValuePattern[ "TimedOut" -> True ] | KeyValuePattern[ "UnresolvedCalls" -> True ] ] ||
    AnyTrue[ Flatten[ Values[ verification[ "Items" ] ], 1 ], Lookup[ #, "Messages", { } ] =!= { } & ], Exit[ 1 ] ];

Get[ FileNameJoin[ { root, "Scripts", "check_completed_scenes.wls" } ] ];
