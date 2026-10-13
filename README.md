# InfraElements

An implementation of [D. Joyce's edition of Euclid's *Elements*](http://aleph0.clarku.edu/~djoyce/java/elements/toc.html) on a graph substrate.

- [Elements](Wiki/Elements.md)
- [Dependency graph](https://www.wolframcloud.com/obj/hajek_pavel/InfraElements/DependencyGraph.nb)
- [Cloud Notebooks](Wiki/Notebooks/Index.md)

## Dependencies

- [InfraGeometry](https://github.com/WolframInstitute/InfraGeometry)
- [DiscreteGeometry](https://github.com/WolframInstitute/DiscreteGeometry)

## Rebuild

To refresh only the five completed per-item notebooks with paired scenes on three Large substrates, use `Scripts/refresh_completed_notebooks.wls`. It evaluates the figures and runs `Scripts/check_completed_scenes.wls`; no cloud publication is performed. See the [completed review](Code/Artifacts/EuclidCompletedReview_LLM_261013/README.md) and the [API requirements learned from it](Wiki/Plans/EuclidAPIRequirements_LLM.md).

- Scrape and analyze D. Joyce's project:
  ```bash
  python3 Scripts/scrape_djoyce.py
  python3 Scripts/extract_dependencies.py
  ```
- Produce content: prompt an LLM to convert each item, following the [conventions](Wiki/Concepts/NotebookConvention.md) and the [template](Wiki/Notebooks/BookIProp1.md).
- Generate and deploy notebooks:
  ```bash
  wolframscript -file Scripts/generate_notebooks.wls
  wolframscript -file Scripts/publish_notebooks.wls
  python3 Scripts/generate_notebook_index.py
  ```

## Funding

Pavel Hájek's work on this repository was supported by the John Templeton Foundation grant 63655, [Causality, Observers and Computation: A New Approach to Fundamental Physics and Metamathematics](https://www.templeton.org/grant/causality-observers-and-computation-a-new-approach-to-fundamental-physics-and-metamathematics) at the Wolfram Institute. The opinions expressed are those of the author and do not necessarily reflect the views of the John Templeton Foundation.

## License

- Code: [MIT](LICENSE)
- Mathematical content: [CC BY 4.0](LICENSE-CC-BY-4.0)
