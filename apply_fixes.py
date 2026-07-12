import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. SEO & Open Graph Tags
seo_tags = '''
    <link rel="icon" type="image/png" href="images/favicon.png">
    <meta property="og:title" content="Usta24 - Professional Santexnika va Elektrik Xizmatlari">
    <meta property="og:description" content="Toshkentda yuqori sifatli santexnika va elektrik xizmatlari. Tezkor chaqiruv va kafolatli ish.">
    <meta property="og:image" content="https://usta24.uz/images/cover.png">
    <meta property="og:url" content="https://usta24.uz">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://usta24.uz">
'''
html = html.replace('</head>', seo_tags + '</head>')

# 2. Mobile toggle button
nav_cta_orig = '<div class="nav-cta">'
nav_cta_new = '''<button class="mobile-toggle" aria-label="Menyu">
                        <i class="fa-solid fa-bars"></i>
                    </button>
                    <div class="nav-cta">'''
html = html.replace(nav_cta_orig, nav_cta_new)

# 3. Add loading="lazy" to all img tags EXCEPT hero image if it was an img tag (none in hero).
# We'll just replace '<img src="' with '<img loading="lazy" src="'
# But first, we should make sure we don't duplicate.
if 'loading="lazy"' not in html:
    html = html.replace('<img src=', '<img loading="lazy" src=')
    html = html.replace('<img loading="lazy" src="https://randomuser.me', '<img loading="lazy" src="https://randomuser.me') # it's fine for testimonials

# 4. Add data-i18n to testimonials title & desc
testimonials_h2_orig = '<h2>Mijozlarimizning <span class="highlight">fikrlari</span></h2>'
testimonials_h2_new = '<h2 data-i18n="t-title">Mijozlarimizning <span class="highlight">fikrlari</span></h2>'
html = html.replace(testimonials_h2_orig, testimonials_h2_new)

testimonials_p_orig = '<p>Bizning xizmatlarimizdan foydalangan mijozlarimizning samimiy fikrlari</p>'
testimonials_p_new = '<p data-i18n="t-desc">Bizning xizmatlarimizdan foydalangan mijozlarimizning samimiy fikrlari</p>'
# Only replace the one in testimonials
html = re.sub(r'(<div class="section-header" data-aos="fade-up">\s*)' + re.escape(testimonials_p_orig), r'\1' + testimonials_p_new, html)

# 5. JS updates
js_lang_orig = "localStorage.setItem('lang', lang);"
js_lang_new = "localStorage.setItem('lang', lang);\n            document.documentElement.lang = lang;"
html = html.replace(js_lang_orig, js_lang_new)

js_mobile_nav = '''
        // Mobile Navigation Logic
        const mobileToggle = document.querySelector('.mobile-toggle');
        const navLinks = document.querySelector('.nav-links');
        
        mobileToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = mobileToggle.querySelector('i');
            if(navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });

        // Close mobile menu when a link is clicked
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                mobileToggle.querySelector('i').classList.remove('fa-xmark');
                mobileToggle.querySelector('i').classList.add('fa-bars');
            });
        });
'''
# Insert right before '// Tab switching logic'
html = html.replace('// Tab switching logic', js_mobile_nav + '\n        // Tab switching logic')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# CSS Update
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_css = '''
.mobile-toggle {
    display: none;
    background: transparent;
    border: none;
    color: var(--text-main);
    font-size: 24px;
    cursor: pointer;
    z-index: 1001;
}

@media (max-width: 768px) {
    .mobile-toggle {
        display: block;
    }

    .nav-links {
        display: flex !important; /* Override previous display:none if any */
        flex-direction: column;
        position: absolute;
        top: 70px;
        left: 0;
        width: 100%;
        background: var(--white);
        padding: 20px;
        transform: translateY(-150%);
        opacity: 0;
        pointer-events: none;
        transition: all 0.3s ease;
        z-index: 1000;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        gap: 15px;
        text-align: center;
    }

    .nav-links.active {
        transform: translateY(0);
        opacity: 1;
        pointer-events: auto;
    }
'''

# We need to replace the specific block in style.css
# The user said: style.cssda @media (max-width: 768px) ichida .nav-links { display: none; } bor
# We'll just replace that line and add our mobile-toggle stuff before @media
css = css.replace('.nav-links {\n        display: none;\n    }', '/* Mobile nav links styled in separate block above */')
# In case format is slightly different
css = re.sub(r'\.nav-links\s*\{\s*display:\s*none;\s*\}', '/* nav-links display none removed */', css)

# add mobile-toggle css right before @media (max-width: 768px)
css = css.replace('@media (max-width: 768px) {', mobile_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

