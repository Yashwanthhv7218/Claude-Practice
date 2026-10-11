---
name: tech-writer-resume-builder
description: |
  Creates ATS-optimized professional resumes and GitHub-hosted HTML portfolio versions for technical writers and documentation engineers. Use this skill when a technical writer has existing materials (resume, performance reviews, old CV) and needs a modern, polished resume that showcases quantified achievements and aligns with current SaaS/AI-industry standards. Generates two outputs: a clean Markdown resume (ATS-compliant) and a modern, responsive HTML version ready for GitHub portfolio hosting. **NEW:** Optionally provide a GitHub Pages URL and the skill will analyze its design (color palette, typography, layout) to generate a resume HTML that takes design inspiration from it. Incorporates best practices for API documentation specialists and documentation engineers—skills commanding $30-50K salary premiums.
compatibility: "Requires: file system access to read input documents (PDF, Markdown, text). Outputs: Markdown + HTML files."
---

## Overview

This skill transforms fragmented resume/CV materials into a cohesive, modern resume tailored for technical writers in fast-moving AI-led companies. It synthesizes input from:
- **Existing resume** (baseline structure)
- **Performance reviews** (Betterworks PDF with manager feedback and metrics)
- **Old CV** (for skills/experience continuity)

And produces:
1. **resume.md** — ATS-optimized, clean Markdown format
2. **resume.html** — Self-contained, modern HTML for GitHub portfolio

## Why This Matters

Technical writing has shifted dramatically. Today's market values:
- **Quantified impact** (not just "wrote docs")
- **API documentation expertise** (+$30-50K premium)
- **Docs-as-code workflows** (Git, Markdown, CI/CD)
- **Portfolio visibility** (GitHub hosting is now expected)

This skill bridges the gap between what you've done and how to present it compellingly.

## How It Works

### Input Requirements

**Required:**
Place these files in a single folder:
- **resume** (any format: .md, .txt, .docx content)
- **Betterworks PDF** of performance reviews (manager feedback + ratings)
- **Old CV** (to extract continuity and skills)

Exact filenames flexible; the skill will ask you to identify them or scan the folder.

**Optional:**
- **GitHub Pages Portfolio URL** (e.g., `https://username.github.io/portfolio`) — If provided, the skill will analyze the design (colors, typography, layout) and generate a resume HTML inspired by that aesthetic

### Processing Steps

1. **Parse & Extract**
   - Read resume for structure, roles, dates, core skills
   - Extract quantified achievements from reviews (e.g., "reduced docs review time by 40%")
   - Identify unique skills/tools from old CV (especially technical/specialized ones)

2. **Synthesize & Enhance**
   - Merge experience into a cohesive narrative
   - Inject manager feedback as achievement validation
   - Add metrics to previously vague statements
   - Reorder by impact (highest-ROI skills first)

2b. **[Optional] Analyze GitHub Pages Design** (if portfolio URL provided)
   - Fetch the live GitHub Pages site
   - Extract design elements: color palette, typography, layout patterns
   - Identify CSS structure, spacing/margins, visual hierarchy
   - Document design inspiration points for HTML generation

3. **Optimize for Modern Market**
   - Flag API documentation, docs-as-code, AI literacy skills (high-value keywords)
   - Ensure ATS compliance (single-column, no graphics, proper fonts)
   - Craft professional summary that mirrors SaaS/tech hiring language
   - Include portfolio section with placeholder links (for GitHub/Docusaurus examples)

4. **Generate Outputs**
   - **Markdown**: Clean, portable, version-controllable
   - **HTML**: Modern CSS, responsive, self-contained, GitHub Pages ready

### Output Format

#### resume.md
```
# [Your Name]
[Email] | [Location] | [LinkedIn/GitHub/Portfolio links]

## Professional Summary
[2-3 lines. Specific to your specialty, e.g., "API documentation engineer..."]

## Experience
[Company | Role | Duration]
- [Quantified achievement #1]
- [Quantified achievement #2]
...

## Skills
[10-20 keywords: Git, Markdown, Docusaurus, OpenAPI, Python, CI/CD, etc.]

## Education
[Degree | School | Year]

## Certifications & Recognition
[Optional: industry recognition, Betterworks scores, etc.]
```

#### resume.html
- Self-contained (no external CDN dependencies for core styling)
- Responsive design (looks good on mobile + desktop)
- Print-friendly (exports cleanly to PDF)
- Modern color palette + clean typography
- Portfolio links section ready for your GitHub docs repos
- Accessible (proper heading hierarchy, semantic HTML)

**Design-Inspired Option (if GitHub Pages URL provided):**
- Analyzes your portfolio site's design (colors, fonts, spacing, layout)
- Generates resume HTML that echoes those design elements
- Maintains visual consistency between your portfolio and resume
- Adapts design inspiration while keeping resume-specific content hierarchies
- Color palette, typography, and layout style inspired by (not copied from) your portfolio

### Design Analysis in Action

When you provide a GitHub Pages URL, the skill will:
1. **Extract Design Elements**: Primary/accent colors, font families, spacing patterns, border styles
2. **Analyze Visual Hierarchy**: How the portfolio emphasizes key information, use of whitespace
3. **Document CSS Patterns**: Responsive breakpoints, hover effects, button styles (where applicable)
4. **Adapt for Resume**: Apply the aesthetic to your resume structure while preserving ATS-friendly single-column layout
5. **Output Resume.html**: A self-contained HTML file that visually resonates with your existing portfolio

**Example:**
- Portfolio uses: Dark navy (#1a2332) + coral accent (#ff6b6b), clean sans-serif (Inter/Poppins)
- Resume HTML will use: Similar color scheme, matching typography, coordinated spacing and layout
- Result: Your resume looks like it belongs on your portfolio site

### ATS Optimization Checklist (Built-In)

✅ Single-column layout  
✅ Standard fonts (no custom web fonts that fail parsing)  
✅ No tables, graphics, or text boxes  
✅ All achievements quantified (%, time, count, or $)  
✅ Keywords from job descriptions naturally woven in  
✅ Acronym + spelled-out versions (e.g., "REST APIs")  

### Key Decisions Made

- **Markdown over other formats**: Version-controllable, Git-friendly, can be rendered as-is or converted to PDF/HTML
- **Self-contained HTML**: No external dependencies, works offline, GitHub Pages compatible
- **Quantified metrics throughout**: Non-negotiable for competitive positioning
- **Portfolio section**: Modern hiring expects writing samples; placeholders guide you to add real links
- **API documentation emphasis**: Highest ROI specialty for tech writers right now

## Tips for Best Results

1. **Input quality matters**: If your Betterworks PDF has specific metrics (e.g., "improved clarity score by 28%"), the skill will surface them
2. **Resume consistency**: If your old CV has skills not in your main resume, they'll be merged intelligently
3. **Review & customize**: The generated resume is a strong draft, but personalize portfolio links, add job-specific keywords, and tweak summary as needed
4. **Test ATS parsing**: Before submitting, paste the Markdown resume into an ATS simulator (free tools online) to verify layout
5. **Host on GitHub**: Add a `resume` folder to your portfolio repo, include both `.md` and `.html` versions, and link to it in LinkedIn/GitHub profile

## Design-Matched Resume Workflow

**Scenario:** You already have a GitHub Pages portfolio site and want your resume to visually match it.

**Step 1:** Get your portfolio URL
- Example: `https://username.github.io/portfolio` or `https://username.github.io`

**Step 2:** Run the skill
- Provide your resume materials (as usual)
- Paste your portfolio GitHub Pages URL when prompted
- The skill fetches and analyzes your portfolio's design

**Step 3:** Get a design-matched resume
- `resume.md` is generated (unchanged, ATS-optimized)
- `resume.html` is generated with design inspiration from your portfolio
  - Color palette matches your portfolio
  - Typography echoes your portfolio's fonts
  - Layout and spacing feel cohesive with your brand
  - But structure is optimized for resume readability (not a copy)

**Result:** Your resume looks like a natural extension of your portfolio—visual consistency matters to tech hiring managers.

---

## Example Transformation

**Input Resume (vague):**
> "Responsible for API documentation and user guides. Maintained documentation in Confluence. Received positive feedback in annual review."

**Output Resume (impact-driven):**
> "Reduced API integration time by 40% through comprehensive OpenAPI/Swagger documentation and interactive code examples. Published 120+ technical guides in Markdown/Git, improving developer onboarding efficiency and reducing support tickets by 28%. Achieved 4.5/5 rating on clarity and accuracy in Betterworks annual review."

---

## How to Use This Skill

**When to invoke:**
- You have existing resume materials and need a polished, modern version
- You're preparing to job-hunt in the tech writing space
- You want to showcase your work on GitHub as a portfolio

**What to provide:**
- Folder path with resume + reviews + old CV
- Brief confirmation of file locations (or let the skill auto-detect)
- **(Optional)** GitHub Pages portfolio URL if you want resume.html to match your portfolio's design aesthetic

**What you get:**
- `resume.md` (ready for Git, sharing, PDF conversion)
- `resume.html` (ready to host, print, or email — optionally design-inspired by your portfolio)
- Feedback on gaps/opportunities (e.g., "no portfolio links yet—add 2-3 Docusaurus examples")
- **(If URL provided)** Design analysis report showing color palette, typography, and layout elements used

---

## Modern Tech Writer Context (2024-2025)

The STC (Society for Technical Communication) certification is no longer available (org dissolved Feb 2025). **Portfolio now outweighs credentials.** This skill emphasizes:

- **Docs-as-code** (Git, Markdown, static generators)
- **API documentation expertise** (highest-paying specialty)
- **AI literacy** (growing expectation—Claude, ChatGPT for drafting/editing)
- **Information architecture** (emerging skill set)
- **Accessibility/WCAG** (growing value, +35% YoY)

The skill reflects current market realities, not outdated credentials.

