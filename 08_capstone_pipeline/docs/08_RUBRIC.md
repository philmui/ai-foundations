# Module 8: Grading Rubric
## The Research Pipeline — Final Assignment

**AI Research Foundations Minicourse**  
© Mui-Group

---

## How This Assignment Is Graded

This assignment is graded primarily on **completion**. If you followed the instructions in `08_FINAL_ASSIGNMENT.pdf`, worked through the notebook honestly, and recorded a short video explaining what you built, you will receive full marks. There are no trick questions and no hidden gotchas.

The two deliverables are the completed notebook and the video walkthrough. Together they are worth 100 points.

---

## Notebook: 70 points

### Did you run the notebook? (40 points)

This is the most important question. Open the submitted notebook and scroll from top to bottom. Every cell should have a visible output beneath it.

| Check | Points |
|---|---|
| All cells have been run and have output visible | 20 |
| No cells show an error as their final output | 10 |
| Notebook runs cleanly top-to-bottom via Kernel → Restart & Run All | 10 |

A notebook where every cell ran and every cell produced *some* output gets full marks here, even if the numbers are slightly different from the expected values. A notebook with skipped cells or unexplained errors loses points proportionally.

---

### Did you complete the three lab tasks? (30 points)

Section 10 of the notebook has three required tasks. Each one is worth 10 points and is graded on completion — if the cell ran and printed reasonable output, it is complete.

| Task | What to check | Points |
|---|---|---|
| **Task 1 — Training data** | Statistics are printed: total batches, total samples, mean pixel value, categories seen | 10 |
| **Task 2 — Test data** | Statistics are printed: total batches, total samples for the test split | 10 |
| **Task 3 — Comparison chart** | The grouped bar chart renders and the percentage split is printed beneath it | 10 |

Each task is all-or-nothing at the 10-point level, with one small allowance: if a task cell shows a minor error but the student clearly made a genuine attempt (partial output is visible, or a comment explains the issue), award 5 points instead of 0.

---

## Video Walkthrough: 30 points

### Did you record a video? (10 points)

| Check | Points |
|---|---|
| A video file was submitted | 5 |
| The video shows a screen recording of the notebook | 5 |

---

### Did you cover the five required topics? (20 points)

Each topic is worth 4 points. The student earns the 4 points by mentioning the topic at all, and earns the full 4 points with a clear explanation. A brief mention that shows awareness earns 2–3 points. A topic that is skipped entirely earns 0.

| Topic | Full marks look like | Points |
|---|---|---|
| **1. The manifest pattern** | Student shows `manifest.csv`, explains that each row is one image+caption pair, and says why keeping metadata in a table is useful | 4 |
| **2. The class architecture** | Student scrolls through the `MultimodalDataLoader` class and mentions what `__init__`, `__iter__`, and at least one private helper method does | 4 |
| **3. Batch generation** | Student points to a batch output and explains the `(B, H, W, C)` shape — what each letter stands for | 4 |
| **4. ML framework connection** | Student mentions the PyTorch or TensorFlow pseudocode and explains at least one difference between the two (e.g. the `.permute` step for PyTorch) | 4 |
| **5. Module integration** | Student connects at least two earlier modules to their role in the pipeline (e.g. "Pandas from Module 5 reads the CSV") | 4 |

The video does not need to be polished. A student recording themselves talking while scrolling through the notebook at a table earns full marks as long as the five topics are covered.

---

## Summary Table

| Section | Max Points | Graded On |
|---|---|---|
| All cells run with output | 20 | Completion |
| No errors as final outputs | 10 | Completion |
| Notebook reruns cleanly | 10 | Completion |
| Task 1: Training stats | 10 | Completion |
| Task 2: Test stats | 10 | Completion |
| Task 3: Comparison chart | 10 | Completion |
| Video submitted | 10 | Completion |
| Five topics covered | 20 | Completion + brief explanation |
| **Total** | **100** | |

---

## Grade Bands

| Score | Grade |
|---|---|
| 90 – 100 | A — Full completion, clear video |
| 75 – 89 | B — Mostly complete, minor gaps |
| 60 – 74 | C — Partial completion or video missing |
| Below 60 | Incomplete — please resubmit |

---

## A Note to Students

The goal of this assignment is for you to prove to yourself — and to us — that you can take the skills from eight modules and connect them into something real. If your notebook runs and you can talk through what you built, you have done exactly that. Do not let perfect be the enemy of done.

If something in the notebook is not working and you have genuinely tried to fix it, write a short comment in the affected cell explaining what you tried and what happened. Showing us your debugging process earns partial credit and is far better than leaving the cell blank.

---

*AI Research Foundations Minicourse — Module 8*  
*© Mui-Group*
