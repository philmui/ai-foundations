# Module 8 Setup Guide for Instructors

## Quick Start

```bash
# 1. Install dependencies
pip install -e .

# 2. Generate synthetic dataset
python create_sample_data.py

# 3. Run the capstone lab
python lab_research_pipeline.py

# 4. Open slides in browser
open slides.html
```

## What Was Delivered

### Core Files

1. **`pyproject.toml`** - Dependencies configuration
   - python-dotenv
   - numpy>=1.26.0
   - pandas>=2.1.0
   - opencv-python>=4.8.0

2. **`data/manifest.csv`** - Multimodal data manifest
   - 20 samples across 5 categories
   - 16 train / 4 test split
   - Links images to captions and metadata

3. **`create_sample_data.py`** - Synthetic data generator
   - Creates 20 synthetic images matching manifest
   - Categories: astronomy, biology, geography, engineering, meteorology
   - Each category has distinct visual patterns
   - Demonstrates programmatic image generation with OpenCV

4. **`lab_research_pipeline.py`** - Main capstone lab (comprehensive)
   - ~400 lines of educational code
   - `MultimodalDataLoader` class integrating all 8 modules
   - Full pipeline: CSV → Pandas → Generator → OpenCV → NumPy → Batch
   - Performance timing and statistics
   - PyTorch and TensorFlow integration examples (pseudocode)
   - Detailed inline comments explaining every step

5. **`slides.html`** - Educational presentation
   - 16 slides covering the complete pipeline
   - Inter font, left-aligned design
   - Charcoal/off-white/accent color scheme
   - All diagrams as inline SVG
   - Keyboard and touch navigation
   - Self-contained single HTML file

6. **`README.md`** - Complete documentation
   - Learning objectives
   - Setup instructions
   - Module integration table
   - Usage examples
   - Performance characteristics
   - Final project requirements
   - Video walkthrough guidelines

## Expected Output from `create_sample_data.py`

```
Reading manifest from .../data/manifest.csv

Generating 20 synthetic images...
  [ 1/20] Created galaxy_001.png (astronomy, train)
  [ 2/20] Created galaxy_002.png (astronomy, train)
  ...
  [20/20] Created weather_004.png (meteorology, test)

✓ Successfully generated 20 images in .../data/images

Dataset Statistics:
  Total images: 20
  Training: 16
  Testing: 4

Categories:
  astronomy: 4
  biology: 4
  geography: 4
  engineering: 4
  meteorology: 4
```

## Expected Output from `lab_research_pipeline.py`

The lab script produces:

1. **Initialization Output**
   - MultimodalDataLoader configuration
   - Data cleaning statistics
   - Split counts and categories

2. **Training Set Processing**
   - Batch-by-batch statistics for first 2 batches
   - Image shape, dtype, value range
   - Text batch contents
   - Per-image analysis

3. **Performance Metrics**
   - Total batches and samples
   - Total time
   - Time per batch
   - Samples per second

4. **Test Set Processing**
   - Same analysis for test split
   - Demonstrates non-shuffled iteration

5. **ML Framework Integration**
   - PyTorch connection pseudocode
   - TensorFlow connection pseudocode
   - Explanation of key differences

6. **Summary**
   - Module integration checklist
   - Pipeline features list
   - What students learned
   - Next steps

## Teaching Notes

### Key Learning Points

1. **Module Integration**
   - Shows how all 8 modules work together
   - Real-world pipeline architecture
   - Production-ready patterns

2. **Multimodal Data**
   - Text + images together
   - Manifest pattern for metadata
   - Scalable to any data type

3. **Generator Pattern**
   - Memory-efficient iteration
   - Lazy evaluation benefits
   - Perfect for large datasets

4. **ML Framework Connection**
   - NumPy → PyTorch (zero-copy)
   - NumPy → TensorFlow (direct conversion)
   - Shape conventions (channel-first vs channel-last)

### Discussion Topics

1. **Why use a manifest CSV?**
   - Separation of data and metadata
   - Easy filtering and splits
   - No file renaming needed
   - Supports complex metadata

2. **Why generators instead of loading all data?**
   - Memory efficiency
   - Handles datasets larger than RAM
   - On-demand computation
   - Better for I/O bound tasks

3. **Why normalize images to [0, 1]?**
   - Neural networks expect normalized inputs
   - Faster convergence during training
   - Numerical stability
   - Consistent preprocessing

4. **PyTorch vs TensorFlow differences?**
   - Channel ordering: (B,C,H,W) vs (B,H,W,C)
   - Tensor creation: zero-copy vs conversion
   - Ecosystem and tooling differences

### Extension Activities

1. **Add Data Augmentation**
   - Random flips: `cv2.flip()`
   - Random crops: array slicing
   - Color jitter: adjust HSV values
   - Show impact on training

2. **Implement Text Tokenization**
   - Split captions into words
   - Build vocabulary
   - Convert to integer indices
   - Add padding for batches

3. **Add Caching**
   - Cache preprocessed images
   - Time comparison cached vs uncached
   - Discuss trade-offs (speed vs space)

4. **Multi-GPU Data Loading**
   - Partition data across GPUs
   - Show PyTorch DataLoader `num_workers`
   - Discuss prefetching strategies

5. **Real Dataset Integration**
   - Use CIFAR-10 or similar
   - Create manifest from existing data
   - Compare synthetic vs real data loading

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'cv2'`

**Solution:**
```bash
pip install opencv-python
```

### Issue: Images not found

**Solution:**
```bash
python create_sample_data.py
```
Must run before the lab script.

### Issue: Slides not displaying correctly

**Solution:**
- Open in a modern browser (Chrome, Firefox, Safari, Edge)
- Check browser console for errors
- Ensure JavaScript is enabled

### Issue: Performance too slow

**Factors:**
- Image size (larger = slower)
- Batch size (larger = faster per-sample)
- Disk I/O (SSD vs HDD)
- CPU cores (OpenCV uses threading)

**Optimizations:**
- Reduce image size: `target_size=(128, 128)`
- Increase batch size: `batch_size=8`
- Add prefetching in production
- Use multiprocessing

## Assessment Rubric

### Code (70 points)

- **MultimodalDataLoader class** (25 pts)
  - Correct initialization
  - Generator pattern implementation
  - Proper error handling
  
- **Data processing** (25 pts)
  - Pandas for CSV reading
  - OpenCV for image loading
  - NumPy for batching
  - Data cleaning and validation

- **Integration** (20 pts)
  - All 8 modules used correctly
  - Clean code structure
  - Proper documentation

### Video Walkthrough (30 points)

- **Clarity** (10 pts)
  - Clear explanation of concepts
  - Good pacing and organization

- **Content** (15 pts)
  - Covers all required topics
  - Demonstrates understanding
  - Shows code execution

- **Technical** (5 pts)
  - Good audio/video quality
  - Screen clearly visible
  - 5-minute time limit

## Additional Resources

### Recommended Reading

- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [OpenCV Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [PyTorch Data Loading Tutorial](https://pytorch.org/tutorials/beginner/data_loading_tutorial.html)
- [TensorFlow Data Pipeline Guide](https://www.tensorflow.org/guide/data)

### Example Projects

Students can extend this work into:
- Image classification project
- Multimodal search engine
- Caption generation system
- Data augmentation library
- Custom dataset loader package

## Contact

For questions or issues with this module, contact the course instructor.

---

**Module 8** | AI Research Foundations | © mui-group
