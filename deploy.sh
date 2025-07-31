#!/bin/bash

# 🎀 Hello Kitty Schedule Generator - Deployment Script 🎀

echo "🌸 Hello Kitty Schedule Generator - Deployment Script 🌸"
echo "=================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git add .
    git commit -m "🎀 Initial commit: Hello Kitty Schedule Generator Web App"
    echo "✅ Git repository initialized"
else
    echo "📁 Git repository already exists"
fi

echo ""
echo "🚀 Ready to deploy to your new repository!"
echo ""
echo "📋 Next steps:"
echo ""
echo "1. Create a new repository on GitHub:"
echo "   - Go to https://github.com/new"
echo "   - Name it: Weekly-Work-Schedule-Generator-Hello-Kitty-WEB"
echo "   - Make it public"
echo "   - Don't initialize with README (we already have one)"
echo ""
echo "2. Push to your new repository:"
echo "   git remote add origin https://github.com/candyyetszyu/Weekly-Work-Schedule-Generator-Hello-Kitty-WEB.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to Streamlit Cloud:"
echo "   - Go to https://share.streamlit.io"
echo "   - Sign in with GitHub"
echo "   - Click 'New app'"
echo "   - Select your repository: candyyetszyu/Weekly-Work-Schedule-Generator-Hello-Kitty-WEB"
echo "   - Set Main file path: streamlit_app.py"
echo "   - Set App URL: Weekly-Work-Schedule-Generator-Hello-Kitty-WEB"
echo "   - Click 'Deploy'"
echo ""
echo "🎀 Your app will be available at: https://candyyetszyu.streamlit.app/Weekly-Work-Schedule-Generator-Hello-Kitty-WEB"
echo ""
echo "✨ Happy scheduling with Hello Kitty! ✨" 