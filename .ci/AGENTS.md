# AGENTS.md - CI/CD Infrastructure (.ci/)

## Purpose
CI/CD for building, testing, and releasing across Linux, Windows, CPU/GPU platforms.

## Key Files
- `.ci/pipeline/ci.yml` - Main orchestrator
- `.ci/pipeline/build-and-test-*.yml` - Platform builds
- `.ci/pipeline/linting.yml` - Code quality
- `.ci/scripts/` - Automation utilities

## Quality Gates
- **Linting**: black, isort, clang-format, numpydoc
- **Testing**: pytest cross-platform
- **Coverage**: codecov integration

## Dependencies
- **oneDAL**: Nightly builds from upstream
- **Python**: 3.9-3.13
- **sklearn**: All versions beyond 1.0
- **torch**: PyTorch integration
- **GPU**: dpctl, dpnp

## Environment Variables
```bash
export DALROOT=/path/to/onedal    # Required
export NO_DPC=1                   # Disable GPU
export NO_DIST=1                  # Disable distributed
```

## For AI Agents
- Respect quality gates (linting, testing, coverage)
- Test across Python/sklearn versions
- Set DALROOT before building
- Run pre-commit hooks
