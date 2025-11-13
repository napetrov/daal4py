# AGENTS.md - oneDAL Backend (onedal/)

## Purpose
Low-level Python bindings to Intel oneDAL using pybind11 for CPU/GPU execution.

## Key Components
- `__init__.py` - Backend selection (DPC++/Host)
- `_config.py` - Thread-local configuration
- `_device_offload.py` - Device dispatch
- `common/` - Core infrastructure
- `datatypes/` - Data conversion (NumPy, SYCL USM, DLPack)
- Algorithm modules: `cluster/`, `linear_model/`, `decomposition/`, etc.

## Backend System
```python
# Automatic backend selection
try:
    import onedal._onedal_py_dpc  # GPU backend
except ImportError:
    import onedal._onedal_py_host  # CPU backend
```

## Data Conversion
- **NumPy**: Zero-copy via `to_table()`
- **SYCL USM**: GPU memory sharing
- **DLPack**: Cross-framework tensors

## Algorithm Categories
- Clustering: DBSCAN, K-Means
- Linear Models: Linear/Ridge/Logistic regression
- Decomposition: PCA, Incremental PCA
- SVM: SVC, SVR
- Ensemble: Random Forest
- Statistics: Basic statistics, covariance

## For AI Agents
- Use `config_context` for device selection
- Prefer zero-copy operations with `to_table()`
- Handle CPU/GPU fallback gracefully
- Monitor GPU memory usage
- Test across device configurations
