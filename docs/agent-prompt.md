# 🤖 High-Level Prompt for Future AI Agents

Copy and paste the prompt below when instructing an AI agent to make policy updates:

```markdown
I need you to update the Sheernox Legal Portal in https://github.com/vSkilled/legal.sheernox.com.

Please read `AGENTS.md` thoroughly before beginning.

Here are the policy changes I need:
[INSERT POLICY CHANGES HERE, e.g., Update SLA credit percentage, add new sub-processor, etc.]

Operational Instructions:
1. Update the appropriate Astro page(s) in `src/pages/` directly while maintaining the established semantic structure (`<article class="legal-prose">`, `.legal-section`, `.key-takeaway`, etc.).
2. If metadata changes, update `src/data/documents.ts` with the new Last Revised date in ISO 8601 format (`YYYY-MM-DD`) and increment the version tag by 0.5 (format: `vX.X-KEY`, e.g., `v3.5-TOS`).
3. Ensure Canadian legal standards are strictly preserved (Kamloops BC sole proprietorship, support@sheernox.com for legal/privacy, abuse@sheernox.com for network abuse, official address: `1-1885 Grasslands Blvd, Kamloops, BC, V2B 0B8, Canada`).
4. Run `npm run build` to compile the static routes to `dist/`.
5. Run `npm run generate:pdfs` to generate production vector PDFs into `dist/` and `public/`.
6. Run `npm run generate:txts` to generate plain text documents into `dist/` and `public/`.
7. Run `npm test` to verify zero diagnostic errors or broken types.
8. Keep the repository clean to production code only.
9. Commit and push the changes to `origin/main`.
```
