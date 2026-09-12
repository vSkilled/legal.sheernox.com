# Sheernox Legal Portal

[![Status](https://img.shields.io/badge/Status-Production%20Ready-emerald?style=flat-square)](#)
[![Jurisdiction](https://img.shields.io/badge/Jurisdiction-British%20Columbia%2C%20Canada-0284c7?style=flat-square)](#)
[![Documents](https://img.shields.io/badge/Documents-8%20Policies%20%7C%208%20PDFs-6366f1?style=flat-square)](#)
[![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20Vanilla%20JS-0f4c81?style=flat-square)](#)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20Runtime-10b981?style=flat-square)](#)

Official customer legal agreements, compliance policies, service level commitments, and security governance repository for **Sheernox Technology Group**.

This repository contains the standalone, fully responsive, and accessible HTML5 web agreements that power the public legal hub at [sheernox.com](https://sheernox.com) and the client portal at [my.sheernox.com](https://my.sheernox.com), alongside automated tooling for generating official print-ready vector PDF documents.

---

## 🏛️ Entity & Legal Jurisdiction

All infrastructure, cloud hosting, managed care, and creative agency services are contracted with:

- **Entity**: **Sheernox Technology Group** (Registered Sole Proprietorship)
- **Official Physical & Mailing Address**: `1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada`
- **Governing Law**: Laws of the **Province of British Columbia** and the federal laws of **Canada** applicable therein.
- **Exclusive Venue**: Courts of British Columbia sitting in the **City of Kamloops, British Columbia, Canada**.
- **Dispute Resolution & Arbitration**: Administered under the British Columbia *Arbitration Act* (SBC 2020, c. 2) or the Vancouver International Arbitration Centre (**VanIAC**). Small claims debt recovery is enforced through the **Small Claims Court of British Columbia**.
- **Currency & Monetary Units**: All contractual figures, service retainers, and liquidated damage assessments are denominated in **Canadian Dollars (CAD)** and subject to Canadian Goods and Services Tax (**GST**, 5%) and British Columbia Provincial Sales Tax (**PST**, 7%).

### Statutory Framework
- **Electronic Formation**: Fully enforceable electronic contracting under the British Columbia *Electronic Transactions Act* (SBC 2001, c. 10).
- **Anti-Spam Compliance**: Governed by Canada’s Anti-Spam Legislation (**CASL**, S.C. 2010, c. 23).
- **Copyright & Notice-and-Notice**: Formal compliance with Sections 31.1, 41.25, and 41.26 of the Canadian *Copyright Act* (R.S.C. 1985, c. C-42).
- **Cybersecurity Safe Harbor**: Express research authorization under Sections 342.1 and 430(1.1) of the Canadian *Criminal Code* (R.S.C. 1985, c. C-46).
- **Child Protection (Zero Tolerance)**: Mandatory reporting of CSAM to **Cybertip.ca** (Canadian Centre for Child Protection) and the Royal Canadian Mounted Police (**RCMP**).
- **Privacy & Data Protection**: Aligned with Canada's *Personal Information Protection and Electronic Documents Act* (**PIPEDA**) and BC's *Personal Information Protection Act* (**PIPA**, SBC 2003, c. 63) under the Office of the Information and Privacy Commissioner for British Columbia (**OIPC BC**).
- **Cross-Border Statutory Disclosures**: Upstream cloud infrastructure disclosures regarding extraterritorial legal processes, including the United States Clarifying Lawful Overseas Use of Data Act (**CLOUD Act**, 18 U.S.C. § 2713).
- **Warranty Exclusions**: Implied statutory warranties excluded to the fullest extent permitted under the British Columbia *Sale of Goods Act* (RSBC 1996, c. 410).

---

## 🌐 Sheernox Technology Group Network Header

Every page across the Legal Portal integrates a standardized, responsive enterprise multi-brand navigation bar positioned at the top of the viewport (`.network-bar`), showcasing the Sheernox corporate network:

```
[ Sheernox.com (Active) ● | HostBlizzard.com | VPSTitan.com | UptimeHawk.com | 4Up.ca ]    [ ● Sheernox Technology Group • Kamloops, BC ]
```

- **Participating Brands**:
  1. [`Sheernox.com`](https://sheernox.com) — Active portal state with animated live emerald status pulse.
  2. [`HostBlizzard.com`](https://hostblizzard.com) — Web, cloud, and reseller hosting platform.
  3. [`VPSTitan.com`](https://vpstitan.com) — High-performance virtual private server infrastructure.
  4. [`UptimeHawk.com`](https://uptimehawk.com) — 24/7/365 infrastructure monitoring and telemetry.
  5. [`4Up.ca`](https://4up.ca) — Canadian domain services and network solutions.
- **Enterprise Entity Badge**: Displays `Sheernox Technology Group • Kamloops, BC` on desktop displays.
- **Mobile Responsive**: Horizontally scrollable tab bar on mobile displays (`< 840px`) with hidden scrollbars to prevent page-level horizontal overflow.
- **Print Optimization**: Automatically suppressed on `@media print` across all documents.

---

## 📁 Repository Structure & Production Files

This repository contains **strictly production-grade code** with zero build artifacts, temporary scratch files, or third-party package dependencies:

```text
sheernox_legal_portal/
├── .gitignore                             # Production ignore rules
├── README.md                              # Repository documentation and architecture guide
├── AGENTS.md                              # AI Agent operational runbook & legal guardrails
├── index.html                             # Central Legal Portal Directory & Search Hub
├── terms-and-conditions.html              # Master Terms and Conditions of Service (v4.0-TOS)
├── acceptable-use-policy.html             # Acceptable Use Policy (v3.5-AUP)
├── privacy-policy.html                    # Privacy & Personal Information Policy (v4.0-PRIV)
├── service-level-agreement.html           # Service Level Agreement & Incident Policy (v1.0-SLA)
├── vulnerability-disclosure-policy.html   # Vulnerability Disclosure Policy (v1.0-VDP)
├── copyright-policy.html                  # Copyright & Notice-and-Notice Policy (v1.0-CPR)
├── web-design-terms.html                  # Web Design & Development Terms (v3.0-WDT)
├── website-care-plan-terms.html           # Website Care Plan & Maintenance Terms (v1.0-WCP)
├── pdf/                                   # Official Print-Ready Vector PDF Documents
│   ├── Terms_and_Conditions.pdf
│   ├── Acceptable_Use_Policy.pdf
│   ├── Privacy_Policy.pdf
│   ├── Service_Level_Agreement.pdf
│   ├── Vulnerability_Disclosure_Policy.pdf
│   ├── Copyright_Notice_and_Notice_Policy.pdf
│   ├── Web_Design_Terms_and_Conditions.pdf
│   └── Website_Care_Plan_Terms.pdf
└── scripts/                               # Automated Vector PDF Generation Tooling
    ├── generate_pdfs.py                   # Standalone multi-browser headless PDF compiler
    └── logo_data.py                       # Embedded base64 vector brand logo
```

---

## 📋 Comprehensive Document Registry

| Key | HTML Source | Target PDF Output | Document Title | Version Tag | Category |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `tos` | [`terms-and-conditions.html`](terms-and-conditions.html) | `pdf/Terms_and_Conditions.pdf` | Terms and Conditions of Service | `v4.0-TOS` | Master Services Agreement |
| `aup` | [`acceptable-use-policy.html`](acceptable-use-policy.html) | `pdf/Acceptable_Use_Policy.pdf` | Acceptable Use Policy (AUP) | `v3.5-AUP` | Network & Infrastructure Policy |
| `priv` | [`privacy-policy.html`](privacy-policy.html) | `pdf/Privacy_Policy.pdf` | Privacy & Personal Information Policy | `v4.0-PRIV` | Privacy & Data Protection Policy |
| `sla` | [`service-level-agreement.html`](service-level-agreement.html) | `pdf/Service_Level_Agreement.pdf` | Service Level Agreement & Incident Policy | `v1.0-SLA` | Cloud Infrastructure & Operations |
| `vdp` | [`vulnerability-disclosure-policy.html`](vulnerability-disclosure-policy.html) | `pdf/Vulnerability_Disclosure_Policy.pdf` | Vulnerability Disclosure Policy (VDP) | `v1.0-VDP` | Cybersecurity & Trust Governance |
| `cpr` | [`copyright-policy.html`](copyright-policy.html) | `pdf/Copyright_Notice_and_Notice_Policy.pdf` | Copyright & Notice-and-Notice Policy | `v1.0-CPR` | Intellectual Property & Compliance |
| `wdt` | [`web-design-terms.html`](web-design-terms.html) | `pdf/Web_Design_Terms_and_Conditions.pdf` | Web Design & Development Terms | `v3.0-WDT` | Agency Services Agreement |
| `wcp` | [`website-care-plan-terms.html`](website-care-plan-terms.html) | `pdf/Website_Care_Plan_Terms.pdf` | Website Care Plan & Maintenance Terms | `v1.0-WCP` | Creative & Agency SOW Schedule |
| `hub` | [`index.html`](index.html) | N/A | Legal Portal Directory & Search Hub | N/A | Central Index Directory |

### Document Summary & Legal Highlights

1. **Master Terms and Conditions (`terms-and-conditions.html` / `v4.0-TOS`)**:
   - Master commercial services framework, billing cycles, domain management, and acceptable usage.
   - Exclusive jurisdiction in the Courts of British Columbia sitting in Kamloops, BC.
   - \$5,000.00 CAD liquidated damages for domain typo-squatting, phishing, and brand impersonation.
   - 14-day cancellation notice requirement via client portal ticket.
   - Upstream cloud provider disclosure regarding the US CLOUD Act (18 U.S.C. § 2713).

2. **Acceptable Use Policy (`acceptable-use-policy.html` / `v3.5-AUP`)**:
   - Technical multi-tenancy resource standards, CloudLinux LVE limits, and shared environment protection.
   - Prohibitions on network stress testing, botnets, crypto-mining, email harvesting, and outbound port abuse.
   - Automated quarantine null-routing for compromised virtual instances.
   - CASL anti-spam compliance enforcement; \$250.00 CAD delisting fee for outbound IP blocklisting.
   - Zero-tolerance CSAM policy with mandatory reporting to Cybertip.ca and the RCMP.

3. **Privacy & Personal Information Policy (`privacy-policy.html` / `v4.0-PRIV`)**:
   - Comprehensive data handling transparency complying with PIPEDA, BC PIPA, and international principles.
   - Self-hosted infrastructure guarantees, encrypted database retention (AES-256), and access controls.
   - Disclosures on US CLOUD Act cross-border legal assistance treaties and data sovereign boundaries.
   - Direct escalation to designated Privacy Officer in Kamloops, BC, with OIPC BC complaint rights.

4. **Service Level Agreement & Incident Policy (`service-level-agreement.html` / `v1.0-SLA`)**:
   - Explicit 99.9% monthly network and infrastructure availability guarantee calculated via mathematical formula:
     $$\text{Availability (\%)} = \frac{T - D}{T} \times 100$$
   - Incident severity matrix: P1 (Critical, $< 15$ min initial response) through P4 (Low, $< 12$ hr).
   - Tiered service credits: 10% for $99.0\%–99.89\%$, 25% for $95.0\%–98.99\%$, 50% for $90.0\%–94.99\%$, and 100% for $< 90.0\%$.
   - 30-day claims submission window; credits serve as the customer's sole and exclusive financial remedy.

5. **Vulnerability Disclosure Policy (`vulnerability-disclosure-policy.html` / `v1.0-VDP`)**:
   - Statutory Safe Harbor authorizing authorized security research under Sections 342.1 (*Unauthorized use of computer*) and 430(1.1) (*Mischief in relation to computer data*) of the Canadian *Criminal Code* (R.S.C. 1985, c. C-46).
   - Clear asset scope: `*.sheernox.com`, customer endpoints, APIs, and edge DNS clusters.
   - Ban on DoS/DDoS, data destruction, social engineering, and customer privacy violations.
   - 48-hour response confirmation, 5-day triage SLA, and 90-day coordinated disclosure timeline.

6. **Copyright & Notice-and-Notice Policy (`copyright-policy.html` / `v1.0-CPR`)**:
   - Full statutory alignment with Canada's **Notice-and-Notice** regime (Canadian *Copyright Act*, ss. 31.1, 41.25–41.26).
   - Obligation to forward statutory infringement notices to subscribers within 48 hours without fee.
   - Rejection of non-compliant notices containing settlement offers or statutory release fee demands (s. 41.25(3)).
   - Statutory 6-month log retention period (extendable to 12 months upon formal court notice).
   - Customer identity protection: Subscriber personal information is never disclosed without a Canadian court order.

7. **Web Design & Development Terms (`web-design-terms.html` / `v3.0-WDT`)**:
   - Statement of Work (SOW) legal architecture for bespoke web design, custom engineering, and agency services.
   - 50% initial non-refundable mobilization deposit; progressive milestone billing.
   - 30-day post-launch code warranty covering reproducible defects and responsive layout bugs.
   - Criminal protection: Unauthorized deployment of unreleased deliverables constitutes theft under Sections 322–380 of the Canadian *Criminal Code*.
   - Intellectual property transfer occurs strictly upon receipt of 100% full cleared payment.

8. **Website Care Plan & Maintenance Terms (`website-care-plan-terms.html` / `v1.0-WCP`)**:
   - Recurring maintenance Statement of Work (SOW) schedule operating under `web-design-terms.html`.
   - 3 Care Plan tiers: Essential Care, Professional Care (2 hrs/mo included), and Enterprise Agency Care (5 hrs/mo included + 2h emergency malware response).
   - Staging-First testing protocol with automated visual regression and rollback guarantees.
   - Non-rollover monthly support hours ("use-it-or-lose-it"); discounted subscriber rate (\$95.00 CAD/hr vs \$125.00 CAD/hr standard).
   - Automated recurring billing via Stripe with 30-day written cancellation protocol.

---

## 🎨 Design System & Interactive Capabilities

The portal features a modern, accessible interface tailored for rapid clause discovery and legal readability:

- **Enterprise Network Header**: Persistent multi-brand top bar linking to Sheernox corporate network websites.
- **Dynamic Scrollspy Sidebar**: Table of Contents (TOC) tracks reading progress in real-time with smooth scrolling.
- **Client-Side Clause Search**: Live filter inputs on individual policy sidebars and central hub search filter clauses and cards by keyword instantly without page reloads.
- **Reading Progress Bar**: Top 3px gradient progress bar tracks exact viewport reading completion.
- **"In Plain English" Key Takeaways**: Executive callout summaries translating dense legal prose into concise operational guidelines.
- **Clause Permalinks (`#`)**: Deep-link permalink anchor buttons copy direct section URLs with toast feedback.
- **Mobile Responsive Architecture**: Responsive layout hiding desktop sidebars on mobile screens, providing a clean collapsible mobile Table of Contents accordion, and ensuring zero horizontal page overflow (`scrollWidth === clientWidth`).
- **Accessible WCAG AA Typography**: Clean font pairings using Google Fonts (`Inter` for body copy, `JetBrains Mono` for IP addresses, clause codes, and monetary figures).
- **Print Optimization**: Comprehensive print stylesheets (`@media print`) hide navigation bars, search inputs, sidebars, progress indicators, and footers, preserving clean margins and page break rules.

---

## 🖨️ Automated Vector PDF Generation

A fully self-contained, zero-dependency PDF compiler is provided at [`scripts/generate_pdfs.py`](scripts/generate_pdfs.py). It parses the semantic HTML legal prose, injects enterprise print styling (Variation 1 layout), and compiles vector PDFs via headless Chromium/Brave:

```bash
# Generate all 8 legal policy PDFs
python3 scripts/generate_pdfs.py

# Generate a specific policy document
python3 scripts/generate_pdfs.py --doc tos     # Master Terms and Conditions (v4.0-TOS)
python3 scripts/generate_pdfs.py --doc aup     # Acceptable Use Policy (v3.5-AUP)
python3 scripts/generate_pdfs.py --doc priv    # Privacy Policy (v4.0-PRIV)
python3 scripts/generate_pdfs.py --doc sla     # Service Level Agreement (v1.0-SLA)
python3 scripts/generate_pdfs.py --doc vdp     # Vulnerability Disclosure Policy (v1.0-VDP)
python3 scripts/generate_pdfs.py --doc cpr     # Copyright Policy (v1.0-CPR)
python3 scripts/generate_pdfs.py --doc wdt     # Web Design Terms (v3.0-WDT)
python3 scripts/generate_pdfs.py --doc wcp     # Website Care Plan Terms (v1.0-WCP)

# Specify a custom browser executable
python3 scripts/generate_pdfs.py --browser /usr/bin/brave
```

### PDF Layout Specifications
- **Top Brand Banner**: Deep navy `#071322` header with embedded vector Sheernox logo and cyan Canadian jurisdiction badge (`British Columbia • Canada`).
- **Metadata Subheader**: Clean layout showing category, document title, revision date, and version pill tag (`vX.X-KEY`).
- **Page Numbers & Running Footers**: Dynamic `Page X of Y` footer and revision stamp on every page.
- **Orphan & Widow Prevention**: `break-inside: avoid;` on callout boxes, tables, and clause blocks; `break-after: avoid;` on section headings.

---

## 🚀 Local Development & Deployment

The portal is **100% static** and requires **zero runtime dependencies or build steps**.

### Local Testing

Serve repository files locally using any HTTP server:

```bash
# Python 3 built-in server
python3 -m http.server 8080

# Node.js (npx)
npx serve .

# PHP built-in server
php -S localhost:8080
```

Open `http://localhost:8080` in your web browser.

### Production Hosting Options

- **GitHub Pages**: Deploy directly from the `main` branch root (`/`).
- **Cloudflare Pages / Vercel / Netlify**: Connect repository with no build command and publish root `/`.
- **Nginx / Apache**: Copy static files directly to the webroot directory (`/var/www/html/`).

---

## 🛡️ Abuse & Compliance Communication Channels

To report network abuse, security vulnerabilities, or statutory copyright notices:

- **Network Abuse, Phishing, Malware & Copyright Infringement**: `abuse@sheernox.com`
- **Legal, Compliance, Privacy & Vulnerability Disclosure Inquiries**: `support@sheernox.com`
- **Customer Account & Support Portal**: [`https://my.sheernox.com`](https://my.sheernox.com)
- **Official Physical Address**:
  Sheernox Technology Group
  1-1885 Grasslands Blvd
  Kamloops, BC, V2B 0B8
  Canada

---

## ⚖️ Copyright & Proprietary Notice

&copy; 2026 **Sheernox Technology Group**. All rights reserved. Registered sole proprietorship in the Province of British Columbia, Canada.
