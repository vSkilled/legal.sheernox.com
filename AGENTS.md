# AI Agent Runbook & Repository Context

This document is the authoritative operational guide for AI coding agents (and developers) maintaining the **Sheernox Legal Portal**. If you are an AI tasked with updating terms, modifying policies, or regenerating PDFs, read this document first.

---

## 📋 Repository Overview & Core Principles

- **Repository**: [`vSkilled/sheernox_legal_portal`](https://github.com/vSkilled/sheernox_legal_portal)
- **Tech Stack**: 100% Static HTML5, Modern CSS3, Vanilla JavaScript, Python 3 PDF Generator.
- **Production Standard**: **Strictly production-only code in git**. Never commit test templates, temporary scratch files, or intermediate rendering artifacts.

### Document Registry

| Key | HTML Source | Target PDF Output | Document Title | Version Tag |
| :--- | :--- | :--- | :--- | :--- |
| `tos` | `terms-and-conditions.html` | `pdf/Terms_and_Conditions.pdf` | Terms and Conditions of Service | `v4.5-TOS` |
| `aup` | `acceptable-use-policy.html` | `pdf/Acceptable_Use_Policy.pdf` | Acceptable Use Policy (AUP) | `v4.0-AUP` |
| `wdt` | `web-design-terms.html` | `pdf/Web_Design_Terms_and_Conditions.pdf` | Web Design & Development Terms | `v3.5-WDT` |
| `priv` | `privacy-policy.html` | `pdf/Privacy_Policy.pdf` | Privacy & Personal Information Policy | `v4.5-PRIV` |
| `sla` | `service-level-agreement.html` | `pdf/Service_Level_Agreement.pdf` | Service Level Agreement & Incident Policy | `v1.5-SLA` |
| `vdp` | `vulnerability-disclosure-policy.html` | `pdf/Vulnerability_Disclosure_Policy.pdf` | Vulnerability Disclosure Policy (VDP) | `v1.5-VDP` |
| `cpr` | `copyright-policy.html` | `pdf/Copyright_Notice_and_Notice_Policy.pdf` | Copyright & Notice-and-Notice Policy | `v1.5-CPR` |
| `wcp` | `website-care-plan-terms.html` | `pdf/Website_Care_Plan_Terms.pdf` | Website Care Plan & Maintenance Terms | `v1.5-WCP` |
| `hub` | `index.html` | N/A | Legal Portal Directory & Search Hub | N/A |

---

## 🏛️ Mandatory Legal & Jurisdiction Guardrails

When modifying any document, ensure strict adherence to these legal parameters:

1. **Entity Status**: **Sheernox Technology Group** is a **sole proprietorship** registered in the Province of British Columbia, Canada (Registration Number: `FM0707819`, Business Number: `732754924BC0001`, Original Registration Date: October 29, 2009).
2. **Location & Address**:
   - **Registered Physical & Mailing Address**: `1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada`.
   - All legal agreements, contact channels, and statutory disclosures must consistently reference this official address.
3. **Jurisdiction & Venue**:
   - Governed by the laws of the **Province of British Columbia** and the federal laws of **Canada**.
   - Exclusive legal venue: Courts of British Columbia sitting in the **City of Kamloops, British Columbia, Canada**.
   - Dispute Resolution: Vancouver International Arbitration Centre (**VanIAC**) or BC *Arbitration Act* (SBC 2020, c. 2).
   - Small claims debt recovery: **Small Claims Court of British Columbia**.
4. **Canadian Statutory Framework**:
   - Electronic contracting under the British Columbia *Electronic Transactions Act* (SBC 2001, c. 10).
   - Anti-Spam compliance under Canada's Anti-Spam Legislation (**CASL**, S.C. 2010, c. 23).
   - Copyright notices under the Canadian *Copyright Act* (**Notice-and-Notice** regime, R.S.C. 1985, c. C-42, ss. 31.1, 41.25–41.26).
   - Child exploitation (CSAM) zero-tolerance with mandatory reporting to **Cybertip.ca** and the Royal Canadian Mounted Police (**RCMP**).
   - Personal privacy under Canada's *Personal Information Protection and Electronic Documents Act* (**PIPEDA**) and BC's *Personal Information Protection Act* (**PIPA**, SBC 2003, c. 63).
5. **Monetary Units**: All figures, fees, retainer minimums, and liquidated damages must be in **Canadian Dollars (CAD)** and reference applicable **GST** (5%) and **PST** (7%).

---

## 📬 Communication & Email Routing Rules

- **Abuse Department**: `abuse@sheernox.com`
  - Used **strictly** for reporting network abuse, security incidents, spam, malware, phishing, and DMCA/Copyright infringement.
  - Ticket portal: [`https://my.sheernox.com`](https://my.sheernox.com).
- **All Legal, Compliance, Privacy & General Inquiries**: `support@sheernox.com`
  - **CRITICAL**: The mailboxes `legal@sheernox.com` and `privacy@sheernox.com` are unmonitored. All legal, compliance, and privacy contact points on all pages must route directly to `support@sheernox.com`.

---

## 🚀 CDN Storage & Automated S3 Deployment

- **Production URL**: [`https://legal.sheernox.com`](https://legal.sheernox.com)
- **CDN Edge Infrastructure**: Bunny.net CDN Pull Zone with S3-Compatible Storage Zone.
- **Storage Zone / Bucket**: `sheernox-legal-portal`
- **S3 Endpoint**: `https://la-s3.storage.bunnycdn.com` (Region: `la`)
- **CI/CD Workflow**: [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)
  - Automatically triggers on every `push` to `main` and `workflow_dispatch`.
  - Re-generates all vector PDFs via headless Chrome.
  - Deploys static HTML and `pdf/` documents to Bunny S3 with strict Content-Types.
  - Runs automated live HTTP health checks against `https://legal.sheernox.com`.
- **Encrypted GitHub Secrets**:
  - `BUNNY_STORAGE_BUCKET`
  - `BUNNY_STORAGE_ACCESS_KEY_ID`
  - `BUNNY_STORAGE_SECRET_ACCESS_KEY`
  - `BUNNY_STORAGE_ENDPOINT`
  - `BUNNY_STORAGE_REGION`
  - *Never commit secrets, tokens, or credentials into repository files.*

---

## 🖨️ Automated PDF Generation System

The PDF documents are built using **Variation 1 (Modern Tech Enterprise)** layout specs.

### Generation Script

A fully self-contained generator is maintained at [`scripts/generate_pdfs.py`](file:///home/falsebit/Documents/antigravity/sheernox_legal_portal/scripts/generate_pdfs.py). It automatically extracts legal prose from the HTML files, applies print-optimized CSS, and compiles vector PDFs via headless Chromium/Brave.

### Quick Commands

```bash
# Generate all 8 PDF policy documents
python3 scripts/generate_pdfs.py

# Generate only a specific document
python3 scripts/generate_pdfs.py --doc aup      # Acceptable Use Policy
python3 scripts/generate_pdfs.py --doc tos      # Terms and Conditions
python3 scripts/generate_pdfs.py --doc wdt      # Web Design Terms
python3 scripts/generate_pdfs.py --doc priv     # Privacy Policy
python3 scripts/generate_pdfs.py --doc sla      # Service Level Agreement
python3 scripts/generate_pdfs.py --doc vdp      # Vulnerability Disclosure Policy
python3 scripts/generate_pdfs.py --doc cpr      # Copyright Policy
python3 scripts/generate_pdfs.py --doc wcp      # Website Care Plan Terms

# Specify a custom browser binary
python3 scripts/generate_pdfs.py --browser /usr/bin/brave
```

### Revision Dates & Versioning Standards
- **Standard ISO 8601 Date**: Always use `Last Revised: YYYY-MM-DD` (e.g., `2026-09-11`) consistently across all web pages and PDFs.
- **Consistent Version Tags**: Format version tags strictly as `vX.X-KEY` (e.g., `v3.5-TOS`, `v4.0-AUP`, `v3.0-WDT`, `v3.5-PRIV`).
- **0.5 Version Increments**: Versions must only increase in **0.5 increments** (e.g., `v3.0` -> `v3.5` -> `v4.0`).
- **Colored Version Tag Display**: Web pages and PDF headers must render the version tag as a colored pill (`.version-pill`, cyan background/border, monospaced font).

### PDF Design Specifications (Variation 1)
- **Top Brand Banner**: Deep navy `#071322` background, embedded vector Sheernox logo (`scripts/logo_data.py`), vertical divider, and cyan jurisdiction badge (`British Columbia • Canada`).
- **Top Info Bar**: Do **NOT** include "Governing Law", "Entity Status", or "Document Code". Display only the document category, document title, and the metadata row containing `Last Revised: YYYY-MM-DD` alongside the colored version pill tag (`vX.X-KEY`).
- **Per-Page Running Footer**:
  - **Bottom-Left**: Revision date and version tag: `Last Revised: YYYY-MM-DD • vX.X-KEY`.
  - **Bottom-Right**: Dynamic page numbers: `Page X of Y`.
- **Typography**: `Inter` for body copy, headings, and callouts; `JetBrains Mono` for metadata codes, IP references, version tags, and clause IDs.
- **Page Geometry**: Standard Letter portrait (`8.5in x 11in`), margins: `16mm 16mm 18mm 16mm`.
- **Orphan/Widow Prevention**: `break-inside: avoid;` applied to `.clause-block`, `.key-takeaway`, `.statutory-callout`, `.critical-alert-box`, and `table` so individual sections or cards never break midway across pages awkwardly.
- **Header Protection**: `break-after: avoid;` on `.section-header` to prevent headings from being orphaned at the bottom of a page.

---

## 🤖 High-Level Prompt for Future AI Agents

Copy and paste the prompt below when instructing an AI agent to make policy updates:

```markdown
I need you to update the Sheernox Legal Portal in https://github.com/vSkilled/sheernox_legal_portal.

Please read `AGENTS.md` thoroughly before beginning.

Here are the policy changes I need:
[INSERT POLICY CHANGES HERE, e.g., Update SLA credit percentage, add new sub-processor, etc.]

Operational Instructions:
1. Update the appropriate HTML document(s) directly while maintaining the established semantic structure (`<article class="legal-prose">`, `.legal-section`, `.key-takeaway`, etc.).
2. Update the "Last Revised" date to the current date in ISO 8601 format (`YYYY-MM-DD`) and increment the version tag by 0.5 (format: `vX.X-KEY`, e.g., `v3.5-TOS`).
3. Ensure Canadian legal standards are strictly preserved (Kamloops BC sole proprietorship, support@sheernox.com for legal/privacy, abuse@sheernox.com for network abuse, official address: `1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada`).
4. Regenerate the production vector PDF(s) in `pdf/` using `python3 scripts/generate_pdfs.py`.
5. Verify that PDFs render with the simplified top bar (no Governing Law, Entity Status, or Document Code) and show `Last Revised: YYYY-MM-DD • vX.X-KEY` in the footer of all pages.
6. Keep the repository clean to production code only.
7. Commit and push the changes to `origin/main`.
```

---

## ✅ Quality Assurance & Verification Checklist

Before committing any update:
1. [ ] **Legal Verification**: Are all party definitions set to Sheernox Technology Group in Kamloops, BC, Canada?
2. [ ] **Email Verification**: Is abuse routed to `abuse@sheernox.com` and all other legal/privacy routed to `support@sheernox.com`?
3. [ ] **Address Check**: Is the official physical address `1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada` accurately included across all documents?
4. [ ] **PDF Re-generation**: Was `python3 scripts/generate_pdfs.py` executed successfully?
5. [ ] **Visual Layout Check**: Were page counts and page breaks checked (`break-inside: avoid` intact)?
6. [ ] **Clean Git Tree**: Are only production files staged? (`git status` shows no scratch or debug files).
