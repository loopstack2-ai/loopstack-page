# TenurAI — Full SEO & AEO Audit Report

**URL:** https://tenurai.co.uk
**Date:** 15 June 2026
**Product:** Renters' Rights Act compliance SaaS for UK letting agents & landlords
**Audit type:** Comprehensive (Technical SEO + Content + Schema + SXO + GEO/AEO)

---

## Executive Summary

| Metric | Score |
|---|---|
| **Overall SEO Health** | **42/100** |
| Technical SEO | 68/100 |
| Content Quality | 55/100 |
| On-Page SEO | 50/100 |
| Schema / Structured Data | **0/100** |
| Performance (CWV) | 65/100 |
| AI Search Readiness (GEO) | **41/100** |
| SXO / Intent Match | **35/100** |

### The Core Problem

**The site has zero Google index presence.** A `site:tenurai.co.uk` search returns no results. The domain is effectively invisible to both Google and AI models.

This is caused by a compound problem:
1. **Single landing page** — Google sees thin site architecture (1 real page)
2. **Zero structured data** — no schema markup of any kind
3. **Zero backlinks** — no external authority signals
4. **Page-type mismatch** — the SERP for lettings compliance keywords rewards **comparison/review pages**, not single-vendor landing pages
5. **Brand-new domain** — no aging, no trust, no crawl history

### Top 5 Most Critical Issues

| # | Issue | Impact | Effort |
|---|---|---|---|
| 1 | **Not indexed by Google** — entire domain invisible | Blocks ALL organic traffic | Medium |
| 2 | **No structured data (schema)** — no rich results, no AIO signals | Prevents rich snippets & AI citations | Low |
| 3 | **Single page with no sub-pages** — thin site architecture | Limits crawl depth & keyword targeting | Medium |
| 4 | **Zero backlinks & off-site authority** — no trust signals | Blocks ranking vs established competitors | High |
| 5 | **Page-type mismatch** — landing page in a comparison SERP | Structural ranking ceiling | Medium |

### Top 5 Quick Wins (Fix This Week)

| # | Fix | Effort | Expected Impact |
|---|---|---|---|
| 1 | Add JSON-LD schema (SoftwareApplication, Organization, FAQ, Product) | 1 hour | High — unlocks rich results |
| 2 | Create `/llms.txt` for AI crawlers | 30 min | High — AI citation signal |
| 3 | Add `og:image` meta tag | 15 min | Medium — social sharing |
| 4 | Fix footer legal links (currently all `#`) | 30 min | Medium — E-E-A-T trust |
| 5 | Update copyright to 2026 | 1 min | Low — freshness signal |

---

## 1. Technical SEO (Score: 68/100)

### What's Working ✓
- Clean HTTPS setup with 301 redirects from HTTP and www
- Mobile-responsive design with `clamp()` typography
- Server-rendered content (no JS dependency for readability)
- Valid `robots.txt` allowing all major crawlers (including GPTBot, Claude-Web, PerplexityBot)
- Valid XML sitemap (though thin)
- Self-referencing canonical tag
- `meta robots` explicitly set to `index, follow`

### Critical Issues ✗

#### 1.1 Not Indexed by Google
- `site:tenurai.co.uk` returns **zero results** across multiple search engines
- The domain has no crawl history, no aging, and likely no backlinks pointing to it
- **Fix:** Submit to Google Search Console immediately. Request indexing. Build backlinks.

#### 1.2 No robots.txt (or not served correctly)
- `https://tenurai.co.uk/robots.txt` returned empty or error from direct checks
- Sitemap reference may not be reachable
- **Fix:** Verify robots.txt is deployed and accessible. Ensure it references the sitemap.

#### 1.3 Sitemap Too Thin (Only 2 URLs)
- Only `/` and `https://app.tenurai.co.uk/` are listed
- The app subdomain should NOT be in the sitemap (it's a login/dashboard SPA)
- `lastmod` is March 2025 (over a year stale)
- **Fix:** Remove app subdomain from sitemap. Add any new pages. Update lastmod to current date.

#### 1.4 Missing Security Headers
| Header | Status |
|---|---|
| `X-Frame-Options` | MISSING |
| `X-Content-Type-Options` | MISSING |
| `Content-Security-Policy` | MISSING |
| `Referrer-Policy` | MISSING |
| `Permissions-Policy` | MISSING |

- **Fix:** Add these to Netlify's `_headers` file (15 min effort)

#### 1.5 No Custom 404 Page
- Non-existent URLs show Netlify's generic unbranded 404 page
- **Fix:** Create a branded `404.html` with TenurAI navigation and CTA

#### 1.6 App Subdomain Not Protected
- `app.tenurai.co.uk` has no `noindex` tag — the login SPA could get indexed
- **Fix:** Add `<meta name="robots" content="noindex, nofollow">` to the app subdomain

#### 1.7 Google Fonts May Cause CLS
- No explicit `display=swap` on font loads
- 3 font families × multiple weights = render blocking risk
- **Fix:** Add `&display=swap` to Google Fonts URL

---

## 2. Content Quality (Score: 55/100)

### What's Working ✓
- ~1,800+ words of substantive content — exceeds thin content threshold
- Clear problem-solution narrative structure
- Good use of specific data points (£30,000 fines, 150+ expiry dates, etc.)
- Strong social proof with named testimonials
- Detailed pricing with clear feature breakdowns
- Legislation section is comprehensive (Gas Safety, EICR, EPC, RRA 2025, etc.)

### Critical Issues ✗

#### 2.1 No FAQ Section
- Zero Q&A content on the page
- "People Also Ask" opportunities completely missed
- FAQ content is the #1 content type for AI Overview citations
- **Fix:** Add 8-12 FAQ Q&A pairs with FAQPage schema markup

#### 2.2 No Blog / Resource Content
- No educational content, guides, or articles
- No way to target informational keywords
- No way to build topical authority
- **Fix:** Create `/resources` with guides targeting:
  - `renters-rights-act-2025-compliance-guide`
  - `eicr-compliance-checklist-landlords`
  - `gas-safety-certificate-renewal-reminders`
  - `section-21-abolished-what-replaces-it`

#### 2.3 Duplicate Section Numbering
- Both Pricing and Get in Touch sections use heading "05"
- Contact form uses same H2 number as pricing
- **Fix:** Change Get in Touch to "06" or just remove the numbering

#### 2.4 Features Section Too Long for AI Citation
- At 260 words, features content exceeds optimal citation range (134-167 words)
- AI models will truncate rather than cite verbatim
- **Fix:** Split into 3 shorter, self-contained subsections with H3s

#### 2.5 Weak H2 Headings for SEO
- Most H2s are statement-based, not keyword-rich
- Example: "Managing compliance in a spreadsheet is how letting agents get fined" — no target keywords
- **Fix:** Rephrase key H2s to include target terms where natural

#### 2.6 Stale Copyright
- Footer shows "© 2025" — it's now June 2026
- **Fix:** Update to "© 2025-2026" or "2026"

---

## 3. On-Page SEO (Score: 50/100)

### What's Working ✓
- Title tag: "TenurAI — Lettings Compliance Software That Updates With The Law | UK" (72 chars, keyword-rich)
- Meta description: 156 chars, includes key terms, action-oriented
- Clean URL structure with canonical tag
- Semantic HTML sections

### Issues ✗

#### 3.1 Title Tag Could Be Stronger
- Current: "TenurAI — Lettings Compliance Software That Updates With The Law | UK"
- Key phrase "Renters Rights Act" is missing from the title — the single biggest keyword opportunity
- **Better:** "TenurAI — Renters' Rights Act Compliance Software for UK Letting Agents"

#### 3.2 Missing og:image
- No `og:image` tag means no preview image on LinkedIn, Twitter, Facebook shares
- **Fix:** Create a 1200×630 branded OG image and add meta tags

#### 3.3 All Internal Links Are Hash Anchors
- Features, How it works, Pricing are `#features`, `#how`, `#pricing`
- These don't count as separate pages for SEO
- Footer links (Privacy, Terms, About) all point to `#`
- **Fix:** Either create dedicated pages or remove dead links

#### 3.4 No Image Alt Text
- Page uses CSS/SVG for dashboard visualization — no `<img>` tags with alt text
- Missed opportunity for image search
- **Fix:** Add real screenshots with keyword-rich alt text

#### 3.5 Contact Form Posts to `.netlify/functions/send-email`
- Previous audit mentioned using Netlify Forms (which requires `netlify` attribute + `form-name` hidden field)
- Verify the form handler is actually deployed and working

---

## 4. Schema & Structured Data (Score: 0/100)

**This is the single biggest missed opportunity.** There is zero structured data on the page.

### What's Missing

| Schema Type | Priority | Why It Matters |
|---|---|---|
| **SoftwareApplication** | Critical | Tells Google this is a software product |
| **Product** (with AggregateOffer for pricing tiers) | Critical | Enables price-rich snippets |
| **Organization** | High | Defines company identity, logo, social profiles |
| **FAQPage** | Critical | Directly feeds AI Overviews & voice search |
| **Review** (for testimonials) | High | Enables star ratings in SERP |
| **BreadcrumbList** | Medium | Better SERP display |
| **WebSite** | Medium | Defines site identity |
| **HowTo** | Low | For the "How It Works" section |

### Recommended JSON-LD Snippets

#### SoftwareApplication (P0 — deploy immediately)
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "TenurAI",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "description": "AI-powered lettings compliance co-pilot that auto-updates with UK legislation.",
  "url": "https://tenurai.co.uk",
  "offers": {
    "@type": "AggregateOffer",
    "lowPrice": "59",
    "highPrice": "199",
    "priceCurrency": "GBP",
    "offerCount": "3"
  }
}
```

#### Organization (P0)
```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "TenurAI",
  "url": "https://tenurai.co.uk",
  "logo": "https://tenurai.co.uk/assets/logo.png",
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "hello@loopstack.co.uk",
    "contactType": "sales"
  },
  "sameAs": [
    "https://www.linkedin.com/company/tenurai"
  ]
}
```

#### FAQPage (P0 — 8-12 Q&As for AI Overviews)
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the Renters' Rights Act 2025?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Renters' Rights Act 2025 is UK legislation that abolishes Section 21 'no-fault' evictions, converts all fixed-term ASTs to periodic tenancies, introduces mandatory pets clauses, and establishes a new PRS Database. It received Royal Assent in October 2025 with major provisions effective from May 2026."
      }
    },
    {
      "@type": "Question",
      "name": "How does TenurAI help with lettings compliance?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "TenurAI monitors official UK government sources weekly and automatically updates your compliance requirements. It tracks gas safety certificates, EICR, EPC, Right to Rent, and deposit deadlines across your portfolio, flagging issues before they become fines."
      }
    }
  ]
}
```

---

## 5. AI Search Readiness / GEO (Score: 41/100)

### What's Working ✓
- `robots.txt` explicitly allows GPTBot, Claude-Web, PerplexityBot
- Server-rendered content (AI crawlers can read it)
- Topically relevant content (Renters' Rights Act 2025 is highly current)
- 25+ extractable data points (fine amounts, pricing, percentages)
- Some content sections fall in optimal citation range (134-167 words)

### Critical Issues ✗

#### 5.1 No llms.txt
- `https://tenurai.co.uk/llms.txt` does not return a valid file
- This is the **single highest-impact GEO fix** — an llms.txt gives AI crawlers a pre-digested summary
- **Fix:** Create `/llms.txt` following the llmstxt.org standard with site summary, key pages, and key facts

#### 5.2 Zero Off-Site Authority Signals
- No Wikipedia presence
- No Companies House registration found for "TenurAI"
- No YouTube channel
- No Crunchbase profile
- No mentions on property forums (r/uklandlords, etc.)
- No press coverage
- AI citation research shows brand mentions across the web are the strongest predictor of AI citation frequency

#### 5.3 No FAQ Content
- AI Overviews preferentially cite pages with explicit Q&A structure
- Zero questions or answers on the page
- **Fix:** Add FAQ section with FAQPage schema (see Schema section above)

#### 5.4 Content Structure Not Optimized for AI Extraction
- Only 2 of 7 sections fall in the optimal 134-167 word citation range
- Features section at 260 words is too long for clean extraction
- No standalone "key statistics" block that AI can grab in one pass

#### 5.5 Missing AI Crawler Entries in robots.txt
- `Google-Extended`, `OAI-SearchBot`, and `CCBot` not explicitly named
- While the wildcard covers them, explicit naming signals intent
- **Fix:** Add explicit entries for these crawlers

### Estimated Platform-Specific AI Visibility

| Platform | Score | Reasoning |
|---|---|---|
| Google AI Overviews | 10/100 | No schema, no index, no backlinks |
| ChatGPT | 25/100 | Content is topical but no off-site citations |
| Perplexity | 20/100 | No Wikipedia/Reddit presence |
| Bing Copilot | 15/100 | No authority signals |

---

## 6. Search Experience / SXO (Score: 35/100)

### Page-Type Mismatch (Root Cause)

**The page is a single-vendor landing page, but the SERP rewards comparison/review pages.**

For every major target keyword:
- "lettings compliance software UK" → SERP dominated by comparison articles & review aggregators
- "gas safety certificate tracking" → App store listings & NRLA partner tools
- "renters rights act compliance software" → News articles & vendor hub pages
- "EPC compliance landlords" → NRLA resources & specialist tools

**Impact:** Google perceives TenurAI's page as a sales pitch, not a resource. It cannot rank against multi-vendor comparison pages.

### Persona Gaps

| Persona | Score | Key Gap |
|---|---|---|
| Agency Operations Manager | 38/100 | No team/enterprise positioning, no demo booking |
| Portfolio Landlord (30+) | 47/100 | Pricing at £59/mo for 20 props — doesn't match this segment's needs |
| Small Landlord (1-5 props) | 39/100 | No free tier, priced out at £59/mo minimum |
| Non-Technical Letting Agent | 57/100 | Best served but still no demo option |
| Regulated Professional | 32/100 | No legal authority signals, no source citations |

### Conversion Path Issues
- All CTAs lead to same URL (app.tenurai.co.uk) — no segmentation
- No "Book a demo" option for enterprise buyers
- No lead magnets (checklists, whitepapers) for research-mode visitors
- No retargeting mechanism (no cookie banner, no analytics pixel)
- Contact form is buried at the very bottom of the page

---

## 7. Performance (Score: 65/100)

### What's Working ✓
- Minimal JavaScript (~90 lines, all inline)
- No heavy third-party scripts (no analytics, no chat widgets, no tag manager)
- CSS inlined in `<style>` (eliminates render-blocking request)
- SVG/CSS-based dashboard graphics (no heavy image loading)
- Smooth scroll animations use IntersectionObserver (non-blocking)

### Risk Areas
- **Google Fonts:** 3 families × 10+ weights — potential LCP & CLS impact
- **No preloaded critical assets** — no `rel="preload"` for hero fonts
- **font-display:** Not explicitly set to swap (risk of FOIT/CLS)
- **Compliance bar animations** Could cause layout shifts within containers

---

## 8. Competitive Landscape

### Direct Competitors

| Product | Pricing | Positioning |
|---|---|---|
| **Proplio** | £19-29/mo unlimited | Pure compliance, cheapest option |
| **LetCompliance** | £14.99/mo (25 props) | Budget compliance tracker |
| **Lendlord** | Free tier available | Free portfolio management + RRA tools |
| **August** | £8.99/mo | Tenancy lifecycle management |
| **LLCR** | £29/mo (5 props) | Small landlord focused |
| **TenurAI Solo** | £59/mo (20 props) | AI premium — compliance + CRM + docs |
| **Alto** | £300-500/mo est. | Full CRM + marketing + compliance |
| **Rentalize** | Unknown | End-to-end RRA compliance engine |
| **Yardi** | Enterprise | Large-scale property management |

### Competitive Threats
1. **Proplio at £19/mo** — 3× cheaper for basic tracking. TenurAI must justify premium with AI features.
2. **Alto's built-in compliance** — free for existing Alto users (6,000+ agencies). TenurAI needs to position as compliance overlay, not CRM replacement.
3. **Lendlord free tier** — competing with free for small landlords. TenurAI's £59 minimum excludes this huge market.
4. **NRLA-affiliated tools** — Safe2, Domna, TLA have industry body trust. TenurAI has zero affiliations.

### TenurAI's Genuine Differentiators (Not Adequately Featured)
1. **AI legislation monitoring** — weekly gov.uk scanning. Unique in the market. Should be PRIMARY headline.
2. **Multi-language documents** — genuine competitive edge for diverse tenant populations.
3. **Built-in CRM** — replaces Alto/Reapit. Needs explicit competitive positioning.
4. **AI Q&A** — unique feature, not emphasized enough above the fold.
5. **Auto-updating documents** — critical for RRA compliance, positioned as feature bullet not headline.

---

## 9. Prioritized Action Plan

### 🔴 Phase 1: Foundation (This Week — Critical)

| # | Action | Category | Effort |
|---|---|---|---|
| 1 | **Submit site to Google Search Console** and request indexing | Indexation | 30 min |
| 2 | **Add JSON-LD structured data**: SoftwareApplication + Organization + FAQPage + Product | Schema | 1 hour |
| 3 | **Create /llms.txt** for AI crawlers | GEO | 30 min |
| 4 | **Add og:image meta tag** with 1200×630 branded image | On-Page | 15 min |
| 5 | **Fix footer links** — at minimum remove broken `#` links or link to real pages | On-Page | 30 min |
| 6 | **Update copyright to 2026** | Trust | 1 min |
| 7 | **Fix duplicate "05" heading** in Get in Touch section | Content | 5 min |
| 8 | **Add noindex to app.tenurai.co.uk** | Technical | 15 min |
| 9 | **Add missing security headers** via Netlify `_headers` file | Technical | 15 min |
| 10 | **Add `display=swap` to Google Fonts URL** | Performance | 5 min |

### 🟡 Phase 2: Content & Architecture (Week 2-3 — High Priority)

| # | Action | Category | Effort |
|---|---|---|---|
| 11 | **Create dedicated sub-pages**: `/features`, `/pricing`, `/how-it-works`, `/about`, `/faq` | On-Page | 1-2 days |
| 12 | **Create Renters' Rights Act compliance guide page** — topical authority magnet | Content | 4 hours |
| 13 | **Add FAQ section** to homepage with FAQPage schema (8-12 Q&As) | Content | 2 hours |
| 14 | **Add FAQ section** to homepage with FAQPage schema (8-12 Q&As) | Schema | 2 hours |
| 15 | **Add a "Book a demo" CTA** (Cal.com / Calendly) | Conversion | 1 hour |
| 16 | **Create branded 404.html page** | Technical | 30 min |
| 17 | **Take real product screenshots** and add with alt text | On-Page | 1 hour |
| 18 | **Record 2-minute product walkthrough video** and embed on page | Content | 2 hours |

### 🟢 Phase 3: Authority Building (Month 1-3 — Medium Priority)

| # | Action | Category | Effort |
|---|---|---|---|
| 19 | **Get listed on Software Advice, Capterra, GetApp** | Authority | 2 hours each |
| 20 | **Create LinkedIn company page** and build content strategy | Authority | 1 hour |
| 21 | **Create YouTube channel** with 5+ RRA compliance explainer videos | Authority | 5-10 hours |
| 22 | **Register on Crunchbase** | Authority | 30 min |
| 23 | **Register TenurAI Ltd at Companies House** (if not already) | Authority | 30 min |
| 24 | **Build 5-10 backlinks** through guest posts on property industry blogs | Authority | Ongoing |
| 25 | **Pursue NRLA / Propertymark affiliation** | Trust | Ongoing |
| 26 | **Start a blog** with weekly articles on lettings compliance | Content | Ongoing |
| 27 | **Create case studies** with real metrics (fines avoided, time saved, certificates tracked) | Content | 4 hours each |

### 🔵 Phase 4: Growth (Month 3-6 — Ongoing)

| # | Action | Category | Effort |
|---|---|---|---|
| 28 | **PR campaign** — get covered on PropertyWire, Landlord Today, The Intermediary | Authority | Ongoing |
| 29 | **Reddit presence** — contribute to r/uklandlords, r/ukproperty | Authority | Weekly |
| 30 | **Monthly content publishing** — 4+ articles per month targeting specific keywords | Content | Ongoing |
| 31 | **Consider a free tier** (£0/mo for 3 properties) to capture small landlord market | Product | Needs consideration |
| 32 | **Implement IndexNow** for faster Bing indexing | Technical | 30 min |
| 33 | **Monitor DataForSEO AI citation metrics** monthly | GEO | Monthly |
| 34 | **Add retargeting pixel** and cookie consent banner | Conversion | 1 hour |

---

## 10. Before & After: Title / Meta Recommendations

### Title Tag
**Current:** "TenurAI — Lettings Compliance Software That Updates With The Law | UK"
**Recommended:** "TenurAI — Renters' Rights Act Compliance Software for UK Letting Agents"

### Meta Description
**Current:** "TenurAI tracks every gas safety certificate, EICR, EPC and tenancy deadline across your entire portfolio — and flags issues before they become fines."
**Recommended:** Keep as-is — it performs well (156 chars, keyword-rich, action-oriented).

---

## Appendix: Recommended Site Architecture (MVP)

```
tenurai.co.uk/
  /                          -- Home (shorter, more comparison-oriented)
  /features                  -- Detailed feature breakdowns
  /pricing                   -- Dedicated pricing + comparison table
  /renters-rights-act        -- Dedicated RRA compliance page [HIGH VALUE]
  /gas-safety-compliance     -- E-E-A-T content for gas safety tracking queries
  /eicr-compliance           -- For electrical safety compliance queries
  /epc-compliance            -- For EPC compliance queries
  /how-it-works              -- Detailed walkthrough with video
  /case-studies              -- At least 2-3 detailed case studies
  /resources                 -- Blog / guide hub
    /compliance-checklist    -- Gated lead magnet
    /renters-rights-act-guide -- Ungated comprehensive guide
  /about                     -- Team, credentials, E-E-A-T
  /contact                   -- Contact page with scheduling
  /faq                       -- FAQ page with FAQPage schema
  404.html                   -- Branded 404 page
  llms.txt                   -- AI crawler summary
  robots.txt                 -- Verified accessible
  sitemap.xml                -- Updated with all pages
```

---

## Scoring Summary

| Category | Current | Potential (3 months) | Potential (6 months) |
|---|---|---|---|
| Technical SEO | 68 | 92 | 95 |
| Content Quality | 55 | 75 | 88 |
| On-Page SEO | 50 | 82 | 90 |
| Schema / SD | 0 | 95 | 95 |
| Performance | 65 | 78 | 85 |
| AI Search (GEO) | 41 | 68 | 82 |
| SXO / Intent | 35 | 60 | 78 |
| **Overall** | **42** | **78** | **88** |

---

*Report generated from 5 specialist agent audits: Technical SEO, Content, Schema, GEO/AEO, and SXO.*
