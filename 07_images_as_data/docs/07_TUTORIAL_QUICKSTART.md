# Quick Start: Module 7 Tutorial

## ▶️ Run in Google Colab (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/philmui/ai-foundations/blob/main/07_images_as_data/tutorial.ipynb)

1. Click the **Open in Colab** badge above (or upload `tutorial.ipynb` via **File → Upload notebook** at colab.research.google.com).
2. Run the **first code cell** — it installs all dependencies into the Colab kernel. No `pip install`, `uv sync`, or `pyproject.toml` needed.
3. Run the rest top-to-bottom via **Runtime → Run all**.

The notebook is fully self-contained — any data it uses is generated inside the notebook, so it runs end-to-end with no external files.

<details><summary>Advanced: run locally</summary>

Prefer local Jupyter/VS Code? Install the dependencies and launch the notebook:

```bash
pip install numpy opencv-python matplotlib python-dotenv
jupyter notebook tutorial.ipynb
```

Then run **Cell → Run All** (or **Shift+Enter** for each cell). The notebook generates its own sample images.

</details>

That's it! 🎉

---

## What You'll Learn

✅ Images as 3D NumPy arrays  
✅ Loading images with OpenCV  
✅ BGR vs RGB color conversion  
✅ Resizing to standard dimensions  
✅ Pixel normalization (0-1 range)  
✅ Batch processing for neural networks  
✅ Memory management strategies  

**Time**: 60-90 minutes

---

## Tutorial Structure

```
Section 1: Introduction → Images as numbers
Section 2: Pixels and Arrays → Grayscale vs RGB
Section 3: Loading Images → Using cv2.imread()
Section 4: BGR vs RGB → The OpenCV quirk
Section 5: Resizing → Standard 224×224 size
Section 6: Normalization → 0-255 to 0.0-1.0
Section 7: Batch Processing → Creating 4D arrays
Section 8: Memory → Calculating requirements
Section 9: Lab Exercises → Hands-on practice
```

---

## Key Visualizations

The tutorial includes:
- 📊 Synthetic image generation
- 🎨 RGB channel separation
- 🔄 Before/after comparisons
- 📈 Pixel value histograms
- 🖼️ Batch array grids
- 🔀 Mermaid pipeline diagrams

---

## Exercises Included

1. **Different Image Sizes** - Memory comparison
2. **Channel Statistics** - Per-channel analysis
3. **Advanced Normalization** - ImageNet-style
4. **Memory Calculator** - Batch size optimization

---

## Prerequisites

- Python 3.10+
- Basic NumPy knowledge
- Module 6 completed (recommended)

---

## Need Help?

- **Setup issues**: Check `GETTING_STARTED.md`
- **Detailed guide**: Read `TUTORIAL_GUIDE.md`
- **Dependencies failing (Colab)**: Re-run the first code cell; use **Runtime → Restart and run all**
- **Dependencies failing (local)**: Run `python test_module.py`; install Jupyter with `pip install jupyter`

---

## Complete Preprocessing Pipeline

After this tutorial, you'll be able to write:

```python
import cv2
import numpy as np

def preprocess_image(path):
    # Load → BGR2RGB → Resize → Normalize
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img.astype(np.float32) / 255.0
    return img

# Create batch
images = [preprocess_image(p) for p in image_paths]
batch = np.stack(images, axis=0)  # Shape: (N, 224, 224, 3)
```

---

**Ready to start?** Click the **Open in Colab** badge above and **Runtime → Run all** now! 🚀
