# Module 05: Quick Reference

Pandas DataFrames & Series Cheat Sheet

## DataFrame Creation

```python
import pandas as pd

# From CSV file
df = pd.read_csv('data.csv')

# From JSON file
df = pd.read_json('data.json')

# From dictionary
data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
df = pd.DataFrame(data)

# With explicit data types
df = pd.read_csv('data.csv', dtype={'col1': 'int64', 'col2': 'category'})

# With date parsing
df = pd.read_csv('data.csv', parse_dates=['timestamp'])
```

## Inspection Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `.head(n)` | First n rows (default 5) | `df.head(3)` |
| `.tail(n)` | Last n rows (default 5) | `df.tail(3)` |
| `.info()` | Structure and types | `df.info()` |
| `.describe()` | Statistical summary | `df.describe()` |
| `.shape` | Dimensions (rows, cols) | `df.shape` → `(100, 5)` |
| `.dtypes` | Data types per column | `df.dtypes` |
| `.columns` | Column names | `df.columns.tolist()` |
| `.index` | Row index | `df.index` |

## Selection Patterns

### Single Column (Returns Series)

```python
# Bracket notation (always works)
model_series = df['model']

# Dot notation (only if valid identifier)
model_series = df.model

# Type check
type(model_series)  # pandas.core.series.Series
```

### Multiple Columns (Returns DataFrame)

```python
# Select specific columns
subset = df[['model', 'rating', 'tokens_used']]

# Reorder columns
reordered = df[['category', 'model', 'rating']]
```

### Rows by Position

```python
# Single row by position
first_row = df.iloc[0]

# Multiple rows by position
first_five = df.iloc[0:5]  # Rows 0-4
last_three = df.iloc[-3:]  # Last 3 rows

# Specific rows and columns
subset = df.iloc[0:5, [1, 3, 5]]  # Rows 0-4, columns at positions 1, 3, 5
```

### Rows by Condition (Boolean Indexing)

```python
# Single condition
high_rated = df[df['rating'] > 4.5]

# Multiple conditions with AND (&)
high_rated_coding = df[(df['rating'] > 4.5) & (df['category'] == 'coding')]

# Multiple conditions with OR (|)
extreme_ratings = df[(df['rating'] < 2.0) | (df['rating'] > 4.8)]

# NOT condition (~)
not_coding = df[~(df['category'] == 'coding')]

# Using .isin() for multiple values
major_models = df[df['model'].isin(['gpt-4', 'claude-3'])]
```

## Boolean Indexing Examples

```python
# Equality
df[df['model'] == 'gpt-4']

# Greater than / Less than
df[df['tokens_used'] > 150]

# Between two values
df[(df['rating'] >= 4.0) & (df['rating'] <= 5.0)]

# Contains substring (string methods)
df[df['prompt_text'].str.contains('python', case=False)]

# Starts with / Ends with
df[df['model'].str.startswith('gpt')]

# Is null / Not null
df[df['rating'].isna()]
df[df['rating'].notna()]
```

## Aggregation Methods

### Value Counts

```python
# Count unique values
model_counts = df['model'].value_counts()

# As percentages
model_pct = df['model'].value_counts(normalize=True) * 100

# Include missing values in counts
counts_with_na = df['rating'].value_counts(dropna=False)
```

### GroupBy Operations

```python
# Single column aggregation
avg_tokens_by_model = df.groupby('model')['tokens_used'].mean()

# Multiple aggregations
model_stats = df.groupby('model')['tokens_used'].agg(['count', 'mean', 'std', 'min', 'max'])

# Rename aggregation columns
model_stats = df.groupby('model')['tokens_used'].agg([
    ('count', 'count'),
    ('avg', 'mean'),
    ('stdev', 'std')
])

# Aggregate multiple columns
summary = df.groupby('category').agg({
    'prompt_id': 'count',
    'tokens_used': 'mean',
    'rating': 'mean'
})

# Multi-level groupby
model_category_avg = df.groupby(['model', 'category'])['rating'].mean()

# Unstack for pivot table style
pivot = df.groupby(['model', 'category'])['rating'].mean().unstack(fill_value=0)
```

## Common Operations

### Missing Data

```python
# Detect missing values (returns True/False)
df.isna()

# Count missing values per column
missing_counts = df.isna().sum()

# Drop rows with any missing values
df_clean = df.dropna()

# Drop rows where specific column is missing
df_clean = df.dropna(subset=['rating'])

# Fill missing values with a constant
df_filled = df.fillna(0)

# Fill missing values with column mean
df['rating'] = df['rating'].fillna(df['rating'].mean())

# Fill missing values with previous value (forward fill)
df_ffill = df.fillna(method='ffill')
```

### Sorting

```python
# Sort by single column
df_sorted = df.sort_values('rating', ascending=False)

# Sort by multiple columns
df_sorted = df.sort_values(['category', 'rating'], ascending=[True, False])

# Sort by index
df_sorted = df.sort_index()
```

### Adding/Removing Columns

```python
# Add new column
df['tokens_per_rating'] = df['tokens_used'] / df['rating']

# Add column from conditional logic
df['is_high_rated'] = df['rating'] > 4.5

# Drop columns
df_subset = df.drop(columns=['timestamp', 'prompt_id'])

# Rename columns
df_renamed = df.rename(columns={'tokens_used': 'num_tokens', 'rating': 'score'})
```

### Statistics

```python
# Single column statistics
mean_tokens = df['tokens_used'].mean()
median_rating = df['rating'].median()
std_temp = df['temperature'].std()
max_tokens = df['tokens_used'].max()
min_tokens = df['tokens_used'].min()

# Count non-null values
count = df['rating'].count()

# Correlation between numeric columns
correlation = df['tokens_used'].corr(df['rating'])
```

## Quick Workflow Example

```python
import pandas as pd

# 1. Load data
df = pd.read_csv('data/llm_prompts.csv')

# 2. Quick inspection
print(f"Shape: {df.shape}")
print(df.head())
print(df.info())

# 3. Check for missing data
print(df.isna().sum())

# 4. Filter data
high_rated = df[df['rating'] > 4.5]

# 5. Analyze distributions
print(df['model'].value_counts())

# 6. Group and aggregate
model_performance = df.groupby('model')['rating'].mean().sort_values(ascending=False)
print(model_performance)

# 7. Export results
high_rated.to_csv('high_rated_prompts.csv', index=False)
```

## Data Types Reference

| Pandas dtype | Python type | Example |
|--------------|-------------|---------|
| `int64` | `int` | `42`, `1000` |
| `float64` | `float` | `3.14`, `4.5` |
| `object` | `str` | `"gpt-4"`, `"Hello"` |
| `category` | `str` (categorical) | `"coding"`, `"math"` |
| `datetime64` | `datetime` | `2026-06-01` |
| `bool` | `bool` | `True`, `False` |

## Common Pitfalls

### Chained Indexing (Avoid)

```python
# BAD: May not work as expected
df[df['rating'] > 4.5]['model'] = 'top-model'

# GOOD: Use .loc for assignment
df.loc[df['rating'] > 4.5, 'model'] = 'top-model'
```

### Iterating Over Rows (Slow)

```python
# BAD: Slow for large datasets
for index, row in df.iterrows():
    print(row['model'])

# GOOD: Vectorized operations
print(df['model'])
```

### Modifying While Iterating

```python
# BAD: Don't modify DataFrame while iterating
for i in range(len(df)):
    if df.iloc[i]['rating'] < 3.0:
        df = df.drop(i)  # Don't do this

# GOOD: Use boolean indexing
df = df[df['rating'] >= 3.0]
```

## Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet (Official)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
