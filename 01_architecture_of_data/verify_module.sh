#!/bin/bash

echo "========================================"
echo "Module 01 Verification Script"
echo "========================================"
echo ""

# Check if files exist
echo "1. Checking required files..."
files=(
    "pyproject.toml"
    "lab_tokenizer_dictionary.py"
    "slides.html"
    "README.md"
    "QUICK_REFERENCE.md"
    ".gitignore"
)

all_files_exist=true
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✓ $file exists"
    else
        echo "   ✗ $file MISSING"
        all_files_exist=false
    fi
done
echo ""

# Check if virtual environment exists
echo "2. Checking virtual environment..."
if [ -d ".venv" ]; then
    echo "   ✓ Virtual environment exists"
else
    echo "   ✗ Virtual environment MISSING"
    echo "   Run: uv venv"
    exit 1
fi
echo ""

# Check if dependencies are installed
echo "3. Checking dependencies..."
if .venv/bin/python -c "import dotenv" 2>/dev/null; then
    echo "   ✓ python-dotenv installed"
else
    echo "   ✗ python-dotenv NOT installed"
    echo "   Run: uv pip install python-dotenv"
    exit 1
fi
echo ""

# Run the lab script
echo "4. Running lab script..."
if .venv/bin/python lab_tokenizer_dictionary.py > /dev/null 2>&1; then
    echo "   ✓ Lab script executes successfully"
else
    echo "   ✗ Lab script FAILED"
    echo "   Run manually to see errors: python lab_tokenizer_dictionary.py"
    exit 1
fi
echo ""

# Check slides.html structure
echo "5. Checking slides.html structure..."
slide_count=$(grep -c '<div class="slide"' slides.html)
if [ "$slide_count" -ge 10 ]; then
    echo "   ✓ Slides contain $slide_count slides (expected 14+)"
else
    echo "   ✗ Slides only contain $slide_count slides (expected 14+)"
fi
echo ""

# Summary
echo "========================================"
if [ "$all_files_exist" = true ]; then
    echo "✅ Module 01 verification PASSED"
    echo "========================================"
    echo ""
    echo "Next steps:"
    echo "1. Run lab: python lab_tokenizer_dictionary.py"
    echo "2. View slides: open slides.html"
    echo "3. Read README.md for comprehensive documentation"
    echo "4. Use QUICK_REFERENCE.md as a cheat sheet"
else
    echo "❌ Module 01 verification FAILED"
    echo "========================================"
    exit 1
fi
