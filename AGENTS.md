# AI Agent Runbook & Repository Context

This document is the authoritative operational guide for AI coding agents (and developers) maintaining the **Sheernox Legal Portal**. If you are an AI tasked with updating terms, modifying policies, or regenerating PDFs, read this document first.

---

## 📋 Repository Overview & Core Principles

- **Repository**: [`vSkilled/legal.sheernox.com`](https://github.com/vSkilled/legal.sheernox.com)
- **Tech Stack**: Astro 7, TypeScript, Modern CSS3, Python 3 PDF Generator, Python 3 Plain Text Generator.
- **Production Standard**: **Strictly production-only code in git**. Never commit test templates, temporary scratch files, or intermediate rendering artifacts.

### Document Registry

| Key | Astro Source | Target Deployed HTML | Target PDF Output | Plain Text Output | Document Title | Version Tag |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `tos` | `src/pages/terms-and-conditions.astro` | `terms-and-conditions.html` | `terms-and-conditions.pdf` | `terms-and-conditions.txt` | Terms and Conditions of Service | `v4.5-TOS` |
| `aup` | `src/pages/acceptable-use-policy.astro` | `acceptable-use-policy.html` | `acceptable-use-policy.pdf` | `acceptable-use-policy.txt` | Acceptable Use Policy (AUP) | `v4.0-AUP` |
| `wdt` | `src/pages/web-design-terms.astro` | `web-design-terms.html` | `web-design-terms.pdf` | `web-design-terms.txt` | Web Design & Development Terms | `v3.5-WDT` |
| `priv` | `src/pages/privacy-policy.astro` | `privacy-policy.html` | `privacy-policy.pdf` | `privacy-policy.txt` | Privacy & Personal Information Policy | `v4.5-PRIV` |
| `sla` | `src/pages/service-level-agreement.astro` | `service-level-agreement.html` | `service-level-agreement.pdf` | `service-level-agreement.txt` | Service Level Agreement & Incident Policy | `v1.5-SLA` |
| `vdp` | `src/pages/vulnerability-disclosure-policy.astro` | `vulnerability-disclosure-policy.html` | `vulnerability-disclosure-policy.pdf` | `vulnerability-disclosure-policy.txt` | Vulnerability Disclosure Policy (VDP) | `v1.5-VDP` |
| `cpr` | `src/pages/copyright-policy.astro` | `copyright-policy.html` | `copyright-policy.pdf` | `copyright-policy.txt` | Copyright & Notice-and-Notice Policy | `v1.5-CPR` |
| `wcp` | `src/pages/website-care-plan-terms.astro` | `website-care-plan-terms.html` | `website-care-plan-terms.pdf` | `website-care-plan-terms.txt` | Website Care Plan & Maintenance Terms | `v1.5-WCP` |
| `prm` | `src/pages/promotions.astro` | `promotions.html` | `promotions.pdf` | `promotions.txt` | Promotional Terms and Conditions | `v1.0-PRM` |
| `hub` | `src/pages/index.astro` | `index.html` | N/A | N/A | Legal Portal Directory & Search Hub | N/A |

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
  - Builds static HTML via Astro 7 (`build: { format: 'file' }`).
  - Re-generates all vector PDFs via headless Chromium/Chrome post-build.
  - Re-generates all plain text (`.txt`) documents.
  - Deploys static HTML, vector PDF (`.pdf`), plain text (`.txt`), and assets to Bunny S3 storage zone root.
  - Automatically purges the Bunny.net CDN Pull Zone cache on every deployment to ensure instant edge propagation.
  - Runs automated live HTTP health checks against `https://legal.sheernox.com`.
- **Encrypted GitHub Secrets**:
  - `BUNNY_STORAGE_BUCKET`
  - `BUNNY_STORAGE_ACCESS_KEY_ID`
  - `BUNNY_STORAGE_SECRET_ACCESS_KEY`
  - `BUNNY_STORAGE_ENDPOINT`
  - `BUNNY_STORAGE_REGION`
  - `BUNNY_PULL_ZONE_ID`
  - `BUNNY_API_KEY`
  - *Never commit secrets, tokens, or credentials into repository files.*

---

## 🛠️ Development & Build Commands

```bash
# Install dependencies
npm install

# Run local development server
npm run dev

# Run Astro component diagnostics
npm test

# Build static site with Astro 7
npm run build

# Generate all 8 vector PDF policy documents post-build
npm run generate:pdfs

# Generate all 8 plain text policy documents post-build
npm run generate:txts

# Preview built distribution locally
npm run preview
```

---

## 🖨️ Automated PDF Generation System

The PDF documents are built using **Variation 1 (Modern Tech Enterprise)** layout specs.

### Generation Script

A fully self-contained generator is maintained at [`scripts/generate_pdfs.py`](scripts/generate_pdfs.py). It automatically extracts legal prose from the built HTML in `dist/`, applies print-optimized CSS, and compiles vector PDFs via headless Chromium/Brave/Chrome into `dist/` and `public/`.

### Quick Commands

```bash
# Generate all 8 PDF policy documents against dist/
python3 scripts/generate_pdfs.py --source-dir dist --output-dir dist

# Generate only a specific document
python3 scripts/generate_pdfs.py --doc aup
python3 scripts/generate_pdfs.py --doc tos
python3 scripts/generate_pdfs.py --doc wdt
python3 scripts/generate_pdfs.py --doc priv
python3 scripts/generate_pdfs.py --doc sla
python3 scripts/generate_pdfs.py --doc vdp
python3 scripts/generate_pdfs.py --doc cpr
python3 scripts/generate_pdfs.py --doc wcp
python3 scripts/generate_pdfs.py --doc prm
```

### Revision Dates & Versioning Standards
- **Standard ISO 8601 Date**: Always use `Last Revised: YYYY-MM-DD` (e.g., `2026-09-13`) consistently across `src/data/documents.ts`, pages, and PDFs.
- **Consistent Version Tags**: Format version tags strictly as `vX.X-KEY` (e.g., `v4.5-TOS`, `v4.0-AUP`, `v3.5-WDT`, `v4.5-PRIV`).
- **0.5 Version Increments**: Versions must only increase in **0.5 increments** (e.g., `v3.0` -> `v3.5` -> `v4.0`).
- **Colored Version Tag Display**: Web pages and PDF headers must render the version tag as a colored pill (`.version-pill`, monospaced font).

---

## 📄 Automated Plain Text (.TXT) Generation System

All policy documents feature an official 80-column monospaced plain text version matching the layout of `vulnerability-disclosure-policy.txt`.

### Generation Script

A fully self-contained text generator is maintained at [`scripts/generate_txts.py`](scripts/generate_txts.py). It parses legal prose directly from `dist/`, calculates column wrapping, formats ASCII data tables and callouts, and writes the `.txt` files into `dist/` and `public/`.

### Quick Commands

```bash
# Generate all plain text documents (preserves handcrafted VDP by default)
python3 scripts/generate_txts.py --source-dir dist --output-dir dist

# Force re-generation of all documents including VDP
python3 scripts/generate_txts.py --force --source-dir dist --output-dir dist
```

---

## 🤖 High-Level Prompt for Future AI Agents

The copy-paste prompt for instructing an AI agent on this repo lives in [docs/agent-prompt.md](docs/agent-prompt.md).

---

## ✅ Quality Assurance & Verification Checklist

Before committing any update:
1. [ ] **Legal Verification**: Are all party definitions set to Sheernox Technology Group in Kamloops, BC, Canada?
2. [ ] **Email Verification**: Is abuse routed to `abuse@sheernox.com` and all other legal/privacy routed to `support@sheernox.com`?
3. [ ] **Address Check**: Is the official physical address `1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada` accurately included across all documents?
4. [ ] **Build Check**: Did `npm run build` succeed with 10 routes generated?
5. [ ] **Diagnostics Check**: Did `npm test` pass with 0 errors and 0 warnings?
6. [ ] **PDF Re-generation**: Was `npm run generate:pdfs` executed successfully (9/9 PDFs)?
7. [ ] **Plain Text Re-generation**: Was `npm run generate:txts` executed successfully?
8. [ ] **Clean Git Tree**: Are only production files staged? (`git status` shows no scratch or debug files).
