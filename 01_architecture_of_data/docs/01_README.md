# Module 01: The Architecture of Data

## Overview

This module introduces the fundamental data structures that power AI systems: lists and dictionaries. Students learn why algorithmic complexity matters for AI performance and build a practical tokenizer dictionary.

## Learning Objectives

By the end of this module, students will be able to:

1. **Explain static and runtime analyses in Python** - Understanding when operations happen at compile-time vs runtime
2. **Distinguish mutable from immutable objects** - Understanding memory implications and side effects
3. **Build a tokenizer dictionary** - Using optimized data structures to map words to token IDs

## Topics Covered

- **Python Data Structures**: Deep dive into lists and dictionaries
- **Performance Analysis**: O(n) vs O(1) lookup operations
- **Memory Management**: Mutable vs immutable objects and memory references
- **Nested Dictionaries**: Working with complex JSON structures (API responses)
- **Big O Notation**: Understanding algorithmic complexity for AI scalability
- **Practical Tokenization**: How LLMs convert text to numerical sequences

## Module Contents

### 1. `tutorial.ipynb`
Self-contained, Colab-ready notebook (run it in Google Colab, or locally in Jupyter/VS Code). Its first code cell installs all dependencies into the kernel, and any data it uses is generated inside the notebook. It demonstrates:

- **Demo 1**: List vs Dictionary lookup performance (O(n) vs O(1))
- **Demo 2**: Mutable vs Immutable behavior with `id()` examples
- **Demo 3**: Building a tokenizer dictionary from text corpus
- **Demo 4**: Word frequency counting with dictionaries
- **Demo 5**: Nested dictionary structures (simulated API responses)
- **Demo 6**: Big O notation comparison with timing tests
- **Practical Example**: Text encoding/decoding with token IDs

### 2. `slides.html`
Self-contained HTML slide deck (15 slides) with:

- Clean, educational design using Inter font
- Interactive navigation (keyboard arrows or click)
- Inline SVG diagrams and visualizations
- Code snippets with syntax highlighting
- Performance comparison charts
- Tokenizer workflow flowchart

## Getting Started

## ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/01_architecture_of_data/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files.

<details><summary>Advanced: run locally</summary>

Requires Python >=3.10.

```bash
# From the module directory, create and activate a virtual environment
uv venv
source .venv/bin/activate  # macOS/Linux (use .venv\Scripts\activate on Windows)
```

Then open `tutorial.ipynb` in Jupyter or VS Code and run the cells top-to-bottom. The first code cell installs any dependencies it needs into the kernel.

</details>

### Viewing the Slides

Open `slides.html` in any modern web browser:

```bash
open slides.html  # macOS
# or just double-click the file
```

**Navigation:**
- Press → (right arrow) or click right half of screen to advance
- Press ← (left arrow) or click left half of screen to go back
- Press Space to advance
- Swipe left/right on mobile devices

## Key Insights

### Why Dictionaries for AI?

1. **Performance**: O(1) lookup vs O(n) for lists - 1000x+ speedup at scale
2. **LLM Tokenization**: GPT-4 has 100,000+ token vocabulary - requires instant lookups
3. **Real-world Impact**: 1M token lookups = 0.1s with dict vs 1000s with list

### Mutability Matters

- **Immutable** (str, tuple, numbers): Safe for concurrent access, no side effects
- **Mutable** (list, dict, set): Memory efficient but risk of unintended modification
- Understanding `id()` helps debug memory-related issues in data pipelines

### Big O Notation

Complexity classes from fastest to slowest:
- **O(1)**: Constant time (dict lookup, array index) ✅ Best for AI
- **O(log n)**: Logarithmic (binary search)
- **O(n)**: Linear (list search, single loop)
- **O(n²)**: Quadratic (nested loops) ❌ Avoid for large datasets
- **O(2ⁿ)**: Exponential (recursive fibonacci) ❌ Impractical for AI

## Lab Structure

The lab follows this workflow:

```
Text Input
    ↓
Split Words (tokenization)
    ↓
Count Frequencies
    ↓
Build Vocabulary (unique words)
    ↓
Assign Token IDs (word_to_id, id_to_word dictionaries)
    ↓
Encode Text → Token Sequence
    ↓
Decode Tokens → Text
```

## Real-world Applications

### How LLMs Use These Concepts

1. **Tokenization**: Every LLM (GPT, BERT, LLaMA) uses dictionary-based tokenizers
2. **Vocabulary Lookups**: Millions of lookups per second require O(1) operations
3. **API Responses**: OpenAI, Anthropic, Google APIs return nested dictionaries
4. **Embeddings**: Token IDs map to high-dimensional vectors (also via dictionaries)

### Example: OpenAI API Response

```python
response = {
    "id": "chatcmpl-123",
    "model": "gpt-4",
    "usage": {
        "prompt_tokens": 15,
        "completion_tokens": 30,
        "total_tokens": 45
    },
    "choices": [{
        "message": {
            "role": "assistant",
            "content": "Hello! How can I help?"
        }
    }]
}

# Nested dictionary navigation
total_tokens = response["usage"]["total_tokens"]
message = response["choices"][0]["message"]["content"]
```

## Common Pitfalls

### 1. Using Lists for Lookups
```python
# ❌ BAD: O(n) for every lookup
vocab = ["the", "quick", "brown", "fox", ...]
if word in vocab:  # Scans entire list!
    ...

# ✅ GOOD: O(1) lookup
vocab = {"the": 0, "quick": 1, "brown": 2, "fox": 3, ...}
if word in vocab:  # Instant hash lookup!
    ...
```

### 2. Mutating Shared Lists
```python
# ❌ BAD: Unexpected side effect
def add_item(my_list, item):
    my_list.append(item)  # Modifies original!
    return my_list

original = [1, 2, 3]
new = add_item(original, 4)
print(original)  # [1, 2, 3, 4] - Original changed!

# ✅ GOOD: Return new list
def add_item(my_list, item):
    return my_list + [item]  # Creates new list

original = [1, 2, 3]
new = add_item(original, 4)
print(original)  # [1, 2, 3] - Original unchanged
```

### 3. Ignoring Big O for Small Data
```python
# ⚠️ ACCEPTABLE: Small dataset (< 100 items)
small_list = ["cat", "dog", "fox"]
if "dog" in small_list:  # O(n) but fast enough
    ...

# ❌ BAD: Large dataset (10,000+ items)
large_list = load_vocabulary()  # 50,000 words
for word in text.split():
    if word in large_list:  # O(n) * O(n) = O(n²) disaster!
        ...

# ✅ GOOD: Use dict for large datasets
large_dict = {word: idx for idx, word in enumerate(large_list)}
for word in text.split():
    if word in large_dict:  # O(n) * O(1) = O(n)
        ...
```

## Extensions & Next Steps

### Explore Further

1. **Python Collections Module**
   - `collections.Counter` - Optimized frequency counting
   - `collections.defaultdict` - Automatic default values
   - `collections.OrderedDict` - Maintain insertion order (Python 3.7+ dicts are ordered by default)

2. **Advanced Tokenization**
   - **Byte Pair Encoding (BPE)** - Used by GPT models
   - **WordPiece** - Used by BERT
   - **SentencePiece** - Language-agnostic tokenization
   - **Character-level tokenization** - For rare languages

3. **Hash Table Internals**
   - How Python dictionaries use hash functions
   - Collision resolution strategies
   - Memory-performance tradeoffs

4. **Profiling Tools**
   - `timeit` module for microbenchmarks
   - `cProfile` for full program analysis
   - `memory_profiler` for memory usage

### Hands-on Challenges

1. **Build a Character-level Tokenizer**: Tokenize at character level instead of word level
2. **Implement BPE**: Research and implement a simple Byte Pair Encoding tokenizer
3. **Frequency Analysis**: Analyze a large corpus (e.g., Shakespeare, Wikipedia) and find statistical patterns
4. **API Integration**: Make a real OpenAI API call and navigate the nested response
5. **Performance Benchmark**: Compare list vs dict performance for datasets of varying sizes (100, 1K, 10K, 100K)

## Assessment

Students should be able to:

1. **Explain** why dictionaries are O(1) and lists are O(n) for lookups
2. **Demonstrate** mutability with `id()` function
3. **Build** a working tokenizer that maps words to IDs and back
4. **Analyze** Big O complexity of simple algorithms
5. **Navigate** nested dictionary structures
6. **Apply** these concepts to real LLM tokenization

## Next Module

**Module 02: Pythonic Patterns for Data**
- List comprehensions
- Generator expressions
- Functional programming patterns (map, filter, reduce)
- Iterator protocol
- Context managers

## Resources

### Official Documentation
- [Python Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Time Complexity (Python Wiki)](https://wiki.python.org/moin/TimeComplexity)
- [Collections Module](https://docs.python.org/3/library/collections.html)

### Tokenization
- [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/index)
- [OpenAI Tokenizer](https://platform.openai.com/tokenizer)
- [SentencePiece](https://github.com/google/sentencepiece)

### Big O Notation
- [Big O Cheat Sheet](https://www.bigocheatsheet.com/)
- [Understanding Big O (freeCodeCamp)](https://www.freecodecamp.org/news/big-o-notation-why-it-matters-and-why-it-doesnt-1674cfa8a23c/)

## Credits

**Module Design**: mui-group  
**Target Audience**: Advanced high school students  
**Prerequisites**: Basic Python programming (variables, functions, loops)  
**Duration**: 2-3 hours (1 hour lecture + 1-2 hours lab)

---

© mui-group | AI Research Foundations Minicourse
