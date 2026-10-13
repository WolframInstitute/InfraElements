# Completed Euclid notebook review

**[[ LLM Generated ]]**

Updated only the five existing per-item notebooks: Postulates I.1 and I.3, Definitions I.15 and I.20, and Proposition I.1.
Their statements, proof, attribution, and dependency lists are preserved.
The dependency-graph notebook and all pending Elements items are untouched.

Each notebook contains its classical scene and an evaluated graph comparison on the Large mesh, square grid, and hexagonal tiling.
Definitions I.15 and I.20 and Proposition I.1 use additional rows to show the relevant distinctions and failures.
Interactive scene-viewer inputs are retained; live interaction was not verified by the batch build.

## Open locally

- [Postulate I.1](../../../Notebooks/BookIPost1.nb)
- [Postulate I.3](../../../Notebooks/BookIPost3.nb)
- [Definition I.15](../../../Notebooks/BookIDef15.nb)
- [Definition I.20](../../../Notebooks/BookIDef20.nb)
- [Proposition I.1](../../../Notebooks/BookIProp1.nb)

Earlier local notebooks are preserved in `Notebooks/Archive/2026-10-13-before-refresh/`.
The cloud copies were not republished.

## Verification

[Verification.json](Verification.json) records the evaluated cells, messages, timeouts, unresolved calls, and saved previews.
[SceneVerification.json](SceneVerification.json) records the mathematical checks and exact substrate results.
All 57 checks pass. All ten classical/static outputs render without messages, timeouts, or unresolved calls.
The scripts use the sibling InfraGeometry 2.7.1 checkout, because the installed local paclet was 2.6.2.

The ten PNG previews were inspected, including the failure panels.
The principal findings and proposed contracts are in [Euclid API requirements](../../../Wiki/Plans/EuclidAPIRequirements_LLM.md).

## Rebuild

From the InfraElements root, with a free Wolfram license seat:

```sh
env WOLFRAMSCRIPT_KERNELPATH=/Applications/Wolfram.app/Contents/MacOS/WolframKernel /usr/local/bin/wolframscript -file Scripts/refresh_completed_notebooks.wls
```

This builds the five completed notebooks and runs the scene checks.
Pass one or more completed notebook stems to rebuild a subset.
No new Elements item is generated, and nothing is published.

The Markdown importer is used for prose and structure; fenced Wolfram code is restored verbatim before boxing and evaluation to preserve membership notation.
Sampled cycles are explicitly closed for drawing.
The static figures select one representative per path/circle construction, rather than enumerating or proving a whole family.
