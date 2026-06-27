# Quick Reference: NumPy Arrays

## Why NumPy Over Python Lists?

| Feature | Python List | NumPy Array |
|---------|-------------|-------------|
| Memory layout | Non-contiguous (pointers) | Contiguous block |
| Element type | Mixed types | Single type (homogeneous) |
| Speed | Slow (Python overhead) | Fast (C/BLAS/SIMD) |
| Typical speedup | 1x (baseline) | 50-100x |
| Operations | Element-by-element loops | Vectorized |
| Memory efficiency | ~28 bytes/element | 4-8 bytes/element |

**Key insight**: NumPy arrays store raw numeric values in contiguous memory, enabling CPU cache optimization and vectorized operations.

## Array Creation Patterns

### From Python Lists
```python
arr = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2], [3, 4]])
```

### Filled Arrays
```python
np.zeros(5)              # [0. 0. 0. 0. 0.]
np.zeros((3, 4))         # 3×4 matrix of zeros
np.ones(5)               # [1. 1. 1. 1. 1.]
np.full((2, 3), 7)       # 2×3 matrix filled with 7
```

### Range and Sequences
```python
np.arange(10)            # [0, 1, 2, ..., 9]
np.arange(0, 10, 2)      # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)     # [0.00, 0.25, 0.50, 0.75, 1.00]
```

### Special Arrays
```python
np.eye(3)                # 3×3 identity matrix
np.random.rand(3, 4)     # 3×4 random values [0, 1)
np.random.randn(3, 4)    # 3×4 standard normal
np.random.randint(0, 10, (3, 4))  # 3×4 random integers [0, 10)
```

## Array Shape and Dimensions

### Understanding `.shape`
```python
arr_1d = np.array([1, 2, 3])
arr_1d.shape  # (3,) - tuple with one element

arr_2d = np.array([[1, 2], [3, 4]])
arr_2d.shape  # (2, 2) - 2 rows, 2 columns

arr_3d = np.zeros((2, 3, 4))
arr_3d.shape  # (2, 3, 4) - 2 matrices, each 3×4
```

### Shape Terminology
| Dimension | Name | Example Shape | Description |
|-----------|------|---------------|-------------|
| 1D | Vector | `(5,)` | 5 elements in a line |
| 2D | Matrix | `(3, 4)` | 3 rows × 4 columns |
| 3D | Tensor | `(2, 3, 4)` | 2 layers of 3×4 matrices |
| nD | Tensor | `(a, b, c, ...)` | Nested multidimensional array |

### Rank-1 vs Rank-2 Arrays (Common Bug!)

```python
# Rank-1 array (vector)
arr_1 = np.array([1, 2, 3])
arr_1.shape  # (3,) - one dimension

# Rank-2 array (row vector)
arr_2 = np.array([[1, 2, 3]])
arr_2.shape  # (1, 3) - two dimensions: 1 row, 3 columns

# Problem: they behave differently in matrix operations!
# Solution: always use 2D shapes for matrices
```

**Rule of thumb**: For matrix math, use 2D shapes like `(1, n)` or `(n, 1)`, not `(n,)`.

## Shape Manipulation

### Reshaping
```python
arr = np.arange(12)      # Shape: (12,)
arr.reshape(3, 4)        # Shape: (3, 4) - 3 rows, 4 columns
arr.reshape(2, 6)        # Shape: (2, 6) - 2 rows, 6 columns
arr.reshape(2, 2, 3)     # Shape: (2, 2, 3) - 3D tensor
arr.reshape(-1, 4)       # Shape: (?, 4) - infer first dimension
```

**Rule**: Total elements must stay constant. `12 = 3×4 = 2×6 = 2×2×3`.

### Adding/Removing Dimensions
```python
arr = np.array([1, 2, 3])  # Shape: (3,)

# Add dimension
arr[:, np.newaxis]         # Shape: (3, 1) - column vector
arr[np.newaxis, :]         # Shape: (1, 3) - row vector
np.expand_dims(arr, axis=0)  # Shape: (1, 3)
np.expand_dims(arr, axis=1)  # Shape: (3, 1)

# Remove dimension (only size-1 dimensions)
arr = np.array([[1, 2, 3]])  # Shape: (1, 3)
arr.squeeze()                # Shape: (3,)
```

### Flattening
```python
arr_2d = np.array([[1, 2], [3, 4]])
arr_2d.flatten()         # [1, 2, 3, 4] - 1D copy
arr_2d.ravel()           # [1, 2, 3, 4] - 1D view (no copy if possible)
```

## One-Hot Encoding Patterns

### Single Word One-Hot
```python
vocab_size = 5
word_idx = 2

# Manual approach
onehot = np.zeros(vocab_size)
onehot[word_idx] = 1
# Result: [0. 0. 1. 0. 0.]

# Using np.eye
onehot = np.eye(vocab_size)[word_idx]
# Result: [0. 0. 1. 0. 0.]
```

### Batch One-Hot Encoding
```python
vocab_size = 5
word_indices = [2, 0, 3, 1]

# All words at once
onehot_matrix = np.eye(vocab_size)[word_indices]
# Shape: (4, 5)
# Each row is a one-hot vector for one word
```

### Complete Workflow
```python
# Given text and vocabulary
text = "the cat sat on the mat"
vocab = {"the": 0, "cat": 1, "sat": 2, "on": 3, "mat": 4}

# Convert words to indices
words = text.split()
indices = [vocab[word] for word in words]  # [0, 1, 2, 3, 0, 4]

# Create one-hot matrix
vocab_size = len(vocab)
onehot_matrix = np.eye(vocab_size)[indices]
# Shape: (6, 5) - 6 words × 5 vocab size
```

## Indexing and Slicing

### Basic Indexing
```python
arr = np.array([10, 20, 30, 40, 50])
arr[0]       # 10 - first element
arr[-1]      # 50 - last element
arr[1:4]     # [20, 30, 40] - slice
```

### 2D Indexing
```python
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr[0, 1]    # 2 - row 0, column 1
arr[1, :]    # [4, 5, 6] - entire row 1
arr[:, 2]    # [3, 6] - entire column 2
arr[0:2, 1:3]  # [[2, 3], [5, 6]] - submatrix
```

### Fancy Indexing
```python
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]
arr[indices]  # [10, 30, 50] - select specific positions

# Boolean indexing
mask = arr > 25
arr[mask]     # [30, 40, 50] - elements > 25
```

## Common Data Types (dtype)

| dtype | Description | Bytes | Range |
|-------|-------------|-------|-------|
| `int8` | Integer | 1 | -128 to 127 |
| `int32` | Integer | 4 | -2B to 2B |
| `int64` | Integer | 8 | -9E18 to 9E18 |
| `float32` | Floating point | 4 | ~±1.2E-38 to ±3.4E38 |
| `float64` | Floating point | 8 | ~±2.2E-308 to ±1.8E308 |
| `bool` | Boolean | 1 | True or False |
| `uint8` | Unsigned int | 1 | 0 to 255 (common for images) |

### Specifying dtype
```python
np.zeros(5, dtype=np.int32)
np.array([1, 2, 3], dtype=np.float32)
arr.astype(np.int64)  # Convert existing array
```

## Key Functions Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `np.array(list)` | Create from list | `np.array([1, 2, 3])` |
| `np.zeros(shape)` | Array of zeros | `np.zeros((3, 4))` |
| `np.ones(shape)` | Array of ones | `np.ones(5)` |
| `np.arange(start, stop, step)` | Range | `np.arange(0, 10, 2)` |
| `np.linspace(start, stop, n)` | n evenly spaced | `np.linspace(0, 1, 5)` |
| `np.eye(n)` | Identity matrix | `np.eye(3)` |
| `arr.reshape(shape)` | Change shape | `arr.reshape(3, 4)` |
| `arr.flatten()` | To 1D | `arr.flatten()` |
| `np.expand_dims(arr, axis)` | Add dimension | `np.expand_dims(arr, 0)` |
| `arr.squeeze()` | Remove size-1 dims | `arr.squeeze()` |
| `arr.shape` | Get shape | `arr.shape` |
| `arr.dtype` | Get data type | `arr.dtype` |
| `arr.ndim` | Number of dimensions | `arr.ndim` |
| `arr.size` | Total elements | `arr.size` |

## Memory Layout Visualization

```
Python List (non-contiguous):
┌─────┬─────┬─────┬─────┐
│ ref │ ref │ ref │ ref │  ← List container
└──┬──┴──┬──┴──┬──┴──┬──┘
   │     │     │     │
   ↓     ↓     ↓     ↓
 obj   obj   obj   obj    ← Python objects scattered in RAM

NumPy Array (contiguous):
┌─────┬─────┬─────┬─────┐
│ val │ val │ val │ val │  ← Raw values in one memory block
└─────┴─────┴─────┴─────┘
```

**Result**: NumPy arrays fit in CPU cache → 50-100x speedup.

## Common Gotchas

### 1. Shape Mismatch
```python
# Wrong: creates nested list
arr = np.array([1, 2, 3, [4, 5]])  # dtype=object, not numeric!

# Correct: all elements same level
arr = np.array([1, 2, 3, 4, 5])
```

### 2. Rank-1 Array Trap
```python
a = np.array([1, 2, 3])     # Shape: (3,)
b = np.array([[1], [2], [3]])  # Shape: (3, 1)

# These behave differently in matrix operations!
# Prefer explicit 2D shapes for matrices.
```

### 3. Copy vs View
```python
arr = np.array([1, 2, 3])
view = arr[:]           # View (shares memory)
copy = arr.copy()       # Copy (independent)

view[0] = 99
print(arr)  # [99, 2, 3] - original changed!

copy[0] = 99
print(arr)  # [99, 2, 3] - original unchanged
```

### 4. Integer Division
```python
arr = np.array([1, 2, 3])
arr / 2      # [0.5, 1.0, 1.5] - float result
arr // 2     # [0, 1, 1] - integer division
```

## Connection to AI/ML

- **Embeddings**: Replace one-hot (sparse) with dense vectors learned by neural networks
- **Batch Processing**: Shape `(batch_size, features)` for parallel training
- **Images**: Shape `(height, width, channels)` for RGB images
- **Time Series**: Shape `(sequence_length, features)` for RNNs
- **Tensors**: Higher-dimensional arrays for complex data structures

**Next module**: Learn how to perform fast math operations on these arrays without loops (vectorization and broadcasting).
