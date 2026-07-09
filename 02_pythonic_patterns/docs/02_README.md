# Module 02: Pythonic Patterns for Data Processing

Learn Pythonic patterns that make AI data processing code cleaner, faster, and more memory-efficient.

## Learning Objectives

- Replace verbose for loops with list and dict comprehensions
- Use generator functions with `yield` for memory-efficient data streaming
- Understand lazy evaluation vs eager evaluation
- Apply streaming patterns to process large datasets without loading everything into memory
- Connect these patterns to PyTorch DataLoader concepts used in production AI systems
- Measure and compare memory usage between different approaches

## Prerequisites

- Basic Python syntax (functions, loops, dictionaries)
- Module 01 (Understanding tokenization and data representation)
- Familiarity with reading files in Python

## Files in This Module

| File | Purpose |
|------|---------|
| `tutorial.ipynb` | Self-contained, Colab-ready notebook with explanations, exercises, and all patterns demonstrated on an in-notebook mock corpus |
| `slides.html` | Lecture slides covering the theory behind Pythonic patterns |

## Key Concepts Covered

### 1. List Comprehensions
Replace multi-line for loops with single-line expressions:
```python
# Old way
cleaned = []
for line in file:
    line = line.strip().lower()
    if len(line) > 0:
        cleaned.append(line)

# Pythonic way
cleaned = [line.strip().lower() for line in file if len(line.strip()) > 0]
```

### 2. Dict Comprehensions
Build dictionaries efficiently for vocabulary and frequency counts:
```python
# Build vocabulary from word list
vocab = {word: all_words.count(word) for word in set(all_words)}
```

### 3. Generator Functions
Use `yield` to process data one piece at a time instead of loading everything into memory:
```python
def line_generator(filename, batch_size=100):
    with open(filename) as f:
        batch = []
        for line in f:
            batch.append(line.strip())
            if len(batch) >= batch_size:
                yield batch
                batch = []
```

### 4. Lazy Evaluation
Generator expressions compute values only when needed:
```python
# Eager: computes all 1 million values immediately
squares = [x**2 for x in range(1000000)]

# Lazy: computes values one at a time as requested
squares = (x**2 for x in range(1000000))
```

### 5. Memory-Efficient Data Streaming
Process arbitrarily large files without running out of memory:
- Load data in batches
- Process each batch independently
- Discard batch before loading the next one
- Only one batch in memory at any time

## How to Run

### ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/02_pythonic_patterns/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files.

<details><summary>Advanced: run locally</summary>

```bash
# Install dependencies (uv recommended)
uv sync            # or: pip install -e .
```

Then open `tutorial.ipynb` in Jupyter or VS Code and run the cells top-to-bottom.

</details>

### What the Notebook Covers
Working top-to-bottom, the notebook will:
1. Generate a mock corpus in-memory (configurable size)
2. Demonstrate list comprehensions vs for loops
3. Build vocabularies with dict comprehensions
4. Show the memory problem with loading large files
5. Solve it with generator functions
6. Compare memory usage quantitatively

## Connection to Production AI Systems

These patterns appear everywhere in real AI codebases:

| Pattern | Where You'll See It |
|---------|---------------------|
| List comprehension | Data cleaning pipelines, preprocessing transforms |
| Dict comprehension | Building vocabularies, frequency tables, lookup dictionaries |
| Generator functions | PyTorch `DataLoader`, streaming from S3, ETL pipelines |
| Lazy evaluation | Hugging Face `datasets` library, infinite data augmentation |
| Batch processing | Training loops, inference servers, distributed systems |

PyTorch's `DataLoader` is essentially a production-grade generator that:
- Yields batches of data lazily
- Supports multi-process data loading
- Handles shuffling and sampling
- Never loads the entire dataset into memory

## Memory Efficiency Example

For a 100MB text file with 1 million lines:

| Approach | Memory Usage | Time |
|----------|--------------|------|
| List comprehension | ~100 MB (entire file) | Fast |
| Generator (batch=100) | ~10 KB (one batch) | Fast |
| Generator (batch=1000) | ~100 KB (one batch) | Fast |

**Key Insight**: Generators let you process datasets larger than your available RAM.

## What's Next?

After mastering these Pythonic patterns, you'll move to Module 03 to learn why NumPy arrays are essential for AI (Python lists are too slow) and how to represent data efficiently in N-dimensional arrays.
