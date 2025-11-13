# AGENTS.md - daal4py Package

## Purpose
Direct Python bindings to Intel oneDAL for maximum performance.

## APIs

**1. Native oneDAL:**
```python
import daal4py as d4p
algorithm = d4p.dbscan(epsilon=0.5, minObservations=5)
result = algorithm.compute(data)
```

**2. sklearn-compatible:**
```python
from daal4py.sklearn.cluster import DBSCAN
clusterer = DBSCAN(eps=0.5, min_samples=5)
```

**3. Model Builders:**
```python
from daal4py.mb import convert_model
d4p_model = convert_model(xgb_model)  # XGBoost→oneDAL
predictions = d4p_model.predict(X_test)  # 10-100x faster
```

## Common Algorithms
```python
# Clustering
d4p.dbscan(epsilon=0.5, minObservations=5)
d4p.kmeans(nClusters=3, maxIterations=300)

# Decomposition
d4p.pca(method="defaultDense")
d4p.svd(method="defaultDense")

# Linear Models
d4p.linear_regression_training()
d4p.ridge_regression_training(ridgeParameters=1.0)
```

## Distributed Computing (SPMD)
```python
d4p.daalinit()  # Initialize MPI backend
result = algorithm.compute(local_data)
d4p.daalfini()  # Finalize
```

**Supported**: DBSCAN, K-Means, PCA, Linear Regression

## Model Conversion
**Frameworks**: XGBoost, LightGBM, CatBoost, Treelite
**Benefits**: 10-100x faster inference with oneDAL

## Key Files
- `daal4py/__init__.py` - Core bindings
- `daal4py/sklearn/monkeypatch/dispatcher.py` - Patching system
- `daal4py/mb/` - Model builders
- `src/dist_*.h` - Distributed computing
