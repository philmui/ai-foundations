# Module 8: Capstone — The Research Pipeline

The final module integrating all concepts from Modules 1-7 into a production-ready multimodal data pipeline.

## Learning Objectives

- Integrate Python, NumPy, Pandas, and OpenCV into a single multimodal data pipeline
- Build a `MultimodalDataLoader` class producing batched text and image arrays
- Understand how to connect custom pipelines to ML frameworks (PyTorch/TensorFlow)
- Present and explain code via recorded walkthrough

## Topics Covered

- Multimodal data loading (text + images)
- Pandas for reading CSVs with image filenames and text descriptions
- OpenCV for loading and processing images
- NumPy for batching and vectorization
- Generator patterns for memory-efficient iteration
- Connection points to PyTorch and TensorFlow

## ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/08_capstone_pipeline/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files. This includes the synthetic multimodal dataset (20 images across 5 categories — astronomy, biology, geography, engineering, meteorology — with train/test splits and a manifest CSV) and the full pipeline it demonstrates:

- Loading and cleaning the manifest with Pandas
- Filtering by train/test split
- Generator-based batch iteration
- Image loading and preprocessing with OpenCV
- NumPy array stacking for batches
- Performance timing
- Connection to PyTorch/TensorFlow (pseudocode)

<details><summary>Advanced: run locally</summary>

The dependencies (`numpy>=1.26.0`, `pandas>=2.1.0`, `opencv-python>=4.8.0`, `python-dotenv`) are installed by the notebook's first code cell, so you can simply open `tutorial.ipynb` in Jupyter or VS Code and run all cells — the dataset is generated inside the notebook. If you prefer a project-level install, run `uv sync` (or `pip install -e .`) from the module folder first, then launch Jupyter.

</details>

## Module Integration

This capstone integrates all 8 modules:

| Module | Integration Point |
|--------|------------------|
| **Module 1** | Environment setup with `.env` loading |
| **Module 2** | Generator pattern for batch iteration |
| **Module 3** | NumPy array operations and statistics |
| **Module 4** | Vectorization and performance optimization |
| **Module 5** | Pandas for CSV reading and DataFrame operations |
| **Module 6** | Data cleaning, validation, transformation |
| **Module 7** | OpenCV for image loading and preprocessing |
| **Module 8** | Complete multimodal research pipeline |

## File Structure

```
08_capstone_pipeline/
├── tutorial.ipynb              # Self-contained capstone notebook (Colab-ready)
├── slides.html                 # Educational slides
└── docs/                       # README, setup, assignment, rubric
```

The notebook generates its own synthetic dataset (20 images across 5 categories plus a manifest CSV) at runtime, so there are no separate data files or helper scripts to run first.

## The Manifest Pattern

The manifest CSV links images to their metadata:

```csv
image_filename,caption,category,split
galaxy_001.png,Spiral galaxy with bright core,astronomy,train
cell_001.png,Human red blood cells under microscope,biology,train
landscape_001.png,Mountain range with snow peaks,geography,train
```

This pattern:
- ✓ Keeps metadata separate from images
- ✓ Enables easy filtering and splits
- ✓ Supports multimodal data (text + images)
- ✓ Scales to large datasets
- ✓ Works with existing images (no file renaming)

## MultimodalDataLoader Class

### Architecture

```
Manifest CSV → Pandas (filter/clean) → Generator (batch) →
OpenCV (load/resize/normalize) → NumPy (stack) → Batch Dict
```

### Usage

```python
from pathlib import Path
# The MultimodalDataLoader class is defined in tutorial.ipynb

# Initialize
loader = MultimodalDataLoader(
    manifest_path=Path("data/manifest.csv"),
    image_dir=Path("data/images"),
    batch_size=4,
    target_size=(224, 224),
    split="train",
    shuffle=True,
    normalize=True
)

# Iterate over batches
for batch in loader:
    images = batch['image_batch']  # Shape: (B, H, W, C)
    texts = batch['text_batch']    # List of B strings
    meta = batch['metadata']       # Dict with categories, filenames

    print(f"Batch shape: {images.shape}")
    print(f"Batch size: {len(texts)}")
```

### Output Format

Each batch is a dictionary:

```python
{
    'image_batch': np.ndarray,    # Shape: (B, H, W, C), dtype: float32, range: [0, 1]
    'text_batch': List[str],      # Length B, captions for each image
    'metadata': {
        'batch_size': int,
        'categories': List[str],  # Category for each sample
        'filenames': List[str],   # Source filenames
        'split': str              # 'train' or 'test'
    }
}
```

## Connection to ML Frameworks

### PyTorch

```python
import torch

# Convert batch to PyTorch tensors
image_tensor = torch.from_numpy(batch['image_batch'])  # Zero-copy
image_tensor = image_tensor.permute(0, 3, 1, 2)       # (B,H,W,C) → (B,C,H,W)

# Forward pass
output = model(image_tensor)
```

### TensorFlow

```python
import tensorflow as tf

# Convert batch to TensorFlow tensors
image_tensor = tf.convert_to_tensor(batch['image_batch'])  # Already (B,H,W,C)

# Forward pass
output = model(image_tensor)
```

## Educational Slides

Open `slides.html` in a browser for the educational presentation (16 slides).

**Navigation:**
- Arrow keys: ← → for previous/next
- Space: Next slide
- Home/End: First/last slide
- Touch: Swipe left/right on mobile

**Design:**
- Inter font from Google Fonts
- Left-aligned, asymmetric layouts
- Charcoal (#1a1a2e), off-white (#fafafa), accent (#e94560)
- All diagrams as inline SVG
- No accent lines, 7x7 rule
- Footer: "© mui-group"

## Performance Characteristics

Expected performance (on typical laptop CPU):
- **~0.15 seconds per batch** (batch_size=4)
- **~27 samples/second**
- **Memory-efficient**: Generator pattern loads one batch at a time

Optimization strategies:
- Use generators for memory efficiency
- Batch processing reduces overhead
- OpenCV optimized C++ backend
- NumPy vectorization
- Add prefetching for production
- Consider multiprocessing for CPU-bound tasks

## Final Project Requirements

### Code Requirements

- [x] Create synthetic dataset with manifest.csv
- [x] Implement `MultimodalDataLoader` class
- [x] Integrate all 8 modules
- [x] Process train and test splits
- [x] Generate batches with correct shapes
- [x] Time the pipeline
- [x] Show ML framework integration

### Video Walkthrough (5 minutes)

Record a video covering:

1. **Manifest Pattern** (1 min)
   - Explain the CSV structure
   - Show how it links images and metadata
   - Discuss advantages

2. **Class Architecture** (1.5 min)
   - Walk through `__init__` configuration
   - Explain `__iter__` generator pattern
   - Show image preprocessing steps

3. **Batch Generation** (1 min)
   - Demonstrate running the pipeline
   - Show batch shapes and statistics
   - Explain output dictionary format

4. **ML Integration** (1 min)
   - Show PyTorch connection
   - Show TensorFlow connection
   - Explain shape conversions

5. **Module Integration** (0.5 min)
   - Recap how all 8 modules come together
   - Highlight key learnings

## What's Next

After completing this capstone, you're ready for:

1. **Add Data Augmentation**
   - Random flips, crops, rotations
   - Color jittering
   - Mixup/CutMix strategies

2. **Implement Text Tokenization**
   - Add transformer tokenizers
   - Handle variable-length sequences
   - Padding and attention masks

3. **Build Actual Models**
   - Vision models (ResNet, ViT)
   - Multimodal models (CLIP-style)
   - Fine-tuning strategies

4. **Production Features**
   - Caching for preprocessed images
   - Distributed data loading
   - Logging and monitoring
   - Experiment tracking

5. **Advanced Topics**
   - Zero-shot learning
   - Few-shot learning
   - Self-supervised pretraining
   - Cross-modal retrieval

## Congratulations!

You've completed the **AI Research Foundations** minicourse!

You now have:
- ✓ A solid foundation in data processing for ML
- ✓ Hands-on experience with NumPy, Pandas, OpenCV
- ✓ Production-ready data pipeline skills
- ✓ Understanding of ML framework integration
- ✓ Portfolio project demonstrating your skills

Keep building and learning! 🚀
