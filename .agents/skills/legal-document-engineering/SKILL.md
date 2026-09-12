---
name: legal-document-engineering
description: >-
  Expert guide for digitizing, formatting, and engineering legal documentation,
  contracts, MSAs, SLAs, Terms of Service, and compliance policies into modern,
  semantic, accessible HTML5 web experiences. Use when creating, converting,
  updating, or reviewing legal portal documents, policies, or contracts.
---

# Legal Document Engineering Skill

This skill guides the digitization and conversion of complex legal documents (PDFs, Word documents, scanned agreements) into semantic, responsive, and accessible HTML5 web pages suitable for enterprise legal portals.

---

## 1. Cardinal Rules of Legal Document Engineering

### A. Strict Textual & Verbatim Integrity
- **Never summarize, paraphrase, or alter legal wording** unless explicitly directed by the client or counsel.
- **Preserve Capitalized Defined Terms**: Capitalization carries precise legal meaning in contracts (e.g., "Client", "Agreement", "Effective Date", "Services"). Do not normalize to sentence case.
- **Preserve Statutory All-Caps & Emphasized Text**: Retain uppercase typography for warranty disclaimers, liability caps, and consumer statutory notices (e.g., Uniform Commercial Code / E-SIGN Act disclosures).

### B. Hierarchical Structure & Deep-Linking
- Every article, section, and subsection must possess a distinct, predictable HTML `id` attribute (e.g., `id="sec-1"`, `id="sec-1-2"`, `id="clause-1-2-a"`).
- Provide copyable permalink anchors for each clause so counsel and clients can reference exact provisions via URL.
- Maintain original legal numbering schemas (`1.`, `1.1`, `1.1.1`, `(a)`, `(i)`).

### C. Enterprise Legal UX & Navigation
- **Sticky Table of Contents (TOC)**: Large agreements must have a sticky left- or right-hand sidebar navigation reflecting the document structure with active scrollspy tracking.
- **Document Metadata Header**:
  - Document Title
  - Document Identifier / Classification
  - Effective Date & "Last Revised" Date
  - Download PDF button / link
- **In-Page Quick Search**: Filter clauses or search keywords directly within lengthy terms.
- **Back-to-Top**: Provide seamless navigation back to the document root.

### D. Accessibility & Readability (WCAG 2.1 AA)
- Minimum 4.5:1 text-to-background contrast ratio (7:1 for fine print).
- Legible typographic scale with line-height between `1.6` and `1.75`.
- Reading measure constrained to `65ch`–`80ch` for legal copy blocks.
- Semantic HTML elements (`<article>`, `<header>`, `<nav>`, `<section>`, `<dl>`, `<dt>`, `<dd>`).

### E. Print & Export Fidelity
- Dedicated `@media print` stylesheets:
  - Hide navigation bars, sticky TOC, search boxes, and action buttons.
  - Apply clean margins (`0.75in`), black serif or high-legibility sans-serif text.
  - Use `break-before: page` or `break-inside: avoid` to avoid awkward clause splits across printed pages.
  - Automatically print link URLs using `a[href]::after { content: " (" attr(href) ")"; }` for external references.

---

## 2. Standard Document Architecture

When creating an HTML page for a Sheernox legal document, use the canonical template structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Document Title] | Sheernox Legal Portal</title>
  <!-- Brand Fonts & Styles -->
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <!-- Global Portal Navigation -->
  <header class="legal-nav">...</header>

  <!-- Document Meta Header -->
  <div class="doc-header">
    <div class="container">
      <nav class="breadcrumbs">...</nav>
      <h1>[Document Title]</h1>
      <div class="doc-meta-badges">
        <span class="meta-item">Last Revised: [YYYY-MM-DD]</span>
        <span class="meta-item">Version: [X.X]</span>
        <a href="[PDF_URL]" class="btn-pdf-download">Download Official PDF</a>
      </div>
    </div>
  </div>

  <!-- Document Body Grid (Sidebar + Content) -->
  <div class="legal-layout container">
    <!-- Sticky TOC Sidebar -->
    <aside class="legal-sidebar">
      <div class="toc-wrapper">
        <h4>Table of Contents</h4>
        <nav id="docTOC" class="toc-list">...</nav>
      </div>
    </aside>

    <!-- Main Legal Text Content -->
    <main class="legal-content">
      <article>
        <!-- Notice Callouts (Warning, Disclaimers) -->
        <div class="legal-callout callout-warning">...</div>

        <!-- Sections -->
        <section id="sec-1" class="legal-section">
          <div class="section-title-wrap">
            <h2>1. [Section Title]</h2>
            <button class="anchor-copy-btn" onclick="copyClauseLink('sec-1')">#</button>
          </div>
          <div class="section-body">...</div>
        </section>
      </article>
    </main>
  </div>

  <!-- Footer -->
  <footer class="legal-footer">...</footer>
</body>
</html>
```

---

## 3. Conversion Workflow from PDF/Source

1. **Extract Source Text**: Extract full plain text while preserving paragraph demarcations, headers, and bullet structures.
2. **Scrub Artifacts**: Remove repetitive page headers, footers, "Page X of Y", and printer artifacts.
3. **Parse Hierarchy**: Identify document metadata (Last Revised date, contracting parties, preliminary disclaimers) and section hierarchy.
4. **Mark Up Semantic HTML**:
   - Wrap statutory all-caps warnings in `<div class="legal-callout callout-warning">` or `<div class="legal-notice">`.
   - Structure clauses with nested `<ol class="legal-list">` or explicit `<div class="clause" id="...">` items.
   - Retain full text without omissions.
5. **Build Table of Contents**: Extract section headings to populate the sidebar navigation automatically.
6. **Cross-Link & Test**: Verify internal links, TOC scrollspy behavior, anchor copy triggers, and mobile layout.
