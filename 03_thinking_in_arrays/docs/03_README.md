# Module 3: Thinking in Arrays (Tensors)

## Overview
This module introduces NumPy N-dimensional arrays and one-hot encoding, fundamental concepts for numerical AI computation.

## Learning Objectives
- Create and manipulate NumPy N-dimensional arrays
- Interpret .shape and array dimensions
- Convert tokenizer output into a numerical one-hot encoded matrix

## Topics Covered
1. **Why Python Lists Fail for AI**
   - Non-contiguous memory layout
   - Python object overhead
   - CPU cache performance

2. **NumPy Arrays (ndarray)**
   - Contiguous memory blocks
   - 50-100x faster than Python lists
   - Creating arrays: from lists, zeros, ones, arange, linspace

3. **The .shape Property**
   - Understanding array dimensions
   - Reading shape tuples: (rows, columns), (depth, rows, columns)

4. **Rank-1 vs Rank-2 Arrays**
   - The shape bug: (n,) vs (n,1) vs (1,n)
   - Using .reshape() to fix dimension issues

5. **Reshaping Arrays**
   - Transforming dimensions without copying data
   - Using -1 to infer dimensions

6. **One-Hot Encoding**
   - Converting discrete tokens to binary vectors
   - Building vocabulary from text
   - Creating one-hot matrices
   - Understanding sparsity (99.96% zeros)

7. **Connection to LLM Embeddings**
   - LLM pipeline: Text → Tokens → One-hot → Embeddings → Neural Net
   - From sparse one-hot to dense contextual embeddings

## Files
- `tutorial.ipynb` - Self-contained, Colab-ready notebook (all data generated inside)
- `lab_the_matrix.py` - Educational Python script with 8 demonstrations
- `slides.html` - 14-slide HTML presentation with inline SVG diagrams

## ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/03_thinking_in_arrays/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files.

<details><summary>Advanced: run locally</summary>

```bash
# Install dependencies (from this module folder)
pip install -e .

# Then open tutorial.ipynb in Jupyter or VS Code
jupyter notebook tutorial.ipynb

# Optional: run the standalone script version
python lab_the_matrix.py
```

</details>

## Lab Structure
The lab demonstrates:
1. Why Python lists fail (memory layout)
2. Creating NumPy arrays
3. Understanding .shape property
4. Rank-1 vs Rank-2 arrays (the shape bug)
5. Reshaping arrays
6. One-hot encoding workflow
7. Sparsity analysis
8. Connection to LLM embeddings

## Slides
Open `slides.html` in a browser. Use:
- **Arrow keys** or **Space** to navigate
- **Home** to go to first slide
- **End** to go to last slide
- **Click left/right** side of screen to navigate

### Slide Contents
1. Title
2. Why Python Lists Fail
3. NumPy Arrays: Contiguous Memory
4. Creating Arrays
5. The .shape Property
6. Rank-1 vs Rank-2: The Shape Bug
7. Reshaping Arrays
8. What is One-Hot Encoding?
9. One-Hot Encoding Workflow
10. The One-Hot Matrix
11. From One-Hot to LLM Embeddings
12. Lab Introduction
13. Key Takeaways
14. Next Steps

## Design Specifications
- **Font**: Inter (Google Fonts)
- **Colors**: Charcoal (#1a1a2e), Off-white (#fafafa), Accent (#e94560)
- **Layout**: Left-aligned, asymmetric, generous whitespace
- **Diagrams**: Inline SVG (memory layouts, matrices, flowcharts)
- **Footer**: © mui-group, keyboard navigation

## Key Takeaways
1. NumPy arrays: 50-100x faster than Python lists
2. .shape property reveals dimensions
3. Rank matters: (n,) ≠ (n,1) ≠ (1,n)
4. One-hot encoding: discrete tokens → sparse binary vectors
5. Sparsity problem leads to dense embeddings
6. Foundation for neural network input

## Next Module
**Module 4: Dense Embeddings** - From sparse one-hot vectors to dense semantic representations (Word2Vec, GloVe, contextual embeddings).
