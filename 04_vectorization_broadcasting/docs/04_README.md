# Module 04: Vectorization & Broadcasting

Master the core techniques that make NumPy fast: vectorization (avoiding loops) and broadcasting (automatic shape alignment). These patterns are fundamental to neural network computation.

## Learning Objectives

- Replace slow Python loops with fast element-wise operations
- Understand the three broadcasting rules and how NumPy automatically aligns shapes
- Use matrix multiplication (`@` operator, `np.dot`, `np.matmul`) correctly
- Compute neural network forward passes using vectorized operations
- Measure and compare performance: vectorized vs loop-based approaches
- Connect array operations to real neural network layers

## Prerequisites

- Module 03 (NumPy arrays, shapes, indexing)
- Basic understanding of matrix multiplication from linear algebra
- Familiarity with neural network concepts (neurons, weights, biases) is helpful but not required

## Files in This Module

| File | Purpose |
|------|---------|
| `tutorial.ipynb` | Interactive Jupyter notebook with explanations and exercises |
| `lab_forward_pass.py` | Complete lab implementing a neural network forward pass |
| `slides.html` | Lecture slides covering vectorization and broadcasting theory |
| `pyproject.toml` | Project dependencies (uv/pip) |

## Key Concepts Covered

### 1. Element-Wise Operations

Operations that apply independently to each element:
```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

arr1 + arr2    # [11, 22, 33, 44]
arr1 * arr2    # [10, 40, 90, 160]
arr1 ** 2      # [1, 4, 9, 16]
```

**Key insight**: No loops needed. NumPy applies operations in parallel using optimized C code.

### 2. Scalar Broadcasting

A single value automatically repeats to match an array's shape:
```python
arr = np.array([1, 2, 3, 4])
arr * 5        # [5, 10, 15, 20]
arr + 10       # [11, 12, 13, 14]

# NumPy treats scalar 5 as [5, 5, 5, 5] internally
```

### 3. Broadcasting Rules

When operating on arrays with different shapes, NumPy automatically aligns them if:

**Rule 1**: If arrays have different number of dimensions, pad the smaller shape with 1s on the left.
```python
Shape (3, 4) + Shape (4,)
→ Shape (3, 4) + Shape (1, 4)
```

**Rule 2**: Dimensions are compatible if they are equal or one of them is 1.
```python
(3, 4) + (1, 4) → compatible (3 and 1 are compatible)
(3, 4) + (3, 1) → compatible (4 and 1 are compatible)
(3, 4) + (2, 4) → ERROR (3 and 2 are not compatible)
```

**Rule 3**: After broadcasting, the result shape is the maximum along each dimension.
```python
(3, 1) + (1, 4) → (3, 4)
(5, 3, 4) + (3, 1) → (5, 3, 4)
```

### 4. Matrix Multiplication

Three equivalent ways to multiply matrices:
```python
A = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
B = np.array([[5, 6], [7, 8]])  # Shape: (2, 2)

# All produce the same result
result = A @ B              # Preferred (Python 3.5+)
result = np.dot(A, B)       # Classic NumPy
result = np.matmul(A, B)    # Explicit name
```

**Shape compatibility**: `(m, n) @ (n, p) → (m, p)`

Dot product (1D vectors):
```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

np.dot(v1, v2)  # 32 (= 1×4 + 2×5 + 3×6)
v1 @ v2         # 32 (same result)
```

### 5. Neural Network Forward Pass

A single neuron computes:
```
output = activation(weights · inputs + bias)
```

Vectorized implementation:
```python
inputs = np.array([1.5, 2.0, 3.5])     # 3 features
weights = np.array([0.2, 0.8, -0.5])   # 3 weights
bias = 2.0

# Weighted sum
z = weights @ inputs + bias

# Activation (ReLU: max(0, x))
output = np.maximum(0, z)
```

A layer of neurons (matrix form):
```python
# W: (n_neurons, n_features) weight matrix
# X: (n_features,) input vector
# b: (n_neurons,) bias vector

Z = W @ X + b           # Weighted sums
A = np.maximum(0, Z)    # ReLU activation
```

### 6. Vectorization vs Loops

Replace slow Python loops with fast vectorized operations:

**Loop-based (slow)**:
```python
result = np.zeros(1000)
for i in range(1000):
    result[i] = W[i, :] @ X + b[i]  # ~100 ms
```

**Vectorized (fast)**:
```python
result = W @ X + b  # ~0.1 ms (1000x faster!)
```

**Performance rule**: Vectorized NumPy operations are typically 10-1000x faster than equivalent Python loops.

## How to Run

### Setup Environment
```bash
# Install dependencies using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

### Run the Lab
```bash
# Run the complete lab script
python lab_forward_pass.py

# Or open the Jupyter notebook
jupyter lab tutorial.ipynb
```

### Expected Output
The lab will demonstrate:
1. Element-wise operations on arrays
2. Scalar broadcasting examples
3. Dot product computation (manual and vectorized)
4. Broadcasting rules with visual examples
5. Single neuron forward pass
6. Layer of neurons using matrix multiplication
7. Performance comparison: vectorized vs loops (1000x speedup)

## Broadcasting Examples

### Example 1: Add row vector to matrix
```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])  # Shape: (2, 3)
row = np.array([10, 20, 30])   # Shape: (3,)

result = matrix + row
# [[11, 22, 33],
#  [14, 25, 36]]

# row is broadcast from (3,) → (1, 3) → (2, 3)
```

### Example 2: Add column vector to matrix
```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])      # Shape: (2, 3)
column = np.array([[100],
                   [200]])          # Shape: (2, 1)

result = matrix + column
# [[101, 102, 103],
#  [204, 205, 206]]

# column is broadcast from (2, 1) → (2, 3)
```

### Example 3: Batch processing
```python
# Process multiple samples at once
X_batch = np.random.randn(32, 784)  # 32 images, 784 pixels each
W = np.random.randn(10, 784)        # 10 neurons, 784 inputs each
b = np.random.randn(10)             # 10 biases

# Compute all 32 samples in parallel
Z = X_batch @ W.T + b  # Shape: (32, 10)
# Each row is one sample's output across 10 neurons
```

## Performance Comparison

For a layer with 1000 neurons and 500 input features:

| Approach | Time | Speedup |
|----------|------|---------|
| Python loops | ~100 ms | 1x (baseline) |
| NumPy vectorized | ~0.1 ms | 1000x faster |

**Why so fast?**
- Contiguous memory layout (CPU cache friendly)
- BLAS/LAPACK optimized linear algebra libraries
- SIMD (Single Instruction Multiple Data) parallelization
- No Python interpreter overhead per element

## Connection to Production Neural Networks

Every neural network framework uses vectorized operations:

| Framework | Operation |
|-----------|-----------|
| PyTorch | `torch.nn.Linear(in_features, out_features)` |
| TensorFlow | `tf.keras.layers.Dense(units)` |
| JAX | `jax.numpy.dot(W, X)` |

Under the hood, they all:
1. Store weights as matrices
2. Use matrix multiplication for forward pass
3. Leverage broadcasting for bias addition
4. Apply element-wise activation functions
5. Process batches of samples in parallel

**This module teaches the fundamental operations** that power all modern neural networks.

## Common Patterns You'll See

### Pattern 1: Linear transformation
```python
# Neural network layer
output = X @ W.T + b  # (batch, in) @ (out, in).T + (out,) → (batch, out)
```

### Pattern 2: Batch normalization
```python
# Center and scale each feature
X_normalized = (X - mean) / std  # Broadcasting across batch dimension
```

### Pattern 3: Softmax (classification)
```python
# Convert logits to probabilities
exp_logits = np.exp(logits - logits.max(axis=1, keepdims=True))
probs = exp_logits / exp_logits.sum(axis=1, keepdims=True)
```

## What's Next?

After mastering vectorization and broadcasting:
- **Module 05**: Efficient data structures (DataFrames, Arrow)
- **Module 06**: Real-world data cleaning and transformation pipelines
- **Module 07**: Working with images as arrays
- **Module 08**: Building a complete research data pipeline

These vectorization patterns will appear in every subsequent module.
