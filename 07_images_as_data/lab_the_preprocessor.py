"""
Module 7 Lab: The Preprocessor
===============================

Learning objectives:
- Load images as 3D NumPy arrays
- Convert between BGR and RGB color spaces
- Resize images to a fixed resolution
- Normalize pixel values from 0-255 to 0-1 for model convergence

This script demonstrates the essential image preprocessing pipeline
used in computer vision and deep learning.
"""

import os
import sys
import numpy as np
import cv2
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())


def ensure_sample_images():
    """Generate sample images if they don't exist."""
    images_dir = "data/images"

    if not os.path.exists(images_dir) or len(os.listdir(images_dir)) == 0:
        print("Sample images not found. Generating them now...\n")
        from create_sample_images import create_sample_images
        create_sample_images()
    else:
        print(f"✓ Sample images found in {images_dir}/\n")


def demonstrate_single_image():
    """Load and analyze a single image to understand its structure."""
    print("=" * 70)
    print("PART 1: Understanding Images as NumPy Arrays")
    print("=" * 70)

    # Load first available image
    images_dir = "data/images"
    image_files = sorted([f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))])

    if not image_files:
        print("Error: No images found in data/images/")
        return None

    image_path = os.path.join(images_dir, image_files[0])
    print(f"\n1. Loading image: {image_files[0]}")

    # Load image with OpenCV (returns BGR format)
    img_bgr = cv2.imread(image_path)

    if img_bgr is None:
        print(f"Error: Could not load {image_path}")
        return None

    print(f"   ✓ Image loaded successfully")
    print(f"   ✓ Shape: {img_bgr.shape}")
    print(f"   ✓ Data type: {img_bgr.dtype}")
    print(f"   ✓ Dimensions: Height={img_bgr.shape[0]}, Width={img_bgr.shape[1]}, Channels={img_bgr.shape[2]}")

    # Explain the shape
    print("\n   📐 Understanding the shape (H, W, C):")
    print(f"      - Height (rows):    {img_bgr.shape[0]} pixels")
    print(f"      - Width (columns):  {img_bgr.shape[1]} pixels")
    print(f"      - Channels:         {img_bgr.shape[2]} (B, G, R)")

    # Show pixel value range
    print(f"\n   📊 Pixel value statistics:")
    print(f"      - Minimum value: {img_bgr.min()}")
    print(f"      - Maximum value: {img_bgr.max()}")
    print(f"      - Mean value:    {img_bgr.mean():.2f}")
    print(f"      - Range:         0-255 (8-bit unsigned integers)")

    # Show a sample pixel
    sample_pixel = img_bgr[img_bgr.shape[0]//2, img_bgr.shape[1]//2]
    print(f"\n   🎨 Sample pixel at center (BGR format):")
    print(f"      - Blue:  {sample_pixel[0]}")
    print(f"      - Green: {sample_pixel[1]}")
    print(f"      - Red:   {sample_pixel[2]}")

    return img_bgr, image_files[0]


def demonstrate_bgr_to_rgb(img_bgr):
    """Demonstrate OpenCV's BGR quirk and conversion to RGB."""
    print("\n" + "=" * 70)
    print("PART 2: The BGR Quirk - Converting to RGB")
    print("=" * 70)

    print("\n⚠️  OpenCV loads images in BGR format (not RGB!)")
    print("   This is a historical quirk from early video standards.")
    print("   Most libraries (matplotlib, PIL, PyTorch) expect RGB.")

    # Convert BGR to RGB
    print("\n2. Converting BGR → RGB using cv2.cvtColor()")
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    print(f"   ✓ Conversion complete")
    print(f"   ✓ Shape unchanged: {img_rgb.shape}")
    print(f"   ✓ Only channel order changed: [B,G,R] → [R,G,B]")

    # Show the difference
    sample_pixel_bgr = img_bgr[img_bgr.shape[0]//2, img_bgr.shape[1]//2]
    sample_pixel_rgb = img_rgb[img_rgb.shape[0]//2, img_rgb.shape[1]//2]

    print(f"\n   📊 Same pixel in different formats:")
    print(f"      BGR: [{sample_pixel_bgr[0]:3d}, {sample_pixel_bgr[1]:3d}, {sample_pixel_bgr[2]:3d}]")
    print(f"      RGB: [{sample_pixel_rgb[0]:3d}, {sample_pixel_rgb[1]:3d}, {sample_pixel_rgb[2]:3d}]")
    print(f"           (Blue and Red channels swapped)")

    return img_rgb


def demonstrate_resizing(img_rgb, target_size=(224, 224)):
    """Demonstrate image resizing to a standard size."""
    print("\n" + "=" * 70)
    print("PART 3: Resizing to Standard Dimensions")
    print("=" * 70)

    original_shape = img_rgb.shape
    print(f"\n   Original size: {original_shape[1]}×{original_shape[0]} (W×H)")
    print(f"   Target size:   {target_size[0]}×{target_size[1]} (W×H)")

    print(f"\n3. Resizing to {target_size[0]}×{target_size[1]} using cv2.resize()")

    # Resize image
    img_resized = cv2.resize(img_rgb, target_size, interpolation=cv2.INTER_LINEAR)

    print(f"   ✓ Resize complete")
    print(f"   ✓ New shape: {img_resized.shape}")
    print(f"   ✓ Interpolation method: INTER_LINEAR (bilinear)")

    print(f"\n   🎯 Why 224×224?")
    print(f"      - Standard size for ImageNet pretrained models")
    print(f"      - VGG, ResNet, MobileNet all expect 224×224 input")
    print(f"      - Allows fixed-size input for neural networks")
    print(f"      - Trade-off between detail and computation")

    # Calculate size change
    original_pixels = original_shape[0] * original_shape[1]
    resized_pixels = target_size[0] * target_size[1]
    ratio = resized_pixels / original_pixels

    print(f"\n   📐 Size change:")
    print(f"      - Original: {original_pixels:,} pixels")
    print(f"      - Resized:  {resized_pixels:,} pixels")
    print(f"      - Ratio:    {ratio:.2f}x")

    return img_resized


def demonstrate_normalization(img_resized):
    """Demonstrate pixel value normalization."""
    print("\n" + "=" * 70)
    print("PART 4: Normalizing Pixel Values")
    print("=" * 70)

    print(f"\n   Current range: {img_resized.min()}-{img_resized.max()} (integers)")
    print(f"   Target range:  0.0-1.0 (floats)")

    print(f"\n4. Normalizing pixels by dividing by 255.0")

    # Normalize
    img_normalized = img_resized.astype(np.float32) / 255.0

    print(f"   ✓ Normalization complete")
    print(f"   ✓ Data type: {img_resized.dtype} → {img_normalized.dtype}")
    print(f"   ✓ Value range: {img_normalized.min():.3f}-{img_normalized.max():.3f}")
    print(f"   ✓ Mean value: {img_normalized.mean():.3f}")

    print(f"\n   🎓 Why normalize?")
    print(f"      1. Consistent scale across all features")
    print(f"      2. Helps gradient descent converge faster")
    print(f"      3. Prevents numerical instability")
    print(f"      4. Required by most pretrained models")
    print(f"      5. Typical range: [0,1] or [-1,1]")

    # Show memory usage
    original_bytes = img_resized.nbytes
    normalized_bytes = img_normalized.nbytes

    print(f"\n   💾 Memory usage:")
    print(f"      - uint8:   {original_bytes:,} bytes")
    print(f"      - float32: {normalized_bytes:,} bytes ({normalized_bytes/original_bytes:.1f}x larger)")

    return img_normalized


def process_image_batch(images_dir="data/images", target_size=(224, 224)):
    """Process all images in a directory into a normalized batch."""
    print("\n" + "=" * 70)
    print("PART 5: Processing an Entire Batch")
    print("=" * 70)

    # Get all image files
    image_files = sorted([f for f in os.listdir(images_dir)
                         if f.endswith(('.jpg', '.png'))])

    print(f"\n5. Processing {len(image_files)} images into a batch")
    print(f"   Target size: {target_size[0]}×{target_size[1]}")
    print(f"   Pipeline: Load → BGR→RGB → Resize → Normalize → Stack")

    # Process each image
    processed_images = []

    print(f"\n   Processing images:")
    for i, filename in enumerate(image_files, 1):
        image_path = os.path.join(images_dir, filename)

        # Load
        img = cv2.imread(image_path)
        if img is None:
            print(f"      ✗ {filename} - Failed to load")
            continue

        original_shape = img.shape

        # Convert BGR to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Resize
        img = cv2.resize(img, target_size, interpolation=cv2.INTER_LINEAR)

        # Normalize
        img = img.astype(np.float32) / 255.0

        processed_images.append(img)
        print(f"      ✓ {i:2d}. {filename:30s} {original_shape[1]:4d}×{original_shape[0]:4d} → {target_size[0]}×{target_size[1]}")

    # Stack into batch
    batch = np.stack(processed_images, axis=0)

    print(f"\n   ✓ Batch created successfully")
    print(f"   ✓ Batch shape: {batch.shape}")
    print(f"   ✓ Interpretation: (N={batch.shape[0]} images, H={batch.shape[1]}, W={batch.shape[2]}, C={batch.shape[3]})")

    return batch


def analyze_batch(batch):
    """Analyze the final batch array."""
    print("\n" + "=" * 70)
    print("PART 6: Understanding the Batch Array")
    print("=" * 70)

    N, H, W, C = batch.shape

    print(f"\n   📦 Batch array structure:")
    print(f"      Shape: ({N}, {H}, {W}, {C})")
    print(f"      ├─ N (batch size):  {N} images")
    print(f"      ├─ H (height):      {H} pixels")
    print(f"      ├─ W (width):       {W} pixels")
    print(f"      └─ C (channels):    {C} (R, G, B)")

    print(f"\n   📊 Batch statistics:")
    print(f"      - Data type:    {batch.dtype}")
    print(f"      - Value range:  {batch.min():.3f} to {batch.max():.3f}")
    print(f"      - Mean value:   {batch.mean():.3f}")
    print(f"      - Std dev:      {batch.std():.3f}")

    # Memory analysis
    total_bytes = batch.nbytes
    mb = total_bytes / (1024 * 1024)

    print(f"\n   💾 Memory footprint:")
    print(f"      - Total size:       {total_bytes:,} bytes ({mb:.2f} MB)")
    print(f"      - Per image:        {total_bytes//N:,} bytes ({mb/N:.2f} MB)")
    print(f"      - Pixels per image: {H * W * C:,}")

    # Calculate for larger batches
    print(f"\n   📈 Scaling calculations:")
    for batch_size in [32, 64, 128, 256]:
        batch_mb = (batch_size * H * W * C * 4) / (1024 * 1024)  # float32 = 4 bytes
        print(f"      - {batch_size:3d} images × {H}×{W}×{C}: {batch_mb:7.2f} MB")

    print(f"\n   ⚠️  Memory considerations:")
    print(f"      - GPU memory is limited (typically 4-24 GB)")
    print(f"      - Batch size affects training speed and convergence")
    print(f"      - Trade-off: larger batches = faster but more memory")


def demonstrate_preprocessing_pipeline():
    """Run the complete preprocessing demonstration."""

    print("\n" + "=" * 70)
    print("MODULE 7 LAB: THE PREPROCESSOR")
    print("Image Preprocessing Pipeline for Computer Vision")
    print("=" * 70)

    # Ensure sample images exist
    ensure_sample_images()

    # Part 1: Single image analysis
    result = demonstrate_single_image()
    if result is None:
        return
    img_bgr, filename = result

    # Part 2: BGR to RGB conversion
    img_rgb = demonstrate_bgr_to_rgb(img_bgr)

    # Part 3: Resizing
    img_resized = demonstrate_resizing(img_rgb, target_size=(224, 224))

    # Part 4: Normalization
    img_normalized = demonstrate_normalization(img_resized)

    # Part 5: Process entire batch
    batch = process_image_batch(target_size=(224, 224))

    # Part 6: Analyze batch
    analyze_batch(batch)

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY: The Complete Preprocessing Pipeline")
    print("=" * 70)

    print(f"\n   🎯 What we learned:")
    print(f"      1. Images are 3D NumPy arrays: (Height, Width, Channels)")
    print(f"      2. OpenCV uses BGR format, convert to RGB for compatibility")
    print(f"      3. Resize images to consistent dimensions (e.g., 224×224)")
    print(f"      4. Normalize pixel values from 0-255 to 0-1")
    print(f"      5. Stack into batches: (N, H, W, C) for model input")

    print(f"\n   💡 Key takeaways:")
    print(f"      - Preprocessing is essential for computer vision models")
    print(f"      - Standardization ensures consistent model inputs")
    print(f"      - Normalization improves training convergence")
    print(f"      - Batch processing enables efficient GPU utilization")
    print(f"      - Memory management is crucial for large datasets")

    print(f"\n   🚀 Next steps:")
    print(f"      - Try different target sizes (96×96, 512×512)")
    print(f"      - Experiment with different normalization ranges")
    print(f"      - Add data augmentation (rotation, flips, crops)")
    print(f"      - Implement ImageNet normalization (mean/std per channel)")
    print(f"      - Use this pipeline with real image datasets")

    print("\n" + "=" * 70)
    print("✓ Lab completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    demonstrate_preprocessing_pipeline()
