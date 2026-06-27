"""
Module 3 Lab: The Matrix
=====================================================
Demonstrates NumPy arrays and one-hot encoding:
- Why Python lists are too slow (memory layout)
- Creating N-dimensional arrays
- Understanding .shape and array dimensions
- Rank-1 vs Rank-2 arrays (the shape bug)
- One-hot encoding from tokenizer output
- Connection to LLM token representations
"""

from dotenv import load_dotenv, find_dotenv
import numpy as np
from typing import List, Dict

# Load environment variables
load_dotenv(find_dotenv())


def explain_python_list_problem() -> None:
    """
    Why Python lists are too slow for AI.
    Explains non-contiguous memory layout.
    """
    print("=" * 60)
    print("PART 1: Why Python Lists Fail for AI")
    print("=" * 60)

    print("\n❌ Python list memory layout:")
    print("   [ref] → object")
    print("   [ref] → object")
    print("   [ref] → object")
    print("   └─ Scattered across RAM (non-contiguous)")
    print("   └─ Each element is a Python object (overhead)")
    print("   └─ CPU cache misses on every access")

    print("\n✓ NumPy array memory layout:")
    print("   [value][value][value][value]...")
    print("   └─ Contiguous block in RAM")
    print("   └─ Raw numeric data (no Python overhead)")
    print("   └─ CPU can load entire chunk into cache")

    print("\n🚀 Speed difference:")
    print("   NumPy: ~50-100x faster for numerical operations")
    print("   Reason: Contiguous memory + vectorization + SIMD")


def demonstrate_array_creation() -> None:
    """
    Show different ways to create NumPy arrays.
    """
    print("\n" + "=" * 60)
    print("PART 2: Creating NumPy Arrays")
    print("=" * 60)

    # From Python list
    print("\n1️⃣ From Python list:")
    python_list = [1, 2, 3, 4, 5]
    arr_from_list = np.array(python_list)
    print(f"   Python list: {python_list}")
    print(f"   NumPy array: {arr_from_list}")
    print(f"   Type: {type(arr_from_list)}")
    print(f"   dtype: {arr_from_list.dtype}")

    # Using np.zeros
    print("\n2️⃣ Using np.zeros (all zeros):")
    zeros = np.zeros(5)
    print(f"   np.zeros(5): {zeros}")
    print(f"   dtype: {zeros.dtype}")

    # Using np.ones
    print("\n3️⃣ Using np.ones (all ones):")
    ones = np.ones(5)
    print(f"   np.ones(5): {ones}")

    # Using np.arange
    print("\n4️⃣ Using np.arange (range of values):")
    range_arr = np.arange(0, 10, 2)  # start, stop, step
    print(f"   np.arange(0, 10, 2): {range_arr}")

    # Using np.linspace
    print("\n5️⃣ Using np.linspace (evenly spaced):")
    linspace_arr = np.linspace(0, 1, 5)  # start, stop, num_points
    print(f"   np.linspace(0, 1, 5): {linspace_arr}")


def demonstrate_shape_property() -> None:
    """
    Explain the .shape property and what it means.
    """
    print("\n" + "=" * 60)
    print("PART 3: Understanding .shape")
    print("=" * 60)

    print("\n📐 The .shape property tells you array dimensions")

    # 1D array
    arr_1d = np.array([1, 2, 3, 4, 5])
    print(f"\n   arr_1d = {arr_1d}")
    print(f"   arr_1d.shape = {arr_1d.shape}")
    print("   └─ (5,) means: 1-dimensional with 5 elements")

    # 2D array
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n   arr_2d =")
    print(f"   {arr_2d}")
    print(f"   arr_2d.shape = {arr_2d.shape}")
    print("   └─ (2, 3) means: 2 rows × 3 columns")

    # 3D array
    arr_3d = np.zeros((2, 3, 4))
    print(f"\n   arr_3d.shape = {arr_3d.shape}")
    print("   └─ (2, 3, 4) means: 2 matrices of 3×4 each")
    print("   └─ Like a stack of 2 images, each 3 pixels tall × 4 pixels wide")

    print("\n💡 Reading .shape:")
    print("   (rows, columns) for 2D")
    print("   (depth, rows, columns) for 3D")
    print("   (batch, height, width, channels) for images")


def demonstrate_rank_arrays() -> None:
    """
    Explain Rank-1 vs Rank-2 arrays and the common shape bug.
    """
    print("\n" + "=" * 60)
    print("PART 4: Rank-1 vs Rank-2 Arrays (The Shape Bug)")
    print("=" * 60)

    print("\n🔍 Three different 5-element arrays:")

    # Rank-1 (1D)
    rank1 = np.array([1, 2, 3, 4, 5])
    print(f"\n   Rank-1 (1D): {rank1}")
    print(f"   Shape: {rank1.shape} ← (5,) is a 1D vector")

    # Rank-2 column vector
    column = np.array([[1], [2], [3], [4], [5]])
    print(f"\n   Rank-2 column: {column.T}")  # Transpose for display
    print(f"   Shape: {column.shape} ← (5, 1) is a 2D column")

    # Rank-2 row vector
    row = np.array([[1, 2, 3, 4, 5]])
    print(f"\n   Rank-2 row: {row}")
    print(f"   Shape: {row.shape} ← (1, 5) is a 2D row")

    print("\n⚠️  THE SHAPE BUG:")
    print("   Many NumPy operations return (n,) by default")
    print("   But matrix operations expect (n, 1) or (1, n)")
    print("   This mismatch causes cryptic errors!")

    print("\n✓ Solution: reshape to explicit dimensions")
    fixed_column = rank1.reshape(-1, 1)  # -1 means 'infer this dimension'
    fixed_row = rank1.reshape(1, -1)
    print(f"   rank1.reshape(-1, 1) → shape {fixed_column.shape}")
    print(f"   rank1.reshape(1, -1) → shape {fixed_row.shape}")


def demonstrate_reshaping() -> None:
    """
    Show how to reshape arrays and when to use it.
    """
    print("\n" + "=" * 60)
    print("PART 5: Reshaping Arrays")
    print("=" * 60)

    print("\n🔄 Reshaping transforms array dimensions without copying data")

    # Start with 1D
    original = np.arange(12)
    print(f"\n   Original: {original}")
    print(f"   Shape: {original.shape}")

    # Reshape to 2D (3×4)
    reshaped_3x4 = original.reshape(3, 4)
    print(f"\n   Reshaped to (3, 4):")
    print(reshaped_3x4)

    # Reshape to 2D (4×3)
    reshaped_4x3 = original.reshape(4, 3)
    print(f"\n   Reshaped to (4, 3):")
    print(reshaped_4x3)

    # Use -1 to infer dimension
    auto_shaped = original.reshape(2, -1)
    print(f"\n   Reshaped to (2, -1) → inferred shape: {auto_shaped.shape}")
    print(auto_shaped)

    print("\n💡 Key rule: Total elements must stay the same")
    print(f"   12 elements can be: (12,) or (3,4) or (2,6) or (1,12) etc.")
    print("   12 elements CANNOT be: (5,3) [would need 15 elements]")


def build_vocabulary(text: str) -> Dict[str, int]:
    """
    Build a word-to-index vocabulary from text.
    Similar to Module 1 tokenizer output.
    """
    words = text.lower().split()
    unique_words = sorted(set(words))  # Sort for consistency
    vocab = {word: idx for idx, word in enumerate(unique_words)}
    return vocab


def demonstrate_onehot_manual(vocab: Dict[str, int], word: str) -> np.ndarray:
    """
    Manually create one-hot encoding for a single word.
    """
    vocab_size = len(vocab)
    onehot = np.zeros(vocab_size)
    word_idx = vocab.get(word.lower(), -1)

    if word_idx >= 0:
        onehot[word_idx] = 1

    return onehot


def create_onehot_matrix(text: str, vocab: Dict[str, int]) -> np.ndarray:
    """
    Convert entire text to one-hot encoded matrix.
    Each row is one word, each column is a vocabulary position.
    """
    words = text.lower().split()
    vocab_size = len(vocab)
    num_words = len(words)

    # Initialize matrix with zeros
    onehot_matrix = np.zeros((num_words, vocab_size))

    # Fill in the ones
    for i, word in enumerate(words):
        word_idx = vocab.get(word, -1)
        if word_idx >= 0:
            onehot_matrix[i, word_idx] = 1

    return onehot_matrix


def demonstrate_onehot_encoding() -> None:
    """
    Show the complete one-hot encoding workflow.
    """
    print("\n" + "=" * 60)
    print("PART 6: One-Hot Encoding")
    print("=" * 60)

    # Sample text (like tokenizer output from Module 1)
    sample_text = "the cat sat on the mat"

    print(f"\n📝 Sample text: '{sample_text}'")

    # Step 1: Build vocabulary
    vocab = build_vocabulary(sample_text)
    print(f"\n1️⃣ Build vocabulary:")
    for word, idx in vocab.items():
        print(f"   '{word}' → index {idx}")

    # Step 2: One-hot encode a single word
    word_to_encode = "cat"
    onehot_single = demonstrate_onehot_manual(vocab, word_to_encode)
    print(f"\n2️⃣ One-hot encode '{word_to_encode}':")
    print(f"   {onehot_single}")
    print(f"   └─ Shape: {onehot_single.shape}")
    print(f"   └─ Meaning: 1 at index {vocab[word_to_encode]} ('{word_to_encode}'), 0 elsewhere")

    # Step 3: Create full matrix
    onehot_matrix = create_onehot_matrix(sample_text, vocab)
    print(f"\n3️⃣ One-hot matrix for entire text:")
    print(f"   Shape: {onehot_matrix.shape}")
    print(f"   └─ {onehot_matrix.shape[0]} words × {onehot_matrix.shape[1]} vocabulary size")
    print(f"\n   Matrix:")
    print(onehot_matrix)

    # Explain what each row/column means
    words = sample_text.split()
    print(f"\n📊 Reading the matrix:")
    for i, word in enumerate(words):
        word_idx = vocab[word]
        print(f"   Row {i}: '{word}' → 1 at column {word_idx}")

    print(f"\n💡 Why one-hot encoding?")
    print("   - Converts discrete tokens (words) → numerical vectors")
    print("   - Each word is a unique, orthogonal vector")
    print("   - No implicit ordering (unlike word indices)")
    print("   - Foundation for neural network input")


def demonstrate_sparse_representation() -> None:
    """
    Show why one-hot encoding is 'sparse' and what that means.
    """
    print("\n" + "=" * 60)
    print("PART 7: The Sparsity Problem")
    print("=" * 60)

    # Large vocabulary example
    vocab_size = 50000
    sentence_length = 20

    print(f"\n📈 Real-world example:")
    print(f"   Vocabulary size: {vocab_size:,} words")
    print(f"   Sentence length: {sentence_length} words")

    # Calculate matrix size
    onehot_shape = (sentence_length, vocab_size)
    total_elements = sentence_length * vocab_size
    nonzero_elements = sentence_length  # Only 1 per row

    print(f"\n   One-hot matrix shape: {onehot_shape}")
    print(f"   Total elements: {total_elements:,}")
    print(f"   Non-zero elements: {nonzero_elements}")
    print(f"   Sparsity: {(1 - nonzero_elements/total_elements)*100:.4f}%")

    print(f"\n⚠️  Problem: 99.96% of values are zero!")
    print("   - Wastes memory")
    print("   - Wastes computation")
    print("   - No semantic meaning (cat ≠ dog)")

    print(f"\n✓ Solution: Dense embeddings (next modules)")
    print("   - Compress 50,000 dimensions → 768 dimensions")
    print("   - Learn semantic relationships")
    print("   - Similar words have similar vectors")


def demonstrate_llm_connection() -> None:
    """
    Connect one-hot encoding to LLM embeddings.
    """
    print("\n" + "=" * 60)
    print("PART 8: Connection to LLM Embeddings")
    print("=" * 60)

    print("\n🔗 From one-hot to embeddings:")

    print("\n   Stage 1: One-hot encoding (what we just did)")
    print("   'cat' → [0, 0, 1, 0, 0, ..., 0]  (50,000 dims)")
    print("   └─ Sparse, no semantics")

    print("\n   Stage 2: Embedding layer (what LLMs do)")
    print("   'cat' → [0.24, -0.81, 0.53, ..., 0.19]  (768 dims)")
    print("   └─ Dense, semantic meaning")

    print("\n   Stage 3: Contextual embeddings (Transformers)")
    print("   'cat' in 'The cat sat' vs 'Cat Stevens'")
    print("   └─ Same word, different vectors based on context")

    print("\n💡 Why this matters:")
    print("   1. Tokenizer splits text → tokens")
    print("   2. Tokens → one-hot vectors (discrete)")
    print("   3. Embedding layer: one-hot → dense vectors (continuous)")
    print("   4. Dense vectors → neural network input")
    print("   5. Network learns semantic relationships")


def main():
    """
    Run all demonstrations.
    """
    print("=" * 60)
    print("Module 3 Lab: The Matrix")
    print("Thinking in Arrays (Tensors)")
    print("=" * 60)

    # Part 1: Why lists fail
    explain_python_list_problem()

    # Part 2: Creating arrays
    demonstrate_array_creation()

    # Part 3: .shape property
    demonstrate_shape_property()

    # Part 4: Rank-1 vs Rank-2
    demonstrate_rank_arrays()

    # Part 5: Reshaping
    demonstrate_reshaping()

    # Part 6: One-hot encoding
    demonstrate_onehot_encoding()

    # Part 7: Sparsity
    demonstrate_sparse_representation()

    # Part 8: LLM connection
    demonstrate_llm_connection()

    print("\n" + "=" * 60)
    print("🎓 Key Takeaways:")
    print("=" * 60)
    print("1. NumPy arrays: Contiguous memory → 50-100x faster than Python lists")
    print("2. .shape property: Tells you array dimensions (rows, columns, etc.)")
    print("3. Rank matters: (n,) ≠ (n,1) ≠ (1,n) — use .reshape() explicitly")
    print("4. One-hot encoding: Converts words → sparse binary vectors")
    print("5. Sparsity problem: 99.96% zeros → need dense embeddings")
    print("6. LLM pipeline: Text → Tokens → One-hot → Embeddings → Neural Net")
    print("=" * 60)
    print("✓ Lab complete!")


if __name__ == "__main__":
    main()
