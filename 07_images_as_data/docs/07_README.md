# Module 7: Images as Data (OpenCV)

Learn how to work with images as numerical data using OpenCV and NumPy for computer vision applications.

## Learning Objectives

- Load images as 3D NumPy arrays
- Convert between BGR and RGB color spaces
- Resize images to a fixed resolution
- Normalize pixel values from 0-255 to 0-1 for model convergence

## Topics Covered

- Computer vision fundamentals for ML
- `cv2.imread` and color space conversion (BGR to RGB)
- Image resizing to standard dimensions (224×224)
- Pixel normalization for neural network input
- Understanding images as (Height × Width × Channels) arrays
- Batch processing for multiple images

## Prerequisites

- Module 6: Data Storage Options (understanding NumPy arrays)
- Python 3.10+
- Basic understanding of arrays and matrices

## ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/07_images_as_data/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files.

<details><summary>Advanced: run locally</summary>

Prefer local Jupyter/VS Code? Install the dependencies and open the notebook:

```bash
pip install numpy opencv-python matplotlib python-dotenv
jupyter notebook tutorial.ipynb
```

The notebook generates its own sample images, so no separate data step is needed.

</details>

## Lab: The Preprocessor

Build a complete image preprocessing pipeline that:
- Loads a folder of random-sized images
- Converts BGR → RGB color space
- Resizes all images to 224×224 pixels
- Normalizes pixel values to 0-1 range
- Creates a batch array of shape (N, 224, 224, 3)

### Run the Lab

```bash
python lab_the_preprocessor.py
```

The lab includes:
1. **Single image analysis** - Understanding 3D array structure
2. **BGR to RGB conversion** - Handling OpenCV's quirk
3. **Image resizing** - Standardizing dimensions
4. **Pixel normalization** - Preparing for model input
5. **Batch processing** - Processing multiple images efficiently
6. **Memory analysis** - Understanding resource requirements

## Sample Images

The lab automatically generates 8 synthetic sample images with different:
- Sizes (to demonstrate need for resizing)
- Patterns (gradients, shapes, noise, checkerboards)
- Colors (various RGB combinations)

You can generate new samples by running:
```bash
python create_sample_images.py
```

## Key Concepts

### Image Array Structure
```python
img.shape  # (Height, Width, Channels)
# Example: (480, 640, 3)
#          └─┬─┘ └─┬─┘ └┬┘
#            │     │     └─ RGB channels
#            │     └─────── Width (columns)
#            └───────────── Height (rows)
```

### Complete Preprocessing Pipeline
```python
import cv2
import numpy as np

# 1. Load image (BGR format)
img = cv2.imread('photo.jpg')

# 2. Convert BGR → RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 3. Resize to standard size
img = cv2.resize(img, (224, 224))

# 4. Normalize to 0-1 range
img = img.astype(np.float32) / 255.0

# Result: (224, 224, 3) array with values in [0, 1]
```

### Batch Processing
```python
# Process multiple images into a batch
batch = []
for filename in image_files:
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    batch.append(img)

# Stack into 4D array: (N, H, W, C)
batch = np.stack(batch, axis=0)
print(batch.shape)  # (8, 224, 224, 3)
```

## Why 224×224?

- Standard input size for ImageNet pretrained models
- VGG, ResNet, MobileNet all expect 224×224 input
- Allows fixed-size input for neural networks
- Trade-off between detail and computation
- Enables batch processing on GPU

## Why Normalize?

1. **Consistent scale** - All features in the same range
2. **Faster convergence** - Gradient descent optimizes better
3. **Numerical stability** - Prevents overflow/underflow
4. **Model compatibility** - Required by pretrained models
5. **Better training** - Reduces internal covariate shift

## Memory Considerations

Batch size affects memory usage:

| Batch Size | Memory (224×224×3, float32) |
|------------|----------------------------|
| 32         | ~18 MB                     |
| 64         | ~37 MB                     |
| 128        | ~73 MB                     |
| 256        | ~147 MB                    |

GPU memory is limited (typically 4-24 GB). Start with smaller batches and increase if memory allows.

## Slides

View the presentation:
```bash
open slides.html
```

Navigation:
- **Arrow Right / Space**: Next slide
- **Arrow Left**: Previous slide
- **Home**: First slide
- **End**: Last slide
- **Click right/left half**: Navigate slides

## Common Issues

### Issue: Images look weird colors
**Cause**: Forgot to convert BGR → RGB
**Solution**: Always use `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)` after loading

### Issue: Out of memory error
**Cause**: Batch size too large
**Solution**: Reduce batch size or use image generators

### Issue: Model not converging
**Cause**: Forgot to normalize pixel values
**Solution**: Always divide by 255.0 after resizing

### Issue: Shape mismatch error
**Cause**: Images not resized to same dimensions
**Solution**: Ensure all images resized to same size before stacking

## Next Steps

After completing this module:

1. **Data Augmentation** - Random rotations, flips, crops
2. **Advanced Normalization** - ImageNet mean/std per channel
3. **Performance Optimization** - Batch generators, parallel loading
4. **Real Applications** - Object detection, image classification
5. **Transfer Learning** - Using pretrained CNNs

## Resources

- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [NumPy for Images](https://numpy.org/doc/stable/user/howtos_io.html)
- [ImageNet Dataset](https://www.image-net.org/)
- [PyTorch Vision Transforms](https://pytorch.org/vision/stable/transforms.html)
- [TensorFlow Image Preprocessing](https://www.tensorflow.org/tutorials/load_data/images)

## Related Modules

- **Module 6**: Data Storage Options (NumPy arrays)
- **Module 8**: Text as Data (next topic)
- **Module 10**: Feature Extraction (applying to images)

---

**Module 7** • AI Research Foundations Minicourse
