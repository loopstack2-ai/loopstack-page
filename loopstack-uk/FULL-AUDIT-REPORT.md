# Full SEO Audit Report: loopstack.uk

**Audit Date:** 24 June 2026
**URL:** https://loopstack.uk
**Business Type:** UK Service Area Business — AI Consultancy, Automation Agency, SaaS Development

---

## Executive Summary

### Overall SEO Health Score: 74/100

| Category | Weight | Score | Weighted |
|----------|--------|-------|----------|
| Technical SEO | 22% | 89/100 | 19.6 |
| Content Quality (E-E-A-T) | 23% | 72/100 | 16.6 |
| On-Page SEO | 20% | 80/100 | 16.0 |
| Schema / Structured Data | 10% | 85/100 | 8.5 |
| Performance (CWV) | 10% | 75/100 | 7.5 |
| AI Search Readiness (GEO) | 10% | 74/100 | 7.4 |
| Images | 5% | 60/100 | 3.0 |
| **Total** | **100%** | | **74/100** |

### Top 5 Critical Issues
1. **llms-full.txt returns 404** — AI crawlers hitting this link get a dead end
2. **Favicon 404** — `/favicon.svg` returns 404, browser console error
3. **Duplicate tenurai content** — root `tenurai.html` has no redirect, creating duplicate content risk
4. **No third-party social proof** — testimonials use initials only, no Trustpilot/Google reviews linked
5. **No YouTube presence** — strongest AI citation signal (0.737 correlation) is completely missing

### Top 5 Quick Wins
1. **Create llms-full.txt** — 10 minute fix, high GEO impact
2. **Copy favicon.svg to root** — resolves browser 404
3. **Add BreadcrumbList schema to homepage** — missing from index.html
4. **Expand hero copy to 60-80 words** — makes it citable by AI extracts
5. **Add Service schema to 7 service pages** — they currently only have Organization + BreadcrumbList

---

## 1. Technical SEO — 89/100

### Crawlability — 9/10 ✅
| Check | Status | Details |
|-------|--------|---------|
| robots.txt | ✅ PASS | All AI crawlers explicitly allowed. Sitemap declared. |
| Sitemap | ✅ PASS | 16 URLs, valid XML, changefreq + priority set |
| Status code 200 | ✅ PASS | All sitemap URLs return 200 |
| Redirects | ⚠️ WARN | `/tenurai.html` returns 200 instead of 301 to `/projects/tenurai` |

### Indexability — 7/10 ⚠️
| Check | Status | Details |
|-------|--------|---------|
| Canonical tags | ✅ PASS | Self-referencing on all pages |
| Robots meta | ✅ PASS | `index, follow, max-snippet:-1` — optimal |
| Hreflang | ⚠️ WARN | Present on homepage only, missing from 15 subpages |
| Duplicate content | ⚠️ WARN | Root `tenurai.html` duplicates `/projects/tenurai` |

### Security — 10/10 ✅
| Header | Value | Status |
|--------|-------|--------|
| HSTS | `max-age=31536000` | ✅ PASS |
| X-Frame-Options | `DENY` | ✅ PASS |
| X-Content-Type-Options | `nosniff` | ✅ PASS |
| X-XSS-Protection | `1; mode=block` | ✅ PASS |
| Referrer-Policy | `strict-origin-when-cross-origin` | ✅ PASS |

### URL Structure — 9/10 ✅
- Extensionless clean URLs with 301 redirects from .html versions ✅
- Logical hierarchy: `/insights/`, `/projects/` ✅
- `/tenurai.html` returns 200 (no 301) ⚠️

---

## 2. Content Quality & E-E-A-T — 72/100

### E-E-A-T Score Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Experience | 18/20 ✅ | Founder's detailed career bio, shipped products (TenurAI, Recruit) |
| Expertise | 18/25 ⚠️ | Strong technical knowledge, but no formal AI certifications shown |
| Authoritativeness | 14/25 ⚠️ | No external backlinks, no 3rd-party reviews, anonymous testimonials |
| Trustworthiness | 22/30 ⚠️ | Transparent pricing, but no registered address, no company number |

**Total E-E-A-T: 72/100**

### Readability — Good ✅
- Jargon-light, accessible language for non-technical buyers
- Paragraphs 2-4 sentences, appropriate for web
- Some service page copy is structurally repetitive

### Thin Content — No issues ✅
- Every page has substantial content (400-2,500+ words)
- No page falls below 300 words

### Duplicate Content — Low risk ⚠️
- Shared template content (FAQ, pricing, nav, footer) across service pages is expected and not penalised
- Root `tenurai.html` duplicates `/projects/tenurai` — fix needed

### Internal Linking — Needs improvement ⚠️
- Footer `#pricing` and `#faq` anchors break on non-homepage pages
- No contextual cross-links between service pages
- Footer Services column duplicates links

---

## 3. On-Page SEO — 80/100

### Meta Tags
| Page | Title | Description | Status |
|------|-------|-------------|--------|
| Home | Fixed Price AI Consultant UK from £997 \| AI Automation — LoopStack | ✅ Good keyword targeting | ✅ |
| /about | About Andy Hatcher — LoopStack AI Automation Consultant | ✅ | ✅ |
| Service pages | Varies per page | ✅ Present on all | ✅ |

### Heading Structure
- H1: Clear, keyword-optimised on homepage ✅
- H2/H3 hierarchy present on all pages ✅
- Some service pages have weak differentiation in headings ⚠️

### Mobile UX — 9/10 ✅
- Responsive viewport meta tag ✅
- `text-size-adjust: 100%` ✅
- No separate mobile site ✅

---

## 4. Schema & Structured Data — B+ / 85/100

### Implemented Schema Types
| Type | Location | Status |
|------|----------|--------|
| Organization | Homepage + subpages | ✅ Rich with legalName, address, contactPoint, sameAs |
| Person | Homepage + About | ✅ Detailed with 35+ year experience, knowsAbout |
| ProfessionalService | Homepage + ai-automation-consultant | ✅ With AggregateRating, priceRange |
| WebSite | Homepage + 404 | ✅ |
| WebPage | Homepage + 404 | ✅ |
| FAQPage | Homepage (12 Q&A) | ✅ Excellent GEO value |
| Review (x3) | Homepage | ✅ 5-star ratings |
| OfferCatalog | Nestled in Organization | ✅ 3 tiers with GBP pricing |
| AggregateRating | Homepage | ✅ 5.0, 3 reviews |
| Article + BreadcrumbList | Insight pages | ✅ |
| CollectionPage | Insights hub | ✅ |

### Missing Schema (Priority Order)
| Schema Type | Where Needed | Priority |
|-------------|-------------|----------|
| **BreadcrumbList** | Homepage | 🔴 High |
| **Service** | 7 service pages (currently only have Organization + BreadcrumbList) | 🔴 High |
| **Product + Offer** | tenurai.html | 🟡 Medium |
| **VideoObject** | Homepage (services video) | 🟡 Medium |
| **ImageObject** | About page (founder photo) | 🟢 Low |

---

## 5. Performance (CWV) — 75/100

### Lab Data (PageSpeed Insights)
| Metric | Mobile | Desktop | Rating |
|--------|--------|---------|--------|
| Performance Score | **84/100** | **97/100** | 🟢 Desktop 🟡 Mobile |
| LCP | 3.4s | 1.0s | 🟡 Mobile 🟢 Desktop |
| CLS | 0.019 | 0 | 🟢 Both |
| TBT | 0ms | 0ms | 🟢 Both |
| FCP | 3.4s | 1.0s | 🟡 Mobile 🟢 Desktop |
| SI | 3.4s | 1.0s | 🟢 Both |

### Field Data (CrUX)
- **No data available** — insufficient Chrome traffic for real-user metrics

### Opportunities
- **Mobile LCP at 3.4s** is the biggest drag (desktop is 1.0s)
- Render-blocking Google Fonts CSS is the main cause
- No images, no SPAs, no heavy JS — the technical foundation is clean

### Recommendations
- Preload Google Fonts CSS with non-blocking pattern
- Consider `font-display: swap` verification
- No other performance bottlenecks identified

---

## 6. AI Search Readiness (GEO) — 74/100

| Dimension | Score | Status |
|-----------|-------|--------|
| AI Crawler Access | 100/100 | ✅ Best-in-class, all crawlers allowed |
| llms.txt | 75/100 | ⚠️ llms-full.txt returns 404 |
| FAQ Schema Quality | 78/100 | ✅ Good, but missing GDPR/industry-specific Q&A |
| Passage Citability | 68/100 | ⚠️ Key passages too short for AI extraction |
| Authority & Brand | 62/100 | ⚠️ No YouTube, no Wikipedia, no review platforms |
| Technical Accessibility | 95/100 | ✅ Static HTML, full SSR, clean schema |
| **Total** | **74/100** | |

### Top GEO Gaps
1. **llms-full.txt returns 404** — critical fix
2. **No YouTube channel** — strongest AI citation signal missing
3. **FAQ answers too short** — need 80-120 word self-contained answers
4. **No external citations** — no press mentions, awards, or directory listings
5. **No Google Business Profile** visible — important for local + AI citations

### Platform-Specific Readiness
| Platform | Est. Visibility | Notes |
|----------|---------------|-------|
| Google AI Overviews | Medium | Strong FAQ schema, weak external citations |
| ChatGPT/OpenAI Search | Medium-High | llms.txt present, all crawlers allowed |
| Perplexity | Medium-High | Strong on-page, weak off-page signals |
| Bing Copilot | Medium | Technical setup strong, social signals weak |
| Claude | High | Explicitly allowed, llms.txt present |

---

## 7. Google Search Console Data (Last 28 Days)

| Metric | Value |
|--------|-------|
| Total Clicks | 3 |
| Total Impressions | 1,287 |
| Average CTR | 0.2% |
| Average Position | 60.8 |

### Top Queries
| Query | Clicks | Impressions | CTR | Position |
|-------|--------|------------|-----|----------|
| andy hatcher | 1 | 2 | 50.0% | 2.5 |
| loopstack | 1 | 6 | 16.7% | 13.3 |
| loopstack ai | 1 | 2 | 50.0% | 8.5 |

### Key Observation
All clicks are brand-name queries. No non-brand clicks. The site is visible in search but ranking at positions 60-80 for non-brand terms — typical for a new domain.

---

## 8. Images — 60/100

| Check | Status | Details |
|-------|--------|---------|
| Alt text on images | ✅ PASS | No images on most pages |
| Image compression | N/A | Only og-image.png exists on the site |
| Missing og:image | ✅ PASS | OG image is 1200x630, present with alt text |
| Favicon | ❌ FAIL | `/favicon.svg` returns 404 |

The site is almost entirely text/CSS-based with no `<img>` elements on the homepage or service pages. This is good for performance but a missed opportunity for visual engagement. Consider adding:
- Screenshots of automation workflows on service pages
- Architecture diagrams on case study pages
- Team photo or workspace image on About page

---

## Scoring Summary

| Category | Weight | Score | Weighted | Priority |
|----------|--------|-------|----------|----------|
| Technical SEO | 22% | 89 | 19.6 | 🟢 Strong |
| Content Quality | 23% | 72 | 16.6 | 🟡 Needs work |
| On-Page SEO | 20% | 80 | 16.0 | 🟢 Good |
| Schema / Data | 10% | 85 | 8.5 | 🟢 Strong |
| Performance | 10% | 75 | 7.5 | 🟡 Needs work |
| AI Readiness | 10% | 74 | 7.4 | 🟡 Needs work |
| Images | 5% | 60 | 3.0 | 🟡 Needs work |
| **Overall** | **100%** | | **74/100** | |

---

*Audit performed via Chrome DevTools, Google PageSpeed Insights API, Search Console API, and manual page inspection. Google API credentials: Tier 1 (API Key + Service Account).*
