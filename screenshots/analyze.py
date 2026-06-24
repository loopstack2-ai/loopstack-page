from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    # ── DESKTOP ANALYSIS ──
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('https://loopstack.uk/', wait_until='networkidle', timeout=30000)
    page.wait_for_timeout(2000)

    above_fold = page.evaluate("""() => {
        const vp = window.innerHeight;
        const r = [];
        const h1 = document.querySelector('h1');
        const hero_sub = document.querySelector('.hero-sub');
        const primary_btn = document.querySelector('.btn-primary');
        const secondary_btn = document.querySelector('.btn-ghost');
        const video = document.querySelector('.video-wrapper');
        const stats = document.querySelector('.hero-stats');
        const nav = document.querySelector('nav');
        const marquee = document.querySelector('.marquee-wrap');

        r.push('H1: ' + (h1 && h1.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Subtitle: ' + (hero_sub && hero_sub.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Primary CTA: ' + (primary_btn && primary_btn.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Secondary CTA: ' + (secondary_btn && secondary_btn.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Video wrapper: ' + (video && video.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Hero stats: ' + (stats && stats.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Nav visible: ' + (nav && nav.getBoundingClientRect().bottom <= vp && nav.getBoundingClientRect().top >= 0 ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Marquee: ' + (marquee && marquee.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        return r;
    }""")

    print('=== DESKTOP ABOVE-FOLD (1920x1080) ===')
    for line in above_fold:
        print('  ' + line)

    nav_height = page.evaluate("() => document.querySelector('nav').offsetHeight")
    logo_height = page.evaluate("() => { const img = document.querySelector('.nav-logo img'); return img ? img.offsetHeight : null; }")
    print(f'  Nav height: {nav_height}px')
    print(f'  Logo height: {logo_height}px')

    h1_font = page.evaluate("() => { const h1 = document.querySelector('h1'); return h1 ? getComputedStyle(h1).fontSize : null; }")
    print(f'  H1 font size: {h1_font}')

    # Check hero section full height
    hero_height = page.evaluate("() => { const h = document.querySelector('.hero'); return h ? h.offsetHeight : null; }")
    print(f'  Hero section height: {hero_height}px')

    # ── MOBILE ANALYSIS ──
    page_m = browser.new_page(viewport={'width': 375, 'height': 812})
    page_m.goto('https://loopstack.uk/', wait_until='networkidle', timeout=30000)
    page_m.wait_for_timeout(2000)

    above_fold_m = page_m.evaluate("""() => {
        const vp = window.innerHeight;
        const r = [];
        const h1 = document.querySelector('h1');
        const hero_sub = document.querySelector('.hero-sub');
        const primary_btn = document.querySelector('.btn-primary');
        const secondary_btn = document.querySelector('.btn-ghost');
        const video = document.querySelector('.video-wrapper');
        const stats = document.querySelector('.hero-stats');
        const toggle = document.querySelector('.nav-mobile-toggle');
        const nav_cta = document.querySelector('.nav-cta');
        const nav_links = document.querySelector('.nav-links');
        const hero = document.querySelector('.hero');

        r.push('H1: ' + (h1 && h1.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Subtitle: ' + (hero_sub && hero_sub.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Primary CTA: ' + (primary_btn && primary_btn.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Secondary CTA: ' + (secondary_btn && secondary_btn.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Video wrapper: ' + (video && video.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Hero stats: ' + (stats && stats.getBoundingClientRect().bottom <= vp ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Mobile toggle visible: ' + (toggle && toggle.getBoundingClientRect().bottom <= vp && toggle.getBoundingClientRect().top >= 0 ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Nav CTA visible: ' + (nav_cta && nav_cta.getBoundingClientRect().bottom <= vp && nav_cta.getBoundingClientRect().top >= 0 ? 'VISIBLE' : 'NOT VISIBLE'));
        r.push('Nav links display: ' + (nav_links ? getComputedStyle(nav_links).display : 'N/A'));
        r.push('Hero ends above fold: ' + (hero && hero.getBoundingClientRect().bottom <= vp ? 'YES - full hero visible' : 'NO - hero continues below'));
        return r;
    }""")

    print('\n=== MOBILE ABOVE-FOLD (375x812) ===')
    for line in above_fold_m:
        print('  ' + line)

    # Touch target analysis (mobile)
    small_targets = page_m.evaluate("""() => {
        const btns = document.querySelectorAll('button, .btn-primary, .btn-ghost, .nav-cta, .chat-bubble, .nav-mobile-toggle, .faq-q, .form-submit');
        const results = [];
        btns.forEach(btn => {
            const r = btn.getBoundingClientRect();
            if (r.width < 48 || r.height < 48) {
                results.push({ el: btn.className.slice(0,25) || btn.tagName, w: Math.round(r.width), h: Math.round(r.height) });
            }
        });
        return results;
    }""")

    print(f'\n  Touch targets under 48px: {len(small_targets)}')
    for t in small_targets:
        print(f'    {t["el"]}: {t["w"]}x{t["h"]}px')

    # Horizontal scroll
    hscroll = page_m.evaluate("() => document.body.scrollWidth > window.innerWidth")
    print(f'  Horizontal scroll: {hscroll}')

    base_font = page_m.evaluate("() => parseFloat(getComputedStyle(document.body).fontSize)")
    print(f'  Base font size: {base_font}px')

    h1_size_m = page_m.evaluate("() => { const h = document.querySelector('h1'); return h ? parseFloat(getComputedStyle(h).fontSize) : null; }")
    print(f'  H1 font size mobile: {h1_size_m}px')

    # Hero mobile height
    hero_m_height = page_m.evaluate("() => { const h = document.querySelector('.hero'); return h ? h.offsetHeight : null; }")
    print(f'  Hero section height (mobile): {hero_m_height}px')
    print(f'  Viewport height (mobile): 812px')

    browser.close()
