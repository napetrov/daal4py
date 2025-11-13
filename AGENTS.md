# AGENTS.md - Intel Extension for Scikit-learn

## Quick Context
- **Purpose**: Accelerate scikit-learn using Intel oneDAL optimizations
- **License**: Apache 2.0
- **Platforms**: CPU (x86_64, ARM), GPU (Intel via SYCL)

## Architecture
```
User Apps → sklearnex/ → daal4py/ → onedal/ → Intel oneDAL C++
```
- `sklearnex/`: sklearn API compatibility + patching
- `daal4py/`: Direct oneDAL access + model builders
- `onedal/`: Pybind11 bindings + memory management
- `src/`: C++/Cython core

## Entry Points

**sklearn acceleration:**
```python
from sklearnex import patch_sklearn; patch_sklearn()
from sklearnex.cluster import DBSCAN  # Direct import
```

**Native oneDAL:**
```python
import daal4py as d4p
algorithm = d4p.dbscan(epsilon=0.5, minObservations=5)
```

**Model conversion:**
```python
from daal4py.mb import convert_model
d4p_model = convert_model(xgb_model)  # XGBoost→oneDAL
```

## Accelerated Algorithms
- Clustering: DBSCAN, K-Means
- Classification: SVM, RandomForest, LogisticRegression, NaiveBayes
- Regression: LinearRegression, Ridge, Lasso, ElasticNet, SVR
- Decomposition: PCA, IncrementalPCA
- Neighbors: KNeighbors
- Preprocessing: Scalers, normalizers

## Device Configuration
```python
from sklearnex import config_context

with config_context(target_offload="gpu:0"):
    model.fit(X, y)  # GPU
```

## Development Setup

**Prerequisites:**
- Python: 3.9-3.13
- oneDAL: 2021.1+
- Dependencies: See dependencies-dev file

**Build:**
```bash
pip install -r dependencies-dev
export DALROOT=/path/to/onedal
python setup.py develop
```

**Environment options:**
```bash
export NO_DPC=1    # Disable GPU
export NO_DIST=1   # Disable distributed
```

**Testing:**
```bash
pytest --verbose --pyargs sklearnex  # sklearn compatibility
pytest --verbose --pyargs daal4py     # Native oneDAL
```

## Performance

**Fallback chain:**
oneDAL → sklearn → error

**GPU Support:**
- Full: DBSCAN, K-Means, PCA, KNeighbors
- Limited: LogisticRegression, SVM
- CPU Only: RandomForest, Ridge, IncrementalPCA

**Data requirements:**
- Dense arrays (not sparse)
- float32/float64 dtypes
- C-contiguous preferred for zero-copy

## SPMD (Distributed)
- **Use for**: Large datasets exceeding single-node memory
- **Algorithms**: DBSCAN, K-Means, PCA, Linear Regression
- **Requirements**: MPI, mpi4py
- **Test**: `mpirun -n 4 python ...`

## Component Docs
- `sklearnex/AGENTS.md`: API patterns, device offloading
- `daal4py/AGENTS.md`: Native bindings, model builders
- `onedal/AGENTS.md`: Pybind11 implementation
- `src/AGENTS.md`: C++/Cython core
- `examples/AGENTS.md`: Usage patterns
- `tests/AGENTS.md`: Testing infrastructure
