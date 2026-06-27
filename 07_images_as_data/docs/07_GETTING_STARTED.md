# Getting Started with Module 7: Images as Data

## Quick Start (3 Steps)

### 1. Install Dependencies
```bash
cd module_07_images_as_data
pip install -e .
```

### 2. Run the Lab
```bash
python lab_the_preprocessor.py
```

### 3. View the Slides
```bash
# macOS/Linux
open slides.html

# Windows
start slides.html

# Or just open slides.html in your browser
```

That's it! 🎉

---

## Detailed Setup Guide

### Prerequisites

Before starting, ensure you have:
- Python 3.10 or higher
- pip (Python package manager)
- A terminal/command prompt
- A web browser (for slides)

#### Check Your Python Version
```bash
python --version
# Should show: Python 3.10.x or higher
```

If you see Python 2.x or 3.9 or lower, you need to upgrade:
- **macOS**: `brew install python@3.10`
- **Windows**: Download from [python.org](https://www.python.org/downloads/)
- **Linux**: `sudo apt install python3.10` (Ubuntu/Debian)

### Installation

#### Step 1: Navigate to Module Directory
```bash
cd /path/to/agent-tutorials/topics/data_foundations/module_07_images_as_data
```

#### Step 2: (Optional) Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

#### Step 3: Install Dependencies
```bash
pip install -e .
```

This installs:
- `numpy` (numerical computing)
- `opencv-python` (image processing)
- `python-dotenv` (environment variables)

#### Step 4: Verify Installation
```bash
python test_module.py
```

You should see:
```
✓ NumPy                        - OK
✓ OpenCV (opencv-python)       - OK
✓ python-dotenv                - OK
✓ All dependencies available
✓ Module 7 is ready!
```

### Running the Lab

#### Option 1: Full Lab Experience
```bash
python lab_the_preprocessor.py
```

This will:
1. Generate 8 sample images (if not already present)
2. Demonstrate single image preprocessing
3. Show BGR→RGB conversion
4. Demonstrate resizing
5. Show normalization
6. Process a full batch
7. Analyze memory usage

**Expected output**: Detailed, color-coded walkthrough with statistics

**Duration**: ~5 seconds

#### Option 2: Just Generate Sample Images
```bash
python create_sample_images.py
```

This creates 8 synthetic images in `data/images/`:
- Different sizes (240×320 to 640×480)
- Different patterns (gradients, noise, shapes)
- Different colors (RGB combinations)

#### Option 3: Explore the Code
Open the files in your favorite editor:
```bash
# VS Code
code .

# PyCharm
pycharm .

# Vim
vim lab_the_preprocessor.py
```

### Viewing the Slides

#### Open in Browser
```bash
# macOS
open slides.html

# Linux
xdg-open slides.html

# Windows
start slides.html
```

#### Navigation
- **Arrow Right / Space**: Next slide
- **Arrow Left**: Previous slide
- **Home**: First slide
- **End**: Last slide
- **Click**: Right half = next, left half = previous
- **Touch**: Swipe left/right on mobile

#### Presentation Tips
- Use fullscreen (F11 in most browsers)
- Works offline (no internet needed)
- Self-contained (no external dependencies)
- Responsive (works on phones/tablets)

### Troubleshooting

#### Problem: `pip: command not found`
**Solution**: Install pip
```bash
# macOS/Linux
python -m ensurepip --upgrade

# Windows
python -m ensurepip --upgrade
```

#### Problem: `ModuleNotFoundError: No module named 'cv2'`
**Solution**: OpenCV not installed
```bash
pip install opencv-python
```

#### Problem: `ImportError: No module named 'numpy'`
**Solution**: NumPy not installed
```bash
pip install numpy
```

#### Problem: Permission denied during pip install
**Solution**: Use user install flag
```bash
pip install --user -e .
```

#### Problem: Lab fails with "No images found"
**Solution**: Generate sample images first
```bash
python create_sample_images.py
```

#### Problem: Python 2.x is being used
**Solution**: Use `python3` explicitly
```bash
python3 --version
python3 -m pip install -e .
python3 lab_the_preprocessor.py
```

#### Problem: Slides don't display correctly
**Solution**: Try a different browser
- Chrome/Edge (Recommended)
- Firefox
- Safari
- Avoid Internet Explorer

#### Problem: Visual artifacts or slow performance
**Solution**: Close other applications, use hardware acceleration in browser

### Directory Structure

After installation, you should see:
```
module_07_images_as_data/
├── .env.example              # Environment template (empty)
├── create_sample_images.py   # Generate synthetic images
├── data/
│   └── images/              # Sample images (auto-generated)
│       ├── sample_01_red_gradient.jpg
│       ├── sample_02_blue_green_diagonal.jpg
│       └── ... (8 images total)
├── lab_the_preprocessor.py   # Main lab script
├── MODULE_SUMMARY.md         # Build documentation
├── pyproject.toml           # Project configuration
├── QUICK_REFERENCE.md       # Cheat sheet
├── README.md                # Full documentation
├── slides.html              # Interactive presentation
├── test_module.py           # Setup validation
└── GETTING_STARTED.md       # This file
```

### What to Do After Setup

#### 1. Read the README
```bash
cat README.md
# or open in editor
```

#### 2. Review the Quick Reference
```bash
cat QUICK_REFERENCE.md
```

#### 3. Watch the Slides
- Open `slides.html` in browser
- Go through all 15 slides
- Understand concepts before coding

#### 4. Run the Lab
```bash
python lab_the_preprocessor.py
```

#### 5. Experiment
- Modify `lab_the_preprocessor.py`
- Try different target sizes
- Add your own images to `data/images/`
- Calculate memory for different batch sizes

### Learning Path

Follow this sequence:

1. **Conceptual** (30 min)
   - Review slides
   - Read README
   - Understand theory

2. **Hands-on** (30 min)
   - Run lab
   - Observe output
   - Read code comments

3. **Practice** (1 hour)
   - Modify target size
   - Process your own images
   - Experiment with batch sizes

4. **Apply** (1+ hours)
   - Build image classifier
   - Create augmentation pipeline
   - Optimize for production

### Resources

#### Module Files
- `README.md` - Comprehensive guide
- `QUICK_REFERENCE.md` - One-page cheat sheet
- `MODULE_SUMMARY.md` - Build documentation
- `slides.html` - Visual presentation

#### External Resources
- [OpenCV Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [ImageNet Dataset](https://www.image-net.org/)
- [Deep Learning Book - Chapter 9](https://www.deeplearningbook.org/contents/convnets.html)

### Getting Help

#### Check Existing Resources
1. Read error message carefully
2. Check README troubleshooting section
3. Review QUICK_REFERENCE.md
4. Re-run test_module.py

#### Debug Steps
1. Verify Python version (`python --version`)
2. Check dependencies (`pip list`)
3. Validate file structure (`ls -la`)
4. Run test script (`python test_module.py`)

#### Common Solutions
- Reinstall dependencies: `pip install --force-reinstall -e .`
- Clear cache: `pip cache purge`
- Use clean virtual environment
- Check Python path: `which python`

### Next Steps

After completing Module 7:

1. ✓ **Understand images as data** - Arrays and dimensions
2. ✓ **Master preprocessing** - Load, convert, resize, normalize
3. ✓ **Process batches** - Efficient multi-image handling

**Move on to**:
- Module 8: Text as Data
- Module 9: Working with APIs
- Module 10: Feature Extraction

**Or explore further**:
- Data augmentation techniques
- Real dataset processing (CIFAR-10, ImageNet)
- Building image classifiers
- Transfer learning with pretrained models

### Quick Commands Reference

```bash
# Setup
pip install -e .

# Run lab
python lab_the_preprocessor.py

# Generate images
python create_sample_images.py

# Test setup
python test_module.py

# View slides
open slides.html

# Activate virtual environment (if created)
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Deactivate virtual environment
deactivate
```

---

## Success Checklist

Before moving to the next module, ensure you can:

- [ ] Install dependencies without errors
- [ ] Generate sample images
- [ ] Run the complete lab
- [ ] Explain image array shape (H, W, C)
- [ ] Convert BGR to RGB
- [ ] Resize images to target dimensions
- [ ] Normalize pixel values to 0-1
- [ ] Create batches with shape (N, H, W, C)
- [ ] Calculate memory requirements
- [ ] Navigate the slides
- [ ] Apply pipeline to new images

If you can check all boxes, you're ready to proceed! 🚀

---

**Need help?** Re-run `python test_module.py` to diagnose issues.

**Ready to go?** Run `python lab_the_preprocessor.py` to start learning!
