# References Archive

This folder will contain offline PDF copies of all sources listed in the formal bibliography of `readme.md`.

How to populate this folder:
1. Ensure dependencies are installed:
   - `pip install -r requirements.txt`
   - If using `pdfkit`, install `wkhtmltopdf` on your system (optional but recommended).
2. Run the downloader:
   - `python scripts/save_references_to_pdf.py`
3. Outputs:
   - PDFs saved into this folder.
   - A manifest file `manifest.csv` summarizing each reference, the output filename, and conversion status.
   - If a source cannot be converted to PDF automatically, its HTML snapshot will be saved and noted in the manifest.

Notes:
- Direct PDF sources (e.g., links that end with `.pdf` or return `Content-Type: application/pdf`) are saved as-is.
- HTML sources are converted using one of: `pdfkit` (wkhtmltopdf), `WeasyPrint`, or `xhtml2pdf`. The script tries these in order and falls back to saving raw HTML if no converter is available.
- Filenames are sanitized for filesystem safety (e.g., removing special characters).