#!/usr/bin/env python3
"""
Sheernox Legal Portal - Plain Text (.TXT) Policy Generator
==========================================================
Generates high-fidelity, monospaced 80-column plain text versions of all legal
policy documents from built HTML sources, matching the styling of vulnerability-disclosure-policy.txt.

Usage:
  python3 scripts/generate_txts.py --source-dir dist --output-dir dist
  python3 scripts/generate_txts.py --doc sla
  python3 scripts/generate_txts.py --doc tos
  python3 scripts/generate_txts.py --force
"""

import os
import sys
import re
import argparse
import textwrap
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

REPO_ROOT = Path(__file__).resolve().parent.parent

DOC_REGISTRY = {
    "tos": {
        "source": "terms-and-conditions.html",
        "category": "Master Services Agreement",
        "title": "Terms and Conditions of Service",
        "version": "v4.5-TOS",
        "last_revised": "2026-09-13",
        "output_txt": "terms-and-conditions.txt",
        "output_pdf": "terms-and-conditions.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
    "aup": {
        "source": "acceptable-use-policy.html",
        "category": "Network & Cloud Infrastructure Policy",
        "title": "Acceptable Use Policy (AUP)",
        "version": "v4.0-AUP",
        "last_revised": "2026-09-12",
        "output_txt": "acceptable-use-policy.txt",
        "output_pdf": "acceptable-use-policy.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
    "wdt": {
        "source": "web-design-terms.html",
        "category": "Agency Services Agreement",
        "title": "Web Design & Development Terms and Conditions",
        "version": "v3.5-WDT",
        "last_revised": "2026-09-13",
        "output_txt": "web-design-terms.txt",
        "output_pdf": "web-design-terms.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
    "priv": {
        "source": "privacy-policy.html",
        "category": "Privacy & Data Protection Policy",
        "title": "Privacy & Personal Information Policy",
        "version": "v4.5-PRIV",
        "last_revised": "2026-09-13",
        "output_txt": "privacy-policy.txt",
        "output_pdf": "privacy-policy.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
    "sla": {
        "source": "service-level-agreement.html",
        "category": "Cloud Infrastructure & Operations",
        "title": "Service Level Agreement & Incident Policy (SLA)",
        "version": "v1.5-SLA",
        "last_revised": "2026-09-12",
        "output_txt": "service-level-agreement.txt",
        "output_pdf": "service-level-agreement.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
    "vdp": {
        "source": "vulnerability-disclosure-policy.html",
        "category": "Cybersecurity & Trust Governance",
        "title": "Vulnerability Disclosure Policy (VDP)",
        "version": "v1.5-VDP",
        "last_revised": "2026-09-12",
        "output_txt": "vulnerability-disclosure-policy.txt",
        "output_pdf": "vulnerability-disclosure-policy.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
    "cpr": {
        "source": "copyright-policy.html",
        "category": "Intellectual Property & Compliance",
        "title": "Copyright Notice & Notice-and-Notice Policy",
        "version": "v1.5-CPR",
        "last_revised": "2026-09-12",
        "output_txt": "copyright-policy.txt",
        "output_pdf": "copyright-policy.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
    "wcp": {
        "source": "website-care-plan-terms.html",
        "category": "Creative & Agency SOW Schedule",
        "title": "Website Care Plan & Maintenance Terms",
        "version": "v1.5-WCP",
        "last_revised": "2026-09-13",
        "output_txt": "website-care-plan-terms.txt",
        "output_pdf": "website-care-plan-terms.pdf",
        "support_email": "support@sheernox.com",
        "abuse_email": "abuse@sheernox.com",
    },
}

WIDTH = 80
DIVIDER_DOUBLE = "=" * WIDTH
DIVIDER_SINGLE = "-" * WIDTH

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def wrap_text(text, width=WIDTH, initial_indent="", subsequent_indent=""):
    text = clean_text(text)
    if not text:
        return ""
    return textwrap.fill(
        text,
        width=width,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent,
        break_long_words=False,
        break_on_hyphens=False
    )

def format_table(table_tag):
    rows = []
    headers = []
    
    thead = table_tag.find("thead")
    if thead:
        th_tags = thead.find_all(["th", "td"])
        headers = [clean_text(th.get_text()) for th in th_tags]
    
    tbody = table_tag.find("tbody") or table_tag
    for tr in tbody.find_all("tr"):
        td_tags = tr.find_all(["td", "th"])
        if not td_tags:
            continue
        row_vals = [clean_text(td.get_text()) for td in td_tags]
        if row_vals:
            rows.append(row_vals)
            
    if not rows and not headers:
        return ""
        
    num_cols = max(len(headers), max(len(r) for r in rows) if rows else 0)
    if num_cols == 0:
        return ""
        
    if headers and len(headers) < num_cols:
        headers.extend([""] * (num_cols - len(headers)))
    for r in rows:
        if len(r) < num_cols:
            r.extend([""] * (num_cols - len(r)))
            
    # Check if this table has dense prose (e.g. any cell > 60 chars or total width > 90)
    max_cell_len = max(max(len(c) for c in r) for r in rows) if rows else 0
    
    lines = []
    if num_cols <= 3 and max_cell_len < 65:
        # Aligned column table with wrapping
        # Calculate optimal column widths
        col_w = [len(h) for h in headers] if headers else [0] * num_cols
        for r in rows:
            for i, val in enumerate(r):
                col_w[i] = max(col_w[i], len(val))
                
        # Total spacing: 2 spaces between columns
        spacing = 2 * (num_cols - 1)
        avail = WIDTH - spacing
        
        # If total exceeds avail, adjust proportionally
        if sum(col_w) > avail:
            # First column(s) usually short, last column wraps
            if num_cols == 2:
                col_w[0] = min(col_w[0], 28)
                col_w[1] = avail - col_w[0]
            elif num_cols == 3:
                col_w[0] = min(col_w[0], 25)
                col_w[1] = min(col_w[1], 28)
                col_w[2] = avail - col_w[0] - col_w[1]
                
        if headers:
            header_lines = []
            max_h_lines = 1
            for i in range(num_cols):
                w = col_w[i]
                wrapped = textwrap.wrap(headers[i], width=w) if len(headers[i]) > w else [headers[i]]
                if not wrapped:
                    wrapped = [""]
                header_lines.append(wrapped)
                max_h_lines = max(max_h_lines, len(wrapped))
                
            for l_idx in range(max_h_lines):
                line_parts = []
                for i in range(num_cols):
                    val = header_lines[i][l_idx] if l_idx < len(header_lines[i]) else ""
                    line_parts.append(val.ljust(col_w[i]))
                lines.append("  ".join(line_parts).rstrip())
            lines.append("-" * min(WIDTH, sum(col_w) + spacing))
            
        for r in rows:
            cell_lines = []
            max_lines = 1
            for i in range(num_cols):
                w = col_w[i]
                wrapped = textwrap.wrap(r[i], width=w) if len(r[i]) > w else [r[i]]
                if not wrapped:
                    wrapped = [""]
                cell_lines.append(wrapped)
                max_lines = max(max_lines, len(wrapped))
                
            for l_idx in range(max_lines):
                line_parts = []
                for i in range(num_cols):
                    val = cell_lines[i][l_idx] if l_idx < len(cell_lines[i]) else ""
                    line_parts.append(val.ljust(col_w[i]))
                lines.append("  ".join(line_parts).rstrip())
    else:
        # Dense record block format
        lines.append(DIVIDER_SINGLE)
        for r_idx, r in enumerate(rows):
            # First item as heading
            item_title = r[0]
            lines.append(f"[{item_title}]")
            for c_idx in range(1, num_cols):
                h_label = headers[c_idx] if headers and c_idx < len(headers) else f"Field {c_idx}"
                val = r[c_idx]
                prefix = f"  {h_label}: "
                indent = " " * len(prefix)
                wrapped_val = textwrap.fill(val, width=WIDTH, initial_indent=prefix, subsequent_indent=indent)
                lines.append(wrapped_val)
            if r_idx < len(rows) - 1:
                lines.append("")
        lines.append(DIVIDER_SINGLE)
            
    return "\n".join(lines)

def build_txt_document(key, doc_info, source_dir=None):
    if source_dir is None:
        source_dir = REPO_ROOT / "dist" if (REPO_ROOT / "dist").exists() else REPO_ROOT
    source_file = Path(source_dir) / doc_info["source"]
    with open(source_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        
    article = soup.find("article", class_="legal-prose")
    if not article:
        raise ValueError(f"Could not find <article class='legal-prose'> in {source_file}")
        
    for btn in article.find_all("button", class_="clause-anchor-btn"):
        btn.decompose()
    for s in article.find_all("script"):
        s.decompose()
    for br in article.find_all("br"):
        br.replace_with(" ")
        
    lines = []
    
    # Header Banner
    lines.append(DIVIDER_DOUBLE)
    lines.append(f"SHEERNOX TECHNOLOGY GROUP - {doc_info['title'].upper()}")
    lines.append(DIVIDER_DOUBLE)
    lines.append(f"Document:       {doc_info['title']}")
    lines.append("Entity:         Sheernox Technology Group (Kamloops, BC, Canada)")
    lines.append(f"Version:        {doc_info['version']}")
    lines.append(f"Last Revised:   {doc_info['last_revised']}")
    lines.append(f"Web Policy:     https://legal.sheernox.com/{doc_info['source']}")
    lines.append(f"Plain Text:     https://legal.sheernox.com/{doc_info['output_txt']}")
    lines.append(f"PDF Document:   https://legal.sheernox.com/{doc_info['output_pdf']}")
    lines.append(f"General Admin:  {doc_info['support_email']}")
    lines.append(f"Abuse & Sec:    {doc_info['abuse_email']}")
    lines.append(DIVIDER_DOUBLE)
    lines.append("")
    
    sections = article.find_all("section", class_="legal-section")
    for sec in sections:
        h_tag = sec.find(["h2", "h3"], class_="section-title") or sec.find(["h2", "h3"])
        if h_tag:
            sec_num_tag = h_tag.find(class_="section-num")
            sec_num = clean_text(sec_num_tag.get_text()) if sec_num_tag else ""
            h_text = clean_text(h_tag.get_text())
            if sec_num and h_text.startswith(sec_num):
                h_text = h_text[len(sec_num):].strip()
                title_line = f"{sec_num} {h_text.upper()}"
            else:
                title_line = h_text.upper()
                
            lines.append(title_line)
            lines.append(DIVIDER_SINGLE)
            
        for elem in sec.children:
            if isinstance(elem, NavigableString):
                continue
            if not isinstance(elem, Tag):
                continue
            if elem == h_tag or elem.find(["h2", "h3"], class_="section-title"):
                continue
                
            classes = elem.get("class", [])
            
            if "key-takeaway" in classes:
                badge = elem.find(class_="takeaway-badge")
                badge_text = f"[{clean_text(badge.get_text()).upper()}]" if badge else "[IN PLAIN ENGLISH]"
                lines.append(badge_text)
                for p in elem.find_all("p"):
                    lines.append(wrap_text(p.get_text()))
                lines.append("")
                continue
                
            if "statutory-callout" in classes or "critical-alert-box" in classes:
                h = elem.find(["h4", "div", "span"], class_=["statutory-header", "alert-header"]) or elem.find("h4")
                h_text = f"[{clean_text(h.get_text()).upper()}]" if h else "[STATUTORY LEGAL NOTICE]"
                lines.append(DIVIDER_SINGLE)
                lines.append(h_text)
                body_elem = elem.find(class_=["statutory-content", "alert-body"]) or elem
                p_tags = body_elem.find_all(["p", "div"])
                found_text = False
                for p in p_tags:
                    if p != h and p.get_text().strip():
                        lines.append(wrap_text(p.get_text()))
                        found_text = True
                if not found_text:
                    raw_p = clean_text(elem.get_text())
                    if h and raw_p.startswith(clean_text(h.get_text())):
                        raw_p = raw_p[len(clean_text(h.get_text())):].strip()
                    lines.append(wrap_text(raw_p))
                lines.append(DIVIDER_SINGLE)
                lines.append("")
                continue
                
            if "clause-block" in classes:
                c_num_tag = elem.find(class_="clause-num")
                c_num = clean_text(c_num_tag.get_text()) if c_num_tag else ""
                
                c_title_tag = elem.find(["h3", "h4", "strong"], class_="clause-title") or elem.find("strong")
                c_title = clean_text(c_title_tag.get_text()) if c_title_tag else ""
                
                if c_num and c_title.startswith(c_num):
                    c_title = c_title[len(c_num):].strip().lstrip(".:-— ")
                    
                paragraphs = elem.find_all("p")
                if paragraphs:
                    for p_idx, p in enumerate(paragraphs):
                        p_text = clean_text(p.get_text())
                        if p_idx == 0 and (c_num or c_title):
                            lead = f"{c_num} {c_title}".strip()
                            if not lead.endswith(":"):
                                lead = f"{lead}:"
                            lines.append(lead)
                            
                            rest_text = p_text
                            if c_num and rest_text.startswith(c_num):
                                rest_text = rest_text[len(c_num):].strip()
                            if c_title and rest_text.startswith(c_title):
                                rest_text = rest_text[len(c_title):].strip()
                            if rest_text.startswith(":") or rest_text.startswith("-") or rest_text.startswith("—"):
                                rest_text = rest_text.lstrip(":—- ").strip()
                                
                            if rest_text:
                                lines.append(wrap_text(rest_text, width=WIDTH, initial_indent="    ", subsequent_indent="    "))
                        else:
                            lines.append(wrap_text(p_text, width=WIDTH, initial_indent="    ", subsequent_indent="    "))
                else:
                    raw_text = clean_text(elem.get_text())
                    lines.append(wrap_text(raw_text, width=WIDTH, initial_indent="    ", subsequent_indent="    "))
                
                for ul in elem.find_all(["ul", "ol"]):
                    for li in ul.find_all("li"):
                        lines.append(wrap_text(f"- {li.get_text()}", width=WIDTH, initial_indent="    ", subsequent_indent="      "))
                
                pills = [clean_text(s.get_text()) for s in elem.find_all(class_="service-grid-pill")]
                if pills:
                    for pill in pills:
                        lines.append(wrap_text(f"- {pill}", width=WIDTH, initial_indent="    ", subsequent_indent="      "))
                        
                lines.append("")
                continue
                
            if elem.name == "p":
                p_text = clean_text(elem.get_text())
                if p_text:
                    lines.append(wrap_text(p_text))
                    lines.append("")
                continue
                
            if elem.name in ["ul", "ol"]:
                for li in elem.find_all("li", recursive=False) or elem.find_all("li"):
                    c_num = li.find(class_="clause-num")
                    c_title = li.find("strong")
                    li_text = clean_text(li.get_text())
                    if c_num and c_title:
                        num_str = clean_text(c_num.get_text())
                        title_str = clean_text(c_title.get_text())
                        rest = li_text
                        if rest.startswith(num_str):
                            rest = rest[len(num_str):].strip()
                        if rest.startswith(title_str):
                            rest = rest[len(title_str):].strip()
                        rest = rest.lstrip("—-: ").strip()
                        lead = f"{num_str} {title_str}"
                        if not lead.endswith(":"):
                            lead += ":"
                        lines.append(lead)
                        lines.append(wrap_text(rest, width=WIDTH, initial_indent="    ", subsequent_indent="    "))
                        lines.append("")
                    else:
                        lines.append(wrap_text(f"- {li_text}", width=WIDTH, initial_indent="", subsequent_indent="  "))
                lines.append("")
                continue
                
            if elem.name == "table" or elem.find("table"):
                table = elem if elem.name == "table" else elem.find("table")
                t_str = format_table(table)
                if t_str:
                    lines.append(t_str)
                    lines.append("")
                continue
                
        lines.append("")
        
    lines.append(DIVIDER_DOUBLE)
    lines.append("OFFICIAL CONTACT & GOVERNING JURISDICTION COORDINATES")
    lines.append(DIVIDER_SINGLE)
    lines.append("Entity:                  Sheernox Technology Group (Sole Proprietorship)")
    lines.append("Registration Number:     FM0707819 (Province of British Columbia)")
    lines.append("Business Number:         732754924BC0001 (Canada Revenue Agency)")
    lines.append("Physical Address:        1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada")
    lines.append("Governing Law:           Province of British Columbia and Federal Laws of Canada")
    lines.append("Exclusive Legal Venue:   Courts of British Columbia in Kamloops, BC, Canada")
    lines.append(f"General & Legal Inquiries: {doc_info['support_email']}")
    lines.append(f"Abuse & Security Incidents: {doc_info['abuse_email']}")
    lines.append("Client Support Hub:      https://my.sheernox.com")
    lines.append(DIVIDER_DOUBLE)
    lines.append("")
    
    final_output = "\n".join(lines)
    final_output = re.sub(r'\n{3,}', '\n\n', final_output).strip() + "\n"
    return final_output

def main():
    parser = argparse.ArgumentParser(description="Sheernox Plain Text Legal Policy Generator")
    parser.add_argument("--doc", choices=list(DOC_REGISTRY.keys()), help="Generate a specific policy document")
    parser.add_argument("--force", action="store_true", help="Force overwrite of all files including hand-crafted VDP")
    parser.add_argument("--source-dir", default=None, help="Directory containing source HTML files (default: dist/ or repo root)")
    parser.add_argument("--output-dir", default=None, help="Directory where TXTs will be written (default: dist/ or repo root)")
    args = parser.parse_args()
    
    source_dir = Path(args.source_dir) if args.source_dir else (REPO_ROOT / "dist" if (REPO_ROOT / "dist").exists() else REPO_ROOT)
    output_dir = Path(args.output_dir) if args.output_dir else (REPO_ROOT / "dist" if (REPO_ROOT / "dist").exists() else REPO_ROOT)
    output_dir.mkdir(parents=True, exist_ok=True)
    public_dir = REPO_ROOT / "public"

    targets = [args.doc] if args.doc else list(DOC_REGISTRY.keys())
    
    print(f"[*] Processing plain text generation for: {', '.join(targets)} (source: {source_dir}, dest: {output_dir})")
    for key in targets:
        info = DOC_REGISTRY[key]
        dest_file = output_dir / info["output_txt"]
        if key == "vdp" and dest_file.exists() and not args.force and not args.doc:
            print(f"[*] Preserving perfected hand-crafted {info['output_txt']} (use --force to overwrite)")
            continue
        print(f"[*] Generating: {info['title']} -> {dest_file}")
        content = build_txt_document(key, info, source_dir=source_dir)
        with open(dest_file, "w", encoding="utf-8") as f:
            f.write(content)
        
        # Also sync to public/ if public exists and output_dir is not public
        if public_dir.exists() and output_dir.resolve() != public_dir.resolve():
            pub_file = public_dir / info["output_txt"]
            with open(pub_file, "w", encoding="utf-8") as f:
                f.write(content)

        print(f"[+] Successfully wrote {len(content.splitlines())} lines to {info['output_txt']}")

if __name__ == "__main__":
    main()
