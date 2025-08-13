#!/bin/bash

echo "🚀 Deploying ALLOWED_HOSTS fix for Medical Management System"
echo "============================================================"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Not in a git repository. Please run this from the project root."
    exit 1
fi

# Show current git status
echo "📋 Current git status:"
git status --short

# Add all changes
echo "➕ Adding changes to git..."
git add .

# Commit the changes
echo "💾 Committing changes..."
git commit -m "Fix ALLOWED_HOSTS for Render deployment - resolves Bad Request 400 error

- Updated render.yaml with correct Render URL
- Fixed ALLOWED_HOSTS parsing in settings.py
- Added production security settings
- Improved deployment testing script"

# Push to remote
echo "🔄 Pushing to remote repository..."
git push origin main

echo ""
echo "✅ Changes successfully pushed to repository!"
echo ""
echo "🌐 Next steps to fix your Render deployment:"
echo "1. Go to your Render dashboard"
echo "2. Find your 'medical-management-system' service"
echo "3. Go to Environment tab"
echo "4. Add/Update these environment variables:"
echo "   - ALLOWED_HOSTS: medical-management-system-v8d5.onrender.com,localhost,127.0.0.1"
echo "   - EMAIL_HOST_PASSWORD: (your Gmail app password)"
echo "   - SECRET_KEY: (generate a new one if not already set)"
echo "5. Click 'Deploy Latest Commit' to redeploy"
echo ""
echo "Your site should be accessible at:"
echo "🔗 https://medical-management-system-v8d5.onrender.com"
