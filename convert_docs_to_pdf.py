#!/usr/bin/env python3
"""Convert all docs/*.md files to PDF using markdown + Playwright (Chromium)."""

import os
import sys
import glob
import asyncio
import tempfile
import markdown
from playwright.async_api import async_playwright

CSS_STYLE = """
    body {
        font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
        font-size: 12pt;
        line-height: 1.65;
        color: #1a1a1a;
        max-width: 820px;
        margin: 0 auto;
        padding: 20px;
    }

    h1 {
        font-size: 24pt;
        font-weight: 700;
        color: #0f172a;
        border-bottom: 2px solid #3b82f6;
        padding-bottom: 0.3em;
        margin-top: 1.2em;
        margin-bottom: 0.5em;
    }

    h2 {
        font-size: 17pt;
        font-weight: 600;
        color: #1e3a5f;
        border-bottom: 1px solid #d1d5db;
        padding-bottom: 0.2em;
        margin-top: 1.4em;
        margin-bottom: 0.4em;
    }

    h3 {
        font-size: 14pt;
        font-weight: 600;
        color: #374151;
        margin-top: 1.2em;
        margin-bottom: 0.3em;
    }

    h4, h5, h6 {
        font-size: 12pt;
        font-weight: 600;
        color: #4b5563;
        margin-top: 1em;
        margin-bottom: 0.2em;
    }

    p { margin: 0.5em 0 0.8em 0; }

    a { color: #2563eb; text-decoration: none; }

    code {
        font-family: "SF Mono", "Fira Code", "Consolas", monospace;
        font-size: 10pt;
        background: #f3f4f6;
        border: 1px solid #e5e7eb;
        border-radius: 3px;
        padding: 0.1em 0.35em;
    }

    pre {
        background: #1e293b;
        border-radius: 6px;
        padding: 1em 1.2em;
        overflow-x: auto;
        margin: 0.8em 0;
        page-break-inside: avoid;
    }

    pre code {
        background: transparent;
        border: none;
        color: #e2e8f0;
        font-size: 9.5pt;
        padding: 0;
        white-space: pre;
        word-wrap: normal;
    }

    blockquote {
        border-left: 4px solid #3b82f6;
        margin: 0.8em 0;
        padding: 0.4em 1em;
        background: #eff6ff;
        color: #1e3a5f;
        border-radius: 0 4px 4px 0;
    }

    blockquote p { margin: 0.2em 0; }

    table {
        border-collapse: collapse;
        width: 100%;
        margin: 0.8em 0;
        font-size: 10.5pt;
        page-break-inside: avoid;
    }

    th {
        background: #1e3a5f;
        color: white;
        font-weight: 600;
        padding: 0.5em 0.75em;
        text-align: left;
    }

    td {
        padding: 0.4em 0.75em;
        border-bottom: 1px solid #e5e7eb;
        vertical-align: top;
    }

    tr:nth-child(even) td { background: #f8fafc; }
    tr:last-child td { border-bottom: 2px solid #d1d5db; }

    ul, ol {
        padding-left: 1.6em;
        margin: 0.4em 0 0.8em 0;
    }

    li { margin: 0.25em 0; }
    li > ul, li > ol { margin: 0.2em 0; }

    hr {
        border: none;
        border-top: 2px solid #e5e7eb;
        margin: 1.5em 0;
    }

    strong { font-weight: 700; color: #111827; }
    em { font-style: italic; }
"""

# Playwright header/footer templates use a specific subset of HTML.
# Spans with class pageNumber / totalPages are replaced by Chrome.
# The font-size must be set inline; external CSS does not apply here.
FOOTER_TEMPLATE = """
<div style="
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2.5cm;
    font-family: -apple-system, Helvetica Neue, Arial, sans-serif;
    font-size: 8pt;
    color: #9ca3af;
    border-top: 1px solid #e5e7eb;
    box-sizing: border-box;
">
  <span>(c) Mui-Group</span>
  <span><span class="pageNumber"></span> / <span class="totalPages"></span></span>
</div>
"""

HEADER_TEMPLATE = "<div></div>"  # empty — suppresses default Chrome header


async def md_to_pdf_async(browser, md_path: str, pdf_path: str) -> None:
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    md_ext = ["extra", "toc", "nl2br", "sane_lists", "fenced_code"]
    html_body = markdown.markdown(md_text, extensions=md_ext)

    title = os.path.splitext(os.path.basename(md_path))[0].replace("_", " ").title()

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
  <style>{CSS_STYLE}</style>
</head>
<body>
{html_body}
</body>
</html>"""

    with tempfile.NamedTemporaryFile(suffix=".html", mode="w",
                                     encoding="utf-8", delete=False) as tf:
        tf.write(full_html)
        tmp_html = tf.name

    try:
        page = await browser.new_page()
        await page.goto(f"file://{tmp_html}", wait_until="networkidle")
        await page.pdf(
            path=pdf_path,
            format="Letter",
            margin={"top": "2cm", "bottom": "2.2cm", "left": "2.5cm", "right": "2.5cm"},
            display_header_footer=True,
            header_template=HEADER_TEMPLATE,
            footer_template=FOOTER_TEMPLATE,
            print_background=True,
        )
        await page.close()
    finally:
        os.unlink(tmp_html)


async def main():
    base = "/Users/pmui/dev/ai-foundations"
    pattern = os.path.join(base, "*/docs/*.md")
    md_files = sorted(glob.glob(pattern))

    if not md_files:
        print("No markdown files found.")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown files.\n")
    errors = []

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        for md_path in md_files:
            rel = os.path.relpath(md_path, base)
            pdf_path = os.path.splitext(md_path)[0] + ".pdf"
            try:
                await md_to_pdf_async(browser, md_path, pdf_path)
                size_kb = os.path.getsize(pdf_path) // 1024
                print(f"  [OK]  {rel}  ({size_kb} KB)")
            except Exception as e:
                print(f"  [ERR] {rel}: {e}")
                errors.append((rel, e))
        await browser.close()

    print(f"\nDone. {len(md_files) - len(errors)}/{len(md_files)} converted successfully.")
    if errors:
        print("\nErrors:")
        for path, err in errors:
            print(f"  {path}: {err}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
