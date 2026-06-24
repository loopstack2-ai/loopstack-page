from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()

    # ── DESKTOP: Additional checks ──
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto('https://loopstack.uk/', wait_until='networkidle', timeout=30000)
    page.wait_for_timeout(2000)

    details = page.evaluate("""() => {
        const r = {};

        // Check logo src
        const logo = document.querySelector('.nav-logo img');
        r['logo_src'] = logo ? logo.getAttribute('src') : 'N/A';

        // Check video source
        const video = document.querySelector('.video-wrapper video');
        r['video_exists'] = video !== null;
        r['video_src'] = video ? video.querySelector('source')?.getAttribute('src') : 'N/A';
        r['video_autoplay'] = video ? video.hasAttribute('autoplay') : false;
        r['video_muted'] = video ? video.hasAttribute('muted') : false;
        r['video_loop'] = video ? video.hasAttribute('loop') : false;
        r['video_playsinline'] = video ? video.hasAttribute('playsinline') : false;

        // Check if video loaded
        r['video_ready_state'] = video ? video.readyState : 'N/A';

        // CSS variables
        const style = getComputedStyle(document.documentElement);
        r['cyan_color'] = style.getPropertyValue('--cyan').trim();
        r['bg_color'] = style.getPropertyValue('--bg').trim();
        r['font_display'] = style.getPropertyValue('--font-display').trim();
        r['font_body'] = style.getPropertyValue('--font-body').trim();

        // Contrast check: grey on bg
        r['grey_on_bg'] = style.getPropertyValue('--grey').trim();

        // Section ordering
        const sections = document.querySelectorAll('section, div.marquee-wrap');
        const ids = [];
        sections.forEach(s => {
            const id = s.id || s.className.slice(0,20) || s.tagName;
            ids.push(id);
        });
        r['sections'] = ids.slice(0,15);

        // Cal.com embed
        const cal_iframe = document.querySelector('.cal-embed-wrapper iframe');
        r['cal_embed_exists'] = cal_iframe !== null;
        r['cal_src'] = cal_iframe ? cal_iframe.getAttribute('src') : 'N/A';
        r['cal_embed_loaded'] = cal_iframe ? cal_iframe.getBoundingClientRect().width > 0 : false;

        // Form fields
        const form = document.getElementById('contactForm');
        r['form_exists'] = form !== null;
        r['form_netlify'] = form ? form.hasAttribute('netlify') : false;
        r['form_hidden'] = form ? form.querySelector('input[type=\"hidden\"]') !== null : false;

        return r;
    }""")

    print('=== SITE DETAILS ===')
    for k, v in details.items():
        print(f'  {k}: {v}')

    # ── MOBILE: More detail on nav and hamburger ──
    page_m = browser.new_page(viewport={'width': 375, 'height': 812})
    page_m.goto('https://loopstack.uk/', wait_until='networkidle', timeout=30000)
    page_m.wait_for_timeout(2000)

    mobile_nav = page_m.evaluate("""() => {
        const r = {};
        const nav = document.querySelector('nav');
        const toggle = document.querySelector('.nav-mobile-toggle');
        const links = document.querySelector('.nav-links');
        const navCta = document.querySelector('.nav-cta');

        r['nav_links_display'] = links ? getComputedStyle(links).display : 'N/A';
        r['nav_links_visible'] = links ? links.offsetParent !== null : false;
        r['hamburger_display'] = toggle ? getComputedStyle(toggle).display : 'N/A';
        r['hamburger_width'] = toggle ? toggle.offsetWidth : 0;
        r['hamburger_height'] = toggle ? toggle.offsetHeight : 0;
        r['nav_cta_display'] = navCta ? getComputedStyle(navCta).display : 'N/A';
        r['nav_cta_width'] = navCta ? navCta.offsetWidth : 0;
        r['nav_cta_height'] = navCta ? navCta.offsetHeight : 0;
        r['nav_height'] = nav ? nav.offsetHeight : 0;
        r['nav_padding'] = nav ? getComputedStyle(nav).padding : 'N/A';

        // Check aria-label on hamburger
        r['hamburger_aria'] = toggle ? toggle.getAttribute('aria-label') : 'N/A';

        return r;
    }""")

    print('\n=== MOBILE NAV DETAILS ===')
    for k, v in mobile_nav.items():
        print(f'  {k}: {v}')

    # Check mobile hamburger click reveals menu
    page_m.click('.nav-mobile-toggle')
    page_m.wait_for_timeout(500)
    after_click = page_m.evaluate("""() => {
        const links = document.querySelector('.nav-links');
        const r = {};
        r['links_display_after_click'] = links ? getComputedStyle(links).display : 'N/A';
        r['links_visible_after_click'] = links ? links.offsetParent !== null : false;
        return r;
    }""")
    print(f'\n  After hamburger click:')
    for k, v in after_click.items():
        print(f'    {k}: {v}')

    # Check if there's JS for hamburger menu toggle
    has_mobile_toggle_js = page_m.evaluate("""() => {
        // Check if there's any event listener or function that handles mobile menu
        const inline = document.querySelector('body script:last-of-type');
        const scriptText = inline ? inline.textContent : '';
        // Check for any .nav-mobile-toggle related code
        const scripts = document.querySelectorAll('script');
        let found = false;
        scripts.forEach(s => {
            if (s.textContent.includes('nav-mobile-toggle') || s.textContent.includes('navMenuToggle') || s.textContent.includes('hamburger')) {
                found = true;
            }
        });
        return found;
    }""")
    print(f'  Hamburger toggle JS found: {has_mobile_toggle_js}')

    # Check layout shift possibility
    layout_shifts = page_m.evaluate("""() => {
        const imgs = document.querySelectorAll('img');
        const videos = document.querySelectorAll('video');
        const issues = [];
        imgs.forEach(img => {
            if (!img.hasAttribute('width') && !img.hasAttribute('height') && !img.complete) {
                issues.push('img without dimensions: ' + (img.getAttribute('src') || 'unknown'));
            }
        });
        return issues;
    }""")
    if layout_shifts and len(layout_shifts) > 0:
        print(f'\n  Layout shift risks: {layout_shifts}')
    else:
        print('\n  Layout shift risks: None detected')

    browser.close()
