"""
Generate synthetic sample images for Module 7: Images as Data

This script creates diverse synthetic images to demonstrate:
- Different sizes (to show need for resizing)
- Different patterns (gradients, shapes, noise)
- RGB color channels
"""

import numpy as np
import cv2
import os


def create_sample_images(output_dir: str = "data/images", num_images: int = 8):
    """Generate synthetic sample images with different sizes and patterns."""

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"Generating {num_images} synthetic sample images in {output_dir}/")
    print("=" * 60)

    # Image 1: Red gradient (320x240)
    img1 = np.zeros((240, 320, 3), dtype=np.uint8)
    for i in range(240):
        img1[i, :, 2] = int((i / 240) * 255)  # Red channel gradient
    cv2.imwrite(os.path.join(output_dir, "sample_01_red_gradient.jpg"), img1)
    print("✓ sample_01_red_gradient.jpg (320x240) - vertical red gradient")

    # Image 2: Green and Blue diagonal (480x360)
    img2 = np.zeros((360, 480, 3), dtype=np.uint8)
    for i in range(360):
        for j in range(480):
            img2[i, j, 0] = int(((i + j) / (360 + 480)) * 255)  # Blue
            img2[i, j, 1] = int(((i + j) / (360 + 480)) * 128)  # Green
    cv2.imwrite(os.path.join(output_dir, "sample_02_blue_green_diagonal.jpg"), img2)
    print("✓ sample_02_blue_green_diagonal.jpg (480x360) - diagonal gradient")

    # Image 3: Random noise (256x256)
    img3 = np.random.randint(0, 256, (256, 256, 3), dtype=np.uint8)
    cv2.imwrite(os.path.join(output_dir, "sample_03_random_noise.jpg"), img3)
    print("✓ sample_03_random_noise.jpg (256x256) - random RGB noise")

    # Image 4: Colored rectangles (640x480)
    img4 = np.zeros((480, 640, 3), dtype=np.uint8)
    # Red rectangle
    img4[50:200, 50:250, 2] = 255
    # Green rectangle
    img4[280:430, 150:350, 1] = 255
    # Blue rectangle
    img4[150:300, 390:590, 0] = 255
    cv2.imwrite(os.path.join(output_dir, "sample_04_rectangles.jpg"), img4)
    print("✓ sample_04_rectangles.jpg (640x480) - three colored rectangles")

    # Image 5: Checkerboard pattern (512x512)
    img5 = np.zeros((512, 512, 3), dtype=np.uint8)
    square_size = 64
    for i in range(0, 512, square_size):
        for j in range(0, 512, square_size):
            if ((i // square_size) + (j // square_size)) % 2 == 0:
                img5[i:i+square_size, j:j+square_size] = [255, 255, 255]
    cv2.imwrite(os.path.join(output_dir, "sample_05_checkerboard.jpg"), img5)
    print("✓ sample_05_checkerboard.jpg (512x512) - black and white checkerboard")

    # Image 6: Radial gradient (300x300)
    img6 = np.zeros((300, 300, 3), dtype=np.uint8)
    center_x, center_y = 150, 150
    max_dist = np.sqrt(center_x**2 + center_y**2)
    for i in range(300):
        for j in range(300):
            dist = np.sqrt((i - center_y)**2 + (j - center_x)**2)
            value = int((1 - dist / max_dist) * 255)
            img6[i, j] = [value, value // 2, value]  # Purple gradient
    cv2.imwrite(os.path.join(output_dir, "sample_06_radial_gradient.jpg"), img6)
    print("✓ sample_06_radial_gradient.jpg (300x300) - radial purple gradient")

    # Image 7: Horizontal stripes (400x300)
    img7 = np.zeros((300, 400, 3), dtype=np.uint8)
    stripe_height = 50
    colors = [
        [255, 0, 0],    # Blue
        [0, 255, 0],    # Green
        [0, 0, 255],    # Red
        [255, 255, 0],  # Cyan
        [255, 0, 255],  # Magenta
        [0, 255, 255],  # Yellow
    ]
    for i, color in enumerate(colors):
        img7[i*stripe_height:(i+1)*stripe_height, :] = color
    cv2.imwrite(os.path.join(output_dir, "sample_07_stripes.jpg"), img7)
    print("✓ sample_07_stripes.jpg (400x300) - horizontal color stripes")

    # Image 8: Random colored circles (600x400)
    img8 = np.ones((400, 600, 3), dtype=np.uint8) * 240  # Light gray background
    np.random.seed(42)
    for _ in range(10):
        center = (np.random.randint(50, 550), np.random.randint(50, 350))
        radius = np.random.randint(20, 60)
        color = tuple(np.random.randint(0, 256, 3).tolist())
        cv2.circle(img8, center, radius, color, -1)
    cv2.imwrite(os.path.join(output_dir, "sample_08_circles.jpg"), img8)
    print("✓ sample_08_circles.jpg (600x400) - random colored circles")

    print("=" * 60)
    print(f"✓ All {num_images} sample images generated successfully!\n")


if __name__ == "__main__":
    create_sample_images()
