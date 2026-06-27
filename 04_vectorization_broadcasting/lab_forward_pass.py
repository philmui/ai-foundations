"""
Module 4: Vectorization & Broadcasting
Lab: The Forward Pass

Learn how to compute neural network operations using NumPy vectorization
without writing any for loops.
"""

import time
from dotenv import load_dotenv, find_dotenv
import numpy as np

# Load environment variables
load_dotenv(find_dotenv())

print("=" * 70)
print("MODULE 4: VECTORIZATION & BROADCASTING")
print("Lab: The Forward Pass")
print("=" * 70)
print()

# ============================================================================
# PART 1: Element-wise Operations
# ============================================================================
print("\n" + "=" * 70)
print("PART 1: Element-wise Operations")
print("=" * 70)

# Create two simple arrays
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])

print("\nArray 1:", arr1)
print("Array 2:", arr2)

# Addition
print("\nElement-wise Addition:")
print(f"{arr1} + {arr2} = {arr1 + arr2}")

# Multiplication
print("\nElement-wise Multiplication:")
print(f"{arr1} * {arr2} = {arr1 * arr2}")

# Division
print("\nElement-wise Division:")
print(f"{arr2} / {arr1} = {arr2 / arr1}")

# Squaring
print("\nSquaring (element-wise):")
print(f"{arr1}² = {arr1 ** 2}")

# ============================================================================
# PART 2: Scalar Broadcasting
# ============================================================================
print("\n" + "=" * 70)
print("PART 2: Scalar Broadcasting")
print("=" * 70)

scalar = 5
array = np.array([1, 2, 3, 4])

print(f"\nScalar: {scalar}")
print(f"Array:  {array}")

print("\nBroadcasting multiplication:")
print(f"{scalar} * {array} = {scalar * array}")

print("\nBroadcasting addition:")
print(f"{array} + {scalar} = {array + scalar}")

print("\nWhat happens internally:")
print(f"NumPy treats {scalar} as if it were [{scalar}, {scalar}, {scalar}, {scalar}]")
print("Then performs element-wise operation")

# ============================================================================
# PART 3: The Dot Product
# ============================================================================
print("\n" + "=" * 70)
print("PART 3: The Dot Product")
print("=" * 70)

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

print(f"\nVector 1: {vec1}")
print(f"Vector 2: {vec2}")

# Manual computation
print("\nManual computation:")
print(f"(1×4) + (2×5) + (3×6) = {1*4} + {2*5} + {3*6} = {1*4 + 2*5 + 3*6}")

# Using np.dot
dot_result = np.dot(vec1, vec2)
print(f"\nUsing np.dot: {dot_result}")

# Using @ operator
at_result = vec1 @ vec2
print(f"Using @ operator: {at_result}")

print("\nThe dot product is the sum of element-wise products.")

# ============================================================================
# PART 4: Matrix Multiplication
# ============================================================================
print("\n" + "=" * 70)
print("PART 4: Matrix Multiplication")
print("=" * 70)

# Create matrices
mat_a = np.array([[1, 2, 3],
                  [4, 5, 6]])  # Shape: (2, 3)

mat_b = np.array([[10, 11],
                  [20, 21],
                  [30, 31]])   # Shape: (3, 2)

print("\nMatrix A (2×3):")
print(mat_a)

print("\nMatrix B (3×2):")
print(mat_b)

# Matrix multiplication
result = mat_a @ mat_b
print("\nMatrix A @ Matrix B (2×2):")
print(result)

print("\nShape requirement for matrix multiplication:")
print(f"A: {mat_a.shape} @ B: {mat_b.shape} → Result: {result.shape}")
print("The inner dimensions must match: (2, 3) @ (3, 2) → (2, 2)")

# Manual verification of one element
print("\nManual computation of result[0, 0]:")
print(f"Row 0 of A: {mat_a[0]}")
print(f"Col 0 of B: {mat_b[:, 0]}")
print(f"Dot product: {mat_a[0] @ mat_b[:, 0]}")

# ============================================================================
# PART 5: Broadcasting Rules
# ============================================================================
print("\n" + "=" * 70)
print("PART 5: Broadcasting Rules")
print("=" * 70)

print("\nNumPy Broadcasting Rules:")
print("1. If arrays have different ranks, prepend 1s to the smaller rank")
print("2. Arrays are compatible if dimensions are equal OR one is 1")
print("3. After broadcasting, each array behaves as if it had the larger shape")

# Example 1: Simple broadcasting
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])  # Shape: (2, 3)
arr_1d = np.array([10, 20, 30])  # Shape: (3,)

print("\n--- Example 1: Broadcasting 1D to 2D ---")
print(f"2D array shape: {arr_2d.shape}")
print(arr_2d)
print(f"\n1D array shape: {arr_1d.shape}")
print(arr_1d)

result_broadcast = arr_2d + arr_1d
print(f"\nResult shape: {result_broadcast.shape}")
print(result_broadcast)

print("\nWhat happened:")
print(f"1D array {arr_1d.shape} was treated as {(1, 3)}")
print("Then broadcast to (2, 3) by repeating the row")

# Example 2: Column vector broadcasting
col_vec = np.array([[100],
                    [200]])  # Shape: (2, 1)

print("\n--- Example 2: Broadcasting column vector ---")
print(f"Column vector shape: {col_vec.shape}")
print(col_vec)

result_broadcast2 = arr_2d + col_vec
print(f"\nResult shape: {result_broadcast2.shape}")
print(result_broadcast2)

print("\nWhat happened:")
print(f"Column vector {col_vec.shape} was broadcast to {arr_2d.shape}")
print("by repeating across columns")

# ============================================================================
# PART 6: The Artificial Neuron
# ============================================================================
print("\n" + "=" * 70)
print("PART 6: The Artificial Neuron")
print("=" * 70)

print("\nAn artificial neuron performs:")
print("  output = activation(weights · inputs + bias)")
print()
print("Components:")
print("  - inputs: data features (x₁, x₂, ..., xₙ)")
print("  - weights: learned parameters (w₁, w₂, ..., wₙ)")
print("  - bias: learned offset (b)")
print("  - activation: non-linear function (e.g., ReLU, sigmoid)")

# Single neuron example
inputs = np.array([1.5, 2.0, 3.5])  # 3 features
weights = np.array([0.2, 0.8, -0.5])  # 3 weights
bias = 2.0

print("\n--- Single Neuron Forward Pass ---")
print(f"Inputs:  {inputs}")
print(f"Weights: {weights}")
print(f"Bias:    {bias}")

# Compute weighted sum
z = np.dot(weights, inputs) + bias
print(f"\nWeighted sum z = w·x + b = {z:.4f}")

# Apply ReLU activation
def relu(x):
    """ReLU activation: max(0, x)"""
    return np.maximum(0, x)

output = relu(z)
print(f"After ReLU activation: {output:.4f}")

print("\nStep-by-step:")
print(f"1. w·x = {weights} · {inputs}")
print(f"   = ({weights[0]}×{inputs[0]}) + ({weights[1]}×{inputs[1]}) + ({weights[2]}×{inputs[2]})")
print(f"   = {weights @ inputs:.4f}")
print(f"2. z = w·x + b = {weights @ inputs:.4f} + {bias} = {z:.4f}")
print(f"3. output = ReLU(z) = max(0, {z:.4f}) = {output:.4f}")

# ============================================================================
# PART 7: Layer of Neurons (Matrix Multiplication)
# ============================================================================
print("\n" + "=" * 70)
print("PART 7: Layer of Neurons")
print("=" * 70)

print("\nA layer with multiple neurons uses matrix multiplication:")
print("  Z = W @ X + b")
print("  where W is (n_neurons × n_features)")
print("        X is (n_features,)")
print("        b is (n_neurons,)")

# Layer with 4 neurons, 3 inputs each
n_neurons = 4
n_features = 3

# Initialize random weights and biases
np.random.seed(42)
W = np.random.randn(n_neurons, n_features) * 0.5  # Shape: (4, 3)
b = np.random.randn(n_neurons)                     # Shape: (4,)
X = np.array([1.0, 2.0, 3.0])                       # Shape: (3,)

print(f"\nWeight matrix W shape: {W.shape}")
print(W)

print(f"\nBias vector b shape: {b.shape}")
print(b)

print(f"\nInput vector X shape: {X.shape}")
print(X)

# Forward pass
Z = W @ X + b  # Matrix multiplication + broadcasting
A = relu(Z)    # Element-wise activation

print(f"\nWeighted sums Z shape: {Z.shape}")
print(Z)

print(f"\nActivations A shape: {A.shape}")
print(A)

print("\nWhat happened:")
print(f"1. W @ X: ({n_neurons}, {n_features}) @ ({n_features},) → ({n_neurons},)")
print(f"   Each neuron computes its own weighted sum")
print(f"2. Z + b: Broadcasting adds bias to each neuron's sum")
print(f"3. ReLU(Z): Element-wise activation applied to all neurons")

# ============================================================================
# PART 8: Vectorization vs For Loops
# ============================================================================
print("\n" + "=" * 70)
print("PART 8: Vectorization vs For Loops")
print("=" * 70)

print("\nLet's compare the speed of vectorized operations vs for loops")

# Large layer
large_n_neurons = 1000
large_n_features = 500

W_large = np.random.randn(large_n_neurons, large_n_features)
b_large = np.random.randn(large_n_neurons)
X_large = np.random.randn(large_n_features)

# Vectorized approach
print("\n--- Vectorized Approach ---")
start_time = time.time()
Z_vectorized = W_large @ X_large + b_large
A_vectorized = relu(Z_vectorized)
vectorized_time = time.time() - start_time
print(f"Time taken: {vectorized_time*1000:.4f} ms")

# For loop approach
print("\n--- For Loop Approach ---")
start_time = time.time()
Z_loop = np.zeros(large_n_neurons)
for i in range(large_n_neurons):
    for j in range(large_n_features):
        Z_loop[i] += W_large[i, j] * X_large[j]
    Z_loop[i] += b_large[i]
A_loop = relu(Z_loop)
loop_time = time.time() - start_time
print(f"Time taken: {loop_time*1000:.4f} ms")

# Compare
speedup = loop_time / vectorized_time
print(f"\nSpeedup: {speedup:.1f}x faster")
print(f"Vectorized is {speedup:.1f} times faster than for loops!")

# Verify results are the same
print(f"\nResults match: {np.allclose(A_vectorized, A_loop)}")

print("\nWhy is vectorization faster?")
print("1. NumPy operations are implemented in C")
print("2. CPU can perform SIMD (Single Instruction, Multiple Data)")
print("3. Better cache utilization")
print("4. Less Python overhead")

# ============================================================================
# PART 9: Connection to Real Neural Networks
# ============================================================================
print("\n" + "=" * 70)
print("PART 9: Connection to Real Neural Networks")
print("=" * 70)

print("\nWhat we just learned is the foundation of neural networks:")
print()
print("Single neuron forward pass:")
print("  y = f(w·x + b)")
print()
print("Layer of neurons:")
print("  Y = f(W @ X + b)")
print()
print("Deep neural network:")
print("  Layer 1: H₁ = f(W₁ @ X + b₁)")
print("  Layer 2: H₂ = f(W₂ @ H₁ + b₂)")
print("  Layer 3: Y = f(W₃ @ H₂ + b₃)")
print()
print("Each layer is just matrix multiplication + activation!")

print("\nModern frameworks (PyTorch, TensorFlow) use the same principles,")
print("but with:")
print("  - GPU acceleration for massive parallelism")
print("  - Automatic differentiation for backpropagation")
print("  - Optimized memory management")
print("  - Batching multiple examples at once")

# Example: batched computation
print("\n--- Example: Batched Forward Pass ---")
batch_size = 3
X_batch = np.random.randn(batch_size, n_features)  # Shape: (3, 3)

print(f"Batch of {batch_size} examples, {n_features} features each:")
print(f"X_batch shape: {X_batch.shape}")
print(X_batch)

# Forward pass for entire batch
Z_batch = X_batch @ W.T + b  # Shape: (3, 4)
A_batch = relu(Z_batch)

print(f"\nOutput shape: {A_batch.shape}")
print(f"({batch_size} examples, {n_neurons} neuron outputs)")
print(A_batch)

print("\nIn PyTorch/TensorFlow:")
print("  - Replace np.array with torch.tensor or tf.Tensor")
print("  - Move to GPU with .cuda() or .to('gpu')")
print("  - Use built-in layers like nn.Linear")
print("  - But the math is exactly the same!")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 70)
print("SUMMARY: Key Takeaways")
print("=" * 70)

print("\n✓ Element-wise operations work on corresponding array elements")
print("✓ Broadcasting extends smaller arrays to match larger shapes")
print("✓ Dot product: sum of element-wise products")
print("✓ Matrix multiplication: (m×n) @ (n×p) → (m×p)")
print("✓ Vectorization eliminates for loops and speeds up code")
print("✓ Neural networks are just repeated matrix operations")
print("✓ Single neuron: output = f(w·x + b)")
print("✓ Layer of neurons: output = f(W @ x + b)")

print("\n" + "=" * 70)
print("Lab Complete!")
print("=" * 70)
