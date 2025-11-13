# AGENTS.md - sklearnex Package

## Purpose
Primary sklearn-compatible interface with oneDAL acceleration.

## Usage Patterns

**Global patching:**
```python
from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.cluster import DBSCAN  # Now accelerated
```

**Selective patching:**
```python
patch_sklearn(["DBSCAN", "KMeans"])
```

**Direct import:**
```python
from sklearnex.cluster import DBSCAN  # Always accelerated
```

## Device Configuration
```python
from sklearnex import config_context

# GPU acceleration
with config_context(target_offload="gpu:0"):
    model.fit(X, y)

# CPU only
with config_context(target_offload="cpu"):
    model.fit(X, y)

# Fallback control
with config_context(allow_fallback_to_host=True):
    model.fit(X_gpu, y_gpu)  # GPU→CPU fallback
```

## Supported Algorithms

**CPU + GPU:**
- DBSCAN, K-Means, PCA, KNeighbors

**CPU Only:**
- RandomForest, Ridge, IncrementalPCA, LinearRegression

**Limited GPU:**
- LogisticRegression, SVM

## Dispatch Flow
1. Check GPU oneDAL support → Use GPU
2. Check CPU oneDAL support → Use CPU
3. Fallback → Use sklearn

## Key Files
- `dispatcher.py:36` - `get_patch_map_core()`
- `_device_offload.py:72` - `dispatch()`
- `_config.py` - Configuration API
- `base.py` - oneDALEstimator base class

## Distributed (SPMD)
```python
from sklearnex.spmd.cluster import DBSCAN  # MPI distributed
```

## Preview Features
```bash
export SKLEARNEX_PREVIEW=1
```
Location: `sklearnex/preview/`
