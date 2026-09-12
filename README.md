# Sheernox Legal Portal

[![Status](https://img.shields.io/badge/Status-Production%20Ready-emerald?style=flat-square)](#)
[![Jurisdiction](https://img.shields.io/badge/Jurisdiction-British%20Columbia%2C%20Canada-0284c7?style=flat-square)](#)
[![Stack](https://img.shields.io/badge/Stack-HTML5%20%7C%20CSS3%20%7C%20Vanilla%20JS-0f4c81?style=flat-square)](#)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero%20Runtime-10b981?style=flat-square)](#)

Official customer legal agreements, compliance policies, and service documentation repository for **Sheernox Technology Group**.

This repository contains the standalone, fully responsive, and accessible HTML5 web agreements that power the public legal hub at [sheernox.com](https://sheernox.com) and the client portal at [my.sheernox.com](https://my.sheernox.com).

---

## 🏛️ Entity & Legal Jurisdiction

All services, infrastructure, and creative contracts are provided by and contracted with:

- **Entity**: **Sheernox Technology Group** (Registered Sole Proprietorship)
- **Location**: `Kamloops, British Columbia, Canada`
- **Governing Law**: Laws of the **Province of British Columbia** and the federal laws of **Canada** applicable therein.
- **Exclusive Venue**: Courts of British Columbia sitting in the **City of Kamloops, British Columbia, Canada**.
- **Currency & Taxation**: All contractual figures, service retainers, and liquidated damage assessments are denominated in **Canadian Dollars (CAD)** and subject to Canadian Goods and Services Tax (**GST**) and British Columbia Provincial Sales Tax (**PST**).

### Statutory Framework
- **Electronic Formation**: Enforceable under the British Columbia *Electronic Transactions Act* (SBC 2001, c. 10).
- **Anti-Spam**: Strictly governed by Canada’s Anti-Spam Legislation (**CASL**, S.C. 2010, c. 23).
- **Copyright & Infringement**: Enforced via the Canadian *Copyright Act* (**Notice-and-Notice** regime, R.S.C. 1985, c. C-42, ss. 31.1, 41.25–41.26).
- **Child Protection**: Mandatory reporting to **Cybertip.ca** (Canadian Centre for Child Protection) and the Royal Canadian Mounted Police (RCMP).
- **Privacy & Data Protection**: Fully aligned with Canada's *Personal Information Protection and Electronic Documents Act* (**PIPEDA**) and British Columbia’s *Personal Information Protection Act* (**PIPA**, SBC 2003, c. 63) under the regulatory oversight of the Office of the Information and Privacy Commissioner for British Columbia (**OIPC BC**).
- **Dispute Resolution & Arbitration**: Administered under the British Columbia *Arbitration Act* (SBC 2020, c. 2) or the Vancouver International Arbitration Centre (**VanIAC**).
- **Warranty Exclusions**: Statutory implied warranties are excluded to the fullest extent permitted by the British Columbia *Sale of Goods Act* (RSBC 1996, c. 410).
- **Criminal Theft of Deliverables**: Unauthorized copying or deployment of unreleased creative deliverables prior to full payment constitutes criminal theft under **Sections 322–380 of the *Criminal Code of Canada*** (R.S.C. 1985, c. C-46).
- **Debt Recovery**: Enforced through the **Small Claims Court of British Columbia** or the Supreme Court of British Columbia, with full recovery of collection and legal costs on a **solicitor-and-own-client indemnity basis**.

---

## 📁 Repository Structure & Production Files

This repository contains **strictly production-grade code** with zero build artifacts, temporary scratch files, or third-party package dependencies:

```text
sheernox_legal_portal/
├── .gitignore                   # Production ignore rules
├── README.md                    # Repository documentation and architecture guide
├── index.html                   # Central Legal Portal Directory & Interactive Hub
├── terms-and-conditions.html    # Master Terms and Conditions (TOS, SLA, Infrastructure)
├── acceptable-use-policy.html   # Acceptable Use Policy (AUP, 33 Rules, Resource Ceilings)
├── web-design-terms.html        # Web Design, Branding & Maintenance Care Agreement
└── privacy-policy.html          # Global Data Protection & Privacy Policy (PIPEDA/GDPR)
```

### Production Document Index

| Document | Primary Focus | Sections | Canadian Legal Highlights |
| :--- | :--- | :--- | :--- |
| **[`index.html`](index.html)** | Portal Hub & Directory | N/A | Central search, filter by service type, direct deep links, and enterprise MSA inquiries. |
| **[`terms-and-conditions.html`](terms-and-conditions.html)** | Master Services & Infrastructure | 23 Sections | Kamloops BC venue, $5,000 CAD typo-squatting liquidated damages, 14-day cancellation notice via portal, 99.9% SLA credit tiers, SOW on-site builds. |
| **[`acceptable-use-policy.html`](acceptable-use-policy.html)** | Network & Compute Rules | 8 Core Sections | All 33 original unacceptable categories, 26 itemized prohibited activities, cron/MySQL limits, CASL compliance, $250 CAD delisting fee. |
| **[`web-design-terms.html`](web-design-terms.html)** | Creative, UI/UX & Care Retainers | 13 Sections | 50% non-refundable deposit, net 30 (1.8% monthly interest), Small Claims Court of BC, $250 CAD file transfer fee, Criminal Code theft protections. |
| **[`privacy-policy.html`](privacy-policy.html)** | Data Privacy & GDPR/PIPEDA | 10 Sections | Self-hosted, PIPEDA & BC PIPA compliance, vetted sub-processor registry, DPO in Kamloops, OIPC BC complaint rights. |

---

## ⚡ Solutions Scope

Sheernox operates as a complete, end-to-end technology solutions provider. The contractual provisions across these documents comprehensively govern:

1. **Web Hosting Solutions**: Shared, Reseller, Cloud, VPS, and Dedicated Bare-Metal Servers.
2. **Domain Services**: Domain Registration, DNSSEC, Domain Transfers, and Domain Reseller Platforms.
3. **Email & Communication**: Secure Business Email, Webmail, Anti-Spam Filtering, and CASL compliance.
4. **Branding & Creative Design**: Brand Identity, Style Guides, Vector Assets, and UI/UX Prototyping.
5. **Website Care & Maintenance**: Scheduled CMS core updates, security patching, uptime checks, and database care.
6. **Server Management & Monitoring**: 24/7/365 infrastructure telemetry, reactive incident triage, and automated failover.
7. **DNS & Content Delivery Networks (CDN)**: Anycast global routing, DDoS mitigation, and edge caching.
8. **Storage & Disaster Recovery**: Automated encrypted backups (AES-256), off-site replication, and retention management.
9. **Custom Engineering & On-Site Deployments**: Bespoke system builds, network topology planning, rack cabling, datacenter commissioning, and hardware repairs.

---

## 🎨 Design System & Interactive Features

The portal utilizes the **Modern SaaS (Option 1)** design system, prioritizing rapid clause discovery, legal clarity, and executive accessibility:

- **Sticky Navigation & Dynamic Scrollspy**: Table of Contents (TOC) tracks reading location in real-time using native `IntersectionObserver` / scroll listeners.
- **Client-Side Clause Search**: Live filter input on sidebars and the directory hub instantly filters clauses by keyword without page reload.
- **Reading Progress Bar**: Dynamic gradient progress bar affixed to the top viewport tracks reading progress across lengthy agreements.
- **"In Plain English" Key Takeaways**: High-visibility callout boxes summarize dense contractual clauses into straightforward, executive-friendly summaries.
- **Deep Clause Permalinks (`#`)**: Every heading and clause block features a dedicated permalink button that copies direct anchored URLs to the clipboard with visual toast confirmations.
- **Typography & Accessibility**: Clean, legible typography powered by Google Fonts (`Inter` for body copy, `JetBrains Mono` for metadata, IPs, code, and ports) with WCAG AA compliant contrast ratios.
- **Native Print Stylesheets (`@media print`)**: Hides interactive sidebars, progress bars, and navigation headers, formatting the legal text with clean page breaks and professional headers for offline PDF generation.

---

## 🚀 Deployment & Local Development

This portal is **100% static** and has **zero build steps or runtime dependencies**. It can be deployed instantly to any web server or static hosting platform.

### Local Development

Serve the repository locally using any lightweight HTTP server:

```bash
# Python 3
python3 -m http.server 8080

# Node.js (via npx)
npx serve .

# PHP built-in server
php -S localhost:8080
```

Open `http://localhost:8080` in any modern web browser.

### Production Deployment Options

- **GitHub Pages**: Set source to branch `main` and root directory `/`.
- **Cloudflare Pages / Vercel / Netlify**: Connect repository, leave build command empty, and set publish directory to `/`.
- **Nginx / Apache**: Copy files directly into the web document root (e.g., `/var/www/html/`).

---

## 🛡️ Abuse & Compliance Reporting

To report system abuse, security vulnerabilities, or copyright infringement originating from Sheernox IP ranges:

- **Client Portal**: [my.sheernox.com](https://my.sheernox.com)
- **Abuse Desk**: `abuse@sheernox.com`
- **Legal & Compliance**: `legal@sheernox.com`
- **Data Privacy Officer**: `privacy@sheernox.com`
- **Location & Inquiries**: Sheernox Technology Group, Kamloops, British Columbia, Canada

---

## ⚖️ Copyright & Proprietary Rights

&copy; 2026 **Sheernox Technology Group**. All rights reserved. Registered sole proprietorship in Kamloops, British Columbia, Canada.
