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
├── tutorial.ipynb      # self-contained lesson + lab notebook (Colab-ready)
├── slides.html         # slide deck
└── docs/               # reference docs and quick guides
```

The `tutorial.ipynb` leads with an **Open in Colab** badge and a first code cell that installs all dependencies, so each module runs with zero local setup.

---

## ▶️ Run in Google Colab (recommended)

Every module's `tutorial.ipynb` is fully self-contained and Colab-ready.

1. Open a module's `tutorial.ipynb` and click the **Open in Colab** badge at the top of the notebook (or upload the notebook via **File → Upload notebook** at [colab.research.google.com](https://colab.research.google.com)).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

Each notebook generates any data it uses inside the notebook, so it runs end-to-end with no external files. Work through modules in order — each builds conceptually on the previous one.

<details><summary>Advanced: run locally</summary>

If you prefer a local Jupyter/VS Code setup, clone the repo, open a module's `tutorial.ipynb` in Jupyter or VS Code, and run it top-to-bottom. The first code cell installs the dependencies it needs, so you don't need any separate install step.

```bash
cd 01_architecture_of_data
jupyter notebook tutorial.ipynb
```

</details>

---

## Prerequisites

- Python 3.10+
- Basic Python syntax: variables, loops, functions, and lists
- No prior NumPy, Pandas, or ML experience required
