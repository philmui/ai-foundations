"""
Module 1: The Architecture of Data - Lab: Building a Tokenizer Dictionary

This lab demonstrates:
1. List vs Dictionary lookup performance (O(n) vs O(1))
2. Mutable vs Immutable behavior with memory references
3. Building a tokenizer dictionary (word → token ID mapping)
4. Word frequency counting with dictionaries
5. Nested dictionary structures (like API responses)
6. Big O notation comparison with timing tests

Learning Objectives:
- Understand why dictionaries are critical for AI/ML applications
- Grasp the performance difference between O(n) and O(1) operations
- Learn how tokenizers map words to integer IDs efficiently
"""

from dotenv import load_dotenv, find_dotenv
import time
from typing import Dict, List, Tuple

# Load environment variables
load_dotenv(find_dotenv())


def demo_list_vs_dict_performance():
    """
    Demonstrates the performance difference between list and dictionary lookups.
    Lists: O(n) - must check each element
    Dictionaries: O(1) - direct hash-based access
    """
    print("=" * 60)
    print("DEMO 1: List vs Dictionary Lookup Performance")
    print("=" * 60)

    # Create test data
    size = 10000
    test_list = list(range(size))
    test_dict = {i: i for i in range(size)}

    # Search for an item near the end
    search_item = size - 1

    # Time list lookup (O(n))
    start = time.perf_counter()
    for _ in range(1000):
        result = search_item in test_list
    list_time = time.perf_counter() - start

    # Time dict lookup (O(1))
    start = time.perf_counter()
    for _ in range(1000):
        result = search_item in test_dict
    dict_time = time.perf_counter() - start

    print(f"\nSearching for item {search_item} in {size} elements:")
    print(f"List (O(n)) time: {list_time:.6f} seconds")
    print(f"Dict (O(1)) time: {dict_time:.6f} seconds")
    print(f"Speedup: {list_time / dict_time:.2f}x faster with dictionary")
    print("\n💡 Key Insight: For large datasets (like LLM vocabularies with 50K+ tokens),")
    print("   dictionary lookup is essential for performance!\n")


def demo_mutable_vs_immutable():
    """
    Demonstrates mutable vs immutable objects and memory references.
    Mutable: Lists, Dicts - can be modified in-place
    Immutable: Strings, Tuples, Numbers - create new objects on modification
    """
    print("=" * 60)
    print("DEMO 2: Mutable vs Immutable Objects")
    print("=" * 60)

    # Immutable example: string
    print("\n--- Immutable: String ---")
    original_str = "hello"
    print(f"Original string: '{original_str}', id: {id(original_str)}")

    modified_str = original_str.upper()
    print(f"Modified string: '{modified_str}', id: {id(modified_str)}")
    print(f"Original unchanged: '{original_str}', id: {id(original_str)}")
    print("→ Different memory addresses! Strings are immutable.\n")

    # Mutable example: list
    print("--- Mutable: List ---")
    original_list = [1, 2, 3]
    print(f"Original list: {original_list}, id: {id(original_list)}")

    original_list.append(4)  # Modifies in-place
    print(f"After append: {original_list}, id: {id(original_list)}")
    print("→ Same memory address! Lists are mutable.\n")

    # Dictionary example (also mutable)
    print("--- Mutable: Dictionary ---")
    original_dict = {"a": 1, "b": 2}
    print(f"Original dict: {original_dict}, id: {id(original_dict)}")

    original_dict["c"] = 3  # Modifies in-place
    print(f"After adding key: {original_dict}, id: {id(original_dict)}")
    print("→ Same memory address! Dictionaries are mutable.\n")

    print("💡 Key Insight: Understanding mutability is critical for:")
    print("   - Avoiding unexpected side effects in functions")
    print("   - Memory-efficient data structure design")
    print("   - Building safe concurrent AI systems\n")


def build_tokenizer_dictionary(text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
    """
    Builds a tokenizer dictionary from text corpus.
    Returns:
        - word_to_id: Maps words to unique token IDs
        - id_to_word: Reverse mapping (token IDs to words)

    This simulates how LLMs convert text to token sequences.
    """
    print("=" * 60)
    print("DEMO 3: Building a Tokenizer Dictionary")
    print("=" * 60)

    # Step 1: Tokenize (split text into words)
    print("\n--- Step 1: Tokenization ---")
    words = text.lower().split()
    print(f"Original text: {text[:100]}...")
    print(f"Total words: {len(words)}")
    print(f"Sample tokens: {words[:10]}\n")

    # Step 2: Build unique vocabulary
    print("--- Step 2: Build Vocabulary ---")
    unique_words = sorted(set(words))
    print(f"Unique words (vocabulary size): {len(unique_words)}")
    print(f"Sample vocabulary: {unique_words[:10]}\n")

    # Step 3: Assign token IDs
    print("--- Step 3: Assign Token IDs ---")
    word_to_id = {word: idx for idx, word in enumerate(unique_words)}
    id_to_word = {idx: word for word, idx in word_to_id.items()}

    # Show sample mappings
    print("Sample word → token ID mappings:")
    for word in list(unique_words)[:8]:
        print(f"  '{word}' → {word_to_id[word]}")

    print("\n💡 Key Insight: This is exactly how GPT/BERT tokenizers work!")
    print("   They map text to integer sequences for neural network processing.\n")

    return word_to_id, id_to_word


def count_word_frequencies(text: str) -> Dict[str, int]:
    """
    Counts word frequencies using a dictionary.
    Demonstrates O(1) increment operations for efficient counting.
    """
    print("=" * 60)
    print("DEMO 4: Word Frequency Counting")
    print("=" * 60)

    words = text.lower().split()
    frequency_dict = {}

    # Count occurrences with O(1) dictionary operations
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    # Or more Pythonically:
    # from collections import Counter
    # frequency_dict = Counter(words)

    # Sort by frequency (most common first)
    sorted_frequencies = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    print("\nTop 10 most frequent words:")
    for word, count in sorted_frequencies[:10]:
        print(f"  '{word}': {count} occurrences")

    print("\n💡 Key Insight: Dictionary-based counting is O(n) total complexity")
    print("   because each lookup/insert is O(1). Essential for text analysis!\n")

    return frequency_dict


def demo_nested_dictionary_structure():
    """
    Demonstrates nested dictionary structures like OpenAI API responses.
    Shows how complex JSON data is represented in Python.
    """
    print("=" * 60)
    print("DEMO 5: Nested Dictionary Structures (API Response)")
    print("=" * 60)

    # Simulated OpenAI API response structure
    api_response = {
        "id": "chatcmpl-123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": "gpt-4",
        "usage": {
            "prompt_tokens": 15,
            "completion_tokens": 30,
            "total_tokens": 45
        },
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Hello! How can I help you today?"
                },
                "finish_reason": "stop",
                "index": 0
            }
        ]
    }

    print("\nNested API Response Structure:")
    print(f"Model: {api_response['model']}")
    print(f"Total tokens used: {api_response['usage']['total_tokens']}")
    print(f"Response: {api_response['choices'][0]['message']['content']}")

    print("\n💡 Key Insight: Real AI APIs return complex nested dictionaries.")
    print("   Understanding dict navigation is essential for AI development!\n")


def demo_big_o_comparison():
    """
    Demonstrates Big O notation with practical timing examples.
    Shows why algorithmic complexity matters for AI scalability.
    """
    print("=" * 60)
    print("DEMO 6: Big O Notation - Performance at Scale")
    print("=" * 60)

    sizes = [100, 1000, 10000]

    print("\nComparing search operations across different data sizes:")
    print(f"{'Size':<10} {'List O(n)':<15} {'Dict O(1)':<15} {'Speedup':<10}")
    print("-" * 55)

    for size in sizes:
        # Create test data
        test_list = list(range(size))
        test_dict = {i: i for i in range(size)}
        search_item = size - 1  # Worst case for list

        # Time list search
        start = time.perf_counter()
        for _ in range(1000):
            _ = search_item in test_list
        list_time = time.perf_counter() - start

        # Time dict search
        start = time.perf_counter()
        for _ in range(1000):
            _ = search_item in test_dict
        dict_time = time.perf_counter() - start

        speedup = list_time / dict_time
        print(f"{size:<10} {list_time:<15.6f} {dict_time:<15.6f} {speedup:<10.2f}x")

    print("\n💡 Key Insight: As data grows, O(1) operations maintain constant time,")
    print("   while O(n) operations slow down linearly. For LLM vocabularies with")
    print("   50,000+ tokens, this difference is critical for real-time inference!\n")

    print("Common Complexity Classes (from fastest to slowest):")
    print("  O(1)      - Constant time (dict lookup, array index)")
    print("  O(log n)  - Logarithmic (binary search)")
    print("  O(n)      - Linear (list search, single loop)")
    print("  O(n²)     - Quadratic (nested loops)")
    print("  O(2ⁿ)     - Exponential (recursive fibonacci)\n")


def encode_text_to_tokens(text: str, word_to_id: Dict[str, int]) -> List[int]:
    """
    Converts text to a sequence of token IDs using the tokenizer dictionary.
    """
    words = text.lower().split()
    token_ids = [word_to_id.get(word, 0) for word in words]  # 0 for unknown words
    return token_ids


def decode_tokens_to_text(token_ids: List[int], id_to_word: Dict[int, str]) -> str:
    """
    Converts token IDs back to text using the reverse dictionary.
    """
    words = [id_to_word.get(token_id, "<UNK>") for token_id in token_ids]
    return " ".join(words)


def main():
    """
    Main function to run all demonstrations.
    """
    print("\n" + "=" * 60)
    print(" Module 1: The Architecture of Data - Tokenizer Lab")
    print("=" * 60 + "\n")

    # Sample text corpus (simulating training data for an LLM)
    corpus = """
    The quick brown fox jumps over the lazy dog. The dog was sleeping under a tree.
    Machine learning models process text by converting words into numerical tokens.
    These tokens are then embedded into high-dimensional vector spaces. The embeddings
    capture semantic relationships between words. Similar words have similar embeddings.
    Deep learning revolutionized natural language processing. Transformers use attention
    mechanisms to process text efficiently. The attention mechanism allows models to
    focus on relevant parts of the input sequence. This breakthrough enabled models
    like GPT and BERT to achieve state-of-the-art performance on many tasks.
    """

    # Run all demonstrations
    demo_list_vs_dict_performance()
    demo_mutable_vs_immutable()
    word_to_id, id_to_word = build_tokenizer_dictionary(corpus)
    count_word_frequencies(corpus)
    demo_nested_dictionary_structure()
    demo_big_o_comparison()

    # Practical tokenization example
    print("=" * 60)
    print("PRACTICAL EXAMPLE: Text Encoding & Decoding")
    print("=" * 60)

    sample_text = "the quick brown fox jumps"
    print(f"\nOriginal text: {sample_text}")

    token_ids = encode_text_to_tokens(sample_text, word_to_id)
    print(f"Encoded tokens: {token_ids}")

    decoded_text = decode_tokens_to_text(token_ids, id_to_word)
    print(f"Decoded text: {decoded_text}")

    print("\n💡 This is exactly how LLMs process text:")
    print("   1. Text → Tokens (encoding)")
    print("   2. Process tokens through neural network")
    print("   3. Tokens → Text (decoding)\n")

    print("=" * 60)
    print("🎯 SUMMARY: Key Takeaways")
    print("=" * 60)
    print("""
1. Dictionaries provide O(1) lookup - essential for AI performance
2. Lists are O(n) - use for ordered sequences, not lookups
3. Understanding mutability prevents bugs in data pipelines
4. Tokenizers map words to IDs using dictionaries
5. Big O notation helps predict scalability of AI systems
6. Nested dictionaries structure complex API responses
7. Word frequency counting demonstrates real-world dict usage

Next Steps:
- Experiment with larger corpora
- Try building a character-level tokenizer
- Explore Python's collections.Counter for frequency counting
- Learn about subword tokenization (BPE, WordPiece)
    """)


if __name__ == "__main__":
    main()
