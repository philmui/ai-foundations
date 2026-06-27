# Quick Reference: Vectorization & Broadcasting

## Broadcasting Rules

NumPy automatically aligns arrays with different shapes using three rules:

### Rule 1: Pad Smaller Shape with 1s
If arrays have different dimensions, pad the smaller shape on the left with 1s.
```python
Shape (3, 4) + Shape (4,)
→ (3, 4) + (1, 4)  # Padded with 1
```

### Rule 2: Compatible Dimensions
Dimensions are compatible if they are:
- Equal, OR
- One of them is 1

```python
Compatible:
  (3, 4) + (3, 4)  # Equal dimensions
  (3, 4) + (1, 4)  # 3 vs 1 (compatible)
  (3, 4) + (3, 1)  # 4 vs 1 (compatible)

Not compatible:
  (3, 4) + (2, 4)  # 3 vs 2 (not equal, neither is 1)
```

### Rule 3: Result Shape
After broadcasting, result shape is the maximum along each dimension.
```python
(3, 1) + (1, 4) → (3, 4)
(2, 3, 4) + (3, 1) → (2, 3, 4)
(1, 5) + (4, 1) → (4, 5)
```

## Broadcasting Patterns

### Scalar + Array
```python
arr = np.array([1, 2, 3, 4])
arr + 5      # [6, 7, 8, 9]
arr * 2      # [2, 4, 6, 8]

# Internally: 5 broadcasts to [5, 5, 5, 5]
```

### Row Vector + Matrix
```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])    # Shape: (2, 3)
row = np.array([10, 20, 30])     # Shape: (3,)

result = matrix + row             # Shape: (2, 3)
# [[11, 22, 33],
#  [14, 25, 36]]

# row (3,) → (1, 3) → broadcast to (2, 3)
```

### Column Vector + Matrix
```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])    # Shape: (2, 3)
col = np.array([[10],
                [20]])            # Shape: (2, 1)

result = matrix + col             # Shape: (2, 3)
# [[11, 12, 13],
#  [24, 25, 26]]

# col (2, 1) → broadcast to (2, 3)
```

### Matrix + Matrix (Different Shapes)
```python
a = np.ones((3, 1))    # Shape: (3, 1)
b = np.ones((1, 4))    # Shape: (1, 4)

result = a + b         # Shape: (3, 4)
# Both broadcast to (3, 4)
```

## Vectorization Patterns

### Replace Loops with Element-Wise Operations

**Loop-based (slow)**:
```python
result = np.zeros(n)
for i in range(n):
    result[i] = arr1[i] + arr2[i]
```

**Vectorized (fast)**:
```python
result = arr1 + arr2
```

### Common Element-Wise Operations
```python
arr1 + arr2      # Addition
arr1 - arr2      # Subtraction
arr1 * arr2      # Multiplication
arr1 / arr2      # Division
arr1 ** 2        # Power
np.sqrt(arr1)    # Square root
np.exp(arr1)     # Exponential
np.log(arr1)     # Natural log
np.maximum(arr1, arr2)  # Element-wise maximum
```

## Matrix Multiplication Options

### Three Equivalent Ways
```python
A = np.array([[1, 2], [3, 4]])  # Shape: (2, 2)
B = np.array([[5, 6], [7, 8]])  # Shape: (2, 2)

# Method 1: @ operator (preferred in Python 3.5+)
C = A @ B

# Method 2: np.dot()
C = np.dot(A, B)

# Method 3: np.matmul()
C = np.matmul(A, B)
```

### Shape Compatibility
```
(m, n) @ (n, p) → (m, p)

Examples:
  (3, 4) @ (4, 5) → (3, 5) ✓
  (2, 3) @ (3, 1) → (2, 1) ✓
  (3, 4) @ (5, 6) → ERROR (4 ≠ 5) ✗
```

### Dot Product (1D Vectors)
```python
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

dot_product = v1 @ v2  # 32 (= 1×4 + 2×5 + 3×6)
# Or: np.dot(v1, v2)
```

### Matrix-Vector Multiplication
```python
A = np.array([[1, 2, 3],
              [4, 5, 6]])    # Shape: (2, 3)
x = np.array([10, 20, 30])   # Shape: (3,)

result = A @ x               # Shape: (2,)
# [1×10 + 2×20 + 3×30,
#  4×10 + 5×20 + 6×30]
```

### Batch Matrix Multiplication
```python
# Multiple samples processed together
X = np.random.randn(32, 784)    # 32 samples, 784 features
W = np.random.randn(10, 784)    # 10 neurons, 784 weights each

Z = X @ W.T                     # Shape: (32, 10)
# Each row: one sample's output across 10 neurons
```

## Neural Network Forward Pass Pattern

### Single Neuron
```python
# Components
inputs = np.array([x1, x2, x3])      # Input features
weights = np.array([w1, w2, w3])     # Learned weights
bias = b                              # Learned bias

# Computation
z = weights @ inputs + bias           # Weighted sum
output = np.maximum(0, z)             # ReLU activation

# Formula: output = ReLU(w·x + b)
```

### Layer of Neurons
```python
# Inputs
X = np.array([x1, x2, ..., xn])      # Shape: (n_features,)
W = np.random.randn(m, n)             # Shape: (n_neurons, n_features)
b = np.random.randn(m)                # Shape: (n_neurons,)

# Forward pass
Z = W @ X + b                         # Shape: (n_neurons,)
A = np.maximum(0, Z)                  # Shape: (n_neurons,)
```

### Batch Processing
```python
# Multiple samples at once
X_batch = np.random.randn(32, 784)    # 32 samples
W = np.random.randn(10, 784)          # 10 neurons
b = np.random.randn(10)               # 10 biases

Z = X_batch @ W.T + b                 # Shape: (32, 10)
A = np.maximum(0, Z)                  # Shape: (32, 10)
# Each row: one sample, each column: one neuron
```

## Activation Functions

| Function | Formula | NumPy |
|----------|---------|-------|
| ReLU | max(0, x) | `np.maximum(0, x)` |
| Sigmoid | 1/(1+e^(-x)) | `1 / (1 + np.exp(-x))` |
| Tanh | tanh(x) | `np.tanh(x)` |
| Leaky ReLU | max(0.01x, x) | `np.maximum(0.01*x, x)` |
| Softmax | e^x / Σe^x | See below |

### Softmax (Numerically Stable)
```python
def softmax(x):
    exp_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)
```

## Performance Comparison

| Operation | Loop Time | Vectorized Time | Speedup |
|-----------|-----------|-----------------|---------|
| Add arrays (n=10,000) | ~10 ms | ~0.01 ms | 1000x |
| Matrix multiply (100×100) | ~500 ms | ~0.5 ms | 1000x |
| Element-wise exp (n=100,000) | ~100 ms | ~0.1 ms | 1000x |

**Key insight**: Vectorized operations are typically 10-1000x faster than Python loops.

## Shape Compatibility Table

| Operation | Shape A | Shape B | Result Shape | Valid? |
|-----------|---------|---------|--------------|--------|
| Add | (3, 4) | (3, 4) | (3, 4) | ✓ |
| Add | (3, 4) | (4,) | (3, 4) | ✓ |
| Add | (3, 4) | (3, 1) | (3, 4) | ✓ |
| Add | (3, 4) | (1, 4) | (3, 4) | ✓ |
| Add | (3, 4) | (2, 4) | ERROR | ✗ |
| Matmul | (3, 4) | (4, 5) | (3, 5) | ✓ |
| Matmul | (3, 4) | (5, 6) | ERROR | ✗ |
| Matmul | (32, 784) | (784, 10) | (32, 10) | ✓ |

## Common Gotchas

### 1. Matmul vs Element-Wise Multiply
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

A * B   # Element-wise: [[5, 12], [21, 32]]
A @ B   # Matrix multiply: [[19, 22], [43, 50]]
```

### 2. Shape Mismatch in Broadcasting
```python
a = np.ones((3, 4))
b = np.ones((3, 5))

a + b  # ERROR! Shapes not compatible
# (3, 4) vs (3, 5) - neither 4 nor 5 is 1
```

### 3. Unexpected Broadcasting
```python
a = np.ones((3, 1))
b = np.ones((1, 4))

result = a + b  # Shape: (3, 4) - might not be what you expect!
```

### 4. Transposing for Batch Operations
```python
# WRONG: Shape mismatch
X = np.random.randn(32, 784)  # Batch of 32 samples
W = np.random.randn(10, 784)  # 10 neurons
Z = X @ W  # ERROR! (32, 784) @ (10, 784) incompatible

# CORRECT: Transpose W
Z = X @ W.T  # (32, 784) @ (784, 10) → (32, 10) ✓
```

## Debugging Shape Errors

```python
# Always print shapes when debugging
print(f"X shape: {X.shape}")
print(f"W shape: {W.shape}")
print(f"Result shape: {(X @ W.T).shape}")

# Use keepdims to preserve dimensions
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.sum(axis=1)              # Shape: (2,)
arr.sum(axis=1, keepdims=True)  # Shape: (2, 1) - easier to broadcast
```

## Key Takeaways

1. **Broadcasting** automatically aligns shapes using 3 rules
2. **Vectorization** replaces loops with fast array operations (10-1000x speedup)
3. **Matrix multiplication** is the core operation for neural networks
4. **Shape compatibility** is critical - always check shapes
5. **Batch processing** computes multiple samples in parallel using 2D arrays

**Next**: Apply these patterns to real data in Modules 5-8.
