# Module 8: Quick Reference Card

## 🚀 Quick Start

```bash
pip install -e .                    # Install dependencies
python create_sample_data.py        # Generate dataset
python lab_research_pipeline.py    # Run pipeline
open slides.html                    # View slides
```

## 📊 The Manifest Pattern

**manifest.csv structure:**
```csv
image_filename,caption,category,split
galaxy_001.png,Spiral galaxy...,astronomy,train
```

**Why?**
- ✓ Links images to metadata
- ✓ Easy filtering (train/test/val)
- ✓ No file renaming needed
- ✓ Supports any metadata

## 🔄 Pipeline Architecture

```
CSV → Pandas → Generator → OpenCV → NumPy → Batch
```

1. **Pandas**: Read CSV, filter split, clean text
2. **Generator**: Yield batches, shuffle if needed
3. **OpenCV**: Load images, resize, BGR→RGB
4. **NumPy**: Stack to (B,H,W,C), normalize [0,1]

## 💻 MultimodalDataLoader Usage

```python
from pathlib import Path
from lab_research_pipeline import MultimodalDataLoader

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

# Iterate
for batch in loader:
    images = batch['image_batch']  # (B, H, W, C) float32 [0,1]
    texts = batch['text_batch']    # List[str] length B
    meta = batch['metadata']       # Dict
```

## 🎯 Batch Output Format

```python
{
    'image_batch': np.ndarray,
        # Shape: (B, H, W, C)
        # dtype: float32
        # range: [0.0, 1.0]

    'text_batch': List[str],
        # Length: B
        # One caption per image

    'metadata': {
        'batch_size': int,
        'categories': List[str],
        'filenames': List[str],
        'split': str
    }
}
```

## 🔗 ML Framework Connection

### PyTorch

```python
import torch

# Convert (zero-copy)
tensor = torch.from_numpy(batch['image_batch'])

# Permute to (B, C, H, W)
tensor = tensor.permute(0, 3, 1, 2)

# Forward
output = model(tensor)
```

### TensorFlow

```python
import tensorflow as tf

# Convert (already (B, H, W, C))
tensor = tf.convert_to_tensor(batch['image_batch'])

# Forward
output = model(tensor)
```

## 🛠️ Key Methods

### __init__(self, ...)
- Loads manifest with Pandas
- Cleans and validates data
- Filters by split

### __iter__(self) → Iterator[Dict]
- Shuffles indices if enabled
- Yields batches using generator pattern
- Loads images lazily with OpenCV

### _load_and_preprocess_image(self, path) → np.ndarray
- cv2.imread() - Load image
- cv2.resize() - Resize to target
- cv2.cvtColor() - BGR → RGB
- / 255.0 - Normalize to [0,1]

## 📦 Module Integration

| Module | Integration |
|--------|------------|
| 1 | Environment setup (.env) |
| 2 | Generator pattern |
| 3 | NumPy arrays & stats |
| 4 | Vectorization |
| 5 | Pandas DataFrames |
| 6 | Data cleaning |
| 7 | OpenCV images |
| 8 | Complete pipeline |

## ⚡ Performance Tips

**Memory Efficiency**
- Use generators (don't load all at once)
- Process one batch at a time
- Delete unused variables

**Speed Optimization**
- Increase batch size (better GPU util)
- Reduce image size if possible
- Use prefetching in production
- Consider multiprocessing

**Typical Performance**
- ~0.15 sec/batch (batch_size=4)
- ~27 samples/sec
- Scales with batch size & CPU

## 🐛 Common Issues

### Images not found
```bash
# Run this first!
python create_sample_data.py
```

### ModuleNotFoundError: cv2
```bash
pip install opencv-python
```

### Slow performance
- Reduce `target_size=(128, 128)`
- Increase `batch_size=8`
- Check disk speed (SSD > HDD)

### Wrong batch shapes
- Check: images.shape == (B, H, W, C)
- Not: (B, C, H, W) - that's PyTorch format
- Convert: `tensor.permute(0, 3, 1, 2)` for PyTorch

## 📝 Final Project Checklist

### Code
- [ ] Create synthetic dataset
- [ ] Implement MultimodalDataLoader class
- [ ] Use all 8 modules
- [ ] Process train & test splits
- [ ] Generate correct batch shapes
- [ ] Time the pipeline
- [ ] Show ML framework connection

### Video (5 min)
- [ ] Explain manifest pattern (1 min)
- [ ] Walk through class architecture (1.5 min)
- [ ] Demonstrate batch generation (1 min)
- [ ] Show ML integration (1 min)
- [ ] Recap module integration (0.5 min)

## 🎓 Key Takeaways

1. **Manifests > File naming conventions**
   - More flexible, easier to maintain

2. **Generators > Loading everything**
   - Memory efficient, scales to large datasets

3. **Normalization matters**
   - Neural networks expect [0,1] or [-1,1]

4. **Shape conventions differ**
   - PyTorch: (B, C, H, W)
   - TensorFlow: (B, H, W, C)
   - Our pipeline: (B, H, W, C)

5. **Preprocessing is crucial**
   - Bad data → bad model
   - Clean data → good model

## 🚀 Next Steps

After this module, try:

1. **Real datasets**
   - CIFAR-10, ImageNet, COCO
   - Create manifests for them

2. **Data augmentation**
   - Random flips, crops, rotations
   - Color jittering, cutout

3. **Text processing**
   - Tokenization
   - Embeddings
   - Padding & masking

4. **Model building**
   - Vision models (ResNet, ViT)
   - Multimodal (CLIP-style)
   - Fine-tuning

5. **Production features**
   - Caching
   - Distributed loading
   - Monitoring & logging

---

**Module 8** | AI Research Foundations | © mui-group
