# AGENTS.md - Examples (examples/)

## Purpose
113 Python scripts + 19 Jupyter notebooks demonstrating usage patterns.

## Structure
- `daal4py/` - Native oneDAL API (80+ scripts)
- `sklearnex/` - sklearn acceleration (25+ scripts)
- `mb/` - Model conversion examples
- `notebooks/` - Jupyter tutorials

## Key Patterns

**Native oneDAL:**
```python
import daal4py as d4p
algorithm = d4p.dbscan(epsilon=0.5, minObservations=5)
result = algorithm.compute(data)
```

**sklearn acceleration:**
```python
from sklearnex import patch_sklearn
patch_sklearn()
```

**GPU:**
```python
from sklearnex import config_context
with config_context(target_offload="gpu:0"):
    model.fit(X, y)
```

**Distributed:**
```python
d4p.daalinit()  # MPI
# ... computation
d4p.daalfini()
```

**Model conversion:**
```python
from daal4py.mb import convert_model
d4p_model = convert_model(xgb_model)  # 10-100x faster
```

## For AI Agents
- Use examples as templates
- Follow patterns for performance optimization
- Include sklearn/oneDAL comparisons
- Test across CPU/GPU configurations
