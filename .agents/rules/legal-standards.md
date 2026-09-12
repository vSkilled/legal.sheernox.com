# Legal Documentation Engineering Standards

When creating, converting, or modifying legal documents and policies in the Sheernox Legal Portal:

1. **Verbatim Fidelity**: Maintain the exact original contractual phrasing, disclaimers, liability provisions, indemnity clauses, and capitalized defined terms. Never summarize or omit contract clauses.
2. **Structural Integrity**:
   - Each major article/section must have an unambiguous anchor `id` (e.g. `sec-terms-1`, `sec-aup-3`).
   - Retain complete numbered hierarchy (`1.`, `1.1`, `(a)`, `(i)`).
3. **Accessibility & Design Standards**:
   - Adhere to the Sheernox design tokens (Navy `#071322`, primary blue `#0f4c81`, neutral backgrounds `#f8fafc`).
   - Implement responsive Table of Contents (TOC) with scrollspy.
   - Include permalink copy buttons for legal clauses.
   - Include print stylesheets (`@media print`) and fallback links to download original PDF files.
4. **Portal Synchronization**:
   - When new legal documents are converted into HTML, update `index.html` cards so that:
     - The type pill indicates "HTML Document" or "Web Policy".
     - The "Open" action button routes directly to the local HTML document.
     - Direct PDF download options remain available as alternative formats.
