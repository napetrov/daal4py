# AGENTS.md - Core Implementation (src/)

## Purpose
C++/Cython bindings to Intel oneDAL with zero-overhead access and distributed computing.

## Key Files
- `daal4py.cpp/.h` - Main C++ interface, NumPy integration
- `npy4daal.h` - NumPy-oneDAL conversion
- `gbt_model_builder.pyx` - Gradient boosting builder
- `gettree.pyx` - Tree visitor (sklearn compatibility)
- `transceiver.h` - Distributed communication
- `dist_*.h` - Distributed algorithms (DBSCAN, K-Means)

## Core Features

**Memory Management:**
- Zero-copy NumPy integration
- Thread-safe reference counting
- GIL-protected cleanup

**Distributed Computing:**
- MPI-based communication (gather, broadcast, reduce)
- Map-reduce patterns

**Tree Model Building:**
```cython
# External model conversion interface
gbt_classification_model_builder.create_tree(n_nodes, class_label)
gbt_classification_model_builder.add_split(feature_index, threshold)
gbt_classification_model_builder.add_leaf(response, cover)
```

## For AI Agents
- Use existing patterns for memory management
- Follow map-reduce patterns for distributed algorithms
- Maintain thread safety and GIL protection
- Ensure cross-platform compatibility
