#!/usr/bin/env python3
"""Convert resume.md to PDF"""

import markdown2
from weasyprint import HTML, CSS
from pathlib import Path
import tempfile

def convert_md_to_pdf():
    """Convert markdown file to PDF"""

    # File paths
    md_file = Path(__file__).parent / "resume.md"
    pdf_file = Path(__file__).parent / "resume.pdf"

    print("Converting resume.md to PDF...")

    # Read markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert markdown to HTML
    html_content = markdown2.markdown(md_content, extras=['tables', 'fenced-code-blocks'])

    # Create full HTML document
    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Yashwanth HV - Resume</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Segoe UI', 'Calibri', sans-serif;
                line-height: 1.6;
                color: #333;
                background: white;
                padding: 40px;
            }}

            h1 {{
                font-size: 2.5em;
                margin-bottom: 0.5em;
                color: #1a1a1a;
            }}

            h2 {{
                font-size: 1.5em;
                margin-top: 1.5em;
                margin-bottom: 0.75em;
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 0.5em;
            }}

            h3 {{
                font-size: 1.2em;
                margin-top: 1em;
                margin-bottom: 0.5em;
                color: #34495e;
            }}

            p {{
                margin-bottom: 0.75em;
            }}

            ul, ol {{
                margin-left: 2em;
                margin-bottom: 1em;
            }}

            li {{
                margin-bottom: 0.4em;
            }}

            strong {{
                color: #2c3e50;
            }}

            em {{
                color: #555;
            }}

            a {{
                color: #3498db;
                text-decoration: none;
            }}

            a:hover {{
                text-decoration: underline;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1em 0;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 0.75em;
                text-align: left;
            }}

            th {{
                background-color: #ecf0f1;
                font-weight: bold;
            }}

            hr {{
                border: none;
                border-top: 2px solid #bdc3c7;
                margin: 2em 0;
            }}

            .contact-info {{
                text-align: center;
                color: #666;
                font-size: 0.95em;
                margin-bottom: 1.5em;
            }}

            @page {{
                margin: 0.75in;
                size: A4;
            }}

            @media print {{
                body {{
                    padding: 0;
                }}
                a {{
                    color: #2c3e50;
                }}
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Convert to PDF
    try:
        HTML(string=full_html).write_pdf(str(pdf_file))
        print(f"SUCCESS! PDF created: {pdf_file}")
        print(f"File size: {pdf_file.stat().st_size / 1024:.1f} KB")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    success = convert_md_to_pdf()
    exit(0 if success else 1)
