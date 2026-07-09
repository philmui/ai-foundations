# Module 05: DataFrames & Series

Working with Structured Data in AI

## Overview

This module teaches you how to work with structured data using Pandas, Python's most powerful data manipulation library. You'll learn to load, inspect, filter, and analyze real LLM prompt-response datasets, building the foundation for all AI data workflows.

## Learning Objectives

By the end of this module, you will be able to:

- Load CSV and JSON data into Pandas DataFrames
- Inspect data structure using `.head()`, `.tail()`, `.info()`, `.describe()`, and `.shape`
- Understand the difference between DataFrames and Series
- Select specific rows and columns using boolean indexing
- Identify and handle missing data using `.isna()` and related methods
- Analyze distributions with `.value_counts()`, histograms, and `.groupby()` aggregations
- Prepare structured data for machine learning workflows

## Prerequisites

- Basic Python programming (variables, functions, loops)
- Understanding of data types (strings, integers, floats)
- Module 02: Data Foundations patterns (optional but recommended)

## Files in This Module

| File | Description |
|------|-------------|
| `tutorial.ipynb` | Self-contained Jupyter/Colab notebook with step-by-step lessons (installs deps and generates its data in-notebook) |

## Key Concepts Covered

### 1. Loading Data

- Using `pd.read_csv()` to load tabular data
- Using `pd.read_json()` for API responses
- Specifying data types with `dtype` parameter
- Parsing dates with `parse_dates` parameter

### 2. DataFrame Anatomy

- **Index**: Row labels (default 0, 1, 2, ...)
- **Columns**: Column labels (feature names)
- **Values**: The actual data in a 2D array
- **Series**: Each column is a 1D labeled array

### 3. Inspection Methods

| Method | Purpose |
|--------|---------|
| `.head(n)` | Display first n rows (default 5) |
| `.tail(n)` | Display last n rows (default 5) |
| `.info()` | Show structure, types, and non-null counts |
| `.describe()` | Generate statistical summary for numeric columns |
| `.shape` | Get dimensions as (rows, columns) |
| `.dtypes` | View data type for each column |
| `.columns` | List all column names |

### 4. Selection Patterns

- **Single column**: `df['column_name']` returns a Series
- **Multiple columns**: `df[['col1', 'col2']]` returns a DataFrame
- **Rows by position**: `df.iloc[0:5]` selects rows 0-4
- **Boolean indexing**: `df[df['rating'] > 4.5]` filters rows by condition
- **Multiple conditions**: Use `&` (AND), `|` (OR), `~` (NOT)

### 5. Missing Data

- `.isna()` returns True/False for each cell
- `.isna().sum()` counts missing values per column
- `.dropna()` removes rows with missing values
- `.fillna(value)` fills missing values with a specified value

### 6. Aggregation Methods

| Method | Description |
|--------|-------------|
| `.value_counts()` | Count unique values in categorical columns |
| `.groupby()` | Split data by category, apply function, combine results |
| `.agg()` | Apply multiple aggregation functions at once |
| `.mean()`, `.sum()`, `.count()` | Calculate statistics |

### 7. Real-World Dataset

The module uses a dataset of LLM prompt-response pairs tracking:

- `prompt_id`: Unique identifier for each interaction
- `prompt_text`: The question or instruction sent to the model
- `model`: Which AI model responded (GPT-4, Claude-3, Gemini-Pro)
- `category`: Task type (coding, analysis, creative, math)
- `temperature`: Model randomness setting (0.0 - 1.0)
- `tokens_used`: Length of the generated response
- `rating`: User satisfaction score (0.0 - 5.0)
- `timestamp`: When the prompt was submitted

This mirrors real AI research workflows where you analyze model performance across different tasks.

## How to Run

## ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/05_dataframes_series/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files.

Work through the notebook cells sequentially, executing each with `Shift+Enter`.

<details><summary>Advanced: run locally</summary>

```bash
# Install dependencies (from the repo root)
uv sync   # or: pip install -e .

# Open the notebook in Jupyter or VS Code
jupyter notebook 05_dataframes_series/tutorial.ipynb
```

</details>

## Next Steps

After completing this module:

1. Complete the lab exercises in `tutorial.ipynb` (Section 9)
2. Try the extension exercises at the end of the notebook
3. Proceed to **Module 06: Cleaning & Transformation** to learn how to prepare messy data for machine learning

## Why This Matters for AI

Every AI project starts with data exploration:

- **Before training**: Understand distribution, find class imbalances, spot outliers
- **During experiments**: Track metrics across model variants, analyze failure cases
- **After deployment**: Monitor performance metrics, detect data drift

Pandas is your primary tool for all of these tasks. Mastering DataFrames is essential for every AI researcher and data scientist.
