# Sheernox Legal Portal (`legal.sheernox.com`)

[![Framework](https://img.shields.io/badge/Framework-Astro%207-bc52ee?style=flat-square)](https://astro.build)
[![Language](https://img.shields.io/badge/Language-TypeScript%20%7C%20Python%203-3178c6?style=flat-square)](#)
[![CDN Deployment](https://img.shields.io/badge/CDN-Bunny.net%20S3-f59e0b?style=flat-square)](https://legal.sheernox.com)
[![Status](https://img.shields.io/badge/Status-Production%20Live-10b981?style=flat-square)](https://legal.sheernox.com)

The public legal documentation portal, policy registry, and automated document generation pipeline for **Sheernox Technology Group**.

This repository hosts the client agreements, service level guarantees, cybersecurity policies, and compliance standards powering [legal.sheernox.com](https://legal.sheernox.com). It compiles static HTML pages via **Astro 7**, generates production vector PDFs via headless Chromium, formats 80-column monospaced plain-text documents, and deploys directly to Bunny.net edge CDN storage.

---

## 🏗️ Architecture & Tech Stack

- **Static Site Generator**: [Astro 7](https://astro.build) with `build: { format: 'file' }` for root-level `.html` static file output matching CDN routing requirements.
- **Component Architecture**: Reusable Astro components for shared navigation (`NetworkHeader.astro`, `PortalHeader.astro`), document headers (`DocHero.astro`), interactive sidebar navigation (`TableOfContents.astro` with scrollspy), and global footers (`SiteFooter.astro`).
- **Styling**: Modern CSS3 with centralized design tokens, CSS variables, responsive mobile drawer navigation, and comprehensive `@media print` layouts.
- **Automated PDF Engine**: Self-contained Python 3 headless Chromium compiler generating vector-grade PDF legal agreements.
- **Plain-Text Engine**: Automated Python 3 DOM parser producing standardized 80-column monospaced plain-text files.
- **CI/CD & Storage**: GitHub Actions pipeline building static routes, compiling assets, deploying to Bunny.net S3 storage via `aws s3 sync --delete`, and executing instant CDN edge cache purges.

---

## 📋 Document Registry

| Key | Astro Source | Target Deployed HTML | Target PDF Output | Plain Text Output | Document Title | Version Tag |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `tos` | `src/pages/terms-and-conditions.astro` | `terms-and-conditions.html` | `terms-and-conditions.pdf` | `terms-and-conditions.txt` | Terms and Conditions of Service | `v4.5-TOS` |
| `aup` | `src/pages/acceptable-use-policy.astro` | `acceptable-use-policy.html` | `acceptable-use-policy.pdf` | `acceptable-use-policy.txt` | Acceptable Use Policy (AUP) | `v4.0-AUP` |
| `priv` | `src/pages/privacy-policy.astro` | `privacy-policy.html` | `privacy-policy.pdf` | `privacy-policy.txt` | Privacy & Personal Information Policy | `v4.5-PRIV` |
| `sla` | `src/pages/service-level-agreement.astro` | `service-level-agreement.html` | `service-level-agreement.pdf` | `service-level-agreement.txt` | Service Level Agreement & Incident Policy | `v1.5-SLA` |
| `vdp` | `src/pages/vulnerability-disclosure-policy.astro` | `vulnerability-disclosure-policy.html` | `vulnerability-disclosure-policy.pdf` | `vulnerability-disclosure-policy.txt` | Vulnerability Disclosure Policy (VDP) | `v1.5-VDP` |
| `cpr` | `src/pages/copyright-policy.astro` | `copyright-policy.html` | `copyright-policy.pdf` | `copyright-policy.txt` | Copyright & Notice-and-Notice Policy | `v1.5-CPR` |
| `wdt` | `src/pages/web-design-terms.astro` | `web-design-terms.html` | `web-design-terms.pdf` | `web-design-terms.txt` | Web Design & Development Terms | `v3.5-WDT` |
| `wcp` | `src/pages/website-care-plan-terms.astro` | `website-care-plan-terms.html` | `website-care-plan-terms.pdf` | `website-care-plan-terms.txt` | Website Care Plan & Maintenance Terms | `v1.5-WCP` |
| `hub` | `src/pages/index.astro` | `index.html` | N/A | N/A | Legal Portal Directory & Search Hub | N/A |

---

## 🚀 Quick Start & Development Commands

### Prerequisites
- **Node.js**: `v20.x` or `v22.x+`
- **Python**: `3.10+` with `beautifulsoup4` (`pip install beautifulsoup4`)
- **Browser** (for PDF generation): Google Chrome, Brave, or Chromium

### Setup & Local Server

```bash
# Install dependencies
npm install

# Start local development server
npm run dev

# Run Astro TypeScript and component diagnostics
npm test

# Build static production bundle to dist/
npm run build

# Preview built distribution locally
npm run preview
```

---

## 🖨️ Document Generation Tooling

### Automated Vector PDF Generator
Compiles production print-ready vector PDFs directly from the built static HTML in `dist/`:

```bash
# Generate all 8 PDF documents into dist/ and sync public/
npm run generate:pdfs

# Or invoke the Python script directly with custom parameters
python3 scripts/generate_pdfs.py --source-dir dist --output-dir dist

# Compile a specific document (e.g., Terms of Service)
python3 scripts/generate_pdfs.py --doc tos --source-dir dist --output-dir dist

# Specify an explicit browser binary
python3 scripts/generate_pdfs.py --browser /usr/bin/google-chrome
```

### Automated Plain Text (.TXT) Generator
Parses the semantic legal prose from `dist/` and generates 80-column monospaced plain-text versions:

```bash
# Generate all plain-text policies into dist/ and sync public/
npm run generate:txts

# Or invoke the Python script directly
python3 scripts/generate_txts.py --source-dir dist --output-dir dist

# Compile a single document
python3 scripts/generate_txts.py --doc sla --source-dir dist --output-dir dist

# Force re-generation of all documents (including hand-crafted VDP)
python3 scripts/generate_txts.py --force --source-dir dist --output-dir dist
```

---

## 📁 Repository Structure

```text
legal.sheernox.com/
├── .github/
│   └── workflows/
│       └── deploy.yml            # CI/CD: Node 22 build, Python asset compile, Bunny S3 sync
├── .gitignore                    # Production git ignore (node_modules, dist, .astro)
├── README.md                     # Technical architecture, setup & operational documentation
├── AGENTS.md                     # AI Agent runbook & statutory legal parameters
├── astro.config.mjs              # Astro 7 configuration (file output format, sitemap)
├── package.json                  # Scripts & dependencies
├── tsconfig.json                 # TypeScript strict configuration
├── public/                       # Static root assets copied verbatim to dist/
│   ├── favicon.ico               # Official Sheernox browser favicon
│   ├── security.txt              # Security vulnerability reporting metadata
│   ├── .well-known/security.txt  # RFC 9116 security contact endpoint
│   ├── *.pdf                     # Generated vector PDF documents
│   └── *.txt                     # Generated 80-column monospaced text documents
├── src/
│   ├── components/               # Shared Astro components
│   │   ├── NetworkHeader.astro   # Unified Sheernox multi-brand network bar
│   │   ├── PortalHeader.astro    # Sticky Legal Portal header & navigation
│   │   ├── DocHero.astro         # Document metadata header, version tag & action buttons
│   │   ├── TableOfContents.astro # Sticky sidebar TOC with filter & active scrollspy
│   │   ├── SiteFooter.astro      # Global footer with statutory entity coordinates
│   │   └── Toast.astro           # Toast notification element
│   ├── data/
│   │   └── documents.ts          # Central metadata registry (versions, dates, slugs)
│   ├── layouts/
│   │   └── LegalDocumentLayout.astro # Base legal page layout wrapping <article class="legal-prose">
│   ├── pages/                    # Astro page routes
│   │   ├── index.astro           # Portal search hub & interactive directory
│   │   └── *.astro               # 8 Legal policy page components
│   └── styles/
│       ├── legal.css             # Shared design system, typography, callouts & print styles
│       └── hub.css               # Directory cards, search input & filter styles
└── scripts/                      # Automated asset compilers
    ├── generate_pdfs.py          # Headless Chromium vector PDF generator
    ├── generate_txts.py          # 80-column monospaced plain-text generator
    └── logo_data.py              # Embedded base64 vector brand logo
```

---

## 🌐 CI/CD & Deployment Pipeline

Every push to `main` (or manual `workflow_dispatch`) triggers [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml):

1. **Environment Setup**: Configures Node.js 22 and Python 3.11 with Google Chrome.
2. **Diagnostics**: Executes `npm test` (`astro check`) for type-safety and syntax validation.
3. **Static Build**: Runs `npm run build` to generate all static HTML routes to `dist/`.
4. **Asset Generation**: Re-generates all 8 vector PDFs and 8 plain-text documents directly into `dist/`.
5. **Storage Sync**: Synchronizes `dist/` to Bunny.net S3 storage root (`s3://${BUNNY_STORAGE_BUCKET}`) using AWS CLI with `--delete`.
6. **CDN Cache Purge**: Calls the Bunny.net REST API to purge the CDN Pull Zone cache for instant edge propagation.
7. **Health Verification**: Performs live HTTP `HEAD` checks against `https://legal.sheernox.com` endpoints.

---

## 📬 Contact & Routing Channels

- **Network Abuse, Phishing & Copyright / DMCA**: `abuse@sheernox.com`
- **Legal, Privacy & General Inquiries**: `support@sheernox.com`
- **Customer Account Portal**: [`https://my.sheernox.com`](https://my.sheernox.com)
