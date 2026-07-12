import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Restore Header
header_orig = '''<header class="header">
        <div class="container">
            <nav class="navbar">
                <a href="#" class="logo">Usta<span>24</span></a>
                <ul class="nav-links">
                    <li><a href="#home" data-i18n="nav-home">Asosiy</a></li>
                    <li><a href="#services" data-i18n="nav-services">Xizmatlar</a></li>
                    <li><a href="#features" data-i18n="nav-features">Nega Biz?</a></li>
                    <li><a href="#contact" data-i18n="nav-contact">Aloqa</a></li>
                </ul>
                <div class="nav-cta">
                    <div class="lang-switcher">
                        <button class="lang-btn active" data-lang="uz">UZ</button>
                        <button class="lang-btn" data-lang="ru">RU</button>
                    </div>
                    <a href="tel:+998917254111" class="phone-link">+998 91 725-41-11</a>
                    <a href="https://t.me/shoxrux_atayev" target="_blank" class="btn btn-primary" data-i18n="call-btn">Chaqirish</a>
                </div>
            </nav>
        </div>
    </header>'''

html = re.sub(r'<header class="header">.*?</header>', header_orig, html, flags=re.DOTALL)

# 2. Restore Testimonials
testimonials_orig = '''<section id="testimonials" class="testimonials">
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <h2 data-i18n="t-title">Mijozlarimizning <span class="highlight">fikrlari</span></h2>
                    <p data-i18n="t-desc">Bizning xizmatlarimizdan foydalangan mijozlarimizning samimiy fikrlari</p>
                </div>
                <div class="swiper testimonials-swiper">
                    <div class="swiper-wrapper">
                        <!-- Card 1 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card" data-aos="fade-up" data-aos-delay="100">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="Madina Aliyeva" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                                        <h4 class="testimonial-name">Madina Aliyeva</h4>
                                        <span class="testimonial-location" data-i18n="loc-toshkent">Toshkent</span>
                                        <div class="testimonial-stars">
                                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="testimonial-quote-icon">
                                    <i class="fa-solid fa-quote-right"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t1-title">'Natija kutilganidan a\\'lo bo\\'ldi!'</h5>
                                <p class="testimonial-text" data-i18n="t1-desc">Santexnika bo\\'yicha yordam oldim. Natija kutilganidan a\\'lo bo\\'ldi. Jamoa professional ekan.</p>
                            </div>
                        </div>

                        <!-- Card 2 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card" data-aos="fade-up" data-aos-delay="200">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Olim Karimov" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                                        <h4 class="testimonial-name">Olim Karimov</h4>
                                        <span class="testimonial-location" data-i18n="loc-samarqand">Samarqand</span>
                                        <div class="testimonial-stars">
                                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="testimonial-quote-icon">
                                    <i class="fa-solid fa-quote-right"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t2-title">'Biznesim uchun katta yordam...'</h5>
                                <p class="testimonial-text" data-i18n="t2-desc">Elektrik tarmoqlarini yangilashni joriy qildik. Endi xavfsizlikni nazorat qilish oson.</p>
                            </div>
                        </div>

                        <!-- Card 3 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card" data-aos="fade-up" data-aos-delay="300">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/women/68.jpg" alt="Nigora Olimova" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                                        <h4 class="testimonial-name">Nigora Olimova</h4>
                                        <span class="testimonial-location" data-i18n="loc-fargona">Farg\\'ona</span>
                                        <div class="testimonial-stars">
                                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="testimonial-quote-icon">
                                    <i class="fa-solid fa-quote-right"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t3-title">'Muloqot juda yoqimli!'</h5>
                                <p class="testimonial-text" data-i18n="t3-desc">Ta\\'mirlash borasida hamkorlik qildik. Men xohlagandek bo\\'ldi. Ba\\'zi o\\'zgarishlar tezda amalga oshirildi.</p>
                            </div>
                        </div>

                        <!-- Card 4 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card" data-aos="fade-up" data-aos-delay="400">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/men/46.jpg" alt="Sanjar Tursunov" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                                        <h4 class="testimonial-name">Sanjar Tursunov</h4>
                                        <span class="testimonial-location" data-i18n="loc-urganch">Urganch</span>
                                        <div class="testimonial-stars">
                                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="testimonial-quote-icon">
                                    <i class="fa-solid fa-quote-right"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t4-title">'Narxlari hamyonbop!'</h5>
                                <p class="testimonial-text" data-i18n="t4-desc">Boshqa ustalarga qaraganda narxlari ancha yaxshi. Eng muhimi ishi sifatli va kafolatli. Barchaga tavsiya qilaman.</p>
                            </div>
                        </div>

                        <!-- Card 5 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card" data-aos="fade-up" data-aos-delay="500">
                                <div class="testimonial-header">
                                    <img src="https://randomuser.me/api/portraits/women/21.jpg" alt="Dilnoza Rahmatova" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                                        <h4 class="testimonial-name">Dilnoza Rahmatova</h4>
                                        <span class="testimonial-location" data-i18n="loc-xorazm">Xorazm</span>
                                        <div class="testimonial-stars">
                                            <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="testimonial-quote-icon">
                                    <i class="fa-solid fa-quote-right"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t5-title">'Kechasi ham kelib yordam berishdi.'</h5>
                                <p class="testimonial-text" data-i18n="t5-desc">Suv quvuri yorilganda tunda qo\\'ng\\'iroq qildik, yarim soatda yetib kelishdi. Ularning tezkorligidan juda minnatdormiz!</p>
                            </div>
                        </div>
                    </div>
                    <div class="swiper-pagination"></div>
                </div>
            </div>
        </section>'''

html = re.sub(r'<section id="testimonials" class="testimonials">.*?</section>', testimonials_orig, html, flags=re.DOTALL)

# 3. Restore Swiper Logic
js_orig = '''// Initialize Testimonials Swiper
        const testimonialsSwiper = new Swiper('.testimonials-swiper', {
            slidesPerView: 1,
            spaceBetween: 24,
            loop: true,
            autoplay: {
                delay: 4000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            breakpoints: {
                768: {
                    slidesPerView: 2,
                },
                1024: {
                    slidesPerView: 3,
                }
            }
        });'''
html = re.sub(r'<script>\s*// Mobile Navigation Logic \(Claude Style\).*?(?=\n\n\s*// Tab switching logic)', '<script>\n        ' + js_orig, html, flags=re.DOTALL)

# Write index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Restore style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove Mobile Menu CSS block
css = re.sub(r'/\* Claude Style Mobile Menu \*/.*?(?=/\* Testimonials 3D \*/|/\* Testimonials \*/|$)', '', css, flags=re.DOTALL)

# 2. Restore Testimonials CSS
testimonials_orig_css = '''/* Testimonials */
.testimonials {
    padding: 100px 0;
    background: var(--bg-light);
}

.testimonials .section-header h2 {
    font-size: 36px;
    margin-bottom: 16px;
}

.testimonials-swiper {
    padding-bottom: 50px !important; /* Space for pagination */
}

.testimonial-card {
    background: var(--white);
    border-radius: 12px;
    padding: 32px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
    border: 1px solid #e2e8f0;
    position: relative;
    display: flex;
    flex-direction: column;
    transition: var(--transition);
    height: 100%; /* Ensure all cards stretch to same height */
}

.swiper-slide {
    height: auto; /* Allow slide to determine height based on content or stretch */
}

.testimonial-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.testimonial-header {
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 24px;
}

.testimonial-avatar {
    width: 70px;
    height: 70px;
    border-radius: 50%;
    object-fit: cover;
}

.testimonial-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.testimonial-badge {
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    font-size: 10px;
    font-weight: 700;
    padding: 4px 8px;
    border-radius: 4px;
    margin-bottom: 6px;
    text-transform: uppercase;
}

.testimonial-name {
    font-size: 18px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 2px;
}

.testimonial-location {
    font-size: 13px;
    color: #64748b;
    margin-bottom: 4px;
    line-height: 1.2;
}

.testimonial-stars {
    color: #f59e0b;
    font-size: 12px;
    display: flex;
    gap: 2px;
}

.testimonial-quote-icon {
    position: absolute;
    right: 24px;
    top: 50px;
    font-size: 60px;
    color: #bae6fd;
    opacity: 0.6;
    line-height: 1;
}

.testimonial-title {
    font-size: 18px;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 12px;
    line-height: 1.4;
    position: relative;
    z-index: 2;
}

.testimonial-text {
    font-size: 15px;
    color: #475569;
    line-height: 1.6;
    position: relative;
    z-index: 2;
}

.swiper-pagination-bullet {
    width: 10px;
    height: 10px;
    background-color: #cbd5e1;
    opacity: 1;
}

.swiper-pagination-bullet-active {
    background-color: var(--primary);
    width: 24px;
    border-radius: 5px;
}'''
css = re.sub(r'/\* Testimonials 3D \*/.*?(?=/\* CTA Section \*/)', testimonials_orig_css + '\n\n', css, flags=re.DOTALL)
css = re.sub(r'/\* Testimonials \*/.*?(?=/\* CTA Section \*/)', testimonials_orig_css + '\n\n', css, flags=re.DOTALL)

# Restore display:none to nav-links on mobile
nav_mobile = '''@media (max-width: 768px) {
    .nav-links {
        display: none;
    }
'''
css = re.sub(r'@media \(max-width: 768px\) \{', nav_mobile, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
