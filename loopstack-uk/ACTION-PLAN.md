# Action Plan: loopstack.uk

**Date:** 24 June 2026
**Overall Score:** 74/100
**Priority:** Critical → High → Medium → Low

---

## 🔴 Critical — Fix Immediately (This Week)

| # | Issue | Category | Effort | Impact | Status |
|---|-------|----------|--------|--------|--------|
| 1 | **Fix llms-full.txt 404** — AI crawlers hit a dead end when following the link from llms.txt | GEO | 10 min | High | ❌ Not started |
| 2 | **Fix favicon 404** — `/favicon.svg` returns 404, browser console error | Technical | 5 min | Medium | ❌ Not started |
| 3 | **Add 301 redirect for `/tenurai.html` → `/projects/tenurai`** — duplicate content risk | Technical | 5 min | Medium | ❌ Not started |

### 🔴 C1: Create llms-full.txt
The `llms.txt` file references `https://loopstack.uk/llms-full.txt` which returns 404. Create this file with extended content: full service descriptions, complete case study, full about page content, pricing details, and contact info. Mirror the structure of llms.txt but at greater depth.

**Location:** `C:\Users\loops\Documents\loopstack-page\loopstack-uk\llms-full.txt`

### 🔴 C2: Fix favicon 404
The site references `/favicon.svg` but the file only exists in `loopstack-uk/`. Copy `favicon.svg` to the git root so it's served at the correct URL.

### 🔴 C3: Duplicate tenurai content
Add to `_redirects`:
```
/tenurai.html    /projects/tenurai    301
```

---

## 🟠 High — Fix Within 1 Week

| # | Issue | Category | Effort | Impact | Status |
|---|-------|----------|--------|--------|--------|
| 4 | **Add BreadcrumbList schema to homepage** | Schema | 10 min | Medium | ❌ Not started |
| 5 | **Add Service schema to 7 service pages** | Schema | 15 min per page | High | ❌ Not started |
| 6 | **Expand hero copy to 60-80 words** | Content | 15 min | Medium | ❌ Not started |
| 7 | **Expand FAQ answers to 80-120 words** | Content | 30 min | High | ❌ Not started |
| 8 | **Add hreflang tags to all subpages** | Technical | 30 min | Low | ❌ Not started |
| 9 | **Add Article schema to logistics case study** | Schema | 10 min | Medium | ❌ Not started |
| 10 | **Fix footer anchor links on non-homepage pages** | Technical | 20 min | Medium | ❌ Not started |

### 🟠 H4: BreadcrumbList on homepage
Add to the `@graph` array in `index.html`:
```json
{
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://loopstack.uk/"}
  ]
}
```

### 🟠 H5: Service schema on subpages
Add `Service` type to each service page's existing `@graph`:
- `ai-chatbot-development.html`
- `chatgpt-consultant.html`
- `custom-software-development.html`
- `business-process-automation.html`
- `ai-for-small-business.html`
- `hire-ai-consultant.html`
- `web-app-development.html`

Each needs a block with: `name`, `description`, `url`, `provider` (pointing to `#organization`), `serviceType`, `areaServed`.

### 🟠 H6: Expand hero copy
Current hero subtitle is about 44 words. Expand to 60-80 words to make it a self-contained, AI-citable passage that covers: who, what, where, for whom, pricing, differentiator.

### 🟠 H7: Expand FAQ answers
Target 80-120 words per answer in the in-page HTML FAQ (not just JSON-LD). AI models cite on-page text, not schema. Key FAQs to expand:
- "What is an AI automation consultant?" — add concrete example
- "How much does AI automation cost in the UK?" — add ROI context
- "How quickly can you implement AI automation?" — add timeline comparison

### 🟠 H8: Hreflang on subpages
Add `<link rel="alternate" hreflang="en-GB" href="https://loopstack.uk/{page}">` to each service page, insight, and project page for consistency with the homepage.

---

## 🟡 Medium — Fix Within 1 Month

| # | Issue | Category | Effort | Impact | Status |
|---|-------|----------|--------|--------|--------|
| 11 | **Add Google Business Profile** | Local/GEO | 1 hour | High | ❌ Not started |
| 12 | **Add Product + Offer schema to tenurai.html** | Schema | 15 min | Medium | ❌ Not started |
| 13 | **Publish 6-12 more insight articles** | Content | Days-weeks | Very High | ❌ Not started |
| 14 | **Create section-specific FAQPage on service pages** | Schema | 30 min per page | Medium | ❌ Not started |
| 15 | **Add VideoObject schema for services video** | Schema | 15 min | Low | ❌ Not started |
| 16 | **Add registered address + company number to footer** | Content/Trust | 15 min | Medium | ❌ Not started |
| 17 | **Add contextual cross-links between service pages** | Content | 1 hour | Medium | ❌ Not started |
| 18 | **Replace booking placeholder with live calendar embed** | Conversion | 30 min | Medium | ❌ Not started |
| 19 | **Add client logos or named case studies** | Content/Trust | Days | High | ❌ Not started |
| 20 | **Fix footer Services column deduplication** | Content | 10 min | Low | ❌ Not started |

### 🟡 M11: Google Business Profile
Create a Google Business Profile for LoopStack AI. This unlocks GBP for local search visibility and provides a key citation signal for AI search engines. Even as a non-local consultancy, a GBP adds authority.

### 🟡 M13: Content strategy — insight articles
The site has only 2 insight articles. Target publishing 1-2 per month covering:
- "AI automation for logistics UK" (use existing case study)
- "AI automation for property management UK" (TenurAI tie-in)
- "AI chatbot cost UK — what to expect in 2026"
- "Make.com vs Zapier vs n8n — which is right for your business"
- "How to choose an AI consultant UK"
- "AI for small business UK — the £997 starter guide"

### 🟡 M16: Add registered address
Add to footer or About page: registered company name, company number, and registered address. This is a trust signal that also helps local search.

### 🟡 M18: Live booking calendar
Replace the "Send us a message" placeholder card in the booking section with an actual calendar tool (Cal.com, Calendly, or similar). This gap was noted in multiple sub-agent audits.

### 🟡 M19: Named case studies
Work with existing clients to get full-name + company-name testimonials. Even 1-2 named case studies would significantly improve E-E-A-T.

---

## 🟢 Low — Backlog

| # | Issue | Category | Effort | Impact | Status |
|---|-------|----------|--------|--------|--------|
| 21 | **Start YouTube channel** — 3-5 targeting FAQ keywords | GEO/Marketing | Days | Very High | ❌ Not started |
| 22 | **Preload Google Fonts** — non-blocking font loading pattern | Performance | 30 min | Medium | ❌ Not started |
| 23 | **Update lastmod dates in sitemap** — per-page granularity | Technical | 15 min | Low | ❌ Not started |
| 24 | **Add HSTS preload** — `includeSubDomains; preload` | Security | 10 min | Low | ❌ Not started |
| 25 | **Add IndexNow support** — for Bing/Yandex | Technical | 30 min | Low | ❌ Not started |
| 26 | **Set up GA4** — connect property ID for organic traffic data | Analytics | 30 min | Medium | ❌ Not started |
| 27 | **Add ImageObject schema for founder photo** | Schema | 10 min | Low | ❌ Not started |

### 🟢 L21: YouTube strategy (Long-term Highest Impact)
YouTube mentions correlate at ~0.737 with AI citations — the strongest known signal. Create content answering the exact FAQ questions already on the site:
- "How much does AI automation cost in the UK?" → your £997 vs £5k-25k differentiator
- "What does an AI automation consultant do?" → aligns with FAQ Q1
- "AI automation for small business UK" → aligns with existing service page
- "How to hire an AI consultant UK" → aligns with FAQ Q8
- "Can I get AI automation without vendor lock-in?" → aligns with FAQ Q10

Embed these videos on the corresponding pages for SEO + GEO synergy.

### 🟢 L22: Preload Google Fonts
Replace the standard `<link>` with the non-blocking pattern:
```html
<link rel="preload" as="style" href="https://fonts.googleapis.com/..." crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/..." media="print" onload="this.media='all'">
```
This eliminates the only render-blocking resource on the page.

### 🟢 L25: IndexNow
Add IndexNow support for Bing. Create the API key file at the root and add a deploy script to notify IndexNow on each Netlify deploy.

---

## Priority Implementation Roadmap

### Week 1 (Immediate)
1. ✅ (Done in previous session) — Update page titles for keyword targeting
2. ✅ (Done) — Strengthen pricing differentiation copy
3. ⬜ C1 — Create llms-full.txt
4. ⬜ C2 — Copy favicon.svg to root
5. ⬜ C3 — Add /tenurai.html 301 redirect
6. ⬜ H4+H5 — Add BreadcrumbList + Service schemas

### Week 2
7. ⬜ H6+H7 — Expand hero and FAQ copy for AI citability
8. ⬜ H8 — Add hreflang to subpages
9. ⬜ H10 — Fix footer anchor links
10. ⬜ M11 — Create Google Business Profile

### Week 3-4
11. ⬜ M12+M15 — Add Product and VideoObject schemas
12. ⬜ M16 — Add registered address
13. ⬜ M18 — Replace booking placeholder with live calendar
14. ⬜ L22 — Preload Google Fonts non-blocking

### Month 2+
15. ⬜ M13 — Publish 6-12 insight articles
16. ⬜ M19 — Secure named case studies
17. ⬜ L21 — Create YouTube channel and publish 3-5 videos
18. ⬜ L25 — Set up IndexNow

---

## Quick Wins Dashboard

| # | Fix | Time | Impact | Difficulty |
|---|-----|------|--------|------------|
| 1 | Create llms-full.txt | 10 min | 🟢 High | 🟢 Easy |
| 2 | Copy favicon.svg to root | 2 min | 🟡 Medium | 🟢 Easy |
| 3 | Add /tenurai.html 301 | 2 min | 🟡 Medium | 🟢 Easy |
| 4 | BreadcrumbList schema on homepage | 10 min | 🟡 Medium | 🟢 Easy |
| 5 | Service schema on 7 subpages | 20 min each | 🟢 High | 🟢 Easy |
| 6 | Expand hero copy | 10 min | 🟡 Medium | 🟢 Easy |
| 7 | Footer anchor links fix | 15 min | 🟡 Medium | 🟢 Easy |
| 8 | Google Business Profile | 30 min | 🟢 High | 🟢 Easy |

---

## Effort Estimate Summary

| Priority | Count | Est. Time |
|----------|-------|-----------|
| 🔴 Critical | 3 | 20 min |
| 🟠 High | 7 | ~3 hours |
| 🟡 Medium | 10 | ~2-3 days |
| 🟢 Low | 7 | ~1-2 days |
| **Total** | **27** | **~1 week** |

*Note: Content creation (insight articles, YouTube videos) is the largest time investment and also the highest long-term impact.*
