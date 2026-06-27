# Module 06: Quick Reference

Data Cleaning & Transformation Cheat Sheet

## Missing Value Detection

```python
import pandas as pd

# Check for missing values (returns True/False per cell)
df.isna()

# Count missing values per column
missing_counts = df.isna().sum()
print(missing_counts)

# Show only columns with missing data
has_missing = missing_counts[missing_counts > 0]

# Count total missing cells
total_missing = df.isna().sum().sum()

# Percentage of missing data per column
missing_pct = (df.isna().sum() / len(df)) * 100

# View rows with any missing values
df[df.isna().any(axis=1)]

# View rows where specific column is missing
df[df['rating'].isna()]
```

## Missing Value Handling

| Method | Use Case | Example |
|--------|----------|---------|
| `.dropna()` | Remove rows with any missing values | `df.dropna()` |
| `.dropna(subset=['col'])` | Remove rows where specific column is missing | `df.dropna(subset=['rating'])` |
| `.dropna(how='all')` | Remove rows where ALL values are missing | `df.dropna(how='all')` |
| `.fillna(value)` | Fill missing with a constant | `df.fillna(0)` |
| `.fillna(method='ffill')` | Forward fill (use previous value) | `df.fillna(method='ffill')` |
| `.fillna(method='bfill')` | Backward fill (use next value) | `df.fillna(method='bfill')` |
| `.fillna(df.mean())` | Fill with column mean | `df['tokens'].fillna(df['tokens'].mean())` |

```python
# Strategy 1: Drop rows with missing critical fields
df_clean = df.dropna(subset=['prompt_text', 'rating'])

# Strategy 2: Fill missing non-critical fields
df['tokens_used'] = df['tokens_used'].fillna(0)

# Strategy 3: Fill with column mean
df['temperature'] = df['temperature'].fillna(df['temperature'].mean())

# Strategy 4: Fill with mode (most common value)
df['category'] = df['category'].fillna(df['category'].mode()[0])
```

## Duplicate Detection and Removal

```python
# Check if any duplicates exist
has_dupes = df.duplicated().any()

# Count duplicate rows
num_dupes = df.duplicated().sum()

# View all duplicate rows (including first occurrence)
df[df.duplicated(keep=False)]

# View only the duplicate rows (not first occurrence)
df[df.duplicated(keep='first')]

# Remove duplicates (keep first occurrence)
df_no_dupes = df.drop_duplicates()

# Remove duplicates based on specific columns only
df_no_dupes = df.drop_duplicates(subset=['prompt_id'])

# Keep last occurrence instead of first
df_no_dupes = df.drop_duplicates(keep='last')

# Check duplicates in specific columns
df[df.duplicated(subset=['model', 'category'], keep=False)]
```

## String Cleaning Methods

```python
# Remove leading/trailing whitespace
df['model'] = df['model'].str.strip()

# Convert to lowercase
df['model'] = df['model'].str.lower()

# Convert to uppercase
df['model'] = df['model'].str.upper()

# Replace specific values
df['model'] = df['model'].str.replace('GPT-4', 'gpt-4')

# Replace with regex
df['model'] = df['model'].str.replace(r'gpt[-_\s]?4', 'gpt-4', regex=True)

# Remove all non-alphanumeric characters
df['category'] = df['category'].str.replace(r'[^a-zA-Z0-9]', '', regex=True)

# Title case (capitalize first letter of each word)
df['category'] = df['category'].str.title()

# Check if string contains substring
mask = df['prompt_text'].str.contains('python', case=False)
df_python_prompts = df[mask]

# Starts with / Ends with
df[df['model'].str.startswith('gpt')]
df[df['category'].str.endswith('ing')]
```

## Type Conversion Patterns

```python
# Convert to numeric (coerce errors to NaN)
df['tokens_used'] = pd.to_numeric(df['tokens_used'], errors='coerce')

# Convert to integer (drop NaN first or they'll raise error)
df['tokens_used'] = df['tokens_used'].dropna().astype(int)

# Convert to string
df['prompt_id'] = df['prompt_id'].astype(str)

# Convert to category (saves memory for repeated values)
df['model'] = df['model'].astype('category')

# Convert to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Convert datetime with specific format
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d')

# Handle multiple date formats
df['timestamp'] = pd.to_datetime(df['timestamp'], infer_datetime_format=True)

# Convert to boolean
df['is_high_rated'] = df['is_high_rated'].astype(bool)
```

## Boolean Indexing for Filtering

```python
# Single condition
valid_temp = df[df['temperature'].between(0.0, 1.0)]

# Multiple conditions with AND
clean = df[(df['temperature'] <= 1.0) & (df['tokens_used'] > 0)]

# Multiple conditions with OR
extremes = df[(df['rating'] < 2.0) | (df['rating'] > 4.8)]

# NOT condition
not_coding = df[~(df['category'] == 'coding')]

# Multiple values with .isin()
major_models = df[df['model'].isin(['gpt-4', 'claude-3'])]

# Exclude specific values
no_gemini = df[~df['model'].isin(['gemini-pro'])]

# String contains
contains_python = df[df['prompt_text'].str.contains('python', case=False, na=False)]

# Numeric range
medium_length = df[df['tokens_used'].between(100, 200)]

# Date range (if timestamp is datetime)
recent = df[df['timestamp'] > '2026-01-01']
```

## Train/Test Split

```python
from sklearn.model_selection import train_test_split

# Basic 80/20 split
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Stratified split (maintain class balance)
train_df, test_df = train_test_split(
    df, 
    test_size=0.2, 
    stratify=df['category'],
    random_state=42
)

# Alternative: Manual split with .sample()
train_df = df.sample(frac=0.8, random_state=42)
test_df = df.drop(train_df.index)

# Temporal split (ordered by date)
df_sorted = df.sort_values('timestamp')
split_idx = int(len(df_sorted) * 0.8)
train_df = df_sorted.iloc[:split_idx]
test_df = df_sorted.iloc[split_idx:]
```

## CSV Export

```python
# Basic export
df.to_csv('output.csv', index=False)

# Export with specific columns only
df[['model', 'rating', 'tokens_used']].to_csv('output.csv', index=False)

# Export with custom delimiter
df.to_csv('output.tsv', sep='\t', index=False)

# Export train and test splits
train_df.to_csv('data/output/Train.csv', index=False)
test_df.to_csv('data/output/Test.csv', index=False)

# Export with specific encoding
df.to_csv('output.csv', index=False, encoding='utf-8-sig')
```

## Complete Cleaning Pipeline Example

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Load data
df = pd.read_csv('data/dirty_dataset.csv')
print(f"Original shape: {df.shape}")

# 2. Remove exact duplicates
df = df.drop_duplicates()
print(f"After dropping duplicates: {df.shape}")

# 3. Handle missing values
# Drop rows with missing critical fields
df = df.dropna(subset=['prompt_text', 'response_text', 'rating'])

# Fill missing non-critical fields
df['tokens_used'] = df['tokens_used'].fillna(0)

print(f"After handling missing values: {df.shape}")

# 4. Standardize string formatting
df['model'] = df['model'].str.strip().str.lower()
df['category'] = df['category'].str.strip().str.lower()

# Replace inconsistent model names
model_mapping = {
    'gpt4': 'gpt-4',
    'gpt_4': 'gpt-4',
    'claude3': 'claude-3',
    'claude_3': 'claude-3'
}
df['model'] = df['model'].replace(model_mapping)

# 5. Filter invalid data with boolean indexing
df = df[df['temperature'].between(0.0, 1.0)]
df = df[df['rating'].between(0.0, 5.0)]
df = df[df['tokens_used'] > 0]

print(f"After filtering invalid values: {df.shape}")

# 6. Fix data types
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['tokens_used'] = df['tokens_used'].astype(int)
df['model'] = df['model'].astype('category')
df['category'] = df['category'].astype('category')

# 7. Split into train/test
train_df, test_df = train_test_split(
    df, 
    test_size=0.2, 
    stratify=df['category'],
    random_state=42
)

print(f"Train size: {len(train_df)} ({len(train_df)/len(df)*100:.1f}%)")
print(f"Test size: {len(test_df)} ({len(test_df)/len(df)*100:.1f}%)")

# 8. Export
train_df.to_csv('data/output/Train.csv', index=False)
test_df.to_csv('data/output/Test.csv', index=False)

print("✓ Cleaning complete!")
```

## Common Data Quality Issues

| Issue | Detection | Solution |
|-------|-----------|----------|
| Missing values | `.isna().sum()` | `.dropna()` or `.fillna()` |
| Duplicates | `.duplicated().sum()` | `.drop_duplicates()` |
| Whitespace | `df['col'].str.contains(r'^\s|\s$')` | `.str.strip()` |
| Inconsistent casing | Visual inspection | `.str.lower()` or `.str.upper()` |
| Invalid ranges | `df[(df['col'] < min) | (df['col'] > max)]` | Boolean indexing to filter |
| Wrong data types | `.dtypes` | `.astype()` or `pd.to_numeric()` |
| Mixed date formats | `.info()` shows object type | `pd.to_datetime()` |
| Outliers | `.describe()` shows extreme min/max | `.quantile()` and boolean indexing |

## Best Practices

1. **Always work on a copy**: `df_clean = df.copy()`
2. **Document your cleaning steps**: Write comments explaining why data was removed
3. **Track data loss**: Print shape after each cleaning step
4. **Validate results**: Check `.describe()` and `.info()` after cleaning
5. **Save intermediate results**: Export checkpoint CSVs during long pipelines
6. **Use `.copy()` after filtering**: Avoid SettingWithCopyWarning

## Resources

- [Pandas Data Cleaning](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Working with Text Data](https://pandas.pydata.org/docs/user_guide/text.html)
