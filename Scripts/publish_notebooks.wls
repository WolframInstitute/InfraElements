#!/usr/bin/env wolframscript

(* publish_notebooks.wls — Build .nb from Wiki/Notebooks/*.md and upload to Wolfram Cloud *)

root = ParentDirectory[ExpandFileName[DirectoryName[$ScriptCommandLine[[1]]]]];
wikiDir = FileNameJoin[{root, "Wiki", "Notebooks"}];
nbDir = FileNameJoin[{root, "Notebooks"}];

(* First generate notebooks from wiki sources *)
Print["Building notebooks from wiki sources..."];
Print[RunProcess[{"wolframscript", "-file", FileNameJoin[{root, "Scripts", "generate_notebooks.wls"}]}, "StandardOutput"]];

(* Then evaluate every Input cell and embed the rendered outputs.
   One fresh kernel per notebook so a hang/runaway is isolated to that notebook;
   evaluate_notebooks.wls also caps each cell with TimeConstrained. *)
nbFiles = FileNames["*.nb", nbDir];
Print["Evaluating notebook cells and embedding rendered outputs (one kernel per notebook)..."];
Do[
	Print["  -> ", FileBaseName[nbFile]];
	Print[RunProcess[{"wolframscript", "-file",
		FileNameJoin[{root, "Scripts", "evaluate_notebooks.wls"}],
		FileBaseName[nbFile], "240", "0"}, "StandardOutput"]],
	{nbFile, nbFiles}
];

If[nbFiles === {},
	Print["No .nb files found in ", nbDir];
	Exit[1]
];

(* Determine cloud folder name from project *)
projectName = FileBaseName[root];

Print[""];
Print["Notebook Publisher"];
Print["=================="];
Print["Project: ", projectName];
Print[""];

results = {};

Do[
	baseName = FileBaseName[nbFile];
	Print["[", baseName, "] Uploading..."];
	cloudObj = CloudObject[projectName <> "/" <> baseName <> ".nb", Permissions -> "Public"];
	CopyFile[nbFile, cloudObj, OverwriteTarget -> True];
	Print["[", baseName, "] Published: ", First[cloudObj]];
	Print[""];
	AppendTo[results, baseName -> ToString[First[cloudObj]]],
	{nbFile, nbFiles}
];

Print["=================="];
Do[Print["  ", r[[1]], ": ", r[[2]]], {r, results}];

manifest = FileNameJoin[{wikiDir, "published.json"}];
Export[manifest, Association[results], "JSON"];
Print[""];
Print["Manifest: ", manifest];
