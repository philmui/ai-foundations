#!/usr/bin/env python3
"""
Module 8: Capstone - Create Sample Multimodal Data
Generates synthetic images matching the manifest filenames.
"""

import os
import numpy as np
import cv2
import pandas as pd
from pathlib import Path


def create_synthetic_image(filename: str, size: tuple[int, int] = (256, 256)) -> np.ndarray:
    """
    Create a synthetic image based on category and index.

    Args:
        filename: Image filename (e.g., "galaxy_001.png")
        size: Target image size (height, width)

    Returns:
        Synthetic image as numpy array
    """
    h, w = size

    # Parse category from filename
    category = filename.split('_')[0]
    index = int(filename.split('_')[1].split('.')[0])

    # Create base image with category-specific pattern
    if category == 'galaxy':
        # Create spiral galaxy pattern
        img = np.zeros((h, w, 3), dtype=np.uint8)
        center = (h // 2, w // 2)

        # Background stars
        for _ in range(100 + index * 10):
            x, y = np.random.randint(0, w), np.random.randint(0, h)
            brightness = np.random.randint(150, 255)
            cv2.circle(img, (x, y), 1, (brightness, brightness, brightness), -1)

        # Central galaxy core
        cv2.circle(img, center, 40 + index * 5, (255, 240, 200), -1)
        cv2.circle(img, center, 30 + index * 3, (255, 255, 255), -1)

        # Spiral arms (blue-tinted)
        for angle in range(0, 360, 5):
            rad = np.radians(angle)
            r = 50 + angle * 0.3 + index * 5
            x = int(center[0] + r * np.cos(rad))
            y = int(center[1] + r * np.sin(rad))
            if 0 <= x < w and 0 <= y < h:
                cv2.circle(img, (x, y), 3, (180, 180, 255), -1)

    elif category == 'cell':
        # Create cell patterns
        img = np.full((h, w, 3), (240, 220, 240), dtype=np.uint8)

        # Add multiple cells
        num_cells = 5 + index
        for _ in range(num_cells):
            cx = np.random.randint(30, w - 30)
            cy = np.random.randint(30, h - 30)
            radius = np.random.randint(15, 30)

            # Cell membrane
            cv2.circle(img, (cx, cy), radius, (200, 150, 200), 2)

            # Nucleus
            cv2.circle(img, (cx, cy), radius // 2, (150, 100, 150), -1)

    elif category == 'landscape':
        # Create landscape with gradients
        img = np.zeros((h, w, 3), dtype=np.uint8)

        # Sky gradient (top half)
        for y in range(h // 2):
            color = int(180 - y * 0.5)
            img[y, :] = (color + 20, color + 10, color)

        # Ground gradient (bottom half)
        for y in range(h // 2, h):
            color = int((y - h // 2) * 0.8)
            if index % 2 == 0:
                # Green landscape
                img[y, :] = (color // 2, color + 100, color // 2)
            else:
                # Desert/sand
                img[y, :] = (color + 100, color + 150, color + 200)

        # Add mountains/features
        pts = np.array([[w // 4, h // 2], [w // 2, h // 4 + index * 10],
                        [3 * w // 4, h // 2]], dtype=np.int32)
        cv2.fillPoly(img, [pts], (80, 80, 80))

    elif category == 'circuit':
        # Create circuit board pattern
        img = np.full((h, w, 3), (10, 50, 10), dtype=np.uint8)

        # Draw circuit traces
        for _ in range(20 + index * 5):
            x1, y1 = np.random.randint(0, w), np.random.randint(0, h)
            x2 = x1 + np.random.randint(-50, 50)
            y2 = y1 + np.random.randint(-50, 50)
            cv2.line(img, (x1, y1), (x2, y2), (100, 200, 100), 2)

        # Draw components
        for _ in range(10 + index * 2):
            cx = np.random.randint(20, w - 20)
            cy = np.random.randint(20, h - 20)
            size = np.random.randint(5, 15)
            cv2.rectangle(img, (cx - size, cy - size), (cx + size, cy + size),
                         (150, 150, 50), -1)
            cv2.rectangle(img, (cx - size, cy - size), (cx + size, cy + size),
                         (200, 200, 100), 1)

    elif category == 'weather':
        # Create weather patterns
        if index == 1:
            # Clouds
            img = np.full((h, w, 3), (180, 220, 255), dtype=np.uint8)
            for _ in range(8):
                cx = np.random.randint(0, w)
                cy = np.random.randint(0, h // 2)
                radius = np.random.randint(30, 60)
                cv2.circle(img, (cx, cy), radius, (255, 255, 255), -1)

        elif index == 2:
            # Hurricane (spiral)
            img = np.full((h, w, 3), (20, 40, 80), dtype=np.uint8)
            center = (h // 2, w // 2)

            for angle in range(0, 360, 2):
                rad = np.radians(angle)
                for r in range(20, 100, 5):
                    x = int(center[0] + r * np.cos(rad))
                    y = int(center[1] + r * np.sin(rad))
                    if 0 <= x < w and 0 <= y < h:
                        cv2.circle(img, (x, y), 3, (200, 200, 200), -1)

        elif index == 3:
            # Lightning
            img = np.full((h, w, 3), (30, 30, 30), dtype=np.uint8)
            x1, y1 = w // 2, 0

            for _ in range(10):
                x2 = x1 + np.random.randint(-20, 20)
                y2 = y1 + np.random.randint(20, 30)
                cv2.line(img, (x1, y1), (x2, y2), (255, 255, 200), 3)
                x1, y1 = x2, y2

        else:
            # Tornado
            img = np.full((h, w, 3), (50, 50, 50), dtype=np.uint8)
            for y in range(0, h, 5):
                width = int(20 + (y / h) * 50)
                x = w // 2 + int(np.sin(y * 0.1) * 20)
                cv2.ellipse(img, (x, y), (width, 5), 0, 0, 360, (120, 120, 120), -1)

    else:
        # Default pattern
        img = np.random.randint(0, 255, (h, w, 3), dtype=np.uint8)

    return img


def main():
    """Generate all synthetic images from manifest."""
    # Setup paths
    script_dir = Path(__file__).parent
    data_dir = script_dir / "data"
    images_dir = data_dir / "images"
    manifest_path = data_dir / "manifest.csv"

    # Read manifest
    print(f"Reading manifest from {manifest_path}")
    df = pd.read_csv(manifest_path)

    print(f"\nGenerating {len(df)} synthetic images...")

    # Generate each image
    for idx, row in df.iterrows():
        filename = row['image_filename']
        output_path = images_dir / filename

        # Create synthetic image
        img = create_synthetic_image(filename)

        # Save image
        cv2.imwrite(str(output_path), img)
        print(f"  [{idx+1:2d}/{len(df)}] Created {filename} ({row['category']}, {row['split']})")

    print(f"\n✓ Successfully generated {len(df)} images in {images_dir}")

    # Show statistics
    print("\nDataset Statistics:")
    print(f"  Total images: {len(df)}")
    print(f"  Training: {len(df[df['split'] == 'train'])}")
    print(f"  Testing: {len(df[df['split'] == 'test'])}")
    print("\nCategories:")
    for category, count in df['category'].value_counts().items():
        print(f"  {category}: {count}")


if __name__ == "__main__":
    main()
