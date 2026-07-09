# Tutorial Guide: Module 7 - Images as Data

## Overview

This Jupyter notebook provides a comprehensive, hands-on tutorial for understanding images as numerical data using OpenCV and NumPy. Designed for advanced high school students in an AI Research Foundations minicourse.

## What's Included

### Core Concepts Covered

1. **Images as 3D Arrays** (Height × Width × Channels)
   - Pixel representation as numbers (0-255)
   - Grayscale vs color images
   - Synthetic image creation with NumPy

2. **Loading Images with OpenCV**
   - `cv2.imread()` basics
   - Understanding `.shape` attribute
   - Working with real image files

3. **BGR vs RGB Problem**
   - OpenCV's historical BGR format
   - Visual comparison showing wrong vs correct colors
   - Conversion using `cv2.cvtColor()`

4. **Image Resizing**
   - Why neural networks need fixed sizes
   - Standard 224×224 dimension
   - Interpolation methods comparison
   - Aspect ratio considerations

5. **Pixel Normalization**
   - Converting 0-255 integers to 0.0-1.0 floats
   - Why normalization improves training
   - Histogram visualization before/after
   - ImageNet-style standardization

6. **Batch Processing**
   - Loading multiple images
   - Complete preprocessing pipeline
   - Stacking into 4D arrays with `np.stack()`
   - Memory considerations

7. **Memory Management**
   - Calculating memory requirements
   - GPU memory constraints
   - Batch size optimization strategies
   - Memory budget calculator

## Notebook Structure

### Sequential Learning Path

```
Setup → Concepts → Loading → BGR/RGB → Resizing → Normalization → Batching → Memory → Exercises
```

Each section includes:
- **Markdown explanation** before code (theory first)
- **Code cells** with detailed comments
- **Visualizations** using matplotlib
- **Mermaid diagrams** for pipeline flow
- **Key Insight callouts** (blockquotes) after major concepts
- **Print statements** showing intermediate values

### Visualizations

The notebook includes multiple types of visualizations:

1. **Synthetic Images**: Demonstrate concepts without external dependencies
2. **Channel Separation**: R, G, B channels shown individually
3. **Before/After Comparisons**: Original vs processed images
4. **Histograms**: Pixel value distributions
5. **Batch Grids**: Multiple processed images displayed together

### Mermaid Diagrams

Three key diagrams illustrate:
1. Image array structure (3D tensor)
2. Complete preprocessing pipeline (flowchart)
3. Normalization process (step-by-step)

## How to Use This Tutorial

### Prerequisites

- Python 3.10+
- Basic understanding of NumPy arrays
- Completed Module 6 (NumPy fundamentals)

### Setup

**Recommended — Google Colab:**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/07_images_as_data/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — it generates any sample images it needs inside the notebook, so it runs end-to-end with no external files.

<details><summary>Advanced: run locally</summary>

1. Install dependencies:
   ```bash
   pip install numpy opencv-python matplotlib python-dotenv
   ```
2. Launch Jupyter:
   ```bash
   jupyter notebook tutorial.ipynb
   ```

Sample images are generated automatically on first run.

</details>

### Running the Notebook

**Sequential Execution Recommended**:
- Run cells in order (top to bottom)
- Each cell builds on previous ones
- Some cells depend on variables from earlier cells

**Interactive Exploration**:
- Modify parameters (image sizes, batch sizes)
- Experiment with different values
- Re-run visualization cells with changes

**Estimated Time**:
- Full walkthrough: 60-90 minutes
- Quick review: 30 minutes
- Deep exploration with exercises: 2-3 hours

## Learning Objectives Achievement

After completing this tutorial, students will be able to:

- ✅ Explain images as 3D NumPy arrays with shape (H, W, C)
- ✅ Load images using `cv2.imread()`
- ✅ Convert between BGR and RGB color spaces
- ✅ Resize images to standard dimensions (224×224)
- ✅ Normalize pixel values from 0-255 to 0.0-1.0
- ✅ Process batches of images into 4D arrays (N, H, W, C)
- ✅ Calculate memory requirements for different batch sizes
- ✅ Understand the complete image preprocessing pipeline

## Exercises & Practice

The notebook includes four hands-on exercises:

### Exercise 1: Different Image Sizes
Compare memory usage for 96×96, 224×224, and 512×512 images

### Exercise 2: Channel Statistics
Calculate per-channel mean and standard deviation

### Exercise 3: Advanced Normalization
Implement ImageNet-style normalization (subtract mean, divide by std)

### Exercise 4: Memory Budget Calculator
Create a function to compute max batch size given GPU memory

## Key Functions Demonstrated

### Complete Preprocessing Pipeline

```python
def preprocess_image(image_path, target_size=(224, 224)):
    # 1. Load image (BGR format)
    img = cv2.imread(image_path)
    
    # 2. Convert BGR → RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # 3. Resize to target size
    img = cv2.resize(img, target_size, interpolation=cv2.INTER_LINEAR)
    
    # 4. Normalize to 0-1 range
    img = img.astype(np.float32) / 255.0
    
    return img
```

### Batch Creation

```python
def create_image_batch(folder_path, target_size=(224, 224)):
    processed_images = []
    for img_path in image_files:
        img = preprocess_image(img_path, target_size)
        processed_images.append(img)
    
    # Stack into 4D array: (N, H, W, C)
    batch = np.stack(processed_images, axis=0)
    return batch
```

## Common Issues & Solutions

### Issue: "Sample images not found"
**Solution**: The notebook auto-generates images. If this fails, run:
```bash
python create_sample_images.py
```

### Issue: "Kernel dies / Out of memory"
**Solution**: Reduce batch size or image dimensions in exercises

### Issue: "Colors look wrong"
**Cause**: Forgot BGR → RGB conversion
**Solution**: Check Section 4 on BGR vs RGB problem

### Issue: "Import errors"
**Solution**: Ensure dependencies installed:
```bash
pip install numpy opencv-python matplotlib python-dotenv
```

## Connection to Other Modules

### Prerequisites
- **Module 6**: NumPy arrays and operations (required)
- **Module 3**: Array broadcasting (helpful)

### Follow-up Modules
- **Module 8**: Text as Data (similar preprocessing concepts)
- **Module 10**: Feature Extraction (applying to images)

### Real-world Applications
After this module, students can explore:
- Image classification with CNNs
- Transfer learning with pretrained models
- Data augmentation techniques
- Object detection and segmentation

## Technical Notes

### Dependencies
- `numpy>=1.24.0` - Array operations
- `opencv-python>=4.8.0` - Image loading and processing
- `matplotlib>=3.7.0` - Visualization
- `python-dotenv>=1.0.0` - Environment configuration

### Memory Requirements
- **Minimal**: ~100 MB RAM (for sample images)
- **Comfortable**: 2-4 GB RAM (for exercises)
- **GPU**: Not required (CPU-only tutorial)

### Data Files
- Sample images: 8 synthetic images, ~200 KB total
- Generated automatically on first run
- Located in `data/images/` subdirectory

## Teaching Tips

### For Instructors

1. **Emphasize Visual Understanding**: The Mermaid diagrams and matplotlib plots are crucial for visual learners

2. **Interactive Exploration**: Encourage students to modify parameters and observe results

3. **Memory Awareness**: Use the memory exercises to build intuition about computational constraints

4. **Real-world Context**: Connect to actual ML workflows (ImageNet, transfer learning)

5. **Common Mistakes**: Highlight the BGR/RGB issue early — it's a frequent source of bugs

### Discussion Points

- Why is 224×224 the standard? (Historical: ImageNet competition)
- What happens if we don't normalize? (Poor convergence, numerical instability)
- Why does OpenCV use BGR? (Historical: early video cameras)
- How do we handle images of different aspect ratios? (Padding, cropping, letterboxing)

## Troubleshooting

### Jupyter Notebook Issues

**Cells won't execute**:
- Check kernel is running (look for green indicator)
- Restart kernel: Kernel → Restart

**Variables undefined**:
- Run cells in order from top
- Check for error messages in previous cells

**Visualizations not showing**:
- Ensure `%matplotlib inline` is executed
- Try `plt.show()` explicitly

### OpenCV Issues

**cv2.imread() returns None**:
- Check file path is correct
- Verify file exists with `Path(file).exists()`
- Check file permissions

**Colors still wrong after conversion**:
- Verify you're using `cv2.COLOR_BGR2RGB` (not RGB2BGR)
- Check conversion happened before display

## Assessment Criteria

Students should demonstrate:

1. **Conceptual Understanding**:
   - Can explain why images are 3D arrays
   - Understands purpose of each preprocessing step
   - Knows when and why to normalize

2. **Technical Skills**:
   - Can write preprocessing pipeline from scratch
   - Correctly handles BGR/RGB conversion
   - Calculates memory requirements

3. **Problem Solving**:
   - Completes all four exercises
   - Modifies code to experiment
   - Debugs common issues independently

## Additional Resources

### Official Documentation
- [OpenCV Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

### Further Reading
- [ImageNet Dataset](https://www.image-net.org/)
- [PyTorch Vision Transforms](https://pytorch.org/vision/stable/transforms.html)
- [TensorFlow Image Preprocessing](https://www.tensorflow.org/tutorials/load_data/images)

### Related Topics
- Convolutional Neural Networks (CNNs)
- Transfer Learning
- Data Augmentation
- Image Segmentation

## Feedback & Improvements

This tutorial is designed to be:
- **Self-contained**: No external images required
- **Progressive**: Builds concepts incrementally
- **Practical**: Includes real preprocessing code
- **Visual**: Heavy use of plots and diagrams
- **Interactive**: Hands-on exercises throughout

Suggested improvements welcome via:
- Direct feedback to instructor
- GitHub issues (if using version control)
- Student surveys after completion

---

**Version**: 1.0  
**Last Updated**: June 2026  
**Target Audience**: Advanced high school students (Grades 11-12)  
**Duration**: 1.5-2 hours  
**Prerequisites**: Python basics, NumPy fundamentals
