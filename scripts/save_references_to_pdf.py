#!/usr/bin/env python3
"""
Save offline PDF copies of all references listed in the formal bibliography of readme.md.

Behavior:
- Parses the "## Bibliography (formal)" section in readme.md.
- Extracts (number, title, url) for each entry.
- Downloads the content:
  - If the URL serves PDF (Content-Type: application/pdf or url endswith .pdf), save the bytes directly.
  - Otherwise, attempts to convert HTML to PDF using one of:
    1) pdfkit (wkhtmltopdf required)
    2) WeasyPrint
    3) xhtml2pdf
  - If no converter is available, saves the HTML snapshot (.html) as a fallback.
- Writes a manifest.csv documenting results.

Run:
  pip install -r requirements.txt
  python scripts/save_references_to_pdf.py
"""

import os
import re
import csv
import sys
from pathlib import Path
from typing import List, Tuple, Optional

import requests

# Optional converters; we'll import lazily in functions to avoid hard failures.
def try_pdfkit_from_url(url: str, out_pdf: str) -> bool:
    try:
        import pdfkit  # type: ignore
    except Exception:
        return False
    try:
        pdfkit.from_url(url, out_pdf)
        return os.path.exists(out_pdf) and os.path.getsize(out_pdf) > 0
    except Exception:
        return False

def try_weasyprint_from_html(html: str, base_url: str, out_pdf: str) -> bool:
    try:
        from weasyprint import HTML  # type: ignore
    except Exception:
        return False
    try:
        HTML(string=html, base_url=base_url).write_pdf(out_pdf)
        return os.path.exists(out_pdf) and os.path.getsize(out_pdf) > 0
    except Exception:
        return False

def try_xhtml2pdf_from_html(html: str, out_pdf: str) -> bool:
    try:
        from xhtml2pdf import pisa  # type: ignore
    except Exception:
        return False
    try:
        with open(out_pdf, "wb") as f_out:
            result = pisa.CreatePDF(html, dest=f_out)
        return (result.err == 0) and os.path.exists(out_pdf) and os.path.getsize(out_pdf) > 0
    except Exception:
        return False

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "readme.md"
OUT_DIR = ROOT / "references"
MANIFEST = OUT_DIR / "manifest.csv"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) CosineGenie/1.0 Safari/537.36"

def sanitize_filename(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[\\/*?:\"<>|]+", "", s)
    s = re.sub(r"\s+", " ", s)
    return s[:150]

def parse_bibliography(readme_text: str) -> List[Tuple[str, str, str]]:
    """
    Returns a list of tuples: (number, title, url)
    """
    lines = readme_text.splitlines()
    refs: List[Tuple[str, str, str]] = []
    in_biblio = False
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("## bibliography"):
            in_biblio = True
            continue
        if in_biblio:
            if line.strip().lower().startswith("notes:"):
                break
            # Match lines like:
            # <a id="ref1"></a> (1) McNabb, Miriam. “Title…” DRONELIFE, Oct 11, 2023. https://example.com/path
            if '<a id="' in line and ')' in line:
                # Extract number inside parentheses
                m_num = re.search(r"\((\d+)\)", line)
                num = m_num.group(1) if m_num else ""
                # Extract URL as last http(s) token
                m_url = re.search(r"(https?://\S+)", line)
                url = m_url.group(1) if m_url else ""
                # Title as the part between the number and the URL
                title_part = line
                if url:
                    title_part = line.split(url)[0]
                # Remove anchor and leading numbering fragment
                title_part = re.sub(r"^\s*<a id=\"ref\d+\"></a>\s*\(\d+\)\s*", "", title_part).strip()
                title = title_part
                if num and url:
                    refs.append((num, title, url))
    return refs

def fetch_url(url: str) -> requests.Response:
    headers = {"User-Agent": USER_AGENT}
    resp = requests.get(url, headers=headers, timeout=45)
    resp.raise_for_status()
    return resp

def save_direct_pdf(num: str, title: str, url: str, resp: requests.Response) -> Tuple[str, str]:
    fname = f"{sanitize_filename(num + ' - ' + title)}.pdf"
    out_path = OUT_DIR / fname
    with open(out_path, "wb") as f:
        f.write(resp.content)
    return str(out_path), "saved-pdf-direct"

def save_html_snapshot(num: str, title: str, url: str, html: str) -> Tuple[str, str]:
    fname = f"{sanitize_filename(num + ' - ' + title)}.html"
    out_path = OUT_DIR / fname
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"<!-- Source: {url} -->\n")
        f.write(html)
    return str(out_path), "saved-html"

def convert_html_to_pdf(num: str, title: str, url: str, html: str) -> Tuple[str, str]:
    fname_pdf = f"{sanitize_filename(num + ' - ' + title)}.pdf"
    out_pdf = OUT_DIR / fname_pdf

    # Try pdfkit from URL first (best fidelity if wkhtmltopdf is installed)
    if try_pdfkit_from_url(url, str(out_pdf)):
        return str(out_pdf), "converted-pdf-pdfkit-url"

    # Try WeasyPrint from HTML
    if try_weasyprint_from_html(html, url, str(out_pdf)):
        return str(out_pdf), "converted-pdf-weasyprint-html"

    # Try xhtml2pdf from HTML
    if try_xhtml2pdf_from_html(html, str(out_pdf)):
        return str(out_pdf), "converted-pdf-xhtml2pdf-html"

    # Fallback: save HTML snapshot
    return save_html_snapshot(num, title, url, html)

def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if not README_PATH.exists():
        print(f"Error: README not found at {README_PATH}", file=sys.stderr)
        sys.exit(1)

    readme_text = README_PATH.read_text(encoding="utf-8")
    refs = parse_bibliography(readme_text)
    if not refs:
        print("No references found in bibliography section.", file=sys.stderr)
        sys.exit(1)

    rows = []
    print(f"Found {len(refs)} references. Starting download/conversion...\n")

    for num, title, url in refs:
        print(f"[{num}] {title} -> {url}")
        status = ""
        out_path = ""
        content_type = ""
        try:
            resp = fetch_url(url)
            content_type = resp.headers.get("Content-Type", "")
            # If PDF
            if url.lower().endswith(".pdf") or "application/pdf" in content_type.lower():
                out_path, status = save_direct_pdf(num, title, url, resp)
            else:
                # Convert HTML to PDF
                html = resp.text
                out_path, status = convert_html_to_pdf(num, title, url, html)
            print(f" -> {status}: {out_path}\n")
        except Exception as e:
            status = f"error: {e.__class__.__name__}: {e}"
            out_path = ""
            print(f" -> {status}\n")

        rows.append({
            "number": num,
            "title": title,
            "url": url,
            "output_path": out_path,
            "content_type": content_type,
            "status": status,
        })

    # Write manifest
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["number", "title", "url", "output_path", "content_type", "status"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Done. Manifest written to {MANIFEST}")
    print(f"Outputs saved in {OUT_DIR}")

if __name__ == "__main__":
    main()