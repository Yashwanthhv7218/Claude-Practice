# 🔄 Resume Auto-Sync Guide

## Overview

The automated sync system allows you to **edit only `resume.md`** and **automatically regenerate `resume.html`** with the same professional design, colors, and styling.

**You only edit one file.** The script handles the rest.

---

## Files in This System

| File | Purpose | Edit? |
|------|---------|-------|
| `resume.md` | ✏️ **EDIT THIS** - Content only | ✅ Yes |
| `resume.html` | 🎨 Auto-generated - Design + Content | ❌ No (auto-updated) |
| `sync_resume.py` | Python sync engine | ❌ No |
| `sync_resume.bat` | Windows automation script | ❌ No |
| `sync_resume.sh` | Mac/Linux automation script | ❌ No |
| `design_analysis.md` | Design documentation | ℹ️ Reference |

---

## How to Use

### **Step 1: Edit Your Resume**

Edit `resume.md` with any text editor:
- Add new achievements
- Update metrics
- Modify skills
- Change dates
- Update certifications
- etc.

```markdown
# Your Name

**Your Title | Another Title**

📧 your.email@example.com | 📱 +91-XXXXXXXXXX | 📍 Location

## Professional Summary
Your updated summary here...

## Experience
New experience entries...
```

### **Step 2: Run the Sync Script**

After you save changes to `resume.md`, run ONE of these commands:

#### **Windows Users:**
```bash
# Double-click this file:
sync_resume.bat

# OR run in command prompt:
python sync_resume.py
```

#### **Mac/Linux Users:**
```bash
# Make script executable (first time only):
chmod +x sync_resume.sh

# Run the sync:
./sync_resume.sh

# OR directly:
python3 sync_resume.py
```

### **Step 3: Verify the Output**

1. Open `resume.html` in your browser
2. Check that all your changes are reflected
3. Verify the design (colors, fonts, layout) matches

### **Step 4: Commit & Push**

```bash
git add resume.md resume.html
git commit -m "Update resume with new achievements"
git push origin main
```

---

## What Gets Updated?

### ✅ **Automatically Updated (from resume.md):**
- Name and title
- Contact information (email, phone, location)
- Professional summary
- Experience entries
- Skills and certifications
- Education
- Any metrics or achievements
- All text content

### 🎨 **Design Stays the Same (Never Changes):**
- Dark theme (#1a1b2e)
- Purple (#7c3aed) + Cyan (#06b6d4) accents
- Glassmorphism effects
- Responsive layout
- Typography and fonts
- Color scheme
- Print styles
- Mobile compatibility

**In short:** Your content updates, your design stays beautiful.

---

## Markdown Formatting Tips

The sync script respects standard Markdown formatting:

```markdown
# Heading 1 (Main title)
## Heading 2 (Section title)
### Heading 3 (Subsection)

**Bold text** for emphasis
*Italic text* for emphasis

- Bullet lists (automatic formatting)
- Multiple bullets
- Nested bullets

[Link text](https://example.com) → clickable links
```

**Example:**
```markdown
### 📊 Key Achievement

- Reduced support tickets by **28%** through improved documentation
- Managed **200+ in-app guides** across product platform
- Led successful **Whatfix → Pendo migration** (2025)
```

---

## Workflow Examples

### Example 1: Add a New Achievement

**Before (resume.md):**
```markdown
#### 🎬 Release Documentation

- Produced **15+ quarterly releases**
- Created **50+ technical videos**
```

**After editing:**
```markdown
#### 🎬 Release Documentation

- Produced **15+ quarterly releases**
- Created **50+ technical videos**
- Implemented video library reducing support by **35%**
```

**Then run:** `sync_resume.bat` or `./sync_resume.sh`

**Result:** `resume.html` updates automatically with your new achievement!

---

### Example 2: Update a Metric

**Find in resume.md:**
```markdown
| Quarterly Releases Managed | 15+ |
```

**Change to:**
```markdown
| Quarterly Releases Managed | 18+ |
```

**Run sync → resume.html updates automatically**

---

### Example 3: Add a New Skill

**In resume.md, add to your skills section:**
```markdown
**Documentation & Writing**  
Technical Writing | API Documentation | In-App Guidance | **AI Documentation** | Content Migration
```

**Run sync → New skill appears in resume.html!**

---

## Troubleshooting

### ❌ "Python is not installed"

**Solution 1: Install Python**
- Windows: Download from python.org
- Mac: `brew install python3`
- Linux: `apt-get install python3`

**Solution 2: Use an online converter**
- Manually open `resume.html` and update the content
- (Not ideal, but works in a pinch)

### ❌ "resume.md not found"

**Solution:** Make sure you're running the script from the correct folder:
```bash
# Navigate to the folder containing resume.md
cd "D:\twtaiworkshop\My Portfolio\Yashwanth Resume Automation"

# Then run:
python sync_resume.py
```

### ❌ "Changes didn't update in HTML"

**Possible reasons:**
1. You forgot to save `resume.md` before running sync
2. Script had an error (check console output)
3. Browser cached the old version (press Ctrl+F5 or Cmd+Shift+R)

**Solution:**
- Save `resume.md` first
- Run sync again
- Clear browser cache and refresh

---

## Best Practices

✅ **DO:**
- Edit only `resume.md`
- Run sync after every significant change
- Commit both files together (`resume.md` + `resume.html`)
- Keep formatting consistent
- Test in browser before pushing to GitHub

❌ **DON'T:**
- Edit `resume.html` directly (changes will be lost on next sync)
- Run sync without saving `resume.md` first
- Change design/CSS (if you need design changes, ask me)
- Use unsupported formatting in `resume.md`

---

## GitHub Integration

### Setup (One-time):

```bash
# In your portfolio repository
mkdir -p resume
cp resume.md resume/
cp resume.html resume/
git add resume/
git commit -m "Add resume files"
git push
```

### Update Workflow:

```bash
# 1. Edit resume.md
# (make your changes)

# 2. Run sync
python sync_resume.py

# 3. Commit both
git add resume.md resume.html
git commit -m "Update resume"
git push

# Done! Resume is live on GitHub Pages
```

### Link in Your Portfolio:

In your portfolio README or homepage:
```markdown
## 📄 Resume

- [View Resume (Web)](/resume/resume.html)
- [Download Resume (PDF)](/resume/resume.pdf)
- [View on GitHub](/resume/resume.md)
```

---

## Advanced: Customization

### Changing Design Colors (Requires Manual Edit)

If you want to change the colors, I can help:
1. Tell me what colors you want (e.g., "blue and green instead of purple and cyan")
2. I'll update the HTML template
3. Future syncs will use the new colors

### Adding New Sections

Want to add a section like "Publications" or "Awards"?
1. Edit `resume.md` to add the section
2. I'll update the sync script to recognize and format it
3. Run sync → Done!

---

## Quick Reference

| Need | Action |
|------|--------|
| Update content | Edit `resume.md` |
| Sync to HTML | Run `sync_resume.bat` or `./sync_resume.sh` |
| Verify changes | Open `resume.html` in browser |
| Commit changes | `git add resume.md resume.html && git commit -m "Update"` |
| View live | Open on GitHub Pages |
| Change design | Ask me for template updates |
| Troubleshoot | Check console output or this guide |

---

## Need Help?

If you run into issues:

1. **Read the Troubleshooting section above**
2. **Check the console output** when running the script (it tells you what went wrong)
3. **Verify `resume.md` is properly formatted** (check for syntax errors)
4. **Ask me** - I can help debug or update the sync scripts

---

## Summary

**Your workflow is now:**

```
1. Edit resume.md
   ↓
2. Run sync_resume.bat (or .sh on Mac/Linux)
   ↓
3. Check resume.html in browser
   ↓
4. Commit & push to GitHub
   ↓
✅ Done! Resume updated everywhere
```

**That's it!** No more manual HTML editing. Just update the content, run sync, and your beautiful resume updates everywhere. 🚀

---

**Last Updated:** July 12, 2026  
**Version:** 1.0
