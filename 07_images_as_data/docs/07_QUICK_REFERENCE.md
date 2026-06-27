# Module 7: Images as Data - Quick Reference

## One-Page Cheat Sheet

### Essential Imports
```python
import cv2
import numpy as np
```

### Load Image
```python
img = cv2.imread('photo.jpg')
# Returns: (H, W, 3) array in BGR format
# Returns: None if file not found
```

### Convert BGR → RGB
```python
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Always do this after cv2.imread()!
```

### Resize Image
```python
img_resized = cv2.resize(img, (224, 224))
# First arg: image, Second arg: (width, height)
```

### Normalize Pixels
```python
img_normalized = img.astype(np.float32) / 255.0
# Converts: uint8 [0-255] → float32 [0.0-1.0]
```

### Complete Pipeline (Single Image)
```python
# Load
img = cv2.imread('photo.jpg')

# Convert color space
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Resize to standard size
img = cv2.resize(img, (224, 224))

# Normalize
img = img.astype(np.float32) / 255.0

# Result: (224, 224, 3) array with values in [0, 1]
```

### Complete Pipeline (Batch)
```python
batch = []

for filename in image_files:
    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    batch.append(img)

# Stack into 4D array
batch = np.stack(batch, axis=0)

# Result: (N, 224, 224, 3) array
```

### Check Image Properties
```python
print(img.shape)      # (480, 640, 3)
print(img.dtype)      # uint8
print(img.min())      # 0
print(img.max())      # 255
print(img.mean())     # Average pixel value
print(img.nbytes)     # Memory in bytes
```

### Array Shape Reference
```python
# 3D: Single image
(H, W, C)             # Height × Width × Channels
(480, 640, 3)         # Example: 480 rows, 640 cols, 3 channels

# 4D: Batch of images
(N, H, W, C)          # Number × Height × Width × Channels
(32, 224, 224, 3)     # Example: 32 images, each 224×224×3
```

### Memory Calculation
```python
# One image (224×224×3, float32)
pixels = 224 × 224 × 3 = 150,528
bytes_per_pixel = 4  # float32
memory = 150,528 × 4 = 602,112 bytes ≈ 0.57 MB

# Batch of N images
batch_memory = N × 0.57 MB
```

### Common Batch Sizes
| Batch Size | Memory    |
|------------|-----------|
| 16         | ~9 MB     |
| 32         | ~18 MB    |
| 64         | ~37 MB    |
| 128        | ~73 MB    |
| 256        | ~147 MB   |

### Interpolation Methods
```python
# Resizing methods (quality vs speed)
cv2.INTER_NEAREST   # Fastest, lowest quality
cv2.INTER_LINEAR    # Fast, good quality (default)
cv2.INTER_CUBIC     # Slower, better quality
cv2.INTER_LANCZOS4  # Slowest, best quality

# Usage
img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
```

### Color Space Conversions
```python
# BGR to RGB (most common)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# RGB to Grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# BGR to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

### Quick Checks
```python
# Check if image loaded
if img is None:
    print("Failed to load image")

# Check image dimensions
H, W, C = img.shape
print(f"Image size: {W}×{H}, Channels: {C}")

# Check value range
print(f"Range: {img.min()}-{img.max()}")

# Check data type
print(f"Type: {img.dtype}")
```

### Common Pitfalls

#### ❌ Forgot BGR→RGB conversion
```python
img = cv2.imread('photo.jpg')
# Colors will look wrong in matplotlib/PIL!
```
#### ✅ Always convert
```python
img = cv2.imread('photo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

#### ❌ Forgot to normalize
```python
img = cv2.resize(img, (224, 224))
# Model won't converge well with 0-255 values
```
#### ✅ Always normalize
```python
img = cv2.resize(img, (224, 224))
img = img.astype(np.float32) / 255.0
```

#### ❌ Wrong resize argument order
```python
img = cv2.resize(img, (H, W))  # Wrong! Width first!
```
#### ✅ Width first
```python
img = cv2.resize(img, (W, H))  # Correct: (width, height)
```

#### ❌ Different sizes in batch
```python
batch = [img1, img2, img3]  # Different shapes
np.stack(batch)  # Error!
```
#### ✅ Resize before stacking
```python
batch = [cv2.resize(img, (224, 224)) for img in images]
np.stack(batch)  # Works!
```

### Standard Sizes

| Model       | Input Size  | Use Case           |
|-------------|-------------|-------------------|
| MobileNet   | 224×224     | Mobile/embedded   |
| ResNet      | 224×224     | General purpose   |
| VGG         | 224×224     | Feature extraction|
| Inception   | 299×299     | High accuracy     |
| EfficientNet| 224×224+    | Scalable          |
| YOLO        | 416×416     | Object detection  |

### Typical Workflow

```
1. Load images (cv2.imread)
   ↓
2. Convert BGR→RGB (cv2.cvtColor)
   ↓
3. Resize to fixed size (cv2.resize)
   ↓
4. Normalize 0-1 (÷ 255.0)
   ↓
5. Stack into batch (np.stack)
   ↓
6. Feed to model
```

### Run the Lab
```bash
# Install dependencies
pip install -e .

# Run lab
python lab_the_preprocessor.py

# View slides
open slides.html

# Test setup
python test_module.py
```

### Next Steps
1. Try different target sizes
2. Add data augmentation (rotations, flips)
3. Implement ImageNet normalization
4. Process your own images
5. Build a simple classifier

---

**Quick Tip**: When in doubt, this is the magic formula:
```python
img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (224, 224)).astype(np.float32) / 255.0
```

Print this page and keep it handy! 📄
