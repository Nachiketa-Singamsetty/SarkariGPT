#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting build process..."

# Upgrade pip first
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install packages with retry logic
echo "📦 Installing Python packages..."
pip install -r requirements.txt || {
    echo "⚠️  First attempt failed, trying with --no-deps..."
    pip install -r requirements.txt --no-deps || {
        echo "⚠️  Trying individual packages..."
        pip install flask flask-cors gunicorn
        pip install torch transformers sentence-transformers
        pip install sentencepiece jieba3k tinysegmenter
        pip install PyMuPDF pdfplumber newspaper3k
        pip install beautifulsoup4 requests feedfinder2 sgmllib3k
        pip install pandas scikit-learn numpy
        pip install spacy streamlit python-dotenv
    }
}

# Download spacy model
echo "🤖 Downloading spacy model..."
python -m spacy download en_core_web_sm

# Verify installation
echo "✅ Build completed successfully!"
echo "📋 Installed packages:"
pip list 