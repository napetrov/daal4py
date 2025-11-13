# AGENTS.md - Testing (tests/)

## Purpose
Validation infrastructure for numerical accuracy, performance, and cross-platform reliability.

## Key Modules
- `test_daal4py_examples.py` - Native API validation
- `test_model_builders.py` - Framework integration
- `test_daal4py_spmd_examples.py` - Distributed validation
- `test_estimators.py` - sklearn compatibility
- `run_examples.py` - Cross-platform execution

## Validation Patterns

**Numerical accuracy:**
```python
np.testing.assert_allclose(actual, expected, atol=1e-05)
```

**Model conversion:**
```python
xgb_pred = xgb_model.predict(X)
d4p_pred = convert_model(xgb_model).predict(X)
np.testing.assert_allclose(xgb_pred, d4p_pred)
```

## Test Execution

**Local:**
```bash
pytest --verbose --pyargs sklearnex  # sklearn compatibility
pytest --verbose --pyargs daal4py    # Native API
pytest --verbose --pyargs onedal     # Backend
```

**Distributed:**
```bash
mpirun -n 4 python tests/helper_mpi_tests.py pytest -k spmd --with-mpi --pyargs sklearnex
```

**Coverage:**
```bash
pytest --cov=onedal --cov=sklearnex --cov-config=.coveragerc
```

## For AI Agents
- Use `assert_allclose(atol=1e-05)` for numerical validation
- Configure timeouts for complex algorithms
- Handle missing dependencies with `skipTest()`
- Test sklearn compatibility and numerical accuracy
- Validate model conversion accuracy
- Run distributed tests with `mpirun -n 4`
