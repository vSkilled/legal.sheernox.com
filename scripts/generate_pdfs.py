#!/usr/bin/env python3
"""
Sheernox Legal Portal - Automated PDF Generator
===============================================
Generates high-fidelity, vector-grade PDF legal policy documents from HTML sources
using the "Variation 1: Modern Tech Enterprise" styling layout.

Usage:
  python3 scripts/generate_pdfs.py              # Generate all 4 documents
  python3 scripts/generate_pdfs.py --doc aup    # Generate only AUP
  python3 scripts/generate_pdfs.py --doc tos    # Generate only Terms and Conditions
  python3 scripts/generate_pdfs.py --doc wdt    # Generate only Web Design Terms
  python3 scripts/generate_pdfs.py --doc priv   # Generate only Privacy Policy

Requirements:
  - Python 3.8+
  - beautifulsoup4 (`pip install beautifulsoup4`)
  - Headless Chromium-based browser (Brave, Google Chrome, or Chromium)
"""

import os
import sys
import shutil
import argparse
import tempfile
import subprocess
from pathlib import Path
from bs4 import BeautifulSoup

try:
    from logo_data import LOGO_BASE64
except ImportError:
    # Allow running directly from repo root or scripts/ dir
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from logo_data import LOGO_BASE64

REPO_ROOT = Path(__file__).resolve().parent.parent
PDF_DIR = REPO_ROOT / "pdf"

LAST_REVISED_DATE = "2026-09-11"

DOC_REGISTRY = {
    "aup": {
        "source": "acceptable-use-policy.html",
        "category": "Network & Cloud Infrastructure Policy",
        "title": "Acceptable Use Policy (AUP)",
        "version": "v3.5-AUP",
        "last_revised": "2026-09-11",
        "output_pdf": "Acceptable_Use_Policy.pdf",
        "accent_color": "#d97706",
    },
    "tos": {
        "source": "terms-and-conditions.html",
        "category": "Master Services Agreement",
        "title": "Terms and Conditions of Service",
        "version": "v4.0-TOS",
        "last_revised": "2026-09-12",
        "output_pdf": "Terms_and_Conditions.pdf",
        "accent_color": "#0284c7",
    },
    "wdt": {
        "source": "web-design-terms.html",
        "category": "Agency Services Agreement",
        "title": "Web Design & Development Terms and Conditions",
        "version": "v3.0-WDT",
        "last_revised": "2026-09-11",
        "output_pdf": "Web_Design_Terms_and_Conditions.pdf",
        "accent_color": "#ea580c",
    },
    "priv": {
        "source": "privacy-policy.html",
        "category": "Privacy & Data Protection Policy",
        "title": "Privacy & Personal Information Policy",
        "version": "v4.0-PRIV",
        "last_revised": "2026-09-12",
        "output_pdf": "Privacy_Policy.pdf",
        "accent_color": "#059669",
    },
    "sla": {
        "source": "service-level-agreement.html",
        "category": "Cloud Infrastructure & Operations",
        "title": "Service Level Agreement & Incident Policy",
        "version": "v1.0-SLA",
        "last_revised": "2026-09-12",
        "output_pdf": "Service_Level_Agreement.pdf",
        "accent_color": "#2563eb",
    },
    "vdp": {
        "source": "vulnerability-disclosure-policy.html",
        "category": "Cybersecurity & Trust Governance",
        "title": "Vulnerability Disclosure Policy (VDP)",
        "version": "v1.0-VDP",
        "last_revised": "2026-09-12",
        "output_pdf": "Vulnerability_Disclosure_Policy.pdf",
        "accent_color": "#7c3aed",
    },
    "cpr": {
        "source": "copyright-policy.html",
        "category": "Intellectual Property & Compliance",
        "title": "Copyright & Notice-and-Notice Policy",
        "version": "v1.0-CPR",
        "last_revised": "2026-09-12",
        "output_pdf": "Copyright_Notice_and_Notice_Policy.pdf",
        "accent_color": "#e11d48",
    },
    "wcp": {
        "source": "website-care-plan-terms.html",
        "category": "Creative & Agency SOW Schedule",
        "title": "Website Care Plan & Maintenance Terms",
        "version": "v1.0-WCP",
        "last_revised": "2026-09-12",
        "output_pdf": "Website_Care_Plan_Terms.pdf",
        "accent_color": "#0d9488",
    },
}

def get_css(last_revised, version, accent_color="#0284c7"):
    return f"""
    @page {{
      size: letter portrait;
      margin: 16mm 16mm 18mm 16mm;
      @bottom-left {{
        content: "Last Revised: {last_revised} \\2022  {version}";
        font-family: 'JetBrains Mono', monospace;
        font-size: 7.2pt;
        color: #64748b;
      }}
      @bottom-right {{
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Inter', sans-serif;
        font-size: 7.2pt;
        color: #64748b;
      }}
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      font-size: 8.8pt;
      line-height: 1.52;
      color: #1e293b;
      background: #ffffff;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }}

    /* Top Brand Header */
    .brand-header {{
      background: #071322;
      color: #ffffff;
      padding: 12px 18px;
      border-radius: 6px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
      break-inside: avoid;
    }}

    .brand-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .brand-logo {{
      height: 22px;
      width: auto;
    }}

    .brand-divider {{
      height: 18px;
      width: 1px;
      background: rgba(255, 255, 255, 0.2);
    }}

    .brand-subtitle {{
      font-size: 7.8pt;
      font-weight: 600;
      color: #94a3b8;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}

    .brand-badge {{
      font-size: 7.2pt;
      font-weight: 600;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 3px 8px;
      border-radius: 12px;
      letter-spacing: 0.03em;
    }}

    /* Document Title Block */
    .title-block {{
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 12px;
      margin-bottom: 14px;
      break-inside: avoid;
    }}

    .doc-category {{
      font-size: 7.5pt;
      font-weight: 700;
      color: {accent_color};
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 3px;
    }}

    .doc-title {{
      font-size: 18pt;
      font-weight: 800;
      color: #071322;
      letter-spacing: -0.02em;
      line-height: 1.2;
      margin-bottom: 8px;
    }}

    /* Metadata Info Row */
    .doc-meta-strip {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 8.2pt;
      color: #64748b;
    }}

    .meta-date strong {{
      color: #0f172a;
      font-weight: 700;
    }}

    /* Colored Version Pill Tag */
    .version-pill {{
      display: inline-flex;
      align-items: center;
      background: {accent_color}1a;
      color: {accent_color};
      border: 1px solid {accent_color}4d;
      font-family: 'JetBrains Mono', monospace;
      font-size: 7.2pt;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 9999px;
      letter-spacing: 0.02em;
    }}

    /* Critical Warning Box */
    .critical-alert-box, .alert-box {{
      background: #fffbeb;
      border: 1px solid #fde68a;
      border-left: 4px solid #f59e0b;
      padding: 9px 13px;
      border-radius: 6px;
      margin: 12px 0;
      display: flex;
      gap: 10px;
      align-items: flex-start;
      break-inside: avoid;
    }}

    .alert-icon {{
      font-size: 11pt;
      line-height: 1;
    }}

    .critical-alert-box h3, .alert-content h4 {{
      font-size: 8pt;
      font-weight: 700;
      color: #92400e;
      text-transform: uppercase;
      letter-spacing: 0.03em;
      margin-bottom: 2px;
    }}

    .critical-alert-box p, .alert-content p {{
      font-size: 8.2pt;
      color: #b45309;
      line-height: 1.45;
      margin-bottom: 0;
    }}

    /* Statutory Callouts */
    .statutory-callout {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-left: 3.5px solid #0f172a;
      padding: 9px 13px;
      border-radius: 6px;
      margin: 10px 0;
      break-inside: avoid;
    }}

    .statutory-header {{
      display: flex;
      align-items: center;
      gap: 6px;
      font-size: 7.5pt;
      font-weight: 700;
      color: #0f172a;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 4px;
    }}

    .statutory-content {{
      font-size: 7.8pt;
      line-height: 1.45;
      color: #334155;
      text-align: justify;
    }}

    /* Plain English Callout */
    .key-takeaway, .takeaway-card {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid {accent_color};
      padding: 8px 12px;
      border-radius: 6px;
      margin: 9px 0 11px 0;
      break-inside: avoid;
    }}

    .takeaway-badge {{
      display: inline-block;
      font-size: 6.8pt;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      background: {accent_color};
      color: #ffffff;
      padding: 2px 6px;
      border-radius: 4px;
      margin-bottom: 4px;
    }}

    .key-takeaway p, .takeaway-card p {{
      font-size: 8.2pt;
      color: #334155;
      line-height: 1.42;
      font-weight: 500;
      margin-bottom: 0;
    }}

    /* Section Structure */
    .legal-section {{
      margin-bottom: 14px;
      break-inside: auto;
    }}

    .section-header {{
      margin-top: 14px;
      margin-bottom: 8px;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 4px;
      break-after: avoid;
      break-inside: avoid;
    }}

    .section-title {{
      font-size: 10.8pt;
      font-weight: 700;
      color: #071322;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .section-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 9.5pt;
      font-weight: 700;
      color: {accent_color};
      margin-right: 6px;
    }}

    p {{
      margin-bottom: 6px;
      color: #334155;
      text-align: justify;
      font-size: 8.6pt;
      line-height: 1.5;
    }}

    /* Clause Blocks */
    .clause-block {{
      margin-bottom: 8px;
      break-inside: avoid;
    }}

    .clause-num {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 8.2pt;
      font-weight: 700;
      color: {accent_color};
      margin-right: 5px;
      display: inline;
    }}

    /* Lists */
    ul, ol {{
      margin: 6px 0 8px 20px;
    }}

    li {{
      font-size: 8.5pt;
      line-height: 1.48;
      color: #334155;
      margin-bottom: 4px;
    }}

    .legal-sublist, .sub-list {{
      list-style-type: lower-alpha;
      margin: 4px 0 6px 20px;
    }}

    .legal-sublist li, .sub-list li {{
      margin-bottom: 3px;
      font-size: 8.2pt;
    }}

    /* Custom Numbered Lists */
    .legal-counter-list {{
      list-style-type: none;
      counter-reset: aup-counter;
      margin: 8px 0;
    }}

    .legal-counter-list > li {{
      counter-increment: aup-counter;
      position: relative;
      padding-left: 28px;
      margin-bottom: 7px;
      font-size: 8.5pt;
      line-height: 1.48;
      color: #334155;
      break-inside: avoid;
    }}

    .legal-counter-list > li::before {{
      content: counter(aup-counter);
      position: absolute;
      left: 0;
      top: 1px;
      width: 19px;
      height: 19px;
      background: #f1f5f9;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 7pt;
      font-weight: 700;
      color: #0f4c81;
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Tables */
    table, .sla-table, .summary-table {{
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-size: 8pt;
      break-inside: avoid;
    }}

    th, td {{
      border: 1px solid #e2e8f0;
      padding: 6px 8px;
      text-align: left;
    }}

    th {{
      background: #f8fafc;
      font-weight: 700;
      color: #0f172a;
    }}

    tr:nth-child(even) {{
      background: #fbfcfe;
    }}

    /* Badges & Tags */
    .sec-badge, .status-badge {{
      display: inline-block;
      font-size: 7pt;
      padding: 2px 6px;
      border-radius: 4px;
      background: #e2e8f0;
      color: #334155;
      font-weight: 600;
    }}

    code {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 8pt;
      background: #f1f5f9;
      padding: 1px 4px;
      border-radius: 3px;
      color: #0f172a;
    }}

    a {{
      color: {accent_color};
      text-decoration: none;
    }}

    /* Interactive Elements Hidden in Print */
    .clause-anchor-btn, .btn-action, .toc-card, .search-box, .hero-actions {{
      display: none !important;
    }}

    /* Final Document Sign-off */
    .doc-footer {{
      margin-top: 24px;
      padding-top: 12px;
      border-top: 1.5px solid #e2e8f0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 7.4pt;
      color: #64748b;
      break-inside: avoid;
    }}

    .footer-left {{
      font-family: 'Inter', sans-serif;
    }}

    .footer-right {{
      font-family: 'JetBrains Mono', monospace;
    }}
    """

def find_browser(preferred_bin=None):
    if preferred_bin and shutil.which(preferred_bin):
        return preferred_bin
    
    env_bin = os.environ.get("CHROME_BIN")
    if env_bin and shutil.which(env_bin):
        return env_bin

    candidates = [
        "brave",
        "brave-browser",
        "google-chrome",
        "google-chrome-stable",
        "chromium",
        "chromium-browser",
        "/usr/bin/brave",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium",
    ]
    for c in candidates:
        found = shutil.which(c)
        if found:
            return found
    return None

def build_print_html(source_path, category, title, version, last_revised, accent_color="#0284c7"):
    with open(source_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    article = soup.find("article", class_="legal-prose")
    if not article:
        raise ValueError(f"Could not find <article class='legal-prose'> in {source_path}")

    # Remove anchor copy buttons & scripts
    for btn in article.find_all("button", class_="clause-anchor-btn"):
        btn.decompose()
    for s in article.find_all("script"):
        s.decompose()

    article_html = str(article)
    css_content = get_css(last_revised, version, accent_color)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title} - Sheernox Technology Group</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
{css_content}
  </style>
</head>
<body>

  <!-- Brand Header -->
  <div class="brand-header">
    <div class="brand-left">
      <img src="data:image/png;base64,{LOGO_BASE64}" alt="Sheernox" class="brand-logo">
      <div class="brand-divider"></div>
      <span class="brand-subtitle">Legal &amp; Regulatory Documentation</span>
    </div>
    <div class="brand-badge">British Columbia &bull; Canada</div>
  </div>

  <!-- Title Block with ISO 8601 Last Revised Date & Colored Version Tag -->
  <div class="title-block">
    <div class="doc-category">{category}</div>
    <h1 class="doc-title">{title}</h1>
    <div class="doc-meta-strip">
      <span class="meta-date">Last Revised: <strong>{last_revised}</strong></span>
      <span class="version-pill">{version}</span>
    </div>
  </div>

  <!-- Document Body Content -->
  {article_html}

  <!-- Footer -->
  <div class="doc-footer">
    <div class="footer-left">&copy; 2026 Sheernox Technology Group &bull; 1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada &bull; All Rights Reserved</div>
    <div class="footer-right">Last Revised: {last_revised} // {version}</div>
  </div>

</body>
</html>
"""

def render_doc(browser_bin, key, doc_info, temp_dir):
    source_file = REPO_ROOT / doc_info["source"]
    dest_pdf = PDF_DIR / doc_info["output_pdf"]

    if not source_file.exists():
        print(f"[-] Source file not found: {source_file}", file=sys.stderr)
        return False

    print(f"[*] Preparing HTML for: {doc_info['title']} ({doc_info['version']})")
    html_markup = build_print_html(
        source_file,
        doc_info["category"],
        doc_info["title"],
        doc_info["version"],
        doc_info.get("last_revised", LAST_REVISED_DATE),
        doc_info.get("accent_color", "#0284c7"),
    )

    temp_html = Path(temp_dir) / f"{key}_print.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_markup)

    print(f"[*] Compiling vector PDF -> {dest_pdf.relative_to(REPO_ROOT)}")
    cmd = [
        browser_bin,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={dest_pdf}",
        str(temp_html),
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[-] Failed to compile {dest_pdf.name}: {res.stderr}", file=sys.stderr)
        return False

    size_kb = dest_pdf.stat().st_size / 1024
    print(f"[+] Successfully generated: {dest_pdf.name} ({size_kb:.1f} KB)")
    return True

def main():
    parser = argparse.ArgumentParser(description="Generate Sheernox Legal Portal PDF Documents")
    parser.add_argument(
        "--doc",
        choices=list(DOC_REGISTRY.keys()) + ["privacy", "all"],
        default="all",
        help="Target document key (aup, tos, wdt, priv/privacy, sla, vdp, cpr, wcp, all)",
    )
    parser.add_argument("--browser", default=None, help="Explicit path to Chrome/Brave/Chromium executable")
    args = parser.parse_args()

    browser_bin = find_browser(args.browser)
    if not browser_bin:
        print(
            "[-] Error: No headless Chromium browser found (brave, google-chrome, or chromium). "
            "Please install one or set CHROME_BIN.",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"[i] Using browser binary: {browser_bin}")
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    targets = list(DOC_REGISTRY.keys())
    if args.doc not in ["all", "privacy"]:
        targets = [args.doc]
    elif args.doc == "privacy":
        targets = ["priv"]

    success_count = 0
    with tempfile.TemporaryDirectory() as temp_dir:
        for key in targets:
            ok = render_doc(browser_bin, key, DOC_REGISTRY[key], temp_dir)
            if ok:
                success_count += 1

    print(f"\n[✓] Completed: {success_count}/{len(targets)} PDF(s) generated successfully in {PDF_DIR.relative_to(REPO_ROOT)}/")
    if success_count < len(targets):
        sys.exit(1)

if __name__ == "__main__":
    main()
