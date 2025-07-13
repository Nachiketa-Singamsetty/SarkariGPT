#!/bin/bash

# Exit on any error
set -e

echo "🚀 Starting build process..."

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt

# Download spacy model
echo "🤖 Downloading spacy model..."
python -m spacy download en_core_web_sm

# Verify installation
echo "✅ Build completed successfully!"
echo "📋 Installed packages:"
pip list 