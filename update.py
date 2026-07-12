import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    '<a href="#home">Asosiy</a>': '<a href="#home" data-i18n="nav-home">Asosiy</a>',
    '<a href="#services">Xizmatlar</a>': '<a href="#services" data-i18n="nav-services">Xizmatlar</a>',
    '<a href="#features">Nega Biz?</a>': '<a href="#features" data-i18n="nav-features">Nega Biz?</a>',
    '<a href="#contact">Aloqa</a>': '<a href="#contact" data-i18n="nav-contact">Aloqa</a>',
    'class="btn btn-primary">Chaqirish</a>': 'class="btn btn-primary" data-i18n="call-btn">Chaqirish</a>',
    '<h1>Santexnik va Elektrik xizmatlari</h1>': '<h1 data-i18n="hero-title">Santexnik va Elektrik xizmatlari</h1>',
    '<li>☑️ Urganch bo\'ylab bepul chaqiruv</li>': '<li data-i18n="hero-b1">☑️ Urganch bo\'ylab bepul chaqiruv</li>',
    '<li>☑️ 30 daqiqa ichida yetib boramiz</li>': '<li data-i18n="hero-b2">☑️ 30 daqiqa ichida yetib boramiz</li>',
    '<li>☑️ Shartnoma asosida ishlaymiz</li>': '<li data-i18n="hero-b3">☑️ Shartnoma asosida ishlaymiz</li>',
    '<li>☑️ 1 yil kafolat beramiz</li>': '<li data-i18n="hero-b4">☑️ 1 yil kafolat beramiz</li>',
    '<p class="hero-offer">Hoziroq ustalarga buyurtma bering va barcha xizmatlar uchun <span\n                            class="highlight-yellow">15% chegirmaga</span> ega bo\'ling!</p>': '<p class="hero-offer" data-i18n="hero-offer">Hoziroq ustalarga buyurtma bering va barcha xizmatlar uchun <span class="highlight-yellow">15% chegirmaga</span> ega bo\'ling!</p>',
    'text-transform: uppercase;">Usta chaqirish</a>': 'text-transform: uppercase;" data-i18n="hero-btn1">Usta chaqirish</a>',
    'text-transform: uppercase;">Telegramdan yozish 24/7</a>': 'text-transform: uppercase;" data-i18n="hero-btn2">Telegramdan yozish 24/7</a>',
    '<h2>Bizning <span class="highlight">Xizmatlar</span></h2>': '<h2 data-i18n="serv-title">Bizning <span class="highlight">Xizmatlar</span></h2>',
    '<p>Santexnika va elektrik bo\'yicha barcha professional xizmatlar</p>': '<p data-i18n="serv-desc">Santexnika va elektrik bo\'yicha barcha professional xizmatlar</p>',
    '<button class="tab-btn active" data-tab="santexnika">SANTEXNIK</button>': '<button class="tab-btn active" data-tab="santexnika" data-i18n="tab-santex">SANTEXNIK</button>',
    '<button class="tab-btn" data-tab="elektrik">ELEKTRIK</button>': '<button class="tab-btn" data-tab="elektrik" data-i18n="tab-elek">ELEKTRIK</button>',
    '<h3>TIQILISHLARNI BARTARAF QILISH</h3>': '<h3 data-i18n="s1-title">TIQILISHLARNI BARTARAF QILISH</h3>',
    '<h3>SANTEXNIKA O\'RNATISH</h3>': '<h3 data-i18n="s2-title">SANTEXNIKA O\'RNATISH</h3>',
    '<h3>OQISHLARNI BARTARAF ETISH</h3>': '<h3 data-i18n="s3-title">OQISHLARNI BARTARAF ETISH</h3>',
    '<h3>UNITAZ O\'RNATISH</h3>': '<h3 data-i18n="s4-title">UNITAZ O\'RNATISH</h3>',
    '<h3>KATYOL O\'RNATISH</h3>': '<h3 data-i18n="s5-title">KATYOL O\'RNATISH</h3>',
    '<h3>KANALIZATSIYA TOZALASH</h3>': '<h3 data-i18n="s6-title">KANALIZATSIYA TOZALASH</h3>',
    '<h3>ROZETKALARNI ALMASHTIRISH</h3>': '<h3 data-i18n="e1-title">ROZETKALARNI ALMASHTIRISH</h3>',
    '<h3>QANDILNI O\'RNATISH</h3>': '<h3 data-i18n="e2-title">QANDILNI O\'RNATISH</h3>',
    '<h3>HISOBLAGICH ALMASHTIRISH</h3>': '<h3 data-i18n="e3-title">HISOBLAGICH ALMASHTIRISH</h3>',
    '<h3>CHIROQNI O\'RNATISH</h3>': '<h3 data-i18n="e4-title">CHIROQNI O\'RNATISH</h3>',
    '<h3>AVTOMATNI ALMASHTIRISH</h3>': '<h3 data-i18n="e5-title">AVTOMATNI ALMASHTIRISH</h3>',
    '<h3>QANDILNI O\'RNATISH/DEMONTAJ QILISH</h3>': '<h3 data-i18n="e6-title">QANDILNI O\'RNATISH/DEMONTAJ QILISH</h3>',
    '<p class="service-price\"><span>150 000</span> dan boshlab</p>': '<p class="service-price" data-i18n="price-from"><span>150 000</span> dan boshlab</p>',
    '<p class="service-price\"><span>100 000</span> dan boshlab</p>': '<p class="service-price" data-i18n="price-from-e"><span>100 000</span> dan boshlab</p>',
    'class="btn btn-primary service-btn">Usta chaqirish</a>': 'class="btn btn-primary service-btn" data-i18n="hero-btn1">Usta chaqirish</a>',
    '<h2 style="text-transform: uppercase;\">KOMPANIYA HAQIDA</h2>': '<h2 style="text-transform: uppercase;" data-i18n="about-title">KOMPANIYA HAQIDA</h2>',
    '<p>Bizning kompaniya haqida quyidagi ma\'lumotlardan bilib olishingiz mumkin.</p>': '<p data-i18n="about-desc">Bizning kompaniya haqida quyidagi ma\'lumotlardan bilib olishingiz mumkin.</p>',
    '<h3>5+ YIL</h3>': '<h3 data-i18n="a1-title">5+ YIL</h3>',
    '<p>Barcha santexnik va elektriklar eng kamida 5 yil tajribaga ega.</p>': '<p data-i18n="a1-desc">Barcha santexnik va elektriklar eng kamida 5 yil tajribaga ega.</p>',
    '<h3>100+</h3>': '<h3 data-i18n="a2-title">100+</h3>',
    '<p>Hamkor ustalarga egamiz.</p>': '<p data-i18n="a2-desc">Hamkor ustalarga egamiz.</p>',
    '<h3>30 daqiqa</h3>': '<h3 data-i18n="a3-title">30 daqiqa</h3>',
    '<p>90% holatlarda 30 daqiqa ichida aytilgan manzilga yetib boramiz.</p>': '<p data-i18n="a3-desc">90% holatlarda 30 daqiqa ichida aytilgan manzilga yetib boramiz.</p>',
    '<h3>Garantiya</h3>': '<h3 data-i18n="a4-title">Garantiya</h3>',
    '<p>Biz bajargan ishimizga 1 yil kafolat beramiz.</p>': '<p data-i18n="a4-desc">Biz bajargan ishimizga 1 yil kafolat beramiz.</p>',
    '<h3>200+ ta</h3>': '<h3 data-i18n="a5-title">200+ ta</h3>',
    '<p>Har oy 100 dan oshiq ishimizdan rozi mijozlar.</p>': '<p data-i18n="a5-desc">Har oy 100 dan oshiq ishimizdan rozi mijozlar.</p>',
    '<h3>0 so\'m</h3>': '<h3 data-i18n="a6-title">0 so\'m</h3>',
    '<p>Buyurtma bajarilgan bo\'lsa yo\'l haqqi olinmaydi.</p>': '<p data-i18n="a6-desc\">Buyurtma bajarilgan bo\'lsa yo\'l haqqi olinmaydi.</p>',
    '<h2>Nega aynan <span class="highlight\">bizni</span> tanlashadi?</h2>': '<h2 data-i18n="f-title">Nega aynan <span class="highlight">bizni</span> tanlashadi?</h2>',
    '<p>Biz mijozlarimizga faqat eng yaxshi xizmatni taqdim etishga intilamiz.</p>': '<p data-i18n="f-desc\">Biz mijozlarimizga faqat eng yaxshi xizmatni taqdim etishga intilamiz.</p>',
    '<h4>Tezkor yetib borish</h4>': '<h4 data-i18n="f1-title">Tezkor yetib borish</h4>',
    '<p>Buyurtma tushgandan so\'ng 30 daqiqa ichida yetib boramiz.</p>': '<p data-i18n="f1-desc">Buyurtma tushgandan so\'ng 30 daqiqa ichida yetib boramiz.</p>',
    '<h4>Sifat kafolati</h4>': '<h4 data-i18n="f2-title">Sifat kafolati</h4>',
    '<p>Barcha qilingan ishlarga 1 yillik rasmiy kafolat beramiz.</p>': '<p data-i18n="f2-desc">Barcha qilingan ishlarga 1 yillik rasmiy kafolat beramiz.</p>',
    '<h4>Arzon narxlar</h4>': '<h4 data-i18n="f3-title\">Arzon narxlar</h4>',
    '<p>Yashirin to\'lovlarsiz, oldindan kelishilgan hamyonbop narxlar.</p>': '<p data-i18n="f3-desc\">Yashirin to\'lovlarsiz, oldindan kelishilgan hamyonbop narxlar.</p>',
    '<h2>Uyingizda muammo bormi?</h2>': '<h2 data-i18n="cta-title\">Uyingizda muammo bormi?</h2>',
    '<p>Hoziroq bizga qo\'ng\'iroq qiling va muammoni professionallarga topshiring.</p>': '<p data-i18n="cta-desc\">Hoziroq bizga qo\'ng\'iroq qiling va muammoni professionallarga topshiring.</p>',
    '<p class="cta-subtext\">24 soat dam olish kunlarisiz</p>': '<p class="cta-subtext" data-i18n="cta-sub\">24 soat dam olish kunlarisiz</p>',
    'style="margin-top: 15px; display: inline-block;\">Telegram orqali bog\'lanish</a>': 'style="margin-top: 15px; display: inline-block;" data-i18n="cta-tg\">Telegram orqali bog\'lanish</a>',
    '<p>Urganch shahridagi ishonchli santexnika va elektrik xizmatlari ko\'rsatuvchi kompaniya.</p>': '<p data-i18n="ft-desc\">Urganch shahridagi ishonchli santexnika va elektrik xizmatlari ko\'rsatuvchi kompaniya.</p>',
    '<h3>Havolalar</h3>': '<h3 data-i18n="ft-links\">Havolalar</h3>',
    '<li><a href="#features\">Afzalliklar</a></li>': '<li><a href="#features" data-i18n="ft-adv\">Afzalliklar</a></li>',
    '<h3>Aloqa</h3>': '<h3 data-i18n="ft-contact\">Aloqa</h3>',
    '<p>&copy; 2026 Usta24. Barcha huquqlar himoyalangan.</p>': '<p data-i18n="ft-copy\">&copy; 2026 Usta24. Barcha huquqlar himoyalangan.</p>'
}

for k, v in replacements.items():
    html = html.replace(k, v)

# Language Switcher
nav_cta_orig = '<div class="nav-cta\">'
nav_cta_new = '''<div class="nav-cta">
                    <div class="lang-switcher">
                        <button class="lang-btn active" data-lang="uz">UZ</button>
                        <button class="lang-btn" data-lang="ru">RU</button>
                    </div>'''
html = html.replace(nav_cta_orig, nav_cta_new)

# Testimonials section update
import re
testimonials_orig = re.search(r'(<div class="swiper testimonials-swiper">)(.*?)(</div>\s*</div>\s*</section>)', html, re.DOTALL)
if testimonials_orig:
    testimonials_new = '''<div class="swiper testimonials-swiper">
                    <div class="swiper-wrapper">
                        <!-- Card 1 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Madina Aliyeva" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">MADINA ALIYEVA</h4>
                                        <span class="testimonial-location" data-i18n="loc-toshkent">TOSHKENT</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t1-title">'Natija kutilganidan a\\'lo bo\\'ldi!'</h5>
                                <p class="testimonial-text" data-i18n="t1-desc">Santexnika bo\\'yicha yordam oldim. Natija kutilganidan a\\'lo bo\\'ldi. Jamoa professional ekan.</p>
                                <div class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</div>
                            </div>
                        </div>

                        <!-- Card 2 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Olim Karimov" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">OLIM KARIMOV</h4>
                                        <span class="testimonial-location" data-i18n="loc-samarqand">SAMARQAND</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t2-title">'Biznesim uchun katta yordam...'</h5>
                                <p class="testimonial-text" data-i18n="t2-desc">Elektrik tarmoqlarini yangilashni joriy qildik. Endi xavfsizlikni nazorat qilish oson.</p>
                                <div class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</div>
                            </div>
                        </div>

                        <!-- Card 3 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/women/68.jpg" alt="Nigora Olimova" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">NIGORA OLIMOVA</h4>
                                        <span class="testimonial-location" data-i18n="loc-fargona">FARG\\'ONA</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t3-title">'Muloqot juda yoqimli!'</h5>
                                <p class="testimonial-text" data-i18n="t3-desc">Ta\\'mirlash borasida hamkorlik qildik. Men xohlagandek bo\\'ldi. Ba\\'zi o\\'zgarishlar tezda amalga oshirildi.</p>
                                <div class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</div>
                            </div>
                        </div>

                        <!-- Card 4 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/men/46.jpg" alt="Sanjar Tursunov" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">SANJAR TURSUNOV</h4>
                                        <span class="testimonial-location" data-i18n="loc-urganch">URGANCH</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t4-title">'Narxlari hamyonbop!'</h5>
                                <p class="testimonial-text" data-i18n="t4-desc">Boshqa ustalarga qaraganda narxlari ancha yaxshi. Eng muhimi ishi sifatli va kafolatli. Barchaga tavsiya qilaman.</p>
                                <div class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</div>
                            </div>
                        </div>

                        <!-- Card 5 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/women/21.jpg" alt="Dilnoza Rahmatova" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">DILNOZA RAHMATOVA</h4>
                                        <span class="testimonial-location" data-i18n="loc-xorazm">XORAZM</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t5-title">'Kechasi ham kelib yordam berishdi.'</h5>
                                <p class="testimonial-text" data-i18n="t5-desc">Suv quvuri yorilganda tunda qo\\'ng\\'iroq qildik, yarim soatda yetib kelishdi. Ularning tezkorligidan juda minnatdormiz!</p>
                                <div class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</div>
                            </div>
                        </div>
                    </div>
                    <div class="swiper-pagination"></div>
                    <div class="swiper-button-prev"></div>
                    <div class="swiper-button-next"></div>
                </div>'''
    html = html[:testimonials_orig.start(1)] + testimonials_new + html[testimonials_orig.end(2):]

# Add script at the bottom
script_orig = '<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js\"></script>'
script_new = '<script src="translations.js\"></script>\n    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js\"></script>'
html = html.replace(script_orig, script_new)

# Localization and Swiper JS logic
script_init = '''
        // Translation Logic
        const langBtns = document.querySelectorAll('.lang-btn');
        const elements = document.querySelectorAll('[data-i18n]');
        
        function setLanguage(lang) {
            localStorage.setItem('lang', lang);
            
            langBtns.forEach(btn => {
                if(btn.dataset.lang === lang) {
                    btn.classList.add('active');
                } else {
                    btn.classList.remove('active');
                }
            });
            
            elements.forEach(el => {
                const key = el.getAttribute('data-i18n');
                if(translations[lang] && translations[lang][key]) {
                    el.innerHTML = translations[lang][key];
                }
            });
        }
        
        let savedLang = localStorage.getItem('lang') || 'uz';
        setLanguage(savedLang);
        
        langBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                setLanguage(btn.dataset.lang);
            });
        });

        // Initialize Testimonials Swiper
        const testimonialsSwiper = new Swiper('.testimonials-swiper', {
            effect: 'coverflow',
            grabCursor: true,
            centeredSlides: true,
            slidesPerView: 'auto',
            loop: true,
            coverflowEffect: {
                rotate: 0,
                stretch: 0,
                depth: 100,
                modifier: 2,
                slideShadows: false,
            },
            autoplay: {
                delay: 4000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });
'''

# Replace Swiper init
html = re.sub(r'// Initialize Testimonials Swiper.*}\);', script_init, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
