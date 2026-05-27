#!/usr/bin/env wolframscript

(* evaluate_notebooks.wls — Evaluate every Input cell in Notebooks/*.nb and embed
   the result as an Output cell, so the deployed notebooks ship with rendered output.

   Usage:
     wolframscript -file evaluate_notebooks.wls [target] [cellCapSeconds] [pruneProbability]
       target            basename (e.g. BookIPost1) or "All"  (default All)
       cellCapSeconds     per-cell TimeConstrained cap          (default 240)
       pruneProbability   SetOptions[FindInfraScene, PruneProbability -> p]; p in (0,1)
                          randomly prunes construction branches.        (default 0)

   Two output policies:
     - An InfraSceneViewer result (interactive DynamicModule) is replaced by a STATIC
       rasterized image of the viewer frozen at its final step in Diffuse mode (the
       "diffuse picture").  A flat raster renders for everyone with no paclet installed
       — the live viewer would show raw unevaluated symbols in a cloud kernel that
       lacks WolframInstitute`SyntheticInfrageometry`.
     - Every other result is embedded as its FrontEnd-typeset boxes via
       UsingFrontEnd[ToBoxes[...]].  (Plain NotebookEvaluate[...,InsertResults->True]
       only yields OutputForm text in a headless kernel.)

   Evaluation order: an initialization pre-pass evaluates every InitializationCell
   first (two rounds, to resolve forward references such as a data definition placed
   at the END of the notebook), then the main pass evaluates all cells in document
   order and embeds outputs.

   The paclet is loaded first so the infra function-definition cell's symbols resolve
   to WolframInstitute`SyntheticInfrageometry` instead of interning into Global`. *)

Needs["WolframInstitute`SyntheticInfrageometry`"];

args = Rest[$ScriptCommandLine];
target  = If[Length[args] >= 1 && args[[1]] =!= "All", args[[1]], All];
cellCap = If[Length[args] >= 2, ToExpression[args[[2]]], 240];
prune   = If[Length[args] >= 3, ToExpression[args[[3]]], 0];

If[NumericQ[prune] && prune > 0,
	SetOptions[FindInfraScene, PruneProbability -> prune];
	Print["FindInfraScene PruneProbability -> ", prune]
];

root = ParentDirectory[ExpandFileName[DirectoryName[$ScriptCommandLine[[1]]]]];
nbDir = FileNameJoin[{root, "Notebooks"}];
nbFiles = If[target === All,
	FileNames["*.nb", nbDir],
	{FileNameJoin[{nbDir, target <> ".nb"}]}
];
nbFiles = Select[nbFiles, FileExistsQ];

If[nbFiles === {},
	Print["No matching .nb files in ", nbDir];
	Exit[1]
];

(* Headless kernels have no notebook, so NotebookDirectory[] -> $Failed; bind it so any
   residual path-relative cell still resolves. *)
Unprotect[NotebookDirectory];
NotebookDirectory[] := nbDir <> $PathnameSeparator;
Protect[NotebookDirectory];

(* Static replica of InfraSceneViewer frozen at the final step in Diffuse mode.
   Mirrors the viewer's own Diffuse rendering (InfraSceneInteractive.wl): collect every
   instance's bound objects at the last step, wrap each by its construction type, and
   shade them with InfraSceneHighlight (opacity/thickness encode realisation count). *)
staticDiffuseViewer[scene_InfraScene, graph_Graph] := Module[
	{nSteps, labels, objects, wrap, instances, boundKeys, objs, pic, label},
	nSteps  = Length @ scene["Steps"];
	labels  = scene["Labels"];
	objects = scene["Objects"];
	wrap = AssociationMap[
		Switch[Head @ Lookup[scene["Constructions"], #, InfraPoint],
			InfraSegment | InfraLine, InfraSegment,
			InfraShell,    InfraShell,    InfraPlane,    InfraPlane,
			InfraCircle,   InfraCircle,   InfraPolygon,  InfraPolygon,
			InfraTriangle, InfraTriangle, InfraPolyline, InfraPolyline,
			_, InfraPoint] &,
		objects];
	instances = FindInfraScene[scene, graph, nSteps];
	pic = If[instances === {},
		InfraSceneHighlight[graph, {}, ImageSize -> 600],
		boundKeys = Keys @ First[instances][[1]];
		objs = (obj |-> wrap[obj][DeleteDuplicates[#[[1]][obj] & /@ instances]]) /@
			Select[objects, MemberQ[boundKeys, #] &];
		InfraSceneHighlight[graph, objs, ImageSize -> 600]];
	label = If[labels[[nSteps]] === None, "", Row[{": ", labels[[nSteps]]}]];
	Framed[Column[{
		Style[Row[{"step ", nSteps, "/", nSteps, label}], Bold],
		Row[{Framed["Branch", FrameStyle -> LightGray],
			Framed[Style["Diffuse", Bold], Background -> RGBColor[0.85, 0.92, 1]],
			Spacer[16], Length @ instances, " branches diffused"}],
		pic
	}, Alignment -> Left, Spacings -> 1], FrameStyle -> GrayLevel[0.8], RoundingRadius -> 4]
];

isViewer[result_] := Head[result] === DynamicModule &&
	Cases[result, HoldPattern[FindInfraScene[_, _Graph, _, _]], Infinity] =!= {};

renderOutput[result_] := If[isViewer[result],
	With[{sg = First @ Cases[result, HoldPattern[FindInfraScene[s_, g_Graph, _, _]] :> {s, g}, Infinity]},
		ToBoxes @ Rasterize[staticDiffuseViewer @@ sg, ImageSize -> 620]],
	ToBoxes[result]];

inputCounter = 0;
timedOut = 0;

initCellCode[Cell[CellGroupData[inner_List, ___], ___]] := Flatten[initCellCode /@ inner];
initCellCode[Cell[BoxData[code_], "Input", opts___]] := If[
	MemberQ[Flatten[{opts}], InitializationCell -> True], {code}, {}];
initCellCode[_] := {};

(* Recurse into CellGroupData so nested Input cells are reached in document order. *)
evalCell[Cell[CellGroupData[inner_List, state___], copts___]] :=
	Cell[CellGroupData[evalCell /@ inner, state], copts];

evalCell[Cell[BoxData[code_], "Input", opts___]] := Module[{result, outBoxes, inCell},
	inputCounter++;
	inCell = Cell[BoxData[code], "Input", CellLabel -> "In[" <> ToString[inputCounter] <> "]:=", opts];
	(* Wrap in BoxData so a multi-line cell (BoxData stores a {box,"\n",box,...} list)
	   parses as one input and yields the last value — not a list of per-row results
	   (which produced the spurious {Null, Null, ..., output}). *)
	result = TimeConstrained[ToExpression[BoxData[code]], cellCap, $Timeout];
	Which[
		result === $Timeout,
			timedOut++;
			Print["  ! cell ", inputCounter, " timed out after ", cellCap, "s — left unevaluated"];
			inCell,
		result === Null,
			inCell,
		True,
			outBoxes = TimeConstrained[UsingFrontEnd[renderOutput[result]], cellCap, $Timeout];
			If[outBoxes === $Timeout,
				timedOut++;
				Print["  ! cell ", inputCounter, " typeset timed out after ", cellCap, "s — left unevaluated"];
				inCell,
				Cell[CellGroupData[{
					inCell,
					Cell[BoxData[outBoxes], "Output", CellLabel -> "Out[" <> ToString[inputCounter] <> "]="]
				}, Open]]
			]
	]
];

evalCell[other_] := other;

Print["Notebook Evaluator"];
Print["=================="];

Do[
	baseName = FileBaseName[nbFile];
	Print["[", baseName, "] Evaluating (cap ", cellCap, "s/cell)..."];

	UsingFrontEnd[
		nbObj = NotebookOpen[nbFile, Visible -> False];
		nbExpr = NotebookGet[nbObj];
		NotebookClose[nbObj];
	];

	(* Initialization pre-pass: define everything first (two rounds resolve a
	   data/definition cell placed after its uses, e.g. DependencyGraph). *)
	(* Tight cap: real definitions are fast; a slow one here is a forward reference
	   (e.g. a closure cell using data defined later) that resolves in the next round. *)
	initCodes = initCellCode /@ First[nbExpr] // Flatten;
	Do[Quiet @ TimeConstrained[ToExpression[BoxData[c]], Min[cellCap, 30]], {round, 2}, {c, initCodes}];

	inputCounter = 0;
	timedOut = 0;
	newCells = evalCell /@ First[nbExpr];

	newNb = ReplacePart[nbExpr, 1 -> newCells];
	Export[nbFile, newNb, "NB"];
	Print["[", baseName, "] ", inputCounter, " input cell(s) processed, ", timedOut, " timed out."],
	{nbFile, nbFiles}
];

Print["=================="];
Print["Done."];
