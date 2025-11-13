# AGENTS.md - Documentation (doc/)

## Purpose
Sphinx-based documentation generation for Intel Extension for Scikit-learn.

## Key Files
- `sources/conf.py` - Sphinx configuration
- `build-doc.sh` - Build automation
- `sources/algorithms.rst` - Algorithm support matrix
- `sources/daal4py.rst` - API reference

## Build System
- **Extensions**: autodoc, nbsphinx, intersphinx, napoleon
- **Notebooks**: Jupyter via nbsphinx
- **Cross-refs**: sklearn, numpy, pandas docs
- **Deployment**: GitHub Pages on releases

## Content
- User guides: Quick start, performance
- API reference: Auto-generated from docstrings
- Examples: Real-world applications
- Developer docs: Distributed computing, contributions

## Build Commands
```bash
make html              # Local
./build-doc.sh --gh-pages  # Production
```

## For AI Agents
- Use reStructuredText format
- Include proper docstrings for autodoc
- Test builds locally before submitting
- Maintain cross-references and intersphinx links
