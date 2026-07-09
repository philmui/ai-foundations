# templated syllabus

**ASDRP Summer 2026 Mini-Course**

**Course Syllabus**

**1\. Course Information**

| Course Title | *AI Research Foundations: Data Engineering & Representation* |
| :---- | :---- |
| **Faculty Instructor** | *Phil Mui* |
| **Instructor Email** | *phil.mui@asdrp.org* |
| **Research Group** **Affiliation** | *Mui Group*  |
| **Block Assignment** | *Block 1* |
| **Day & Time** | *Monday, Friday 5-6pm* |
| **Format** | *Zoom* |
| **Location / Zoom Link** | *(will send to student)* |
| **Enrollment Cap** | *No cap* |

**2\. Course Description**

Before a student can build a Transformer or fine-tune a Large Language Model (LLM), they must master the “guts” of AI: how data is represented, stored, and manipulated mathematically. This course moves beyond basic scripting to teach the Vectorization, Data Structuring, and Preprocessing techniques used in actual research labs. We will focus on the “Why” and “How” of data pipelines—using Python Data Structures for efficiency, NumPy for matrix math (the language of LLMs), Pandas for dataset curation, and OpenCV for understanding high-dimensional input (visual data). Ideal for high school students with basic Python knowledge who want to understand how AI systems are built from the ground up.

**3\. Learning Outcomes**

*By the end of this course, students will be able to… *

1. Use advanced Python data structures (lists, dictionaries, generators) for efficient, memory-conscious AI data processing.  
2. Apply NumPy for vectorized matrix operations—including broadcasting and the dot product—to build core neural network components without for loops.  
3. Clean, curate, and transform real-world datasets using Pandas to produce train/test splits ready for machine learning model training.  
4. Process and normalize image data using OpenCV and represent it as numerical NumPy arrays suitable for computer vision models.  
5. Construct a complete multimodal research-grade data pipeline integrating Python, NumPy, Pandas, and OpenCV—mimicking the workflow of an ML engineer.

**4\. Cross-Group Relevance**

Data engineering and numerical representation are foundational skills applicable across every quantitative research group at ASDRP. Students in biology, chemistry, physics, environmental science, and the social sciences increasingly work with large structured datasets, tabular records, and imaging data. This course’s coverage of Pandas (dataset curation), NumPy (mathematical arrays), and OpenCV (image arrays) directly supports data-heavy projects in any domain—from genomics workflows and materials characterization to satellite image analysis. By grounding every concept in AI/ML research context, this course also prepares students to collaborate on interdisciplinary computational projects and to understand the data infrastructure behind modern scientific tools.

**5\. Module-by-Module Schedule**

| 1 | Module Title: *The Architecture of Data (Lists, Dicts, & Complexity)* Learning Objectives: Explain static and runtime analyses in Python; distinguish mutable from immutable objects and their memory implications; build a tokenizer dictionary using optimized data structures. Topics Covered: Deep dive into Python built-in data structures (lists, dictionaries); mutable vs. immutable memory references; nested dictionaries for JSON data (e.g., OpenAI API responses); introduction to Big O notation for AI scalability. Student Work / Assessment: Lab — Building a “Tokenizer” Dictionary: students construct a word frequency-counter for a text corpus using optimized dictionary lookups, simulating how LLMs map words to token IDs. Pre-Reading / Materials: *Google Edu Python Class; DeepLearning.AI “AI Python for Beginners”* |
| :---: | :---- |

| 2 | Module Title: *Pythonic Patterns for AI (Comprehensions & Generators)* Learning Objectives: Write clean, vectorized-ready Python code; use list and dict comprehensions to condense data-cleaning logic; implement generator functions for memory-efficient data streaming. Topics Covered: List & dict comprehensions; generator functions with yield; lazy evaluation; building memory-efficient data streams as a direct precursor to PyTorch DataLoaders. Student Work / Assessment: Lab — The Infinite Data Loader: create a generator function that streams lines from a large mock text file without loading it entirely into RAM. Pre-Reading / Materials: *Google Edu Python Class; DeepLearning.AI “AI Python for Beginners”* |
| :---: | :---- |

| 3 | Module Title: *Thinking in Arrays (Tensors)* Learning Objectives: Create and manipulate NumPy N-dimensional arrays; interpret .shape and array dimensions; convert tokenizer output into a numerical one-hot encoded matrix. Topics Covered: Introduction to the N-dimensional array (ndarray); creating arrays from lists, zeros, ones, and ranges; .shape property; Rank-1 vs Rank-2 arrays; one-hot encoding as a representation technique. Student Work / Assessment: Lab — The Matrix: convert the tokenizer dictionary output from Session 1 into a numerical one-hot encoded NumPy matrix. Pre-Reading / Materials: *W3Schools NumPy Tutorial; MIT 6.036 Linear Algebra context* |
| :---: | :---- |

| 4 | Module Title: *Vectorization & Broadcasting* Learning Objectives: Perform mathematical operations on arrays without for loops; apply NumPy broadcasting rules; manually compute a neural network forward pass using matrix operations. Topics Covered: Element-wise operations (addition, multiplication, scalar math); the dot product and matrix multiplication (np.dot / @); broadcasting—allowing arrays of different shapes to interact mathematically. Student Work / Assessment: Lab — The Forward Pass: manually code a single artificial neuron calculation (Weights × Inputs \+ Bias) using NumPy broadcasting, writing zero for loops. Pre-Reading / Materials: *W3Schools NumPy Tutorial; MIT 6.036 Linear Algebra context* |
| :---: | :---- |

| 5 | Module Title: *DataFrames & Series* Learning Objectives: Load and inspect structured datasets with Pandas; use .head(), .info(), and .describe() to understand data distributions; identify column types in a real AI dataset. Topics Covered: Structured data manipulation; loading CSV/JSON files into DataFrames; inspection methods (.head(), .info(), .describe()); treating data like a programmable Excel spreadsheet. Student Work / Assessment: Lab — Dataset Detective: analyze a raw “LLM Prompt-Response” dataset, identify column types, and summarize statistical distributions. Pre-Reading / Materials: *W3Schools Pandas Tutorial* |
| :---: | :---- |

| 6 | Module Title: *Cleaning & Transformation* Learning Objectives: Preprocess datasets to remove missing values, duplicates, and formatting errors; apply boolean indexing to filter low-quality data; export clean train and test CSV splits. Topics Covered: Boolean indexing for data filtering; handling missing values with dropna() vs fillna(); duplicate removal; data formatting corrections; exporting processed datasets. Student Work / Assessment: Lab — The Curator: take a “dirty” dataset containing missing values, duplicates, and formatting errors; write a cleaning pipeline; export a pristine Train.csv and Test.csv. Pre-Reading / Materials: *W3Schools Pandas Tutorial* |
| :---: | :---- |

| 7 | Module Title: *Images as Data (OpenCV)*  Learning Objectives: Load images as 3D NumPy arrays; convert between BGR and RGB color spaces; resize images to a fixed resolution; normalize pixel values from 0–255 to 0–1 for model convergence. Topics Covered: Computer vision fundamentals for ML; cv2.imread and color space conversion (BGR to RGB); image resizing; pixel normalization; understanding images as (Height × Width × Channels) arrays. Student Work / Assessment: Lab — The Preprocessor: write a script that loads a folder of random images, resizes all to 224×224, and converts them to normalized NumPy arrays. Pre-Reading / Materials: *MIT 6.036 Machine Learning Data; OpenCV Official Documentation* |
| :---: | :---- |

| 8 | Module Title: *Capstone — The Research Pipeline*  Learning Objectives: Integrate Python, NumPy, Pandas, and OpenCV into a single multimodal data pipeline; build a Multimodal Data Loader producing batched text and image arrays; present and explain code via a recorded walkthrough. Topics Covered: Multimodal data loading (text \+ images); Pandas for reading CSVs with image filenames and text descriptions; OpenCV for loading and processing images; NumPy for batching; preview of PyTorch/TensorFlow integration. Student Work / Assessment: Final Project: a pipeline script yielding {image\_batch: np\_array, text\_batch: list\_of\_strings} \+ a short video walkthrough (Loom/Zoom recording) explaining the data pipeline code. Pre-Reading / Materials: *MIT 6.036 Machine Learning Data; OpenCV Official Documentation* |
| :---: | :---- |

# detailed syllabus

# **Mini-Course: AI Research Foundations**

**Course Title:** AI Research Foundations: Data Engineering & Representation

**Duration:** 4 Weeks (Summer Block)

**Frequency:** 2 Sessions/Week (8 Sessions Total)

**Target Audience:** High School Students with basic Python syntax knowledge (loops, variables, functions) interested in AI/ML Research.

## **Course Overview**

Before a student can build a Transformer or fine-tune a Large Language Model (LLM), they must master the "guts" of AI: how data is represented, stored, and manipulated mathematically. This course moves beyond basic scripting to teach the **Vectorization**, **Data Structuring**, and **Preprocessing** techniques used in actual research labs.

We will focus on the "Why" and "How" of data pipelines—using **Python Data Structures** for efficiency, **NumPy** for matrix math (the language of LLMs), **Pandas** for dataset curation, and **OpenCV** for understanding high-dimensional input (visual data).

---

## **Weekly Schedule & Syllabus**

### **Week 1: Advanced Python & Efficient Data Structures**

**Goal:** Transition students from writing "code that works" to "code that scales." We focus on memory management and structural choices essential for handling large datasets.

*Reference Materials: Google Edu Python Class, DeepLearning.AI "AI Python for Beginners"*

#### **Session 1: The Architecture of Data (Lists, Dicts, & Complexity)**

* **Topic:** Deep dive into Python’s built-in data structures.  
* **Concept:** Why looking up data in a List is $O(n)$ while a Dictionary is $O(1)$, and why that matters when processing 1 million tokens for an LLM.  
* **Key Activities:**  
  * **Mutable vs. Immutable:** Understanding memory references (crucial for PyTorch/TensorFlow debugging later).  
  * **Dictionary Manipulations:** Nested dictionaries for JSON data (common in OpenAI API responses).  
  * **Lab:** *Building a "Tokenizer" Dictionary.* Students will build a simple frequency-counter for a text corpus using optimized dictionary lookups, simulating how LLMs map words to IDs.

#### **Session 2: Pythonic Patterns for AI (Comprehensions & Generators)**

* **Topic:** Writing clean, vectorized-ready code.  
* **Concept:** Moving away from for loops towards list comprehensions and generators to handle data streams that don't fit in RAM.  
* **Key Activities:**  
  * **List & Dict Comprehensions:** condensing data cleaning logic into single, readable lines.  
  * **Generators (yield):** Introduction to lazy evaluation.  
  * **Lab:** *The Infinite Data Loader.* Create a generator function that streams lines from a massive mock text file without crashing memory—a direct precursor to PyTorch DataLoaders.

---

### **Week 2: The Math Engine (NumPy)**

**Goal:** Understanding that all AI data—text, images, audio—is just matrices of numbers.

*Reference Materials: W3Schools NumPy, MIT 6.036 (Linear Algebra context)*

#### **Session 3: Thinking in Arrays (Tensors)**

* **Topic:** Introduction to the N-dimensional array (ndarray).  
* **Concept:** Why Python lists are too slow for AI and how NumPy stores data contiguously in memory.  
* **Key Activities:**  
  * **Creating Arrays:** From lists, zeros, ones, and ranges.  
  * **Dimensions & Shapes:** Understanding .shape (Rank-1 vs Rank-2 arrays), a common source of bugs in AI research.  
  * **Lab:** *The Matrix.* converting the "Tokenizer" output from Session 1 into a numerical "One-Hot Encoded" matrix.

#### **Session 4: Vectorization & Broadcasting**

* **Topic:** Performing math without loops.  
* **Concept:** **Broadcasting**—the magic that allows arrays of different shapes to interact mathematically. This is the fundamental operation inside a Neural Network neuron.  
* **Key Activities:**  
  * **Element-wise Operations:** Addition, multiplication, and scalar math.  
  * **The Dot Product:** Understanding matrix multiplication (np.dot / @).  
  * **Lab:** *The Forward Pass.* Students will manually code a single "Artificial Neuron" calculation using NumPy broadcasting (Weights $\\times$ Inputs \+ Bias) without writing a single for loop.

---

### **Week 3: Data Curation (Pandas)**

**Goal:** Real-world data is messy. Students learn to clean and organize datasets (like CSVs of text or metadata) to prepare them for training.

*Reference Materials: W3Schools Pandas*

#### **Session 5: DataFrames & Series**

* **Topic:** Structured data manipulation.  
* **Concept:** Treating data like a programmable Excel sheet.  
* **Key Activities:**  
  * **Loading Data:** Reading CSV/JSON files.  
  * **Inspection:** Using .head(), .info(), and .describe() to understand statistical distribution.  
  * **Lab:** *Dataset Detective.* Analyze a raw "LLM Prompt-Response" dataset. Identify column types and view sample data.

#### **Session 6: Cleaning & Transformation**

* **Topic:** Preprocessing data for models.  
* **Concept:** AI models crash on empty values (NaN). How do we fix them?  
* **Key Activities:**  
  * **Filtering:** Boolean indexing to remove low-quality data.  
  * **Handling Missing Data:** dropna() vs fillna().  
  * **Lab:** *The Curator.* Students take a "dirty" dataset (containing missing values, duplicates, and formatting errors), write a cleaning pipeline, and export a pristine "Train.csv" and "Test.csv".

---

### **Week 4: Vision & Synthesis (OpenCV \+ Integration)**

**Goal:** Handling high-dimensional unstructured data (Images) and combining all skills into a research-grade data pipeline.

*Reference Materials: MIT 6.036 (Machine Learning Data), OpenCV Documentation*

#### **Session 7: Images as Data (OpenCV)**

* **Topic:** Computer Vision fundamentals for Machine Learning.  
* **Concept:** An image is just a 3D NumPy array (Height, Width, Color Channels).  
* **Key Activities:**  
  * **Loading & Color Spaces:** cv2.imread, converting BGR (OpenCV default) to RGB (ML standard).  
  * **Resizing & Normalization:** Rescaling pixel values from 0-255 to 0-1 (crucial for model convergence).  
  * **Lab:** *The Preprocessor.* Write a script that loads a folder of random images, resizes them all to a fixed square (e.g., 224x224), and converts them to normalized NumPy arrays.

#### **Session 8: Capstone \- The Research Pipeline**

* **Topic:** Integration of Python, NumPy, Pandas, and OpenCV.  
* **Concept:** Building a "Multimodal Data Loader." In modern research (like Gemini or GPT-4V), we feed the model both text and images.  
* **Key Activities:**  
  * **Synthesis:** Use **Pandas** to read a CSV containing image filenames and text descriptions. Use **OpenCV** to load/process the images based on the filenames. Use **NumPy** to batch them together.  
  * **Final Output:** A script that yields a dictionary: {'image\_batch': np\_array, 'text\_batch': list\_of\_strings}.  
  * **Planning:** Discussion on how these batches would be fed into a PyTorch/TensorFlow loop (preview of future courses).

---

## **Logistic Details for Canvas Setup**

* **Prerequisites Check:** A self-graded quiz will be deployed on Canvas prior to Day 1 to ensure students are comfortable with basic Python variables and loops.  
* **Software Requirements:**  
  * **Google Colab (recommended):** each module's `tutorial.ipynb` is self-contained — open it via the **Open in Colab** badge, run the first code cell to install all dependencies into the kernel, then **Runtime → Run all**. No separate install or data download is required.  
  * Local Python installation (optional): Python 3.9+, Anaconda distribution.  
* **Submission Format:**  
  * All labs will be submitted as .ipynb (Jupyter Notebooks) via Canvas.  
  * Final Project (Session 8\) requires a short video walkthrough (Loom/Zoom recording) explaining their data pipeline code.

## **Why This Approach?**

1. **Relevance:** We replace generic "learn to code" examples with AI-specific context (e.g., instead of "counting apples," we "count tokens").  
2. **Rigor:** By introducing **Big O notation** (Session 1\) and **Broadcasting** (Session 4), we treat the students as junior researchers, not just coders.  
3. **Synthesis:** The course culminates in a pipeline that combines all four tools, mimicking the actual workflow of an ML Engineer.