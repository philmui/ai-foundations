#!/usr/bin/env python3
"""
Module 8: Capstone - The Research Pipeline
A comprehensive multimodal data pipeline integrating all previous modules.

This script demonstrates:
- Module 1: Environment setup and configuration
- Module 2: Generator patterns for efficient data loading
- Module 3-4: NumPy array operations and vectorization
- Module 5: Pandas for CSV reading and data management
- Module 6: Data cleaning and transformation techniques
- Module 7: OpenCV for image loading and preprocessing

The result is a production-ready multimodal data loader that yields
batches of images and text ready for machine learning.
"""

import os
import time
from pathlib import Path
from typing import Iterator, Dict, List, Tuple, Optional

import numpy as np
import pandas as pd
import cv2

# Module 1: Environment setup
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


class MultimodalDataLoader:
    """
    A production-ready multimodal data loader that processes images and text together.

    This class integrates techniques from all 8 modules:
    - Generator pattern for memory-efficient iteration
    - NumPy for array operations and batching
    - Pandas for manifest reading and filtering
    - OpenCV for image loading and preprocessing
    - Data cleaning and validation

    Architecture:
        Manifest CSV → Pandas (filter/clean) → Generator (batch) →
        OpenCV (load/resize/normalize) → NumPy (stack) → Batch Dict

    Output format:
        {
            "image_batch": np.ndarray of shape (B, H, W, C),
            "text_batch": List[str] of length B,
            "metadata": Dict with category, split, filenames
        }
    """

    def __init__(
        self,
        manifest_path: Path,
        image_dir: Path,
        batch_size: int = 4,
        target_size: Tuple[int, int] = (224, 224),
        split: str = "train",
        shuffle: bool = True,
        normalize: bool = True
    ):
        """
        Initialize the multimodal data loader.

        Args:
            manifest_path: Path to CSV manifest file
            image_dir: Directory containing images
            batch_size: Number of samples per batch
            target_size: (height, width) for image resizing
            split: Data split to load ("train" or "test")
            shuffle: Whether to shuffle the data
            normalize: Whether to normalize images to [0, 1]
        """
        self.manifest_path = manifest_path
        self.image_dir = image_dir
        self.batch_size = batch_size
        self.target_size = target_size
        self.split = split
        self.shuffle = shuffle
        self.normalize = normalize

        # Load and clean manifest (Module 5 & 6)
        self.df = self._load_and_clean_manifest()

        print(f"✓ Initialized MultimodalDataLoader")
        print(f"  Split: {self.split}")
        print(f"  Samples: {len(self.df)}")
        print(f"  Batch size: {self.batch_size}")
        print(f"  Target size: {self.target_size}")
        print(f"  Categories: {self.df['category'].unique().tolist()}")

    def _load_and_clean_manifest(self) -> pd.DataFrame:
        """
        Load manifest CSV and apply data cleaning techniques.

        Module 6 Integration: Data Cleaning & Transformation
        - Remove duplicates
        - Handle missing values
        - Filter by split
        - Validate file paths
        - Clean text captions
        """
        print(f"\nLoading manifest from {self.manifest_path}...")

        # Read CSV
        df = pd.read_csv(self.manifest_path)
        initial_count = len(df)

        # Remove duplicates (Module 6)
        df = df.drop_duplicates(subset=['image_filename'])

        # Handle missing values (Module 6)
        df = df.dropna(subset=['image_filename', 'caption', 'category', 'split'])

        # Filter by split
        df = df[df['split'] == self.split].copy()

        # Clean text captions (Module 6)
        df['caption'] = df['caption'].str.strip()
        df['caption'] = df['caption'].str.replace(r'\s+', ' ', regex=True)

        # Validate image files exist
        valid_mask = df['image_filename'].apply(
            lambda x: (self.image_dir / x).exists()
        )
        df = df[valid_mask].copy()

        # Reset index
        df = df.reset_index(drop=True)

        print(f"  Initial rows: {initial_count}")
        print(f"  After cleaning: {len(df)}")
        print(f"  Duplicates removed: {initial_count - len(df)}")

        if len(df) == 0:
            raise ValueError(f"No valid samples found for split '{self.split}'")

        return df

    def _load_and_preprocess_image(self, image_path: Path) -> Optional[np.ndarray]:
        """
        Load and preprocess a single image using OpenCV.

        Module 7 Integration: Images as Data
        - Load image with cv2.imread
        - Resize to target dimensions
        - Convert BGR to RGB
        - Normalize to [0, 1] if enabled

        Args:
            image_path: Path to image file

        Returns:
            Preprocessed image array or None if loading fails
        """
        try:
            # Load image (returns BGR by default)
            img = cv2.imread(str(image_path))

            if img is None:
                print(f"  Warning: Failed to load {image_path}")
                return None

            # Resize (Module 7)
            img = cv2.resize(img, (self.target_size[1], self.target_size[0]))

            # Convert BGR to RGB (Module 7)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Normalize to [0, 1] (Module 3-4: NumPy operations)
            if self.normalize:
                img = img.astype(np.float32) / 255.0

            return img

        except Exception as e:
            print(f"  Error processing {image_path}: {e}")
            return None

    def __len__(self) -> int:
        """Return the number of batches."""
        return int(np.ceil(len(self.df) / self.batch_size))

    def __iter__(self) -> Iterator[Dict[str, any]]:
        """
        Iterate over batches of multimodal data.

        Module 2 Integration: Generator Pattern
        - Memory-efficient lazy evaluation
        - Yields one batch at a time
        - Handles shuffling

        Module 3-4 Integration: NumPy Operations
        - Array stacking for batching
        - Vectorized operations
        - Shape manipulation

        Yields:
            Dictionary containing:
                - image_batch: (B, H, W, C) array
                - text_batch: List of B captions
                - metadata: Dict with additional info
        """
        # Shuffle if enabled (Module 2)
        indices = np.arange(len(self.df))
        if self.shuffle:
            np.random.shuffle(indices)

        # Generate batches (Module 2: Generator pattern)
        for start_idx in range(0, len(self.df), self.batch_size):
            end_idx = min(start_idx + self.batch_size, len(self.df))
            batch_indices = indices[start_idx:end_idx]

            # Get batch data from DataFrame (Module 5)
            batch_df = self.df.iloc[batch_indices]

            # Load and process images (Module 7 + Module 3-4)
            image_list = []
            text_list = []
            valid_indices = []

            for idx, row in batch_df.iterrows():
                image_path = self.image_dir / row['image_filename']
                img = self._load_and_preprocess_image(image_path)

                if img is not None:
                    image_list.append(img)
                    text_list.append(row['caption'])
                    valid_indices.append(idx)

            # Skip empty batches
            if len(image_list) == 0:
                continue

            # Stack images into batch array (Module 3-4: NumPy)
            image_batch = np.stack(image_list, axis=0)

            # Prepare metadata
            metadata = {
                'batch_size': len(image_list),
                'categories': batch_df.iloc[valid_indices]['category'].tolist(),
                'filenames': batch_df.iloc[valid_indices]['image_filename'].tolist(),
                'split': self.split
            }

            # Yield batch dictionary
            yield {
                'image_batch': image_batch,
                'text_batch': text_list,
                'metadata': metadata
            }


def analyze_batch(batch: Dict[str, any], batch_idx: int) -> None:
    """
    Analyze and display statistics for a single batch.

    Module 3-4 Integration: Array statistics and analysis
    """
    images = batch['image_batch']
    texts = batch['text_batch']
    meta = batch['metadata']

    print(f"\n{'='*70}")
    print(f"BATCH {batch_idx}")
    print(f"{'='*70}")

    # Image statistics (Module 3-4: NumPy statistics)
    print("\n📊 Image Batch Statistics:")
    print(f"  Shape: {images.shape} (B, H, W, C)")
    print(f"  Data type: {images.dtype}")
    print(f"  Value range: [{images.min():.3f}, {images.max():.3f}]")
    print(f"  Mean: {images.mean():.3f}")
    print(f"  Std: {images.std():.3f}")
    print(f"  Memory: {images.nbytes / 1024:.1f} KB")

    # Text statistics
    print("\n📝 Text Batch:")
    for i, text in enumerate(texts):
        category = meta['categories'][i]
        filename = meta['filenames'][i]
        print(f"  [{i}] ({category}) {text[:50]}...")
        print(f"      Source: {filename}")

    # Per-image statistics
    print("\n🖼️  Per-Image Analysis:")
    for i in range(len(images)):
        img = images[i]
        print(f"  Image {i}: mean={img.mean():.3f}, "
              f"std={img.std():.3f}, "
              f"range=[{img.min():.3f}, {img.max():.3f}]")


def demonstrate_pytorch_integration():
    """
    Show how this pipeline would integrate with PyTorch.

    This is commented pseudocode showing the next step after the pipeline.
    """
    print("\n" + "="*70)
    print("PYTORCH INTEGRATION (Pseudocode)")
    print("="*70)

    code = '''
# After Module 8: Connection to PyTorch

import torch
from torch.utils.data import Dataset, DataLoader

class MultimodalDataset(Dataset):
    """Wrapper for our pipeline compatible with PyTorch."""

    def __init__(self, data_loader: MultimodalDataLoader):
        # Collect all samples from our pipeline
        self.samples = []
        for batch in data_loader:
            for i in range(len(batch['image_batch'])):
                self.samples.append({
                    'image': batch['image_batch'][i],
                    'text': batch['text_batch'][i],
                    'category': batch['metadata']['categories'][i]
                })

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        sample = self.samples[idx]
        # Convert to PyTorch tensors
        image_tensor = torch.from_numpy(sample['image']).permute(2, 0, 1)
        return image_tensor, sample['text'], sample['category']

# Usage in training loop
dataset = MultimodalDataset(data_loader)
torch_loader = DataLoader(dataset, batch_size=4, shuffle=True)

for epoch in range(num_epochs):
    for images, texts, categories in torch_loader:
        # images: (B, C, H, W) tensor
        # texts: List[str]
        # Forward pass through model...
        predictions = model(images, texts)
        loss = criterion(predictions, targets)
        loss.backward()
        optimizer.step()
'''

    print(code)

    print("\nKey Points:")
    print("  • Our pipeline produces NumPy arrays ready for PyTorch")
    print("  • torch.from_numpy() creates tensors with zero-copy")
    print("  • Image shape changes from (H,W,C) to (C,H,W) for PyTorch")
    print("  • Text can be tokenized inside the Dataset __getitem__")
    print("  • Same pattern works for TensorFlow/JAX with minor changes")


def demonstrate_tensorflow_integration():
    """
    Show how this pipeline would integrate with TensorFlow.
    """
    print("\n" + "="*70)
    print("TENSORFLOW INTEGRATION (Pseudocode)")
    print("="*70)

    code = '''
# After Module 8: Connection to TensorFlow

import tensorflow as tf

def generator_fn():
    """Generator function for tf.data.Dataset."""
    data_loader = MultimodalDataLoader(
        manifest_path, image_dir, batch_size=4
    )
    for batch in data_loader:
        yield (
            batch['image_batch'],
            batch['text_batch']
        )

# Create TensorFlow dataset
dataset = tf.data.Dataset.from_generator(
    generator_fn,
    output_signature=(
        tf.TensorSpec(shape=(None, 224, 224, 3), dtype=tf.float32),
        tf.TensorSpec(shape=(None,), dtype=tf.string)
    )
)

# Usage in training loop
for epoch in range(num_epochs):
    for images, texts in dataset:
        # images: (B, H, W, C) tensor
        # texts: (B,) tensor of strings
        with tf.GradientTape() as tape:
            predictions = model(images, texts)
            loss = loss_fn(labels, predictions)
        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))
'''

    print(code)

    print("\nKey Points:")
    print("  • Our pipeline can be wrapped as a tf.data.Dataset generator")
    print("  • TensorFlow prefers (B, H, W, C) - same as our output!")
    print("  • from_generator allows lazy loading like our pipeline")
    print("  • Can add .prefetch() and .cache() for performance")


def main():
    """
    Main demonstration of the research pipeline.

    This integrates all 8 modules into a cohesive workflow:
    1. Setup environment
    2. Initialize data loader with all configurations
    3. Iterate through batches using generator pattern
    4. Analyze batch contents and statistics
    5. Time the full pipeline
    6. Show ML framework integration patterns
    """
    print("="*70)
    print("MODULE 8: CAPSTONE - THE RESEARCH PIPELINE")
    print("="*70)
    print("\nIntegrating all 8 modules into a production-ready data pipeline...")

    # Setup paths
    script_dir = Path(__file__).parent
    manifest_path = script_dir / "data" / "manifest.csv"
    image_dir = script_dir / "data" / "images"

    # Verify data exists
    if not manifest_path.exists():
        print(f"\n❌ Error: Manifest not found at {manifest_path}")
        print("   Run create_sample_data.py first!")
        return

    if not image_dir.exists() or not list(image_dir.glob("*.png")):
        print(f"\n❌ Error: No images found in {image_dir}")
        print("   Run create_sample_data.py first!")
        return

    # ========================================================================
    # TRAINING SET PIPELINE
    # ========================================================================

    print("\n" + "="*70)
    print("TRAINING SET PIPELINE")
    print("="*70)

    # Initialize loader for training data
    train_loader = MultimodalDataLoader(
        manifest_path=manifest_path,
        image_dir=image_dir,
        batch_size=4,
        target_size=(224, 224),
        split="train",
        shuffle=True,
        normalize=True
    )

    # Time the pipeline (Module 4: Performance)
    print("\n⏱️  Processing training batches...")
    start_time = time.time()

    batch_count = 0
    total_samples = 0

    for batch_idx, batch in enumerate(train_loader):
        batch_count += 1
        total_samples += len(batch['image_batch'])

        # Analyze first 2 batches in detail
        if batch_idx < 2:
            analyze_batch(batch, batch_idx)

    elapsed = time.time() - start_time

    print("\n" + "="*70)
    print("TRAINING PIPELINE PERFORMANCE")
    print("="*70)
    print(f"  Total batches: {batch_count}")
    print(f"  Total samples: {total_samples}")
    print(f"  Total time: {elapsed:.3f} seconds")
    print(f"  Time per batch: {elapsed/batch_count:.3f} seconds")
    print(f"  Samples per second: {total_samples/elapsed:.1f}")

    # ========================================================================
    # TEST SET PIPELINE
    # ========================================================================

    print("\n" + "="*70)
    print("TEST SET PIPELINE")
    print("="*70)

    # Initialize loader for test data
    test_loader = MultimodalDataLoader(
        manifest_path=manifest_path,
        image_dir=image_dir,
        batch_size=2,
        target_size=(224, 224),
        split="test",
        shuffle=False,  # Don't shuffle test data
        normalize=True
    )

    print("\n⏱️  Processing test batches...")
    test_samples = 0

    for batch_idx, batch in enumerate(test_loader):
        test_samples += len(batch['image_batch'])
        if batch_idx == 0:
            analyze_batch(batch, batch_idx)

    print(f"\n  Test samples processed: {test_samples}")

    # ========================================================================
    # ML FRAMEWORK INTEGRATION
    # ========================================================================

    demonstrate_pytorch_integration()
    demonstrate_tensorflow_integration()

    # ========================================================================
    # SUMMARY
    # ========================================================================

    print("\n" + "="*70)
    print("CAPSTONE COMPLETE")
    print("="*70)

    print("\n✓ Module Integration Summary:")
    print("  Module 1: ✓ Environment setup with .env loading")
    print("  Module 2: ✓ Generator pattern for memory-efficient iteration")
    print("  Module 3: ✓ NumPy array operations and statistics")
    print("  Module 4: ✓ Vectorization and performance optimization")
    print("  Module 5: ✓ Pandas for CSV reading and DataFrame operations")
    print("  Module 6: ✓ Data cleaning, validation, and transformation")
    print("  Module 7: ✓ OpenCV for image loading and preprocessing")
    print("  Module 8: ✓ Complete multimodal research pipeline")

    print("\n✓ Pipeline Features:")
    print("  • Handles images and text together")
    print("  • Memory-efficient generator-based iteration")
    print("  • Configurable batch size and image size")
    print("  • Automatic data cleaning and validation")
    print("  • Train/test split support")
    print("  • Optional shuffling and normalization")
    print("  • Rich metadata for each batch")
    print("  • Ready for PyTorch, TensorFlow, or JAX")

    print("\n🎓 What You've Learned:")
    print("  • How to build a complete ML data pipeline")
    print("  • Integration of multiple data processing libraries")
    print("  • Best practices for multimodal data handling")
    print("  • Connection points to ML frameworks")
    print("  • Performance optimization techniques")

    print("\n🚀 Next Steps:")
    print("  • Add data augmentation (random flips, crops, color jitter)")
    print("  • Implement text tokenization for transformer models")
    print("  • Add caching for preprocessed images")
    print("  • Create train/val/test splits")
    print("  • Build actual PyTorch/TensorFlow models")
    print("  • Add logging and experiment tracking")

    print("\n" + "="*70)
    print("Congratulations! You've completed the AI Research Foundations course!")
    print("="*70)


if __name__ == "__main__":
    main()
