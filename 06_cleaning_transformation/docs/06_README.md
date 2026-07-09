# Module 6: Cleaning & Transformation

## Learning Objectives
- Preprocess datasets to remove missing values, duplicates, and formatting errors
- Apply boolean indexing to filter low-quality data
- Export clean train and test CSV splits

## Topics Covered
- Boolean indexing for data filtering
- Handling missing values with dropna() vs fillna()
- Duplicate removal
- Data formatting corrections
- Exporting processed datasets

## Lab: The Curator

Take a "dirty" dataset containing missing values, duplicates, and formatting errors; write a cleaning pipeline; export a pristine Train.csv and Test.csv.

## Files

- **tutorial.ipynb**: Self-contained, Colab-ready notebook for the lab
- **slides.html**: Interactive presentation (keyboard navigation)

The dataset used in the lab is a "dirty" dataset (80 rows) generated inside the notebook, with:
- 5 exact duplicates
- 12 cells with missing data
- Inconsistent formatting (GPT-4 vs gpt-4 vs GPT4)
- Whitespace issues
- Invalid values (temperature > 1.0)
- Mixed date formats

## ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/06_cleaning_transformation/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files.

<details><summary>Advanced: run locally</summary>

Install the dependencies (`pip install python-dotenv pandas scikit-learn`, or `uv pip install python-dotenv pandas scikit-learn`), then open `tutorial.ipynb` in Jupyter or VS Code and run all cells.

</details>

The lab notebook will:
1. Load and inspect the dirty dataset
2. Remove exact duplicates
3. Handle missing values (drop critical fields, fill non-critical)
4. Standardize formatting (model names, whitespace)
5. Filter invalid data with boolean indexing
6. Fix data types (dates, numerics)
7. Split 80/20 into train/test
8. Export the clean Train.csv and Test.csv

## Expected Output

```
Before Cleaning:
- 80 total rows
- 5 duplicates
- 12 missing cells
- 7 invalid temperatures
- 4 inconsistent model names

After Cleaning:
- 64 clean rows
- 0 duplicates
- 0 missing critical data
- 0 invalid values
- 2 standardized model names

Train/Test Split:
- Train.csv: 51 rows (80%)
- Test.csv: 13 rows (20%)
```

## Key Concepts

### 1. Finding Duplicates
```python
df.duplicated().sum()  # Count duplicates
df.drop_duplicates()   # Remove them
```

### 2. Missing Values Strategy
- **Critical fields** (prompt, response, rating): Drop rows
- **Non-critical fields** (tokens_used): Fill with 0

### 3. Boolean Indexing
```python
# Create a boolean mask
mask = df['temperature'].between(0.0, 1.0)

# Apply the mask
clean_df = df[mask]
```

### 4. Formatting Fixes
```python
# Remove whitespace
df['model'] = df['model'].str.strip()

# Standardize values
df['model'] = df['model'].replace(mapping)
```

### 5. Data Type Corrections
```python
# Fix dates
df['date'] = pd.to_datetime(df['date'], format='mixed')

# Fix numerics
df['temperature'] = df['temperature'].astype(float)
df['tokens_used'] = df['tokens_used'].astype(int)
```

### 6. Train/Test Split
```python
# Shuffle and split
df_shuffled = df.sample(frac=1, random_state=42)
split_idx = int(0.8 * len(df_shuffled))
train_df = df_shuffled[:split_idx]
test_df = df_shuffled[split_idx:]
```

## Why Each Step Matters for ML

1. **Duplicates** → Inflate accuracy, leak test data into training
2. **Missing values** → Crash models or introduce bias
3. **Formatting** → Prevent model from treating same values as different
4. **Invalid data** → Corrupt learning patterns
5. **Data types** → Prevent type errors, enable proper operations
6. **Train/test split** → Measure true generalization, prevent overfitting

## Viewing the Slides

Open `slides.html` in a web browser:

```bash
open slides.html  # macOS
xdg-open slides.html  # Linux
start slides.html  # Windows
```

**Navigation:**
- Right arrow / Space: Next slide
- Left arrow: Previous slide
- Click right half: Next slide
- Click left half: Previous slide

## Next Module

Module 7: Feature Engineering & Selection
