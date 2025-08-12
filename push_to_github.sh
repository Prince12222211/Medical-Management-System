#!/bin/bash

# 🚀 Medical Management System - GitHub Push Script
# ===============================================

echo "🏥 Medical Management System - GitHub Setup"
echo "=========================================="
echo ""

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository!"
    exit 1
fi

echo "📋 Current repository status:"
git status --short

echo ""
echo "🔗 Step 1: Add GitHub remote origin"
echo "Replace YOUR_GITHUB_USERNAME with your actual GitHub username:"
echo ""
echo "git remote add origin https://github.com/YOUR_GITHUB_USERNAME/medical-management-system.git"
echo ""

read -p "Enter your GitHub username: " github_username

if [ -z "$github_username" ]; then
    echo "❌ GitHub username cannot be empty!"
    exit 1
fi

echo ""
echo "🔗 Adding GitHub remote..."
git remote add origin "https://github.com/$github_username/medical-management-system.git"

if [ $? -eq 0 ]; then
    echo "✅ Remote added successfully!"
else
    echo "⚠️  Remote might already exist. Updating remote URL..."
    git remote set-url origin "https://github.com/$github_username/medical-management-system.git"
fi

echo ""
echo "🌿 Step 2: Rename branch to main..."
git branch -M main

echo ""
echo "📤 Step 3: Pushing to GitHub..."
echo "You may be prompted for GitHub credentials."
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Your Medical Management System is now on GitHub!"
    echo ""
    echo "🌐 Repository URL: https://github.com/$github_username/medical-management-system"
    echo ""
    echo "📋 Next steps:"
    echo "1. Visit your repository on GitHub"
    echo "2. Add topics: django, python, healthcare, medical, bootstrap"
    echo "3. Verify README.md displays correctly"
    echo "4. Share your repository URL in your portfolio!"
    echo ""
    echo "🏆 Great job! Your professional Django project is now live on GitHub!"
else
    echo ""
    echo "❌ Push failed. This might be due to:"
    echo "• Authentication issues"
    echo "• Repository doesn't exist on GitHub"
    echo "• Network connectivity issues"
    echo ""
    echo "📖 Check GITHUB_SETUP.md for detailed instructions."
fi

echo ""
echo "🔄 For future updates, use:"
echo "git add ."
echo "git commit -m \"✨ Your commit message\""
echo "git push origin main"
