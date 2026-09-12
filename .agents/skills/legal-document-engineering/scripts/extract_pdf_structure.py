#!/usr/bin/env python3
"""
Extract text and structure from legal PDFs for HTML conversion.
Preserves paragraphs, headers, and section markers while cleaning up
running headers, footers, and page numbers.
"""

import sys
import re
import subprocess
from pathlib import Path

def extract_clean_text(pdf_path: str) -> str:
    # Use pdftotext with layout preservation
    result = subprocess.run(
        ["pdftotext", "-layout", pdf_path, "-"],
        capture_output=True,
        text=True,
        check=True
    )
    raw = result.stdout
    
    # Remove form feed characters
    pages = raw.split("\x0c")
    cleaned_pages = []
    
    for page in pages:
        lines = page.splitlines()
        filtered = []
        for line in lines:
            # Strip footer like "Page X of Y"
            if re.match(r"^\s*Page\s+\d+\s+of\s+\d+\s*$", line):
                continue
            filtered.append(line)
        cleaned_pages.append("\n".join(filtered))
        
    return "\n\n".join(cleaned_pages)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <path_to_pdf>")
        sys.exit(1)
        
    pdf_file = sys.argv[1]
    text = extract_clean_text(pdf_file)
    out_file = Path(pdf_file).with_suffix(".extracted.txt")
    out_file.write_text(text, encoding="utf-8")
    print(f"Extracted {len(text)} characters to {out_file}")
