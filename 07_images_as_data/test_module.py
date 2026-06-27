"""
Quick test script to validate Module 7 setup
"""

import sys
import os

def check_imports():
    """Check if required packages can be imported."""
    print("=" * 60)
    print("Module 7: Images as Data - Setup Check")
    print("=" * 60)

    required = {
        'numpy': 'NumPy',
        'cv2': 'OpenCV (opencv-python)',
        'dotenv': 'python-dotenv'
    }

    all_ok = True

    for module, name in required.items():
        try:
            __import__(module)
            print(f"✓ {name:30s} - OK")
        except ImportError:
            print(f"✗ {name:30s} - MISSING")
            all_ok = False

    print("=" * 60)

    if all_ok:
        print("✓ All dependencies available")
        print("\nRun the lab with:")
        print("  python lab_the_preprocessor.py")
    else:
        print("✗ Some dependencies missing")
        print("\nInstall with:")
        print("  pip install -e .")

    print("=" * 60)

    return all_ok


def check_structure():
    """Check if all required files exist."""
    print("\nFile Structure Check:")
    print("-" * 60)

    required_files = [
        'pyproject.toml',
        'create_sample_images.py',
        'lab_the_preprocessor.py',
        'slides.html',
        'README.md',
        '.env.example'
    ]

    all_exist = True

    for filename in required_files:
        exists = os.path.exists(filename)
        status = "✓" if exists else "✗"
        print(f"{status} {filename}")
        if not exists:
            all_exist = False

    # Check data directory
    data_dir_exists = os.path.exists('data/images')
    status = "✓" if data_dir_exists else "✗"
    print(f"{status} data/images/")

    print("-" * 60)

    if all_exist and data_dir_exists:
        print("✓ All required files present")
    else:
        print("✗ Some files missing")

    print()

    return all_exist and data_dir_exists


if __name__ == "__main__":
    imports_ok = check_imports()
    structure_ok = check_structure()

    if imports_ok and structure_ok:
        print("✓ Module 7 is ready!")
        sys.exit(0)
    else:
        print("✗ Module 7 needs setup")
        sys.exit(1)
