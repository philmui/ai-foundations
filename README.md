# AI Research Foundations: Data Engineering & Representation


---

## Why this course exists

Before you can build a Transformer or fine-tune a Large Language Model, you need to master the *guts* of AI: how data is represented, stored, and manipulated mathematically. Most introductory courses skip this layer and jump straight to model APIs — leaving students unable to debug data pipelines, understand tensor shapes, or reason about why their training loop is slow.

This course fills that gap. It teaches the **vectorization, data structuring, and preprocessing techniques** used in actual research labs, using the same tools that underpin PyTorch, TensorFlow, and every modern ML framework: Python data structures, NumPy, Pandas, and OpenCV.

**Target audience:** High school students with basic Python knowledge (loops, variables, functions) who want to understand how AI systems are built from the ground up.

---

## What you will build

Each module pairs a short tutorial notebook with a hands-on lab. By the end you will have written:

| # | Module | Lab |
|---|--------|-----|
| 1 | The Architecture of Data | A tokenizer dictionary — mapping words to IDs like an LLM |
| 2 | Pythonic Patterns for AI | An infinite data loader using generators, like a PyTorch DataLoader |
| 3 | Thinking in Arrays | A one-hot encoding matrix from scratch with NumPy |
| 4 | Vectorization & Broadcasting | A forward pass through a single neuron — no for loops |
| 5 | DataFrames & Series | Statistical analysis of a real LLM prompt-response dataset |
| 6 | Cleaning & Transformation | A full data cleaning pipeline producing train/test CSV splits |
| 7 | Images as Data | An image preprocessor: load → resize → normalize → NumPy array |
| 8 | Capstone: The Research Pipeline | A multimodal data loader yielding batched text + image arrays |

---

## Learning outcomes

By the end of this course you will be able to:

1. Use Python data structures (lists, dicts, generators) for memory-efficient AI data processing
2. Apply NumPy for vectorized matrix operations — including the dot product — to build neural network components without writing a single for loop
3. Clean and curate real-world datasets with Pandas, producing train/test splits ready for model training
4. Process and normalize image data with OpenCV, representing images as `(H × W × C)` NumPy arrays
5. Assemble a complete multimodal research-grade data pipeline integrating all four tools

---

## Repository layout

```
ai-foundations/
├── 01_architecture_of_data/
├── 02_pythonic_patterns/
├── 03_thinking_in_arrays/
├── 04_vectorization_broadcasting/
├── 05_dataframes_series/
├── 06_cleaning_transformation/
├── 07_images_as_data/
└── 08_capstone_pipeline/
```

Each module is self-contained:

```
<module>/
├── tutorial.ipynb      # lesson notebook
├── lab_*.py            # your lab starter file
├── slides.html         # slide deck
├── pyproject.toml      # module dependencies
└── docs/               # reference docs and quick guides
```

---

## Getting started

1. Clone the repo and enter a module directory:

   ```bash
   cd 01_architecture_of_data
   pip install -e .
   ```

2. Open the tutorial notebook to follow the lesson:

   ```bash
   jupyter notebook tutorial.ipynb
   ```

3. Complete the lab in `lab_*.py` for that module.

Work through modules in order — each builds conceptually on the previous one, even though each module's dependencies can be installed independently.

---

## Prerequisites

- Python 3.10+
- Basic Python syntax: variables, loops, functions, and lists
- No prior NumPy, Pandas, or ML experience required
