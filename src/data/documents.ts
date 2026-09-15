export interface LegalDocument {
  slug: string;
  sourceHtml: string;
  outputPdf: string;
  outputTxt: string;
  title: string;
  shortTitle: string;
  category: string;
  categorySlug: 'hosting' | 'aup' | 'privacy' | 'security' | 'compliance' | 'design';
  version: string;
  lastRevised: string;
  accentColor: string;
  colorTheme: 'blue' | 'amber' | 'emerald' | 'cyan' | 'purple' | 'rose' | 'coral' | 'teal';
  keywords: string;
  desc: string;
  bullets: string[];
}

export const LEGAL_DOCUMENTS: LegalDocument[] = [
  {
    slug: 'terms-and-conditions',
    sourceHtml: 'terms-and-conditions.html',
    outputPdf: 'terms-and-conditions.pdf',
    outputTxt: 'terms-and-conditions.txt',
    title: 'Terms and Conditions of Service',
    shortTitle: 'Terms and Conditions',
    category: 'Master Services Agreement',
    categorySlug: 'hosting',
    version: 'v4.5-TOS',
    lastRevised: '2026-09-13',
    accentColor: '#0284c7',
    colorTheme: 'blue',
    keywords: 'terms and conditions master service agreement billing SLA liability payment subscription hosting cloud vps dedicated domains email backups uptime',
    desc: 'Master service terms covering cloud hosting, VPS, dedicated servers, domain management, email, CDN, backups, and custom systems.',
    bullets: [
      'Shared, VPS, Dedicated & Cloud SLA (99.9% uptime)',
      'Domains, email, automated backups & CDN provisions',
      'Billing cycles, digital cancellation & liability limits',
    ],
  },
  {
    slug: 'acceptable-use-policy',
    sourceHtml: 'acceptable-use-policy.html',
    outputPdf: 'acceptable-use-policy.pdf',
    outputTxt: 'acceptable-use-policy.txt',
    title: 'Acceptable Use Policy (AUP)',
    shortTitle: 'Acceptable Use Policy',
    category: 'Network & Cloud Infrastructure Policy',
    categorySlug: 'aup',
    version: 'v4.0-AUP',
    lastRevised: '2026-09-12',
    accentColor: '#d97706',
    colorTheme: 'amber',
    keywords: 'acceptable use policy aup abuse spam security bandwidth resource limits bots scraping mining network cloud vps',
    desc: 'Comprehensive operational security standards, anti-spam enforcement, resource usage quotas, and system integrity rules.',
    bullets: [
      'Absolute zero-tolerance anti-spam (CAN-SPAM/CASL)',
      'Network security, intrusion prevention & DDoS mitigation',
      'Compute, storage fair use & AI bot scraping protections',
    ],
  },
  {
    slug: 'privacy-policy',
    sourceHtml: 'privacy-policy.html',
    outputPdf: 'privacy-policy.pdf',
    outputTxt: 'privacy-policy.txt',
    title: 'Privacy & Personal Information Policy',
    shortTitle: 'Privacy Policy',
    category: 'Privacy & Data Protection Policy',
    categorySlug: 'privacy',
    version: 'v4.5-PRIV',
    lastRevised: '2026-09-13',
    accentColor: '#059669',
    colorTheme: 'emerald',
    keywords: 'privacy gdpr pipeda ccpa data cookies protection personal tracking encryption sub-processors controller',
    desc: 'Comprehensive disclosure on personal data collection, telemetry, third-party sub-processors, and privacy rights under PIPEDA, GDPR, and CCPA/CPRA.',
    bullets: [
      'Global compliance & user data rights (Access, Erasure)',
      'Hosting, email, CDN & backup data handling rules',
      'Sub-processor registry, cookie controls & encryption',
    ],
  },
  {
    slug: 'service-level-agreement',
    sourceHtml: 'service-level-agreement.html',
    outputPdf: 'service-level-agreement.pdf',
    outputTxt: 'service-level-agreement.txt',
    title: 'Service Level Agreement & Incident Policy',
    shortTitle: 'Service Level Agreement',
    category: 'Cloud Infrastructure & Operations',
    categorySlug: 'hosting',
    version: 'v1.5-SLA',
    lastRevised: '2026-09-12',
    accentColor: '#2563eb',
    colorTheme: 'cyan',
    keywords: 'service level agreement sla incident policy uptime 99.9 incident response priority credit scheduled maintenance downtime penalty outage bare-metal vps',
    desc: 'Formal availability commitments across cloud hosting, VPS, and network infrastructure with transparent credit schedules.',
    bullets: [
      '99.9% monthly uptime guarantee & mathematical formula',
      'P1 (< 15 min) to P4 incident triage response matrix',
      'Tiered service credits up to 100% of monthly invoice',
    ],
  },
  {
    slug: 'vulnerability-disclosure-policy',
    sourceHtml: 'vulnerability-disclosure-policy.html',
    outputPdf: 'vulnerability-disclosure-policy.pdf',
    outputTxt: 'vulnerability-disclosure-policy.txt',
    title: 'Vulnerability Disclosure Policy (VDP)',
    shortTitle: 'Vulnerability Disclosure (VDP)',
    category: 'Cybersecurity & Trust Governance',
    categorySlug: 'security',
    version: 'v1.5-VDP',
    lastRevised: '2026-09-12',
    accentColor: '#7c3aed',
    colorTheme: 'purple',
    keywords: 'vulnerability disclosure policy vdp safe harbor security vulnerability ethical hacking bug bounty cvss reporting coordinated disclosure exploit penetration testing',
    desc: 'Official framework and safe harbor protections for ethical security researchers, penetration testers, and academic cryptographers.',
    bullets: [
      'Criminal Code s. 342.1 safe harbor authorization',
      'In-scope domains, edge DNS, and customer APIs',
      '48h receipt acknowledgement & 90-day coordinated release',
    ],
  },
  {
    slug: 'copyright-policy',
    sourceHtml: 'copyright-policy.html',
    outputPdf: 'copyright-policy.pdf',
    outputTxt: 'copyright-policy.txt',
    title: 'Copyright & Notice-and-Notice Policy',
    shortTitle: 'Copyright & Notice-and-Notice',
    category: 'Intellectual Property & Compliance',
    categorySlug: 'compliance',
    version: 'v1.5-CPR',
    lastRevised: '2026-09-12',
    accentColor: '#e11d48',
    colorTheme: 'rose',
    keywords: 'copyright notice-and-notice policy dmca intellectual property infringement canadian copyright act safe harbor 31.1 designated agent statutory log retention norwich',
    desc: 'Compliance framework under the Canadian Copyright Act Notice-and-Notice regime, forwarding timelines, log retention, and DMCA.',
    bullets: [
      'Statutory Notice-and-Notice forwarding without fee',
      'Mandatory 6 to 12-month IP log preservation rules',
      'Strict subscriber privacy protection (court order required)',
    ],
  },
  {
    slug: 'web-design-terms',
    sourceHtml: 'web-design-terms.html',
    outputPdf: 'web-design-terms.pdf',
    outputTxt: 'web-design-terms.txt',
    title: 'Web Design & Development Terms and Conditions',
    shortTitle: 'Web Design & Development Terms',
    category: 'Agency Services Agreement',
    categorySlug: 'design',
    version: 'v3.5-WDT',
    lastRevised: '2026-09-13',
    accentColor: '#ea580c',
    colorTheme: 'coral',
    keywords: 'web design branding care terms and conditions design development branding care maintenance ux approval milestones creative copyright sow agency',
    desc: 'Master terms governing branding, UI/UX architecture, custom web engineering (Jamstack, CMS, web apps), 30-day warranty, and IP transfer.',
    bullets: [
      'Discovery, UI/UX prototyping & staging review cycles',
      'Flexible architecture: Headless, modern CMS & custom apps',
      '30-day post-launch warranty & source code IP transfer',
    ],
  },
  {
    slug: 'website-care-plan-terms',
    sourceHtml: 'website-care-plan-terms.html',
    outputPdf: 'website-care-plan-terms.pdf',
    outputTxt: 'website-care-plan-terms.txt',
    title: 'Website Care Plan & Maintenance Terms',
    shortTitle: 'Website Care Plan Terms',
    category: 'Creative & Agency SOW Schedule',
    categorySlug: 'design',
    version: 'v1.5-WCP',
    lastRevised: '2026-09-13',
    accentColor: '#0d9488',
    colorTheme: 'teal',
    keywords: 'website care plan maintenance terms sow schedule care plan website maintenance retainer wordpress updates staging backups malware content support hourly rates',
    desc: 'Recurring maintenance Statement of Work (SOW) schedule covering CMS core updates, daily cloud backups, and included developer hours.',
    bullets: [
      'Essential, Professional, and Enterprise Care tiers',
      'Staging-first deployment protocol & rollback safety',
      'Up to 5 hours/mo content tasks & preferred CAD rates',
    ],
  },
];

export const DOC_BY_SLUG = new Map<string, LegalDocument>(
  LEGAL_DOCUMENTS.map((doc) => [doc.slug, doc])
);
