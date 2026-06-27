# Module 8: Final Assignment
## The Research Pipeline — Your Capstone Project

**AI Research Foundations Minicourse**  
© Mui-Group

---

## Welcome to the Final Assignment

This is it — the capstone. Everything you have practiced in Modules 1 through 7 now comes together in one real, working project.

In this assignment you will build a **multimodal data pipeline**: a system that reads a dataset of images paired with text descriptions, cleans and filters the data, and hands out neat batches ready for a machine learning model to train on. "Multimodal" simply means the pipeline handles more than one kind of data at the same time — pictures *and* words, together.

You will not be building a toy demonstration. The pattern you implement here is the same one that powers large AI systems like CLIP, LLaVA, and GPT-4V. You are building a smaller, student-sized version of the real thing.

By the time you submit, you will have:

1. A working environment with all dependencies installed
2. A synthetic dataset of 20 images and a manifest CSV
3. A complete `MultimodalDataLoader` class that you built yourself
4. A filled-in `tutorial.ipynb` notebook with all cells run and outputs visible
5. A short video walkthrough explaining your code

---

## Before You Start: Read the Setup Guide

**Open `08_SETUP.pdf` first.** That document is your technical checklist. It tells you exactly what software to install, what commands to run, and what output to expect when everything is working correctly. Do not skip it — trying to work through the notebook without a functioning environment is frustrating and slow.

Here is a summary of what the setup guide covers, so you know what to expect:

### What `08_SETUP.pdf` covers

**1. Installing the dependencies**

The project uses four libraries. You install all of them with a single command run from inside the `08_capstone_pipeline/` folder:

```bash
pip install -e .
```

The `-e` flag means "editable install," which lets Python find the project files without you having to copy them anywhere. After this command, you should be able to `import numpy`, `import pandas`, and `import cv2` without errors.

**2. Generating the sample data**

The notebook needs a folder of images to work with. You create them by running:

```bash
python create_sample_data.py
```

This script generates 20 synthetic images — simple colored pictures, one per sample — and saves them into `data/images/`. It also creates `data/manifest.csv`, which is the index file that links each image to its text description and tells you whether it belongs to the training set or the test set. You will see a printout confirming each image was created, like this:

```
[ 1/20] Created astronomy_001.png (astronomy, train)
[ 2/20] Created astronomy_002.png (astronomy, train)
...
[20/20] Created meteorology_004.png (meteorology, test)

✓ Successfully generated 20 images in .../data/images
```

**3. Verifying that the lab script runs**

Once the data exists, run the lab script to confirm the full pipeline works end-to-end before you open the notebook:

```bash
python lab_research_pipeline.py
```

If this runs to completion without errors, your environment is ready. If it fails, `08_SETUP.pdf` has a Troubleshooting section that addresses the most common problems, including missing OpenCV, missing images, and slow performance.

> **Only once `lab_research_pipeline.py` runs cleanly should you open `tutorial.ipynb`.**

---

## The Notebook: `tutorial.ipynb`

The notebook is your main workspace. It walks you through the full pipeline in ten numbered sections, building up from scratch so you can see every moving part before they all connect at the end.

Open it with:

```bash
jupyter notebook tutorial.ipynb
```

Or if you are using JupyterLab:

```bash
jupyter lab tutorial.ipynb
```

### How the notebook is structured

Here is a map of all ten sections and what you will do in each one.

---

### Section 1 — Setup

The first cell imports all the libraries and prints their version numbers. Run it and make sure you see something like this:

```
✓ All libraries imported successfully
  NumPy version: 1.26.x
  Pandas version: 2.x.x
  OpenCV version: 4.8.x
```

If any import fails, go back to `08_SETUP.pdf` and re-run `pip install -e .`. A missing import at this stage will cause every later cell to fail.

---

### Section 2 — Recap of Skills

This section shows a diagram of how the eight modules connect. Each one feeds into the final pipeline. Read it carefully — it is the roadmap for everything that follows.

No code to write here. Just read and understand the flow:

```
Modules 1–2 (Python, generators)  ──┐
Modules 3–4 (NumPy arrays)          ├──► Module 8: The complete pipeline
Modules 5–6 (Pandas DataFrames)     │
Module  7   (OpenCV images)        ──┘
```

---

### Section 3 — The Multimodal Data Pattern

This section explains the **manifest** — the CSV file that is the heart of any multimodal dataset. A manifest is simply a table where each row represents one sample. Each row contains the filename of the image, the text caption that describes it, a category label, and a split label ("train" or "test").

Here is what the manifest looks like:

```csv
image_filename,caption,category,split
astronomy_001.png,Spiral galaxy with bright core,astronomy,train
biology_001.png,Human red blood cells under microscope,biology,train
geography_001.png,Mountain range with snow peaks,geography,train
meteorology_004.png,Storm front development,meteorology,test
```

The manifest matters because it keeps your metadata (text, labels, splits) completely separate from your images (the actual picture files). This means:

- You can filter and split your data by simply filtering rows of a table — no touching the image files.
- You can add or change captions without renaming or moving any images.
- The pattern scales to millions of samples without changing anything about how you use it.
- Famous real-world datasets like MS-COCO, ImageNet, and LAION all use exactly this pattern.

No code to write here. Read this section to understand *why* the manifest exists before you start building code that uses it.

---

### Section 4 — Creating Sample Data

This is the first section where you run code that **produces output on disk**. Work through it in the order the notebook presents — there are five clearly labeled stages, and each one teaches something useful.

**Stage 1: Make the folders**

```python
data_dir = Path("./data")
image_dir = data_dir / "images"
image_dir.mkdir(parents=True, exist_ok=True)
```

`Path` is the modern Python way to describe file locations. The `/` operator joins path segments, so `data_dir / "images"` produces `./data/images`. The `exist_ok=True` argument means "do not complain if this folder already exists," which makes the cell safe to run more than once.

**Stage 2: Paint one image as a grid of numbers**

Here you paint a single astronomy image by hand and look at it. This is the most important conceptual stage. An image is not a mysterious thing — it is a 3D NumPy array shaped `(Height, Width, Channels)`. Every pixel is three numbers between 0 and 255, representing how much Red, Green, and Blue it contains.

Run this cell and look at the output image. You should see a dark blue rectangle with small white dots — a simple synthetic night sky.

```python
demo_img = np.zeros((480, 640, 3), dtype=np.uint8)  # all-black canvas
demo_img[:, :] = [20, 20, 60]                        # paint a dark blue sky
# then scatter white star pixels...
```

**Stage 3, 4, and 5: Scale up to the full dataset**

The longer cell that follows wraps the Stage 2 idea in a loop. It paints all 20 images — one for each of the five categories (astronomy, biology, geography, engineering, meteorology), four images per category — and saves each one to disk. As it saves each image it also records one row of manifest information.

Pay attention to two details here:

- **Color conversion before saving.** OpenCV stores colors in Blue-Green-Red (BGR) order, not the standard Red-Green-Blue (RGB) that everything else uses. We build our arrays in RGB, so we must call `cv2.cvtColor(img, cv2.COLOR_RGB2BGR)` right before `cv2.imwrite`. If you forget this, the saved images will have their red and blue channels swapped.

- **The split rule.** The first three images in each category become "train" and the fourth becomes "test." This gives a clean 75/25 split across every category.

After this cell runs, check that `data/images/` contains 20 `.png` files and that `data/manifest.csv` exists.

---

### Section 5 — The Complete Pipeline Architecture

This section shows the full assembly-line diagram before you build it. Read it as a preview — you will implement each stage in Section 6.

```
CSV manifest
    │
    ▼
Pandas: read the CSV, filter by split, clean the captions
    │
    ▼
Generator: hand out one batch at a time (lazy — only loads what you need right now)
    │
    ├──────────────────────────────┐
    ▼                              ▼
OpenCV: load each image,      Text: collect the matching
  resize, BGR → RGB              captions into a list
    │                              │
    ▼                              │
NumPy: normalize pixels to         │
  [0.0, 1.0], stack images         │
  into one (B,H,W,C) array         │
    └──────────────────────────────┘
                │
                ▼
    Batch dictionary:
      image_batch  → NumPy array, shape (B, H, W, C)
      text_batch   → list of B caption strings
      metadata     → batch size, categories, filenames, split
```

The key idea is that the pipeline is **lazy**: the generator does not load all 20 images into memory at once. It loads one batch, yields it to you, waits until you ask for the next batch, and only then loads the next group. This is what makes the pattern scale — the same code works on 20 images or 20 million.

---

### Section 6 — Building the Pipeline Step by Step

This is the core building section. You run six cells, each implementing one stage of the pipeline.

**Step 1: Load the manifest with Pandas**

```python
df = pd.read_csv(manifest_path)
print(df.info())
```

`df.info()` is your first health check. It shows you how many rows there are, the name and data type of each column, and whether any values are missing. Get in the habit of running this every time you load a new dataset.

**Step 2: Filter by split**

```python
train_df = df[df['split'] == 'train'].copy()
```

The expression `df['split'] == 'train'` produces a column of `True` and `False` values, one per row. Passing it back into `df[...]` keeps only the rows where the value was `True`. The `.copy()` at the end creates an independent table so that later edits to `train_df` do not accidentally modify the original `df`.

**Step 3: Clean the text**

```python
train_df['caption'] = train_df['caption'].str.strip()
train_df['caption'] = train_df['caption'].str.replace(r'\s+', ' ', regex=True)
```

`.str.strip()` removes spaces from the start and end of each caption. `.str.replace(r'\s+', ' ', regex=True)` collapses any run of whitespace characters (spaces, tabs, newlines) into a single space. The `\s+` part is a regular expression meaning "one or more whitespace characters."

**Step 4: Load one image with OpenCV**

```python
img_bgr = cv2.imread(str(sample_path))
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
```

`cv2.imread` reads the file and gives you a NumPy array. The immediate `cv2.cvtColor` converts from BGR to RGB. Look at the output image — the colors should look natural. If sky looks orange, you have a BGR/RGB mismatch somewhere.

**Step 5: Resize and normalize**

```python
img_resized = cv2.resize(img_rgb, (224, 224))
img_normalized = img_resized.astype(np.float32) / 255.0
```

Every model expects its inputs to have the same shape, so we resize every image to 224 × 224. The division by 255 scales the pixel values from the range `[0, 255]` (integers) into `[0.0, 1.0]` (floats). Neural networks train faster and more reliably on this smaller range. The `.astype(np.float32)` converts the array to 32-bit floating point before the division.

**Step 6: Stack multiple images into a batch**

```python
image_batch = np.stack(image_batch_list, axis=0)
```

Each preprocessed image is a 3D array shaped `(224, 224, 3)`. Stacking four of them with `axis=0` inserts a new leading dimension and produces a single 4D array shaped `(4, 224, 224, 3)`. Read this as "4 images, each 224 pixels tall, 224 pixels wide, with 3 color channels." That `(B, H, W, C)` shape is the standard input format for most image models.

---

### Section 7 — The MultimodalDataLoader Class

After building the pipeline as loose steps, this section packages everything into a reusable class. Read the class definition carefully before you run it. Here is what each part does:

**`__init__`** — runs once when you create a loader. It saves your settings (batch size, image size, split, etc.) and immediately loads and cleans the manifest so it is ready.

**`_load_and_clean_manifest`** — a private helper (note the leading underscore) that does all the Pandas work: read the CSV, remove duplicates, drop rows with missing values, filter by split, clean the captions, and verify that every image file actually exists on disk. If no valid samples are found, it raises a clear error rather than failing silently later.

**`_load_and_preprocess_image`** — a private helper that does the OpenCV and NumPy work for a single image: read from disk, resize, convert BGR → RGB, normalize. It returns `None` if the image cannot be loaded, which lets the main loop skip bad files gracefully instead of crashing.

**`__len__`** — allows you to call `len(loader)` and get back the number of batches. This is convenient for progress reporting.

**`__iter__`** — the generator. This is the most important method. It shuffles the row indices if you requested it, then loops through them in groups of `batch_size`. For each group it calls `_load_and_preprocess_image` for each image, collects the results, stacks them with NumPy, and `yield`s the batch dictionary. Because it uses `yield` instead of `return`, execution pauses after each batch and only resumes when you ask for the next one. This is what keeps memory usage low.

Run the cell at the end of this section to define the class:

```python
print("✓ MultimodalDataLoader class defined")
```

You should see that confirmation message. If you see an error instead, read the traceback carefully — it will point to the specific line that is wrong.

---

### Section 8 — Using the DataLoader

This is where the payoff becomes visible. Creating and using a loader is now just a few lines:

```python
train_loader = MultimodalDataLoader(
    manifest_path=manifest_path,
    image_dir=image_dir,
    batch_size=4,
    target_size=(224, 224),
    split="train",
    shuffle=True,
    normalize=True
)

for batch in train_loader:
    images = batch['image_batch']   # NumPy array, shape (B, H, W, C)
    texts  = batch['text_batch']    # list of B caption strings
    meta   = batch['metadata']      # dict: batch_size, categories, filenames, split
```

Each key in the batch dictionary serves a purpose:

| Key | What it contains | Shape / Type |
|---|---|---|
| `image_batch` | The preprocessed images | `np.ndarray`, shape `(B, 224, 224, 3)`, dtype `float32`, values in `[0.0, 1.0]` |
| `text_batch` | The matching captions | `list` of `B` strings |
| `metadata` | Bookkeeping info | `dict` with keys `batch_size`, `categories`, `filenames`, `split` |

Run the visualization cell at the end of this section. It draws each image in the first batch with its caption underneath. If all four images look correct and the captions match their pictures, every stage of the pipeline worked.

---

### Section 9 — Performance Analysis

This section measures how fast your pipeline runs. The timing loop is simple:

```python
start_time = time.time()
for batch in train_loader:
    pass                       # we are only timing the pipeline, not doing training yet
elapsed = time.time() - start_time
```

After the loop, you compute time per batch and samples per second. Typical results on a laptop:

- About 0.15 seconds per batch
- About 27 samples per second

The pie chart in this section shows that image loading (the `cv2.imread` call) accounts for roughly 40 percent of the total time. That is the most important number to know if you ever need to speed things up — it tells you where to focus.

---

### Section 10 — Final Lab Tasks

This is the graded hands-on section. You complete three tasks that run the full pipeline end-to-end.

**Task 1: Process the training data**

Create a training loader with `batch_size=4` and `shuffle=True`, then loop through every batch and collect these statistics:

- Total number of batches processed
- Total number of samples processed
- Mean pixel value across all batches (should be around 0.4 to 0.6 for natural images)
- Standard deviation of pixel values (should be around 0.2 to 0.3)
- The complete set of categories seen

The starter code does most of this for you. Run it and read the output carefully. The numbers it prints are a quick sanity check: if the mean pixel value were 0.0, all the images would be black. If it were 1.0, they would all be white.

**Task 2: Process the test data**

Create a test loader with `batch_size=2` and `shuffle=False`, then loop through every batch and record the totals. Two things are different from the training loader, and both differences are intentional:

- `batch_size=2` — smaller, just to show you that batch size is a free parameter you control
- `shuffle=False` — test data is never shuffled because we want results to be reproducible

You should see 5 total test samples spread across 3 batches (two batches of 2 plus one batch of 1).

**Task 3: Compare the splits**

The final cell produces a grouped bar chart comparing train and test counts side by side. It then computes the percentage split. You should see roughly 75% train and 25% test — matching the "first three of every four" rule we used when we generated the data.

When all three tasks are done, every cell in the notebook should have been run and have visible output beneath it.

---

## Deliverables

Submit the following two items.

### 1. The completed notebook (`tutorial.ipynb`)

- Every cell must be run top-to-bottom, in order, without skipping any
- Every cell must have its output visible — do not clear the outputs before submitting
- The final three tasks in Section 10 must be complete with correct statistics printed

To confirm before submitting: use **Kernel → Restart & Run All** in Jupyter, then wait for every cell to finish. If the notebook runs cleanly from start to finish without errors, it is ready to submit.

### 2. A 5-minute video walkthrough

Record your screen while you explain the notebook. You do not need to re-run every cell on camera. Instead, scroll through the notebook and talk about what you built. Cover these five areas:

| Time | Topic | What to say |
|---|---|---|
| 0:00 – 1:00 | The manifest pattern | Show `manifest.csv`. Explain what each column means. Explain why keeping metadata in a table (rather than encoding it in filenames) makes the data easier to work with. |
| 1:00 – 2:30 | The class architecture | Show the `MultimodalDataLoader` class. Walk through `__init__`, `_load_and_clean_manifest`, `_load_and_preprocess_image`, and `__iter__`. Explain in your own words what each method does and why the generator pattern matters. |
| 2:30 – 3:30 | Batch generation | Show the output of the visualization cell in Section 8. Point out the batch shape `(B, H, W, C)`. Explain what each dimension means. |
| 3:30 – 4:30 | ML framework connection | Show the PyTorch and TensorFlow pseudocode in Section 9. Explain the one key difference: PyTorch expects `(B, C, H, W)` and needs `.permute(2, 0, 1)`, while TensorFlow expects `(B, H, W, C)` which is already what our pipeline produces. |
| 4:30 – 5:00 | Module integration recap | Point back at the table in Section 2 that maps each module to its role in the pipeline. Say one sentence about what you found most interesting or surprising. |

The video does not need to be polished. What matters is that you can explain the code in your own words.

---

## Grading Rubric

### Code: 70 points

| Area | Points | What we look for |
|---|---|---|
| **MultimodalDataLoader class** | 25 | Correct `__init__`, working generator in `__iter__`, proper use of `yield`, graceful handling of missing images |
| **Data processing** | 25 | Pandas for CSV reading and filtering, OpenCV with correct BGR→RGB conversion, NumPy for normalization and stacking, text cleaning applied |
| **Integration** | 20 | All 8 modules visibly used, clean notebook with all cells run, statistics computed correctly in Tasks 1–3 |

### Video Walkthrough: 30 points

| Area | Points | What we look for |
|---|---|---|
| **Clarity** | 10 | Can we follow your explanation? Do you use your own words rather than reading the comments? |
| **Content** | 15 | Did you cover all five required topics? Do you demonstrate that you understand what the code is doing, not just that you ran it? |
| **Technical quality** | 5 | Screen is readable, audio is clear, video is close to 5 minutes |

---

## Common Problems and How to Fix Them

**The notebook fails at the first import cell**

This means a library is missing. Go to your terminal, navigate to the `08_capstone_pipeline/` folder, and run:

```bash
pip install -e .
```

Then restart the Jupyter kernel and run the cell again.

---

**`ModuleNotFoundError: No module named 'cv2'`**

OpenCV has an unusual package name — the Python module is called `cv2` but the package you install is called `opencv-python`. Install it directly:

```bash
pip install opencv-python
```

---

**Images load as None / "Images not found" error**

You need to generate the images before running the notebook. Open a terminal in the `08_capstone_pipeline/` folder and run:

```bash
python create_sample_data.py
```

This only takes a few seconds and only needs to be done once.

---

**The image colors look wrong (reds appear blue, sky appears orange)**

This is a BGR versus RGB mismatch. OpenCV reads images in BGR order. You must convert to RGB before displaying or processing:

```python
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
```

Check every place you call `cv2.imread` and make sure you have the `cvtColor` call immediately after.

---

**`ValueError: No valid samples found for split 'train'`**

This usually means the manifest CSV does not exist yet, or the split column has a typo. Check that `data/manifest.csv` exists. If it does not, run `python create_sample_data.py` first. If it does exist, open it and verify the `split` column contains exactly the strings `train` and `test` (lowercase, no extra spaces).

---

**The notebook is slow**

Image loading is the bottleneck. Two quick fixes:

1. Reduce the target image size: change `target_size=(224, 224)` to `target_size=(128, 128)` — this makes each image four times smaller in memory and significantly faster to load.
2. Make sure you are running the script from a local drive, not a network drive or an external HDD.

---

**`Kernel died` message in Jupyter**

This usually means Python ran out of memory. Make sure you are not accidentally storing every image in a list before processing. The loader is designed to hold only one batch in memory at a time — if you are collecting all batches into a list before processing them, you have defeated the purpose of the generator pattern.

---

## Key Concepts to Review Before Submitting

If any of these feel unclear, re-read the corresponding section of the notebook before you record your video.

**What is a manifest?** A CSV file that acts as an index for a multimodal dataset. Each row has an image filename, a text caption, a category label, and a split label. It keeps metadata separate from the image files.

**What is a generator?** A Python function that uses `yield` instead of `return`. It pauses after each `yield`, waits until the caller asks for the next value, and only then resumes. This means it never holds more than one item in memory at a time.

**What does normalization do?** Divides pixel values by 255, scaling them from the integer range `[0, 255]` to the float range `[0.0, 1.0]`. Neural networks expect inputs in this range and train more reliably when they get it.

**What is the batch shape?** `(B, H, W, C)` — Batch size, Height, Width, Channels. For our default settings that is `(4, 224, 224, 3)`. This is the shape of the `image_batch` array you get from each iteration of the loader.

**Why does PyTorch need `.permute(2, 0, 1)`?** PyTorch expects channels first: `(B, C, H, W)`. Our pipeline produces channels last: `(B, H, W, C)`. The permute call reorders the dimensions to match what PyTorch expects. TensorFlow is already happy with channels last, so no permute is needed there.

---

## You Are Ready

If you have:
- ✓ Read `08_SETUP.pdf` and confirmed your environment works
- ✓ Run `python create_sample_data.py` to generate the dataset
- ✓ Opened `tutorial.ipynb` and worked through all ten sections
- ✓ Completed all three tasks in Section 10 with correct outputs
- ✓ Run **Kernel → Restart & Run All** as a final check

...then you are ready to record your video and submit.

This is the end of the AI Research Foundations Minicourse. You started with Python data structures and you finished by building a production-style machine learning data pipeline. The skills you practiced here are the same ones used by engineers at research labs around the world. Keep building.

---

*AI Research Foundations Minicourse — Module 8*  
*© Mui-Group*
