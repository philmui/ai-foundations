"""
Module 6: The Curator
Educational script demonstrating data cleaning and transformation pipeline
"""

from dotenv import load_dotenv, find_dotenv
import pandas as pd
import os
from pathlib import Path

# Load environment variables
load_dotenv(find_dotenv())

# Setup paths
DATA_DIR = Path(__file__).parent / "data"
OUTPUT_DIR = DATA_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 80)
print("THE CURATOR: Data Cleaning Pipeline")
print("=" * 80)
print()

# ============================================================================
# STEP 1: INSPECT THE MESS
# ============================================================================
print("STEP 1: Loading and inspecting the dirty dataset...")
print("-" * 80)

df = pd.read_csv(DATA_DIR / "dirty_dataset.csv")

print(f"✓ Loaded {len(df)} rows")
print()
print("Dataset Info:")
print(df.info())
print()

print("Missing Values per Column:")
missing_counts = df.isna().sum()
print(missing_counts[missing_counts > 0])
print(f"\nTotal cells with missing data: {df.isna().sum().sum()}")
print()

print("Duplicate Rows:")
duplicate_count = df.duplicated().sum()
print(f"Found {duplicate_count} exact duplicate rows")
print()

print("Sample of the messy data:")
print(df.head(10))
print()

# Store initial stats
initial_rows = len(df)
initial_missing = df.isna().sum().sum()
initial_duplicates = duplicate_count

# ============================================================================
# STEP 2: REMOVE EXACT DUPLICATES
# ============================================================================
print("\n" + "=" * 80)
print("STEP 2: Removing exact duplicates...")
print("-" * 80)

# Show some duplicate examples before removal
if duplicate_count > 0:
    print("Example duplicates:")
    duplicated_mask = df.duplicated(keep=False)
    print(df[duplicated_mask].sort_values('prompt_id').head(6))
    print()

df = df.drop_duplicates()

rows_after_dedup = len(df)
removed = initial_rows - rows_after_dedup
print(f"✓ Removed {removed} duplicate rows")
print(f"✓ Remaining rows: {rows_after_dedup}")
print()

# ============================================================================
# STEP 3: HANDLE MISSING VALUES
# ============================================================================
print("=" * 80)
print("STEP 3: Handling missing values...")
print("-" * 80)

print("Strategy decisions:")
print()

# Analyze missing patterns
print("Missing value analysis:")
for col in df.columns:
    missing_pct = (df[col].isna().sum() / len(df)) * 100
    if missing_pct > 0:
        print(f"  {col}: {missing_pct:.1f}% missing")
print()

print("Decision logic:")
print("  • prompt_text: CRITICAL - drop rows (can't evaluate without prompt)")
print("  • response_text: CRITICAL - drop rows (can't evaluate without response)")
print("  • tokens_used: fill with 0 (represents actual usage)")
print("  • rating: drop rows (can't train without target variable)")
print()

# Apply the cleaning strategy
rows_before_missing = len(df)

# Drop rows with missing critical fields
df = df.dropna(subset=['prompt_text', 'response_text', 'rating'])

# Fill missing tokens_used with 0 (actual usage)
df['tokens_used'] = df['tokens_used'].fillna(0)

rows_after_missing = len(df)
removed_missing = rows_before_missing - rows_after_missing

print(f"✓ Dropped {removed_missing} rows with missing critical data")
print(f"✓ Filled {df['tokens_used'].isna().sum()} missing token counts with 0")
print(f"✓ Remaining rows: {rows_after_missing}")
print()

# ============================================================================
# STEP 4: FIX FORMATTING
# ============================================================================
print("=" * 80)
print("STEP 4: Fixing formatting issues...")
print("-" * 80)

print("Unique model names BEFORE standardization:")
print(df['model'].unique())
print()

# Standardize model names
model_mapping = {
    'GPT-4': 'gpt-4',
    'GPT4': 'gpt-4',
    'gpt4': 'gpt-4',
    'GPT-3.5': 'gpt-3.5',
    'Claude-3': 'claude-3',
    'Claude3': 'claude-3',
    'Claude-3-Opus': 'claude-3-opus',
}

df['model'] = df['model'].str.strip()  # Remove whitespace first
df['model'] = df['model'].replace(model_mapping)

print("Unique model names AFTER standardization:")
print(df['model'].unique())
print()

# Strip whitespace from all text columns
text_columns = ['prompt_text', 'response_text', 'category']
for col in text_columns:
    df[col] = df[col].str.strip()

print("✓ Standardized model names")
print("✓ Stripped whitespace from text columns")
print()

# ============================================================================
# STEP 5: BOOLEAN INDEXING TO FILTER INVALID DATA
# ============================================================================
print("=" * 80)
print("STEP 5: Filtering invalid data with boolean indexing...")
print("-" * 80)

rows_before_filter = len(df)

print("Filtering criteria:")
print("  • temperature must be between 0.0 and 1.0")
print("  • tokens_used must be non-negative")
print("  • rating must be between 0.0 and 5.0")
print()

# Show invalid data before filtering
invalid_temp = df[~df['temperature'].between(0.0, 1.0)]
invalid_tokens = df[df['tokens_used'] < 0]
invalid_rating = df[~df['rating'].between(0.0, 5.0)]

if len(invalid_temp) > 0:
    print(f"Found {len(invalid_temp)} rows with invalid temperature:")
    print(invalid_temp[['prompt_id', 'model', 'temperature']])
    print()

if len(invalid_tokens) > 0:
    print(f"Found {len(invalid_tokens)} rows with negative tokens:")
    print(invalid_tokens[['prompt_id', 'model', 'tokens_used']])
    print()

if len(invalid_rating) > 0:
    print(f"Found {len(invalid_rating)} rows with invalid rating:")
    print(invalid_rating[['prompt_id', 'model', 'rating']])
    print()

# Apply filters with boolean indexing
df = df[
    df['temperature'].between(0.0, 1.0) &
    (df['tokens_used'] >= 0) &
    df['rating'].between(0.0, 5.0)
]

rows_after_filter = len(df)
removed_invalid = rows_before_filter - rows_after_filter

print(f"✓ Filtered out {removed_invalid} invalid rows")
print(f"✓ Remaining rows: {rows_after_filter}")
print()

# ============================================================================
# STEP 6: FIX DATA TYPES
# ============================================================================
print("=" * 80)
print("STEP 6: Fixing data types...")
print("-" * 80)

print("Data types BEFORE conversion:")
print(df.dtypes)
print()

# Convert date column to datetime
# The dirty data has mixed formats: "2024-01-15" and "01/16/2024"
df['date'] = pd.to_datetime(df['date'], format='mixed')

# Ensure numeric columns are proper types
df['temperature'] = df['temperature'].astype(float)
df['tokens_used'] = df['tokens_used'].astype(int)
df['rating'] = df['rating'].astype(float)
df['prompt_id'] = df['prompt_id'].astype(int)

print("Data types AFTER conversion:")
print(df.dtypes)
print()

print("✓ Converted date to datetime")
print("✓ Ensured numeric columns are proper types")
print()

# ============================================================================
# STEP 7: SPLIT INTO TRAIN/TEST (80/20)
# ============================================================================
print("=" * 80)
print("STEP 7: Splitting into train/test sets...")
print("-" * 80)

# Random split without sklearn
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)
split_idx = int(0.8 * len(df_shuffled))

train_df = df_shuffled[:split_idx]
test_df = df_shuffled[split_idx:]

print(f"Total clean rows: {len(df)}")
print(f"Train set: {len(train_df)} rows (80%)")
print(f"Test set: {len(test_df)} rows (20%)")
print()

print("Train set category distribution:")
print(train_df['category'].value_counts())
print()

print("Test set category distribution:")
print(test_df['category'].value_counts())
print()

# ============================================================================
# STEP 8: EXPORT CLEAN DATA
# ============================================================================
print("=" * 80)
print("STEP 8: Exporting clean datasets...")
print("-" * 80)

train_path = OUTPUT_DIR / "Train.csv"
test_path = OUTPUT_DIR / "Test.csv"

train_df.to_csv(train_path, index=False)
test_df.to_csv(test_path, index=False)

print(f"✓ Exported {train_path}")
print(f"✓ Exported {test_path}")
print()

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("=" * 80)
print("CLEANING PIPELINE SUMMARY")
print("=" * 80)
print()

print("BEFORE → AFTER")
print("-" * 40)
print(f"Total rows:        {initial_rows:3d} → {len(df):3d}")
print(f"Duplicates:        {initial_duplicates:3d} → {df.duplicated().sum():3d}")
print(f"Missing cells:     {initial_missing:3d} → {df.isna().sum().sum():3d}")
print(f"Unique models:     varied → {df['model'].nunique()} standardized")
print()

print("WHY EACH STEP MATTERS FOR ML:")
print("-" * 40)
print("1. Duplicates → inflate accuracy, leak test data into training")
print("2. Missing values → crash models or introduce bias")
print("3. Formatting → prevent model from treating same values as different")
print("4. Invalid data → corrupt learning patterns")
print("5. Data types → prevent type errors, enable proper operations")
print("6. Train/test split → measure true generalization, prevent overfitting")
print()

print("✨ Clean data is ready for machine learning!")
print()

# Show a sample of the final clean data
print("Sample of CLEAN data:")
print(df.head(10))
print()

print("=" * 80)
print("THE CURATOR: Complete!")
print("=" * 80)
