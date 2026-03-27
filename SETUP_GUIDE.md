# 🎨 Setup Guide for Task Manager Pro

This guide will help you complete the visual setup for your GitHub repository.

## ✅ What's Already Done

- ✓ Professional README.md with attractive formatting
- ✓ SVG banner created (assets/banner.svg)
- ✓ Project structure organized
- ✓ Both GUI and CLI versions ready

## 📸 Next Steps: Add Screenshots

### Step 1: Take GUI Screenshot

1. Run the GUI application:
   ```bash
   python task_manager_gui.py
   ```

2. Add some sample tasks:
   - "Complete project documentation" - High priority - 2026-04-01
   - "Review code changes" - Medium priority - 2026-03-30
   - "Update dependencies" - Low priority - 2026-04-05

3. Take a screenshot:
   - **Windows**: Press `Win + Shift + S`
   - **Mac**: Press `Cmd + Shift + 4`
   - **Linux**: Press `PrtScn` or use Screenshot tool

4. Save as `assets/gui-screenshot.png`

### Step 2: Take CLI Screenshot

1. Run the CLI application:
   ```bash
   python task_manager.py
   ```

2. Add a few tasks (option 1)

3. View tasks (option 2)

4. Take a screenshot of your terminal

5. Save as `assets/cli-screenshot.png`

### Step 3: (Optional) Create Demo GIF

Use one of these free tools:
- **ScreenToGif** (Windows): https://www.screentogif.com/
- **LICEcap** (Windows/Mac): https://www.cockos.com/licecap/
- **Kap** (Mac): https://getkap.co/
- **Peek** (Linux): https://github.com/phw/peek

Record a 5-10 second demo showing:
1. Adding a new task
2. Marking it as complete

Save as `assets/gui-demo.gif`

## 🎨 Optional: Convert SVG Banner to PNG

If you prefer PNG format:

1. Open `assets/banner.svg` in a web browser
2. Take a screenshot or use browser dev tools to export
3. Or use online converter: https://cloudconvert.com/svg-to-png
4. Save as `assets/banner.png`
5. Update README.md to use `.png` instead of `.svg`

## 🖼️ Alternative: Create Custom Banner

If you want a custom design:

### Using Canva (Easiest):
1. Go to https://www.canva.com
2. Create new design (1200 x 400 px)
3. Search for "GitHub banner" templates
4. Customize with:
   - Title: "Task Manager Pro"
   - Subtitle: "Organize • Prioritize • Achieve"
   - Add task/checklist icons
5. Download as PNG
6. Save to `assets/banner.png`

### Using Figma (Professional):
1. Go to https://www.figma.com
2. Create new file (1200 x 400 px)
3. Design your banner
4. Export as PNG
5. Save to `assets/banner.png`

## 🚀 Publishing to GitHub

Once you have your screenshots:

```bash
# Add all files
git add .

# Commit
git commit -m "✨ Add professional README and assets"

# Create repository on GitHub (if not done)
# Then push
git remote add origin https://github.com/your-username/task-manager-pro.git
git branch -M main
git push -u origin main
```

## 📝 Final Checklist

Before publishing:

- [ ] Screenshots added to assets folder
- [ ] Banner image looks good
- [ ] Update `[your-username]` in README.md
- [ ] Update `[Your Name]` in README.md
- [ ] Test both applications work
- [ ] Add LICENSE file (MIT recommended)
- [ ] Review README for any typos

## 💡 Pro Tips

1. **High-Quality Screenshots**: Use 2x or retina display if available
2. **Consistent Theme**: Use the same terminal theme for CLI screenshots
3. **Sample Data**: Use realistic task examples in screenshots
4. **File Size**: Optimize images with https://tinypng.com
5. **Alt Text**: GitHub will use your image filenames as alt text

## 🎉 You're Done!

Your repository will look professional and attract more users!

Need help? Check the main README or open an issue.
