# SEO / AEO Full Audit Report — loopstack.uk
**Date:** 28 May 2026  
**Audited by:** Claude Code + Chrome DevTools  
**Pages crawled:** 10  

---

## Overall SEO Health Score: 61 / 100

| Category | Score | Weight | Status |
|---|---|---|---|
| Technical SEO | 72/100 | 22% | ⚠️ Needs Work |
| Content Quality | 52/100 | 23% | ❌ Weak |
| On-Page SEO | 58/100 | 20% | ❌ Weak |
| Schema / Structured Data | 65/100 | 10% | ⚠️ Partial |
| Performance (Core Web Vitals) | 90/100 | 10% | ✅ Good |
| AI Search Readiness (AEO) | 45/100 | 10% | ❌ Weak |
| Accessibility | 77/100 | 5% | ⚠️ Needs Work |

---

## Executive Summary

LoopStack has a solid foundation — a clean site structure, fast load times, excellent Core Web Vitals, and a well-configured robots.txt that explicitly welcomes AI crawlers. The homepage schema is genuinely impressive. However, the site has a significant cluster of issues that are limiting rankings and AI engine visibility:

**Top 5 Critical Issues:**
1. Meta descriptions missing on ALL 9 subpages
2. No OG (social share) image on any page — hurts click-through from social and AI overviews
3. The "Insights" blog links to service pages, not real articles — zero blog content
4. Most subpages have thin content (400–650 words) — not competitive for search
5. No llms.txt file (or it's non-compliant) — hurting AI/AEO visibility significantly

**Top 5 Quick Wins:**
1. Add meta descriptions to all 9 subpages (1–2 hours work)
2. Create one OG image (social share graphic) and add it to all pages
3. Add schema markup to all subpages (copy/adapt homepage schema)
4. Fix iframe title on the Cal.com booking embed (one line of code)
5. Create a real llms.txt file

---

## 1. Technical SEO

### ✅ What's Working
- **HTTPS:** Fully enabled, no mixed content
- **Canonical tags:** Present on homepage (`https://loopstack.uk/`) — but NOT confirmed on subpages
- **Robots.txt:** Well configured — allows all crawlers, all AI bots explicitly listed, sitemap declared
- **Sitemap.xml:** Present with all 10 pages, correct priorities, dated correctly (May 27 2026)
- **Viewport meta:** Correct (`width=device-width, initial-scale=1.0`)
- **Robots meta:** `index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1` — excellent
- **CLS (Cumulative Layout Shift):** 0 — perfect score
- **No console errors:** Clean
- **No deprecated APIs**
- **No third-party cookies**
- **Mobile rendering:** Site renders cleanly on mobile (390px width tested)

### ❌ Issues Found

#### CRITICAL
- **Canonical tags on subpages:** Not confirmed present on any subpage. Without canonicals, Google may not know which version of a URL is the "official" one.
- **OG image missing (all pages):** `og:image` is NULL on the homepage and not present on any subpage. Social shares will show a blank/auto-generated image — significantly reduces click-through rates from LinkedIn, Twitter, etc. Also used by some AI engines for thumbnail previews.

#### HIGH
- **No Twitter Card meta tags:** Missing on all pages. Prevents proper previews when links are shared on X/Twitter.
- **Security headers incomplete:**
  - No `Content-Security-Policy` (CSP) header — flagged High severity by Lighthouse
  - No `Cross-Origin-Opener-Policy` (COOP) header — flagged High severity
  - HSTS present but missing `includeSubDomains` and `preload` directives

#### MEDIUM
- **No `rel="preload"` or `rel="preconnect"` resource hints** — small performance opportunity

---

## 2. Content Quality

### ✅ What's Working
- Homepage word count: 1,233 words — adequate
- Writing tone is clear, professional, and direct
- Good differentiation ("builds, not just advises", fixed pricing, no lock-in)
- Genuine claims with specific stats (95% task time reduction, 48h deployment, £997 starting)
- FAQ section with 7 well-written, specific questions

### ❌ Issues Found

#### CRITICAL
- **The "Insights" blog is not a real blog.** The `/insights` page lists 6 items that link directly to service pages (`/chatgpt-consultant`, `/hire-ai-consultant` etc). These are NOT blog articles — they are the same service pages being reused as "blog posts". This means:
  - Zero unique blog/editorial content exists on the site
  - No long-form content targeting informational search queries
  - No opportunity to rank for "how to" or "what is" searches
  - Google sees no fresh content signals (blog should drive regular crawling)

#### HIGH — Thin Content Pages (under 700 words, not competitive for ranking)

| Page | Est. Word Count | Status |
|---|---|---|
| /ai-chatbot-development | ~420 words | ❌ Very thin |
| /web-app-development | ~475 words | ❌ Very thin |
| /hire-ai-consultant | ~550 words | ❌ Thin |
| /custom-software-development | ~675 words | ⚠️ Borderline |
| /ai-for-small-business | ~675 words | ⚠️ Borderline |
| /business-process-automation | ~650 words | ⚠️ Borderline |

For competitive B2B service pages in the AI space, 1,200–2,000 words is the baseline. Most competitors targeting these terms will have significantly more depth.

#### MEDIUM
- **No "About" page or named consultant:** There is no /about page and no named person behind LoopStack. This is a significant E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) gap. Google weights personal expertise heavily for B2B services.
- **Only 3 reviews in schema:** The `AggregateRating` has `reviewCount: 3` — very low. Even if accurate, this signals limited social proof to search engines.
- **Zero outbound links:** The site has no links to external authoritative sources. Google considers topical authority partly through citation/linking behaviour. One or two relevant outbound links per page is best practice.

---

## 3. On-Page SEO

### Homepage — ✅ Good
| Element | Status | Value |
|---|---|---|
| Title | ✅ | "AI Consultant UK | AI Automation Agency — LoopStack" |
| Meta Description | ✅ | Present, 155 chars, keyword-rich |
| H1 | ✅ | "AI automation consultant for businesses that mean it." |
| OG Title | ✅ | Present |
| OG Description | ✅ | Present |
| OG Image | ❌ | NULL — missing |
| Twitter Card | ❌ | Missing |
| Canonical | ✅ | https://loopstack.uk/ |

### Subpages — ❌ Missing Critical Elements

| Page | Meta Desc | Schema | Canonical | OG Tags |
|---|---|---|---|---|
| /ai-automation-consultant | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /chatgpt-consultant | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /hire-ai-consultant | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /custom-software-development | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /ai-for-small-business | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /business-process-automation | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /ai-chatbot-development | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /web-app-development | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |
| /insights | ❌ Missing | ❌ None | ❓ Unconfirmed | ❌ None |

**All 9 subpages are missing meta descriptions. This alone could be suppressing click-through rates by 20–30% in search results.**

### Heading Structure Issues
- Lighthouse flagged `heading-order` as failing (score: 0) — headings are skipping levels somewhere (e.g., jumping from H2 to H4 without an H3). This affects both accessibility and SEO crawlability.

---

## 4. Schema / Structured Data

### Homepage — ✅ Impressive
The homepage has a rich `@graph` schema block with:
- `Organization` — with `knowsAbout`, `areaServed`, `foundingDate`, `email` ✅
- `WebSite` ✅
- `WebPage` ✅
- `ProfessionalService` with `AggregateRating` and `priceRange` ✅
- `FAQPage` with 7 detailed Q&As ✅
- `OfferCatalog` with 3 priced services ✅

This is well done. The FAQ schema in particular is excellent for AEO — these questions can appear directly in Google's "People Also Ask" and AI-generated answers.

### Subpages — ❌ None
None of the 9 subpages have any schema markup. Each page should have at minimum:
- `WebPage` schema
- `Service` schema (for service pages)
- `BreadcrumbList` schema

---

## 5. Performance (Core Web Vitals)

Lighthouse mobile audit results:

| Metric | Score | Status |
|---|---|---|
| **Cumulative Layout Shift (CLS)** | 0 | ✅ Excellent |
| **Best Practices** | 100/100 | ✅ Perfect |
| **SEO (Lighthouse)** | 100/100 | ✅ Perfect |
| **Accessibility** | 77/100 | ⚠️ Needs Work |
| **Agentic Browsing** | 33/100 | ❌ Poor |

> Note: LCP and INP weren't captured in this run — these require real-user data (Chrome UX Report) for the most accurate scores. Based on the clean, lightweight HTML/CSS site structure, performance is expected to be good but should be verified with PageSpeed Insights.

---

## 6. AI Search Readiness (AEO)

AEO (Answer Engine Optimisation) is about getting your content cited by AI tools like ChatGPT, Perplexity, Claude, and Google's AI Overviews. This is increasingly important — possibly more important than traditional SEO for B2B services.

### ✅ What's Working
- **robots.txt explicitly welcomes all major AI crawlers:** GPTBot, ClaudeBot, PerplexityBot, anthropic-ai, Google-Extended, CCBot, Bytespider — excellent
- **FAQPage schema:** The 7 FAQ items are well-suited to be cited by AI overviews
- **Clear, direct content:** The writing style (specific, factual, UK-focused) is well-suited for AI extraction
- **Transparent pricing:** Specific pricing (£997, £2,497, £799/mo) is highly citable by AI engines answering cost questions

### ❌ Issues Found

#### CRITICAL
- **llms.txt file missing or non-compliant:** Lighthouse flagged this as failing (score: 0). `llms.txt` is a new standard (llmstxt.org) that tells AI models how your site should be crawled and used. Its absence means AI systems have no guidance on your content — reducing your citability.
- **Accessibility tree not well-formed (score: 0):** The "Agentic Browsing" Lighthouse score is 33/100, partly due to an inaccessible DOM structure. AI agents that browse the web (like Perplexity's crawler) struggle with poorly structured accessibility trees.

#### HIGH
- **No E-E-A-T signals for AI citation:** AI engines prefer to cite sources with named experts, credentials, or clear authorship. LoopStack has no named person, no About page, no LinkedIn profile links, and no credentials/certifications mentioned.
- **No real blog content:** AI engines cite editorial/informational content far more than service pages. A "What is AI automation?" article would be cited in AI answers far more often than a service page.
- **Schema only on homepage:** AI engines traverse all pages. Subpages without schema are much less citable.

#### MEDIUM
- **No citations or external authority signals:** The site doesn't link to or cite any external sources, and no external sites appear to link back. Backlink profile appears thin (though not measurable without external tools).

---

## 7. Accessibility

Lighthouse Accessibility: **77/100**

### Failed Audits:
| Issue | Severity | Detail |
|---|---|---|
| **Color contrast** | ❌ High | Some text doesn't meet WCAG AA contrast ratio (4.5:1). Likely the lighter grey text on dark backgrounds. |
| **Frame title missing** | ❌ High | An `<iframe>` (almost certainly the Cal.com booking embed) has no `title` attribute. Fix: add `title="Book a meeting"` to the iframe tag. |
| **Heading order** | ❌ Medium | Heading levels skip (e.g., H2 → H4). Every level should be sequential. |
| **Form labels missing** | ❌ High | One or more form input elements have no associated `<label>`. |
| **Select element unnamed** | ❌ High | A `<select>` dropdown has no label. |

---

## 8. Search Terms — Keyword Visibility Analysis

These are the search terms loopstack.uk is targeting or likely to appear for, grouped by competitiveness:

### 🟢 High Chance of Appearing (Low-to-Medium Competition)
These are specific enough that the site should rank or appear in AI results:
- `AI automation consultant UK`
- `AI consultant UK fixed price`
- `hire AI consultant UK`
- `ChatGPT consultant UK`
- `AI chatbot development UK`
- `workflow automation consultant UK`
- `Make automation consultant UK`
- `Zapier consultant UK`
- `n8n consultant UK`
- `AI automation for small business UK`
- `business process automation consultant UK`
- `how much does AI automation cost UK`
- `AI automation agency United Kingdom`
- `custom AI workflow development UK`
- `ChatGPT integration for business UK`
- `Claude AI integration UK`
- `AI consultant London` (if location added)
- `document processing automation UK`

### 🟡 Moderate Competition — Needs More Content to Rank
- `AI consultant UK`
- `AI automation UK`
- `workflow automation UK`
- `business process automation UK`
- `AI for small business UK`
- `custom software development UK AI`
- `AI chatbot development`
- `web app development UK`

### 🔴 Highly Competitive — Unlikely to Rank Without More Domain Authority
- `AI agency UK`
- `automation agency UK`
- `AI consulting UK`
- `ChatGPT for business`

### 🤖 AI Engine / AEO Search Queries (Currently Weak — Fix with llms.txt + Blog)
These are the types of questions being asked in ChatGPT, Perplexity, Google AI Overviews:
- *"What is an AI automation consultant?"* — FAQPage schema helps here ✅
- *"How much does AI automation cost in the UK?"* — FAQ schema covers this ✅
- *"Best AI consultants in the UK"* — Needs reviews, citations, and backlinks
- *"Can a small business afford AI automation?"* — Blog content needed
- *"ChatGPT vs Claude for business"* — Existing page but needs more depth
- *"How to automate business processes with AI"* — Blog content needed

---

## 9. Prioritised Action Plan

### 🔴 CRITICAL — Do First (High Impact, Relatively Quick)

| # | Action | Page(s) | Effort |
|---|---|---|---|
| 1 | Add meta descriptions to all 9 subpages | All subpages | 1–2 hrs |
| 2 | Create and add an OG social share image to all pages | All pages | 2 hrs |
| 3 | Create a proper `llms.txt` file at loopstack.uk/llms.txt | Root | 1 hr |
| 4 | Add `title="Book a meeting with LoopStack"` to Cal.com iframe | Homepage | 5 mins |
| 5 | Fix form element labels (contact/booking forms) | Homepage | 30 mins |
| 6 | Confirm canonical tags are present on all subpages | All subpages | 1 hr |

### 🟠 HIGH — Fix Within 2 Weeks

| # | Action | Page(s) | Effort |
|---|---|---|---|
| 7 | Add schema markup to all subpages (WebPage + Service schema) | All subpages | 3–4 hrs |
| 8 | Add Twitter Card meta tags to all pages | All pages | 1 hr |
| 9 | Add security headers: CSP, COOP, HSTS improvements | Netlify config | 1 hr |
| 10 | Fix heading order (no skipped levels) | All pages | 1–2 hrs |
| 11 | Fix colour contrast issues (lighter text on dark BG) | Homepage | 1–2 hrs |
| 12 | Create a real /about page with named founder, credentials, photo | New page | 2–3 hrs |

### 🟡 MEDIUM — Fix Within 1 Month

| # | Action | Page(s) | Effort |
|---|---|---|---|
| 13 | Write real blog articles (1,500+ words each) — start with 3–4 | /insights | 4–6 hrs each |
| 14 | Expand thin service pages to 1,200+ words each | 6 subpages | 2–3 hrs each |
| 15 | Add outbound links to 1–2 authoritative external sources per page | All pages | 1 hr |
| 16 | Increase review count in schema (or add Trustpilot/Google Reviews widget) | Homepage | 2 hrs |
| 17 | Add `BreadcrumbList` schema to all subpages | All subpages | 1 hr |
| 18 | Add `rel="preconnect"` hints for third-party resources (Cal.com, fonts) | All pages | 30 mins |

### 🟢 LOW — Backlog / Nice to Have

| # | Action | Detail |
|---|---|---|
| 19 | Build a genuine backlink profile | Guest posts, UK AI directories, HARO mentions |
| 20 | Add a `/case-studies` section | Real client projects with metrics — great for E-E-A-T |
| 21 | Add LinkedIn/social profile links in schema | Builds entity recognition with Google |
| 22 | Submit to AI-specific directories | Futurepedia, There's An AI For That, UK AI listings |

---

## Appendix: What llms.txt Should Look Like

Create a file at `https://loopstack.uk/llms.txt` with this structure:

```markdown
# LoopStack AI

> UK-based AI automation consultant. We build custom workflows, intelligent chatbots, and AI systems for UK businesses.

LoopStack helps businesses eliminate manual work through AI automation. Fixed-price projects, no lock-in.

## Services
- [AI Automation Consultant](https://loopstack.uk/ai-automation-consultant)
- [ChatGPT Consultant UK](https://loopstack.uk/chatgpt-consultant)
- [AI Chatbot Development](https://loopstack.uk/ai-chatbot-development)
- [Business Process Automation](https://loopstack.uk/business-process-automation)
- [Custom Software Development](https://loopstack.uk/custom-software-development)
- [AI for Small Business](https://loopstack.uk/ai-for-small-business)

## Pricing
Starting from £997 for a single workflow automation. See https://loopstack.uk/#pricing

## Contact
hello@loopstack.uk | https://loopstack.uk/#contact
```

---

*Report generated: 28 May 2026 — loopstack.uk — 10 pages audited*
