#!/bin/bash

# Resume Markdown to HTML Auto-Sync Script
# Run this script anytime you edit resume.md to regenerate resume.html
# Usage: ./sync_resume.sh

echo ""
echo "================================"
echo "  Resume Auto-Sync Tool"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.6+ using: brew install python3 (macOS) or apt-get install python3 (Linux)"
    exit 1
fi

# Check if resume.md exists
if [ ! -f "resume.md" ]; then
    echo "Error: resume.md not found in current directory"
    echo "Please run this script from the folder containing resume.md"
    exit 1
fi

# Run the sync script
echo "Running sync... (resume.md to resume.html)"
echo ""

python3 sync_resume.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Success! resume.html has been updated"
    echo ""
    echo "Next steps:"
    echo "  1. Open resume.html in your browser to verify"
    echo "  2. Commit both files to git: git add resume.md resume.html"
    echo "  3. Push to GitHub Pages: git push"
    echo ""
else
    echo ""
    echo "✗ Sync failed. Please check the error above."
    echo ""
    exit 1
fi
