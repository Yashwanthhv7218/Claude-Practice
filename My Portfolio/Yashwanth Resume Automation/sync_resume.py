#!/usr/bin/env python3
"""
Resume Markdown to HTML Sync Tool
Automatically converts resume.md to resume.html while preserving design
Maintains dark theme, purple/cyan accents, and all styling
"""

import re
import os
from pathlib import Path
from datetime import datetime

class MarkdownToResume:
    def __init__(self, md_file, html_file):
        self.md_file = md_file
        self.html_file = html_file
        self.content = {}

    def read_markdown(self):
        """Read and parse markdown file"""
        with open(self.md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract main sections
        self.content['raw'] = content
        self.extract_sections(content)
        return self.content

    def extract_sections(self, content):
        """Extract different sections from markdown"""
        # Extract name and title
        name_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        self.content['name'] = name_match.group(1) if name_match else "Name"

        title_match = re.search(r'^\*\*(.+?)\*\*', content, re.MULTILINE)
        self.content['title'] = title_match.group(1) if title_match else "Title"

        # Extract contact info
        contact_match = re.search(r'📧 (.+?) \|', content)
        self.content['email'] = contact_match.group(1) if contact_match else "email@example.com"

        phone_match = re.search(r'📱 (.+?) \|', content)
        self.content['phone'] = phone_match.group(1) if phone_match else "+91-XXXXXXXXXX"

        location_match = re.search(r'📍 (.+?)(?:\n|$)', content)
        self.content['location'] = location_match.group(1) if location_match else "Location"

        # Extract summary
        summary_match = re.search(
            r'## Professional Summary\n\n(.+?)(?=\n\n---|\n\n##)',
            content,
            re.DOTALL
        )
        self.content['summary'] = summary_match.group(1).strip() if summary_match else ""

        # Extract experience section
        exp_match = re.search(
            r'## Professional Experience\n\n(.+?)(?=\n\n---|\n\n##)',
            content,
            re.DOTALL
        )
        self.content['experience'] = exp_match.group(1).strip() if exp_match else ""

        # Extract skills section
        skills_match = re.search(
            r'## Technical Skills\n\n(.+?)(?=\n\n---|\n\n##)',
            content,
            re.DOTALL
        )
        self.content['skills'] = skills_match.group(1).strip() if skills_match else ""

        # Extract metrics
        metrics_match = re.search(
            r'## Key Metrics & Impact\n\n(.+?)(?=\n\n---|\n\n##)',
            content,
            re.DOTALL
        )
        self.content['metrics'] = metrics_match.group(1).strip() if metrics_match else ""

        # Extract certifications
        cert_match = re.search(
            r'## Certifications & Professional Development\n\n(.+?)(?=\n\n---|\n\n##)',
            content,
            re.DOTALL
        )
        self.content['certifications'] = cert_match.group(1).strip() if cert_match else ""

        # Extract education
        edu_match = re.search(
            r'## Education\n\n(.+?)(?=\n\n---|\n\n##)',
            content,
            re.DOTALL
        )
        self.content['education'] = edu_match.group(1).strip() if edu_match else ""

    def md_to_html_content(self, md_text):
        """Convert markdown text to HTML"""
        html = md_text

        # Bold text
        html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

        # Links
        html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)

        # Bullet lists
        html = re.sub(
            r'^- (.+?)$',
            r'<li>\1</li>',
            html,
            flags=re.MULTILINE
        )
        html = re.sub(r'(<li>.*?</li>)', r'<ul>\1</ul>', html, flags=re.DOTALL)
        html = html.replace('</li>\n<li>', '</li>\n<li>')

        # Line breaks
        html = re.sub(r'\n{2,}', '</p><p>', html)
        html = f'<p>{html}</p>'

        return html

    def parse_experience_entries(self, exp_text):
        """Parse experience entries from markdown"""
        entries = []

        # Split by role headers (###)
        role_blocks = re.split(r'^### \*\*(.+?)\*\*', exp_text, flags=re.MULTILINE)

        for i in range(1, len(role_blocks), 2):
            if i + 1 < len(role_blocks):
                title = role_blocks[i].strip()
                content = role_blocks[i + 1].strip()

                entries.append({
                    'title': title,
                    'content': content
                })

        return entries

    def parse_skills(self, skills_text):
        """Parse skills into categories"""
        categories = {}

        # Split by category (first line is category)
        lines = skills_text.split('\n')
        current_category = None

        for line in lines:
            line = line.strip()
            if line.startswith('**') and line.endswith('**'):
                current_category = line.replace('**', '').strip()
                categories[current_category] = []
            elif line and current_category and not line.startswith('|'):
                # Remove markdown formatting
                skills = re.findall(r'`(.+?)`', line)
                if skills:
                    categories[current_category].extend(skills)
                elif '|' not in line:
                    skills = [s.strip() for s in line.split(',') if s.strip()]
                    categories[current_category].extend(skills)

        return categories

    def generate_html(self):
        """Generate complete HTML resume"""
        html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Senior Technical Writer Resume</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --bg: #1a1b2e;
            --bg2: #16213e;
            --bg3: #0f3460;
            --accent: #7c3aed;
            --accent2: #06b6d4;
            --accent3: #a855f7;
            --text: #cdd6f4;
            --text2: #a6adc8;
            --text3: #6c7086;
            --card: #1e2139;
            --card2: #252640;
            --border: #313244;
            --border2: #414268;
            --green: #a6e3a1;
            --yellow: #f9e2af;
            --blue: #89b4fa;
            --pink: #cba6f7;
            --red: #f38ba8;
        }}

        html {{
            scroll-behavior: smooth;
        }}

        body {{
            font-family: 'Segoe UI', 'Inter', sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }}

        ::-webkit-scrollbar {{
            width: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: var(--bg);
        }}

        ::-webkit-scrollbar-thumb {{
            background: var(--accent);
            border-radius: 4px;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 3rem 2rem;
        }}

        .resume-header {{
            text-align: center;
            margin-bottom: 3rem;
            padding-bottom: 2rem;
            border-bottom: 2px solid var(--border);
        }}

        .name {{
            font-size: 2.8rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            letter-spacing: -0.02em;
            background: linear-gradient(135deg, var(--text), var(--accent2));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .title {{
            font-size: 1.1rem;
            color: var(--accent2);
            font-weight: 500;
            margin-bottom: 1rem;
            letter-spacing: 0.05em;
        }}

        .contact-info {{
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            flex-wrap: wrap;
            font-size: 0.85rem;
            color: var(--text2);
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .contact-link {{
            color: var(--accent2);
            text-decoration: none;
            transition: color 0.2s;
        }}

        .contact-link:hover {{
            color: var(--accent);
        }}

        section {{
            margin-bottom: 2.5rem;
        }}

        .section-title {{
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--accent2);
            margin-bottom: 1.25rem;
            padding-bottom: 0.75rem;
            border-bottom: 2px solid var(--accent);
            display: flex;
            align-items: center;
            gap: 0.75rem;
            letter-spacing: 0.03em;
        }}

        .section-title::before {{
            content: '';
            display: inline-block;
            width: 4px;
            height: 1.3rem;
            background: linear-gradient(180deg, var(--accent), var(--accent2));
            border-radius: 2px;
        }}

        .summary {{
            background: rgba(26, 27, 46, 0.6);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.5rem;
            color: var(--text2);
            line-height: 1.8;
            font-size: 0.95rem;
            backdrop-filter: blur(10px);
        }}

        .entry {{
            margin-bottom: 1.75rem;
            padding-bottom: 1.75rem;
            border-bottom: 1px solid var(--border2);
        }}

        .entry:last-child {{
            border-bottom: none;
            padding-bottom: 0;
            margin-bottom: 0;
        }}

        .entry-title {{
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text);
        }}

        .entry-company {{
            color: var(--accent2);
            font-weight: 500;
        }}

        .entry-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
            font-size: 0.9rem;
            color: var(--text3);
            flex-wrap: wrap;
            gap: 1rem;
        }}

        .entry-date {{
            color: var(--accent3);
            font-family: 'Courier New', monospace;
        }}

        .entry-description {{
            color: var(--text2);
            line-height: 1.7;
        }}

        .entry-description ul {{
            margin-left: 1.25rem;
            margin-top: 0.75rem;
        }}

        .entry-description li {{
            margin-bottom: 0.5rem;
        }}

        .metric-item {{
            display: inline-block;
            background: rgba(124, 58, 237, 0.1);
            color: var(--accent);
            padding: 0.35rem 0.75rem;
            border-radius: 4px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-right: 0.5rem;
            margin-bottom: 0.5rem;
            border: 1px solid rgba(124, 58, 237, 0.3);
        }}

        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }}

        .skill-category {{
            background: rgba(26, 27, 46, 0.6);
            border: 1px solid var(--border);
            border-radius: 8px;
            padding: 1.25rem;
            backdrop-filter: blur(10px);
        }}

        .skill-category-title {{
            color: var(--accent2);
            font-weight: 600;
            margin-bottom: 0.75rem;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .skill-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }}

        .skill-tag {{
            background: rgba(6, 182, 212, 0.15);
            color: var(--accent2);
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
            font-size: 0.8rem;
            border: 1px solid rgba(6, 182, 212, 0.3);
            transition: all 0.2s;
        }}

        .skill-tag:hover {{
            background: rgba(6, 182, 212, 0.25);
            border-color: var(--accent2);
        }}

        .metrics-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
            font-size: 0.9rem;
        }}

        .metrics-table th,
        .metrics-table td {{
            padding: 0.75rem 1rem;
            text-align: left;
            border-bottom: 1px solid var(--border2);
        }}

        .metrics-table th {{
            background: rgba(124, 58, 237, 0.1);
            color: var(--accent2);
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 0.03em;
        }}

        .metrics-table tr:hover {{
            background: rgba(6, 182, 212, 0.05);
        }}

        .metrics-value {{
            color: var(--accent);
            font-weight: 600;
            font-family: 'Courier New', monospace;
        }}

        .footer {{
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
            color: var(--text3);
            font-size: 0.85rem;
            margin-top: 2rem;
        }}

        .footer-text {{
            margin: 0.5rem 0;
        }}

        @media print {{
            body {{
                background: white;
                color: black;
            }}

            .container {{
                max-width: 100%;
                padding: 0;
            }}

            section {{
                page-break-inside: avoid;
            }}

            .section-title {{
                color: #1a1b2e;
                border-color: #7c3aed;
            }}
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 2rem 1rem;
            }}

            .name {{
                font-size: 2rem;
            }}

            .contact-info {{
                flex-direction: column;
                gap: 0.75rem;
                align-items: center;
            }}

            .skills-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="resume-header">
            <h1 class="name">{name}</h1>
            <p class="title">{title}</p>
            <div class="contact-info">
                <div class="contact-item">📧 <a href="mailto:{email}" class="contact-link">{email}</a></div>
                <div class="contact-item">📱 {phone}</div>
                <div class="contact-item">📍 {location}</div>
            </div>
        </div>

        <section>
            <h2 class="section-title">Professional Summary</h2>
            <div class="summary">
                {summary_html}
            </div>
        </section>

        <section>
            <h2 class="section-title">Professional Experience</h2>
            {experience_html}
        </section>

        <section>
            <h2 class="section-title">Technical Skills</h2>
            {skills_html}
        </section>

        <section>
            <h2 class="section-title">Education</h2>
            {education_html}
        </section>

        <div class="footer">
            <p class="footer-text">💡 Designed with a focus on clarity, impact, and modern web standards</p>
            <p class="footer-text">📄 Print-friendly • 📱 Mobile-responsive • ♿ Accessible</p>
            <p class="footer-text">🔄 Auto-synced from resume.md on {timestamp}</p>
        </div>
    </div>
</body>
</html>
"""

        # Read markdown
        self.read_markdown()

        # Convert content to HTML
        summary_html = self.content['summary']
        experience_html = self.content['experience']
        skills_html = self.content['skills']
        education_html = self.content['education']

        # Format timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Fill template
        html = html_template.format(
            name=self.content['name'],
            title=self.content['title'],
            email=self.content['email'],
            phone=self.content['phone'],
            location=self.content['location'],
            summary_html=summary_html,
            experience_html=experience_html,
            skills_html=skills_html,
            education_html=education_html,
            timestamp=timestamp
        )

        return html

    def write_html(self):
        """Write generated HTML to file"""
        html = self.generate_html()
        with open(self.html_file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Generated: {self.html_file}")

    def sync(self):
        """Main sync function"""
        try:
            print("Syncing resume.md to resume.html...")
            self.write_html()
            print("SUCCESS! Resume updated.")
            return True
        except Exception as e:
            print(f"ERROR: {e}")
            return False


def main():
    """Main entry point"""
    import sys

    # Get current directory
    current_dir = Path(__file__).parent
    md_file = current_dir / "resume.md"
    html_file = current_dir / "resume.html"

    # Check if markdown file exists
    if not md_file.exists():
        print(f"❌ Error: {md_file} not found!")
        sys.exit(1)

    # Sync
    syncer = MarkdownToResume(str(md_file), str(html_file))
    success = syncer.sync()

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
