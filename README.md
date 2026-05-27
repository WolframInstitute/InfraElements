# InfraElements

An implementation of [D. Joyce's edition of Euclid's *Elements*](http://aleph0.clarku.edu/~djoyce/java/elements/toc.html) on a graph substrate.

- [Elements](Wiki/Elements.md)
- [Dependency graph](Wiki/Resources/DependencyGraph.md)
- [Cloud Notebooks](Wiki/Notebooks/Index.md)

## Dependencies

- [SyntheticInfrageometry](https://github.com/WolframInstitute/SyntheticInfrageometry)
- [Infrageometry](https://github.com/WolframInstitute/Infrageometry)

## Rebuild

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

## License

MIT
