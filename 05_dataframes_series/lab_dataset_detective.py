"""
Module 5: DataFrames & Series
Lab: Dataset Detective

Analyze a raw LLM prompt-response dataset using Pandas DataFrame methods.
Learn to inspect, understand, and explore structured data.
"""

from dotenv import load_dotenv, find_dotenv
import pandas as pd
from pathlib import Path

# Load environment variables
load_dotenv(find_dotenv())


def main():
    """Explore the LLM prompts dataset using DataFrame inspection methods."""

    print("=" * 70)
    print("🔍 MODULE 5: DATASET DETECTIVE LAB")
    print("=" * 70)
    print()

    # -------------------------------------------------------------------
    # 1. LOADING DATA
    # -------------------------------------------------------------------
    print("📂 STEP 1: Loading the Dataset")
    print("-" * 70)

    # Construct path to CSV file
    data_path = Path(__file__).parent / "data" / "llm_prompts.csv"

    # Load CSV into DataFrame
    df = pd.read_csv(data_path)

    print(f"✅ Loaded dataset from: {data_path.name}")
    print(f"   Dataset shape: {df.shape[0]} rows × {df.shape[1]} columns")
    print()

    # -------------------------------------------------------------------
    # 2. FIRST LOOK: HEAD AND TAIL
    # -------------------------------------------------------------------
    print("👀 STEP 2: First Look at the Data")
    print("-" * 70)
    print("\n🔝 First 5 rows (.head()):")
    print(df.head())
    print("\n🔚 Last 5 rows (.tail()):")
    print(df.tail())
    print()

    # -------------------------------------------------------------------
    # 3. DATA STRUCTURE: INFO
    # -------------------------------------------------------------------
    print("📊 STEP 3: Understanding Data Structure")
    print("-" * 70)
    print("\n📋 DataFrame info (.info()):")
    df.info()
    print()

    print("💡 What .info() tells us:")
    print("   • Total entries and column count")
    print("   • Non-null counts (revealing missing data)")
    print("   • Data types for each column")
    print("   • Memory usage")
    print()

    # -------------------------------------------------------------------
    # 4. COLUMN TYPES
    # -------------------------------------------------------------------
    print("🏷️  STEP 4: Examining Column Types")
    print("-" * 70)
    print("\n📝 Data types (.dtypes):")
    print(df.dtypes)
    print()

    print("🔑 Common Pandas data types:")
    print("   • int64    → Whole numbers (prompt_id, tokens_used)")
    print("   • float64  → Decimal numbers (temperature, rating)")
    print("   • object   → Text/strings (prompt_text, model, category)")
    print("   • datetime → Date/time values (timestamp)")
    print()

    # Convert timestamp to datetime for demonstration
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    print("✅ Converted 'timestamp' column to datetime type")
    print(f"   New dtype: {df['timestamp'].dtype}")
    print()

    # -------------------------------------------------------------------
    # 5. STATISTICAL SUMMARY
    # -------------------------------------------------------------------
    print("📈 STEP 5: Statistical Summary")
    print("-" * 70)
    print("\n🔢 Numeric columns summary (.describe()):")
    print(df.describe())
    print()

    print("💡 What .describe() reveals:")
    print("   • count → How many non-null values")
    print("   • mean  → Average value")
    print("   • std   → Standard deviation (spread)")
    print("   • min/max → Range of values")
    print("   • 25%/50%/75% → Quartiles (percentiles)")
    print()

    # -------------------------------------------------------------------
    # 6. FINDING MISSING DATA
    # -------------------------------------------------------------------
    print("🔍 STEP 6: Detecting Missing Data")
    print("-" * 70)
    print("\n❌ Missing values per column (.isna().sum()):")
    missing = df.isna().sum()
    print(missing[missing > 0])
    print()

    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isna().sum().sum()
    missing_pct = (missing_cells / total_cells) * 100

    print(f"📊 Missing data statistics:")
    print(f"   • Total cells: {total_cells}")
    print(f"   • Missing cells: {missing_cells}")
    print(f"   • Missing percentage: {missing_pct:.2f}%")
    print()

    # -------------------------------------------------------------------
    # 7. CATEGORICAL DATA EXPLORATION
    # -------------------------------------------------------------------
    print("🏷️  STEP 7: Exploring Categorical Data")
    print("-" * 70)

    print("\n🤖 Model distribution (.value_counts()):")
    print(df['model'].value_counts())
    print()

    print("📚 Category distribution:")
    print(df['category'].value_counts())
    print()

    print("💡 Why value_counts() matters:")
    print("   • Reveals class imbalance in your data")
    print("   • Helps identify dominant categories")
    print("   • Essential for planning ML training strategies")
    print()

    # -------------------------------------------------------------------
    # 8. SELECTING SPECIFIC DATA
    # -------------------------------------------------------------------
    print("🎯 STEP 8: Selecting and Filtering Data")
    print("-" * 70)

    # Select specific columns
    print("\n📝 Selecting specific columns:")
    key_cols = df[['model', 'category', 'rating', 'tokens_used']]
    print(key_cols.head())
    print()

    # Filter rows
    print("🔎 Filtering rows (high-rated coding prompts):")
    high_rated_coding = df[(df['category'] == 'coding') & (df['rating'] >= 4.7)]
    print(high_rated_coding[['prompt_text', 'model', 'rating']])
    print()

    # -------------------------------------------------------------------
    # 9. GROUPING AND AGGREGATION
    # -------------------------------------------------------------------
    print("📊 STEP 9: Grouping and Aggregation")
    print("-" * 70)

    print("\n🤖 Average rating by model (.groupby()):")
    model_stats = df.groupby('model')['rating'].agg(['mean', 'count', 'std'])
    print(model_stats)
    print()

    print("📚 Token usage by category:")
    category_tokens = df.groupby('category')['tokens_used'].agg(['mean', 'min', 'max'])
    print(category_tokens)
    print()

    # -------------------------------------------------------------------
    # 10. CONNECTION TO MACHINE LEARNING
    # -------------------------------------------------------------------
    print("🤖 STEP 10: Connection to Machine Learning")
    print("-" * 70)
    print()
    print("🎯 Why DataFrame inspection matters for ML:")
    print()
    print("1. DATA QUALITY")
    print("   • Missing values must be handled (impute or remove)")
    print("   • Outliers can hurt model performance")
    print("   • Data types must match model expectations")
    print()
    print("2. FEATURE ENGINEERING")
    print("   • Categorical variables need encoding (one-hot, label)")
    print("   • Numeric features may need scaling/normalization")
    print("   • Text data requires tokenization and vectorization")
    print()
    print("3. CLASS BALANCE")
    print("   • Imbalanced classes can bias predictions")
    print("   • May need oversampling, undersampling, or weighted loss")
    print()
    print("4. DATA SPLITS")
    print("   • Understanding distributions helps create representative splits")
    print("   • Train/validation/test sets should reflect real-world data")
    print()

    # -------------------------------------------------------------------
    # 11. PRACTICAL EXAMPLE
    # -------------------------------------------------------------------
    print("💡 PRACTICAL EXAMPLE: Preparing for ML Training")
    print("-" * 70)
    print()
    print("🔧 Steps to prepare this dataset for training:")
    print()
    print("1. Handle missing ratings:")
    print(f"   • Option A: Remove {missing['rating']} rows with NaN")
    print("   • Option B: Fill with median rating ({df['rating'].median():.1f})")
    print()
    print("2. Encode categorical features:")
    print("   • 'model' → One-hot encoding (3 binary columns)")
    print("   • 'category' → Label encoding (0-3 integer mapping)")
    print()
    print("3. Normalize numeric features:")
    print("   • Temperature already in [0, 1] range ✓")
    print("   • Tokens used: scale to [0, 1] or standardize")
    print()
    print("4. Process text features:")
    print("   • Tokenize prompt_text and response_text")
    print("   • Convert to embeddings (next module!)")
    print()

    # -------------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------------
    print("=" * 70)
    print("✅ LAB COMPLETE: Dataset Detective")
    print("=" * 70)
    print()
    print("🎓 What you learned:")
    print("   ✓ Loading CSV data with pd.read_csv()")
    print("   ✓ Inspecting data with .head(), .tail(), .info(), .describe()")
    print("   ✓ Understanding column types with .dtypes")
    print("   ✓ Finding missing data with .isna().sum()")
    print("   ✓ Exploring categorical data with .value_counts()")
    print("   ✓ Selecting and filtering specific data")
    print("   ✓ Grouping and aggregating with .groupby()")
    print("   ✓ Connecting data inspection to ML preparation")
    print()
    print("🚀 Next steps:")
    print("   → Module 6: Vector Embeddings & Semantic Search")
    print("   → Learn how to convert text into numeric vectors")
    print("   → Build a semantic search engine for these prompts!")
    print()


if __name__ == "__main__":
    main()
