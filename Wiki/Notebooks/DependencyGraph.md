# Dependency graph of Euclid's Elements

## Overview

Visualisation of the directed dependency graph extracted from D. Joyce's edition of Euclid's *Elements*. Each node is a Definition / Postulate / Common Notion / Proposition; each directed edge `X -> Y` means *X cites Y in its statement or proof* — i.e. Y is a prerequisite for X.

The graph drives the topological order in which per-item notebooks under `Wiki/Notebooks/` are produced: a notebook is generated only after every item it depends on already has one.

## Load the dependency data

```wolfram
projectRoot = ParentDirectory @ NotebookDirectory[ ];
depGraph    = Get @ FileNameJoin[ { projectRoot, "Wiki", "Resources", "DependencyGraph.m" } ];
{ Length @ depGraph, Total[ Length @ # [ "Dependencies" ] & /@ Values @ depGraph ] }
```

## Build the Wolfram Graph

```wolfram
edges = Flatten @ KeyValueMap[ Function[ { id, info }, # -> id & /@ info[ "Dependencies" ] ], depGraph ];
g = Graph[ Keys @ depGraph, edges,
  VertexStyle      -> ( # -> Switch[ depGraph[ # ][ "Kind" ],
                          "Def",  RGBColor[ 0.95, 0.80, 0.60 ],
                          "Post", RGBColor[ 0.70, 0.85, 0.95 ],
                          "CN",   RGBColor[ 0.90, 0.90, 0.70 ],
                          "Prop", RGBColor[ 0.85, 0.78, 0.95 ] ] & /@ Keys @ depGraph ),
  GraphLayout      -> "LayeredDigraphEmbedding",
  VertexSize       -> 0.8,
  EdgeStyle        -> Directive[ Opacity[ 0.25 ], GrayLevel[ 0.4 ] ],
  ImageSize        -> Large
]
```

## Layered topological sort

```wolfram
topo = TopologicalSort @ g;
layers = ReverseSortBy[
  GatherBy[
    Keys @ depGraph,
    Function[ id,
      If[ depGraph[ id ][ "Dependencies" ] === { }, 0,
        Max[ depGraph[ # ][ "Num" ] & /@ depGraph[ id ][ "Dependencies" ] ] ] ]
  ], Length
];
{ Length @ topo, Length /@ Take[ layers, UpTo @ 5 ] }
```

## Sources (Layer 0 — items with no dependencies)

```wolfram
sources = Select[ Keys @ depGraph, depGraph[ # ][ "Dependencies" ] === { } & ];
TableForm @ { Length @ sources, GroupBy[ sources, depGraph[ # ][ "Kind" ] & , Length ] }
```

## Most-depended-on items (highest in-degree)

```wolfram
inDeg = VertexInDegree[ g, # ] & /@ Keys @ depGraph;
ranked = Reverse @ SortBy[ Transpose @ { Keys @ depGraph, inDeg }, Last ];
TableForm[ Take[ ranked, 20 ], TableHeadings -> { None, { "Item", "In-degree" } } ]
```

## Sub-DAG: dependency closure of `PropI.1`

```wolfram
ancestors[ id_ ] := Module[ { stack, visited },
  visited = <| |>;
  stack = depGraph[ id ][ "Dependencies" ];
  While[ stack =!= { },
    With[ { next = First @ stack },
      stack = Rest @ stack;
      If[ ! KeyExistsQ[ visited, next ],
        visited[ next ] = True;
        stack = Join[ stack, depGraph[ next ][ "Dependencies" ] ] ] ] ];
  Keys @ visited ];

closure = Prepend[ ancestors @ "PropI.1", "PropI.1" ];
Subgraph[ g, closure, GraphLayout -> "LayeredDigraphEmbedding", VertexLabels -> "Name", ImageSize -> Large ]
```
