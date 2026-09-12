# Sheernox Legal Portal Design System & Component Library

## Color Palette
```css
:root {
  --sn-dark-navy: #071322;
  --sn-sidebar-navy: #0b192c;
  --sn-primary-blue: #0f4c81;
  --sn-accent-cyan: #0284c7;
  --sn-amber: #f59e0b;
  --sn-emerald: #10b981;
  --sn-coral: #ef4444;
  --canvas-bg: #f8fafc;
  --surface-card: #ffffff;
  --border-color: #e2e8f0;
  --border-subtle: #edf2f7;
  --text-main: #0f172a;
  --text-muted: #475569;
  --text-subtle: #94a3b8;
}
```

## Typography
- **Primary Body**: `'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
- **Monospace/Code/Permalinks**: `'JetBrains Mono', monospace`
- **Line Height**: `1.6` to `1.75` for legal prose.

## Component Patterns

### 1. Legal Callout Box (Warning & Statutory Notice)
```html
<div class="legal-callout callout-warning">
  <div class="callout-icon">⚠️</div>
  <div class="callout-body">
    <h4>WARNING</h4>
    <p>Abuse of your service will result in your accounts being suspended or terminated...</p>
  </div>
</div>
```

### 2. Clause Deep Linking & Permalinks
Each major section and numbered provision must provide an interactive permalink button:
```html
<div class="clause-header">
  <h3 id="clause-1-1">1.1 Account Registration</h3>
  <a href="#clause-1-1" class="clause-anchor" title="Direct link to this clause">#</a>
</div>
```

### 3. Sticky Sidebar TOC with Scrollspy
- Highlights the current section in view.
- Smooth scroll on click.
- Collapsible on mobile viewports (< 960px).

### 4. Print Layout
```css
@media print {
  .top-nav, .legal-sidebar, .card-actions-bar, .search-box, .btn-pdf, footer {
    display: none !important;
  }
  body {
    background: #fff;
    color: #000;
  }
  .legal-content {
    max-width: 100%;
    margin: 0;
    padding: 0;
  }
}
```
