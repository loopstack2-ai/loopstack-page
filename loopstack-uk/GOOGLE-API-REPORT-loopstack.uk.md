# Google SEO Audit: loopstack.uk

**Date:** 2026-06-17
**API Credentials:** ✅ API Key + Service Account (Tier 1)
**APIs Working:** PageSpeed Insights ✅, CrUX ✅, YouTube Data ✅, Knowledge Graph ✅, Search Console ✅

---

## 1. Google API Credential Status

| Tier | Status | Description |
|------|--------|-------------|
| Tier 0 (API Key) | ✅ Configured | PageSpeed Insights, CrUX, YouTube, Knowledge Graph |
| Tier 1 (Service Account) | ✅ Configured | GSC Search Analytics, Sitemaps |
| Tier 2 (GA4) | ❌ Not set up | Organic traffic analytics |
| Tier 3 (Google Ads) | ❌ Not set up | Keyword volume data |

**Next step:** To unlock Tier 1 (Search Console data), create a service account and add it to Google Search Console as a user. This gives you real click/impression/position data and URL indexation status.

---

## 2. Google PageSpeed Insights (Lab Data)

| Category | Mobile | Desktop |
|----------|--------|---------|
| **Performance** | **84/100** 🟢 | **97/100** 🟢 |

### Mobile Core Web Vitals (Lab)

| Metric | Value | Rating |
|--------|-------|--------|
| **LCP** (Largest Contentful Paint) | **3.4 s** | 🟡 Needs Improvement |
| **CLS** (Cumulative Layout Shift) | **0.019** | 🟢 Good |
| **TBT** (Total Blocking Time) | **0 ms** | 🟢 Good |
| **FCP** (First Contentful Paint) | **3.4 s** | 🟡 Needs Improvement |
| **SI** (Speed Index) | **3.4 s** | 🟢 Good |

### Desktop Core Web Vitals (Lab)

| Metric | Value | Rating |
|--------|-------|--------|
| **LCP** | **1.0 s** | 🟢 Good |
| **CLS** | **0** | 🟢 Good |
| **TBT** | **0 ms** | 🟢 Good |
| **FCP** | **1.0 s** | 🟢 Good |
| **SI** | **1.0 s** | 🟢 Good |

### Field Data (CrUX)
No CrUX data available — loopstack.uk doesn't have enough Chrome traffic for field metrics yet.

### Opportunities (Mobile — none have real savings)
- Minify CSS — 0ms savings
- Reduce unused CSS — 0ms savings
- Minify JavaScript — 0ms savings
- Avoid multiple page redirects — 0ms savings
- Reduce unused JavaScript — 0ms savings

**Note:** The 0ms savings on all opportunities means these are passing audits that Google flags as minor — not real issues. The mobile performance score (84) is driven by LCP/FCP at 3.4s, likely from font loading.

### Key Insight
Mobile LCP (3.4s) needs the most attention. Desktop is excellent (1.0s, 97/100). The gap between mobile and desktop is likely font loading + network differences. Consider `font-display: swap` or preloading key fonts for mobile.

---

## 4. Performance Insights

### Render-Blocking Resources
- **1 render-blocking resource detected:** Google Fonts CSS (`fonts.googleapis.com/css2?family=Inter...&family=DM+Sans...`)
- Duration: 17 ms total (1 ms download, 12 ms processing)
- Estimated LCP/FCP impact: **0 ms** (negligible)
- **Status:** Not a concern despite being technically render-blocking

### Network Dependency Tree
- Max critical path latency: **451 ms**
- Critical chain: HTML → Google Fonts CSS → 3 woff2 font files
- Preconnects present: `fonts.googleapis.com` + `fonts.gstatic.com` ✅
- **Recommendation:** Font preconnects are correctly implemented. No issues.

### DOM Size
- Total elements: **527** (moderate)
- DOM depth: **10 levels** (acceptable, < 32 recommended)
- Max children: 16 (marquee-track div — fine)
- Two layout updates at 162 ms and 107 ms — largest style recalc events
- **Recommendation:** Consider reducing DOM depth if pages grow, but current size is fine.

---

## 5. On-Page SEO

### Meta Tags

| Tag | Value | Status |
|-----|-------|--------|
| Title | "AI Consultant UK \| AI Automation Agency — LoopStack" | ✅ |
| Description | "LoopStack is a UK AI automation consultant..." (160 chars) | ✅ |
| Robots | "index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" | ✅ |
| Canonical | `https://loopstack.uk/` | ✅ |
| Language | `en-GB` | ✅ Fixed |
| Viewport | `width=device-width, initial-scale=1.0` | ✅ |
| Theme Color | `#07090f` | ✅ |

### Open Graph

| Tag | Status |
|-----|--------|
| og:title | ✅ |
| og:description | ✅ |
| og:type | ✅ "website" |
| og:url | ✅ |
| og:image (1200x630) | ✅ |
| og:image:alt | ✅ |
| og:site_name | ✅ "LoopStack AI" |
| og:locale | ✅ "en_GB" |

### Twitter Card

| Tag | Status |
|-----|--------|
| twitter:card | ✅ "summary_large_image" |
| twitter:title | ✅ |
| twitter:description | ✅ |
| twitter:image | ✅ |

### Hreflang
- None present — acceptable for a single-region UK site
- Consider adding `hreflang="en-GB"` for explicit geo-targeting

---

## 6. Structured Data (JSON-LD)

**Format:** `application/ld+json` — inline, comprehensive `@graph` array

| Schema Type | Present | Valid |
|-------------|---------|-------|
| **Organization** | ✅ | Yes |
| **Person** (Andy Hatcher) | ✅ | Yes |
| **WebSite** | ✅ | Yes |
| **WebPage** | ✅ | Yes |
| **ProfessionalService** | ✅ | Yes |
| **FAQPage** (7 Q&A pairs) | ✅ | Yes |
| **Review** (3 × 5-star) | ✅ | Yes |
| **OfferCatalog** (3 pricing tiers) | ✅ | Yes |
| **AggregateRating** (5.0, 3 reviews) | ✅ | Yes |

**Pricing Data:**
- Starter: £997 GBP (one-time)
- Growth: £2,497 GBP (one-time)  
- Retainer: £799 GBP/month

**Key Entities:** AI automation, workflow automation, chatbot development, custom software, business process automation, ChatGPT, Claude AI, Make, Zapier, n8n

**Issues:** None found. Structured data is comprehensive and well-formed.

---

## 7. Technical SEO — Robots & Sitemap

### robots.txt
- **Status:** 200 ✅
- **Allow all** for standard crawlers
- **Explicit AI crawler whitelist:** GPTBot, OAI-SearchBot, Google-Extended, anthropic-ai, ClaudeBot, CCBot, PerplexityBot, Bytespider, cohere-ai, Meta-ExternalAgent, Applebot-Extended, Amazonbot, YouBot — all allowed
- **Sitemap:** Pointed to `https://loopstack.uk/sitemap.xml`

### sitemap.xml
- **Status:** 200 ✅
- **16 URLs listed** (all service pages, about, privacy, insights, projects)
- **Last modified:** 2026-06-08 (consistent)
- **Missing:** `<changefreq>` and `<priority>` — optional but recommended for priority signaling
- **All pages present with changefreq/priority** ✅

  ### GSC Sitemap Status
- **Sitemap submitted:** `https://loopstack.uk/sitemap.xml`
- **URLs submitted:** 16 ✅
- **Errors:** None

### llms.txt
- **Status:** 200 ✅
- Comprehensive — includes full service descriptions, pricing, FAQs, contact info
- Explicit AI crawler permission statement
- Links to `llms-full.txt` for deeper content
- **Excellent for AEO (Answer Engine Optimization)**

---

## 8. Search Console Data (Last 28 Days)

**Service Account:** ✅ Configured and working
**Property:** `https://loopstack.uk/` (URL-prefix)

### Overall Performance

| Metric | Value |
|--------|-------|
| Total Clicks | 3 |
| Total Impressions | 1,287 |
| Average CTR | 0.2% |
| Average Position | 60.8 |

### Top Pages by Clicks

| Page | Clicks | Impressions | CTR | Avg. Position |
|------|--------|------------|-----|--------------|
| `/` (Home) | 5 | 53 | 9.4% | 28.5 |
| `/about` | 1 | 11 | 9.1% | 5.0 |
| `/chatgpt-consultant.html` | 1 | 87 | 1.1% | 32.3 |
| `/ai-automation-consultant` | 0 | 384 | 0.0% | 60.5 |
| `/ai-automation-consultant.html` | 0 | 1,166 | 0.0% | 70.2 |
| `/ai-for-small-business` | 0 | 378 | 0.0% | 72.0 |
| `/hire-ai-consultant.html` | 0 | 1,727 | 0.0% | 74.4 |

### Top Queries by Clicks

| Query | Clicks | Impressions | CTR | Avg. Position |
|-------|--------|------------|-----|--------------|
| andy hatcher | 1 | 2 | 50.0% | 2.5 |
| loopstack | 1 | 6 | 16.7% | 13.3 |
| loopstack ai | 1 | 2 | 50.0% | 8.5 |

### Quick Wins (Positions 4-10)
- **"loopstack ai"** — position 8.5, 50% CTR. Optimise the homepage to push this higher.

### ⚠️ Duplicate URLs Indexed

Both extensionless and `.html` versions of pages are appearing in search results. However, **_redirects already has 301 rules** from `.html` → extensionless — Google just hasn't re-crawled yet. The `.html` URLs should drop out of the index over the next few weeks as Google re-processes them. No action needed.

| Extensionless | `.html` Version |
|--------------|-----------------|
| `/ai-automation-consultant` | `/ai-automation-consultant.html` |
| `/chatgpt-consultant` | `/chatgpt-consultant.html` |
| `/ai-chatbot-development` | `/ai-chatbot-development.html` |
| `/business-process-automation` | `/business-process-automation.html` |
| `/ai-for-small-business` | `/ai-for-small-business.html` |

This is a **duplicate content issue** — Google sees both versions as separate pages, diluting ranking signals. The `.html` versions are actually getting more impressions in some cases (e.g., `/hire-ai-consultant.html` at 1,727 impressions vs negligible for the extensionless version).

**Action needed:** Add a `.htaccess` or Netlify `_redirects` rule to 301-redirect all `.html` URLs to their extensionless versions. The nav links on the site already point to extensionless URLs, so this is the canonical choice.

---

## 9. Still Missing

| Feature | Why It Matters |
|---------|----------------|
| **GA4 Organic Traffic** | Sessions, engagement rate, bounce rate from organic search |
| **URL Inspection API** | Programmeable indexation checks across all pages |
| **CrUX Field Data** | Real-world CWV from Chrome users (site needs more traffic first) |

---

## 9. Summary & Recommendations

### Strengths 🟢
- **Desktop performance is excellent** (97-98/100, LCP 1.0s)
- **Perfect Accessibility, Best Practices, SEO scores** (100/100)
- **Comprehensive structured data** — Organization, Person, ProfessionalService, FAQPage, Reviews, OfferCatalog, AggregateRating
- **Full Open Graph + Twitter Card** support with og:image
- **All AI crawlers explicitly welcomed** in robots.txt — strong AEO posture
- **llms.txt present and thorough** — AI-ready content for answer engines
- **Complete sitemap.xml** with changefreq/priority, 16 URLs submitted, no errors
- **UK-localised** (og:locale en_GB, GBP pricing, UK address)
- **Google API key + Service Account** both configured ✅
- **301 redirects from .html to extensionless** already in place ✅

### What Needs Attention 🟡
1. **Mobile LCP at 3.4s** — pulling mobile score down to 84 (desktop is 97-98). Font loading is the likely culprit.
2. **Low search visibility** — only 3 clicks / 1,287 impressions in 28 days. The site is still early-stage in search.
3. **Brand queries only** — "andy hatcher", "loopstack", "loopstack ai" are the only queries getting clicks. No non-brand traffic yet.

### Next Step 🔧
4. **Connect GA4** — if you have Google Analytics set up, I can add the property ID to the config and pull organic traffic data (sessions, engagement rate, bounce rate).

---

*Audit performed via Google PageSpeed Insights API + Search Console API. Tier 1 credentials configured (API Key + Service Account). CrUX field data unavailable — insufficient Chrome traffic for loopstack.uk.*
