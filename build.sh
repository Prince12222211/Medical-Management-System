#!/bin/bash

# Build script for Medical Management System
set -e  # Exit on any error

echo "🚀 Starting build process..."
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run Django checks
echo "🔍 Running Django system checks..."
python manage.py check --deploy

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --verbosity=2

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --verbosity=2

echo "✅ Build process completed successfully!"
echo "Django apps installed:"
python manage.py showmigrations
