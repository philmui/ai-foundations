"""
Module 2 Lab: The Infinite Data Loader
=====================================================
Demonstrates Pythonic patterns for AI data processing:
- List & dict comprehensions
- Generator functions with yield
- Memory-efficient data streaming
- Connection to PyTorch DataLoader concepts
"""

from dotenv import load_dotenv, find_dotenv
import os
import sys

# Load environment variables
load_dotenv(find_dotenv())


def generate_mock_corpus(filename: str, num_lines: int = 10000) -> None:
    """
    Generate a large mock text file for testing.
    Simulates AI research papers with repeating patterns.
    """
    print(f"\n📝 Generating mock corpus: {num_lines} lines...")

    templates = [
        "Neural networks learn representations from data by optimizing loss functions.",
        "Transformers use self-attention mechanisms to capture contextual relationships.",
        "Gradient descent iteratively updates model parameters to minimize error.",
        "Embeddings map discrete tokens into continuous vector spaces.",
        "Backpropagation computes gradients through computational graphs efficiently.",
        "Regularization techniques prevent overfitting on training datasets.",
        "Batch normalization stabilizes training by normalizing layer activations.",
        "Dropout randomly disables neurons during training to improve generalization.",
        "Learning rate schedules adjust step sizes during optimization.",
        "Cross-entropy loss measures prediction error for classification tasks.",
    ]

    with open(filename, 'w') as f:
        for i in range(num_lines):
            line = templates[i % len(templates)]
            f.write(f"Line {i+1}: {line}\n")

    # Check file size
    size_mb = os.path.getsize(filename) / (1024 * 1024)
    print(f"✓ Created {filename} ({size_mb:.2f} MB)")


def demonstrate_list_comprehension(filename: str) -> list[str]:
    """
    Show how list comprehensions clean data efficiently.
    PROBLEM: Loads entire file into memory at once.
    """
    print("\n" + "="*60)
    print("PART 1: List Comprehension (Memory Intensive)")
    print("="*60)

    # Traditional for loop approach
    print("\n❌ Old way (verbose for loop):")
    cleaned_lines_old = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().lower()
            if len(line) > 0:
                cleaned_lines_old.append(line)
    print(f"   Processed {len(cleaned_lines_old)} lines with for loop")

    # List comprehension approach
    print("\n✓ New way (list comprehension):")
    with open(filename, 'r') as f:
        cleaned_lines = [
            line.strip().lower()
            for line in f
            if len(line.strip()) > 0
        ]
    print(f"   Processed {len(cleaned_lines)} lines with comprehension")

    print(f"\n⚠️  Memory usage: All {len(cleaned_lines)} lines loaded into RAM!")
    return cleaned_lines[:100]  # Return sample for demo


def demonstrate_dict_comprehension(lines: list[str]) -> dict[str, int]:
    """
    Build a vocabulary (word frequency dictionary) using dict comprehension.
    """
    print("\n" + "="*60)
    print("PART 2: Dict Comprehension (Building Vocabularies)")
    print("="*60)

    # First, get all words from sample lines
    all_words = []
    for line in lines:
        words = line.split()
        all_words.extend(words)

    print(f"\n📚 Total words in sample: {len(all_words)}")

    # Traditional way: build vocabulary with for loop
    print("\n❌ Old way (for loop):")
    vocab_old = {}
    for word in all_words:
        if word in vocab_old:
            vocab_old[word] += 1
        else:
            vocab_old[word] = 1
    print(f"   Built vocabulary with {len(vocab_old)} unique words")

    # Dict comprehension way
    print("\n✓ New way (dict comprehension):")
    unique_words = set(all_words)
    vocab = {word: all_words.count(word) for word in unique_words}
    print(f"   Built vocabulary with {len(vocab)} unique words")

    # Show top 5 words
    top_5 = sorted(vocab.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\n   Top 5 words:")
    for word, count in top_5:
        print(f"      {word}: {count}")

    return vocab


def demonstrate_memory_problem(filename: str) -> None:
    """
    Illustrate the memory problem when loading large files.
    """
    print("\n" + "="*60)
    print("PART 3: The Memory Problem")
    print("="*60)

    print("\n❌ Loading everything at once:")
    print("   File → RAM → Process")
    print("   Problem: What if file is 10GB and you have 8GB RAM?")

    # Simulate memory tracking (simplified)
    with open(filename, 'r') as f:
        all_lines = f.readlines()

    mem_estimate = sys.getsizeof(all_lines)
    print(f"\n   Estimated memory: {mem_estimate / (1024*1024):.2f} MB for list object")
    print("   Plus string storage for each line...")


def line_generator(filename: str, batch_size: int = 100):
    """
    Generator function that yields batches of lines lazily.
    Uses the 'yield' keyword for memory-efficient streaming.
    """
    with open(filename, 'r') as f:
        batch = []
        for line in f:
            cleaned_line = line.strip().lower()
            if len(cleaned_line) > 0:
                batch.append(cleaned_line)

                if len(batch) >= batch_size:
                    yield batch
                    batch = []

        # Yield remaining lines
        if batch:
            yield batch


def demonstrate_generators(filename: str) -> None:
    """
    Show how generators stream data efficiently.
    """
    print("\n" + "="*60)
    print("PART 4: Generator Solution (Memory Efficient)")
    print("="*60)

    print("\n✓ Generator approach:")
    print("   File → Generator → Batch → Process → Next Batch")
    print("   Only loads one batch at a time into memory!")

    print("\n🔄 Processing batches with generator:")
    batch_size = 100
    total_processed = 0

    for i, batch in enumerate(line_generator(filename, batch_size)):
        total_processed += len(batch)
        if i < 3:  # Show first 3 batches
            print(f"   Batch {i+1}: {len(batch)} lines")
            print(f"      First line: {batch[0][:60]}...")

    print(f"\n   Total processed: {total_processed} lines")
    print("   Memory used: Only ~1 batch at a time!")


def demonstrate_lazy_evaluation() -> None:
    """
    Explain lazy evaluation with a simple example.
    """
    print("\n" + "="*60)
    print("PART 5: Understanding Lazy Evaluation")
    print("="*60)

    print("\n💡 Lazy evaluation means 'compute only when needed'")

    # Eager evaluation (list comprehension)
    print("\n❌ Eager (list comprehension):")
    print("   squares = [x**2 for x in range(1000000)]")
    print("   → Computes ALL 1 million squares immediately")
    print("   → Stores ALL in memory")

    # Lazy evaluation (generator expression)
    print("\n✓ Lazy (generator expression):")
    print("   squares = (x**2 for x in range(1000000))")
    print("   → Computes NOTHING yet")
    print("   → Only computes when you ask for next value")

    # Demo
    squares_gen = (x**2 for x in range(10))
    print("\n   Generator created (no computation yet)...")
    print("   Calling next():")
    for i in range(3):
        print(f"      next(squares_gen) = {next(squares_gen)}")


def compare_memory_usage(filename: str) -> None:
    """
    Compare memory usage: list vs generator approach.
    """
    print("\n" + "="*60)
    print("PART 6: Memory Comparison")
    print("="*60)

    # List approach
    print("\n📊 List approach:")
    with open(filename, 'r') as f:
        all_lines = [line.strip().lower() for line in f if line.strip()]

    list_size = sys.getsizeof(all_lines)
    # Add approximate string sizes
    string_size = sum(sys.getsizeof(line) for line in all_lines[:1000]) * (len(all_lines) / 1000)
    total_list_memory = (list_size + string_size) / (1024 * 1024)

    print(f"   Total lines: {len(all_lines)}")
    print(f"   Estimated memory: {total_list_memory:.2f} MB")

    # Generator approach
    print("\n📊 Generator approach:")
    gen = line_generator(filename, batch_size=100)
    gen_size = sys.getsizeof(gen)
    print(f"   Generator object size: {gen_size} bytes")
    print(f"   Memory per batch: ~{sys.getsizeof(['sample'] * 100) / 1024:.2f} KB")
    print(f"   Memory savings: {(1 - gen_size / (list_size + string_size)) * 100:.1f}%")


def pytorch_dataloader_connection() -> None:
    """
    Explain how this connects to PyTorch DataLoaders.
    """
    print("\n" + "="*60)
    print("PART 7: Connection to PyTorch DataLoaders")
    print("="*60)

    print("\n🔗 PyTorch DataLoader uses the same generator pattern!")
    print("\n   Your code:")
    print("   def line_generator(filename, batch_size):")
    print("       for batch in batches:")
    print("           yield batch")

    print("\n   PyTorch DataLoader:")
    print("   dataloader = DataLoader(dataset, batch_size=32)")
    print("   for batch in dataloader:")
    print("       # Process batch")

    print("\n   Both use lazy evaluation to stream data efficiently!")
    print("   → Train on billions of samples without loading all into RAM")
    print("   → Perfect for large-scale deep learning")


def main():
    """
    Run all demonstrations.
    """
    print("="*60)
    print("Module 2 Lab: The Infinite Data Loader")
    print("Pythonic Patterns for AI")
    print("="*60)

    # Setup
    corpus_file = "generated_corpus.txt"

    # Generate mock data
    generate_mock_corpus(corpus_file, num_lines=10000)

    # Part 1: List comprehensions
    sample_lines = demonstrate_list_comprehension(corpus_file)

    # Part 2: Dict comprehensions
    demonstrate_dict_comprehension(sample_lines)

    # Part 3: Memory problem
    demonstrate_memory_problem(corpus_file)

    # Part 4: Generator solution
    demonstrate_generators(corpus_file)

    # Part 5: Lazy evaluation
    demonstrate_lazy_evaluation()

    # Part 6: Memory comparison
    compare_memory_usage(corpus_file)

    # Part 7: PyTorch connection
    pytorch_dataloader_connection()

    print("\n" + "="*60)
    print("🎓 Key Takeaways:")
    print("="*60)
    print("1. List comprehensions: Clean, readable data transformations")
    print("2. Dict comprehensions: Efficient vocabulary/mapping creation")
    print("3. Generators (yield): Stream data without loading everything")
    print("4. Lazy evaluation: Compute only what you need, when you need it")
    print("5. Memory efficiency: Critical for training on large datasets")
    print("6. PyTorch DataLoaders: Built on the same generator principles")
    print("="*60)

    # Cleanup
    print(f"\n🧹 Cleaning up: removing {corpus_file}")
    os.remove(corpus_file)
    print("✓ Lab complete!")


if __name__ == "__main__":
    main()
