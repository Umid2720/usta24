import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header for Mobile Menu and Lang Switcher
header_new = '''<header class="header">
        <div class="container">
            <nav class="navbar">
                <a href="#" class="logo">Usta<span>24</span></a>
                
                <div class="nav-right">
                    <div class="lang-switcher desktop-only">
                        <button class="lang-btn active" data-lang="uz">UZ</button>
                        <button class="lang-btn" data-lang="ru">RU</button>
                    </div>
                    <button class="mobile-toggle" aria-label="Menyu">
                        <i class="fa-solid fa-bars"></i>
                    </button>
                </div>

                <div class="nav-links-container">
                    <div class="mobile-menu-header">
                        <a href="#" class="logo">Usta<span>24</span></a>
                        <button class="mobile-close"><i class="fa-solid fa-xmark"></i></button>
                    </div>
                    <ul class="nav-links">
                        <li><a href="#home" data-i18n="nav-home">Asosiy</a></li>
                        <li><a href="#services" data-i18n="nav-services">Xizmatlar</a></li>
                        <li><a href="#features" data-i18n="nav-features">Nega Biz?</a></li>
                        <li><a href="#contact" data-i18n="nav-contact">Aloqa</a></li>
                    </ul>
                    <div class="mobile-menu-footer">
                        <div class="lang-switcher mobile-only" style="margin-bottom: 20px; justify-content: center;">
                            <button class="lang-btn active" data-lang="uz">O'ZBEKCHA</button>
                            <button class="lang-btn" data-lang="ru">РУССКИЙ</button>
                        </div>
                        <a href="tel:+998917254111" class="btn btn-primary" style="width:100%; display:block; text-align:center; margin-bottom:10px; background:#c05621; color:#fff;" data-i18n="call-btn">Usta chaqirish</a>
                        <a href="https://t.me/shoxrux_atayev" target="_blank" class="btn btn-outline" style="width:100%; display:block; text-align:center; border: 1px solid #d1d5db; color: #374151;">Telegramdan yozish</a>
                    </div>
                </div>

                <div class="nav-cta desktop-only">
                    <a href="tel:+998917254111" class="phone-link">+998 91 725-41-11</a>
                    <a href="https://t.me/shoxrux_atayev" target="_blank" class="btn btn-primary" data-i18n="call-btn">Chaqirish</a>
                </div>
            </nav>
        </div>
    </header>'''

html = re.sub(r'<header class="header">.*?</header>', header_new, html, flags=re.DOTALL)


# 2. Update Testimonials to 3D Coverflow
testimonials_new = '''<section id="testimonials" class="testimonials">
            <div class="container">
                <div class="section-header" data-aos="fade-up">
                    <h2 data-i18n="t-title">Mijozlarimizning <span class="highlight">fikrlari</span></h2>
                    <p data-i18n="t-desc">Bizning xizmatlarimizdan foydalangan mijozlarimizning samimiy fikrlari</p>
                </div>
                
                <div class="swiper testimonials-swiper">
                    <div class="swiper-wrapper">
                        <!-- Card 1 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img loading="lazy" src="https://randomuser.me/api/portraits/women/44.jpg" alt="Madina Aliyeva" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">Madina Aliyeva</h4>
                                        <span class="testimonial-location" data-i18n="loc-toshkent">Toshkent</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t1-title">'Natija kutilganidan a\\'lo bo\\'ldi!'</h5>
                                <p class="testimonial-text" data-i18n="t1-desc">Santexnika bo\\'yicha yordam oldim. Natija kutilganidan a\\'lo bo\\'ldi. Jamoa professional ekan.</p>
                                <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                            </div>
                        </div>

                        <!-- Card 2 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img loading="lazy" src="https://randomuser.me/api/portraits/men/32.jpg" alt="Olim Karimov" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">Olim Karimov</h4>
                                        <span class="testimonial-location" data-i18n="loc-samarqand">Samarqand</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t2-title">'Biznesim uchun katta yordam...'</h5>
                                <p class="testimonial-text" data-i18n="t2-desc">Elektrik tarmoqlarini yangilashni joriy qildik. Endi xavfsizlikni nazorat qilish oson.</p>
                                <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                            </div>
                        </div>

                        <!-- Card 3 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img loading="lazy" src="https://randomuser.me/api/portraits/women/68.jpg" alt="Nigora Olimova" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">Nigora Olimova</h4>
                                        <span class="testimonial-location" data-i18n="loc-fargona">Farg\\'ona</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t3-title">'Muloqot juda yoqimli!'</h5>
                                <p class="testimonial-text" data-i18n="t3-desc">Ta\\'mirlash borasida hamkorlik qildik. Men xohlagandek bo\\'ldi. Ba\\'zi o\\'zgarishlar tezda amalga oshirildi.</p>
                                <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                            </div>
                        </div>

                        <!-- Card 4 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img loading="lazy" src="https://randomuser.me/api/portraits/men/46.jpg" alt="Sanjar Tursunov" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">Sanjar Tursunov</h4>
                                        <span class="testimonial-location" data-i18n="loc-urganch">Urganch</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t4-title">'Narxlari hamyonbop!'</h5>
                                <p class="testimonial-text" data-i18n="t4-desc">Boshqa ustalarga qaraganda narxlari ancha yaxshi. Eng muhimi ishi sifatli va kafolatli. Barchaga tavsiya qilaman.</p>
                                <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                            </div>
                        </div>

                        <!-- Card 5 -->
                        <div class="swiper-slide">
                            <div class="testimonial-card">
                                <div class="testimonial-header">
                                    <img loading="lazy" src="https://randomuser.me/api/portraits/women/21.jpg" alt="Dilnoza Rahmatova" class="testimonial-avatar">
                                    <div class="testimonial-info">
                                        <h4 class="testimonial-name">Dilnoza Rahmatova</h4>
                                        <span class="testimonial-location" data-i18n="loc-xorazm">Xorazm</span>
                                    </div>
                                </div>
                                <div class="testimonial-stars">
                                    <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
                                </div>
                                <h5 class="testimonial-title" data-i18n="t5-title">'Kechasi ham kelib yordam berishdi.'</h5>
                                <p class="testimonial-text" data-i18n="t5-desc">Suv quvuri yorilganda tunda qo\\'ng\\'iroq qildik, yarim soatda yetib kelishdi. Ularning tezkorligidan juda minnatdormiz!</p>
                                <span class="testimonial-badge" data-i18n="badge"><i class="fa-solid fa-check"></i> TASDIQLANGAN</span>
                            </div>
                        </div>
                    </div>
                    <!-- Swiper Pagination & Navigation -->
                    <div class="swiper-pagination"></div>
                    <div class="swiper-button-prev"></div>
                    <div class="swiper-button-next"></div>
                </div>
            </div>
        </section>'''

html = re.sub(r'<section id="testimonials" class="testimonials">.*?</section>', testimonials_new, html, flags=re.DOTALL)


# 3. Update Swiper JS Logic for 3D Coverflow and Mobile Menu Logic
js_logic = '''
        // Mobile Navigation Logic (Claude Style)
        const mobileToggle = document.querySelector('.mobile-toggle');
        const mobileClose = document.querySelector('.mobile-close');
        const navContainer = document.querySelector('.nav-links-container');
        const navLinksList = document.querySelectorAll('.nav-links a');
        
        if (mobileToggle) {
            mobileToggle.addEventListener('click', () => {
                navContainer.classList.add('active');
                document.body.style.overflow = 'hidden'; // Prevent background scrolling
            });
        }
        
        if (mobileClose) {
            mobileClose.addEventListener('click', () => {
                navContainer.classList.remove('active');
                document.body.style.overflow = ''; 
            });
        }

        navLinksList.forEach(link => {
            link.addEventListener('click', () => {
                navContainer.classList.remove('active');
                document.body.style.overflow = ''; 
            });
        });

        // Initialize 3D Coverflow Swiper
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
                delay: 3500,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            }
        });
'''
# Replace old swiper logic and the mobile nav logic from the previous script
# Just drop everything after <script> and before Aos.init
html = re.sub(r'<script>\s*// Initialize.*?(?=AOS\.init)', '<script>\n' + js_logic + '\n        ', html, flags=re.DOTALL)
html = re.sub(r'// Mobile Navigation Logic.*?\n        // Tab switching logic', '// Tab switching logic', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 4. Update CSS (style.css)
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add styles for the new Claude-style mobile menu and 3D Coverflow
new_css = '''
/* Language Switcher */
.lang-switcher {
    display: flex;
    gap: 8px;
    background: rgba(0, 0, 0, 0.05);
    padding: 4px;
    border-radius: 20px;
    border: 1px solid rgba(0,0,0,0.1);
}

.lang-btn {
    background: transparent;
    border: none;
    padding: 6px 16px;
    border-radius: 16px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    color: var(--text-main);
    transition: var(--transition);
}

.lang-btn.active {
    background: var(--primary);
    color: var(--white);
}

/* Claude Style Mobile Menu */
.nav-right {
    display: flex;
    align-items: center;
    gap: 15px;
}

.mobile-toggle {
    display: none;
    background: transparent;
    border: none;
    color: var(--text-main);
    font-size: 24px;
    cursor: pointer;
}

.nav-links-container {
    display: flex;
    align-items: center;
}

.mobile-menu-header, .mobile-menu-footer, .mobile-only {
    display: none;
}

/* Testimonials 3D */
.testimonials {
    padding: 120px 0;
    background: #0f172a; /* Dark background */
    color: #fff;
    position: relative;
    overflow: hidden;
}

.testimonials .section-header h2, .testimonials .section-header p {
    color: #fff;
}

.testimonials::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) rotateX(60deg);
    width: 800px;
    height: 800px;
    border-radius: 50%;
    border: 4px solid rgba(59, 130, 246, 0.3);
    box-shadow: 0 0 50px rgba(59, 130, 246, 0.5), inset 0 0 50px rgba(59, 130, 246, 0.5);
    z-index: 0;
}

.testimonials-swiper {
    padding: 50px 0 80px !important;
    z-index: 1;
}

.swiper-slide {
    width: 350px;
    height: auto;
    filter: drop-shadow(0 20px 30px rgba(0,0,0,0.5));
}

.testimonial-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.2);
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: all 0.5s ease;
    height: 100%;
}

.swiper-slide-active .testimonial-card {
    background: linear-gradient(145deg, #1d4ed8, #2563eb);
    border: 2px solid #60a5fa;
    box-shadow: 0 0 30px rgba(59, 130, 246, 0.6);
    transform: scale(1.05);
}

.swiper-slide-prev .testimonial-card {
    background: linear-gradient(145deg, #d97706, #f59e0b);
    border: 1px solid #fbbf24;
}

.swiper-slide-next .testimonial-card {
    background: linear-gradient(145deg, #7e22ce, #a855f7);
    border: 1px solid #c084fc;
}

.testimonial-header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 16px;
    width: 100%;
}

.testimonial-avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 2px solid #fff;
    object-fit: cover;
}

.testimonial-info {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    text-align: left;
}

.testimonial-name {
    font-size: 16px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 2px;
    text-transform: uppercase;
}

.testimonial-location {
    font-size: 12px;
    color: rgba(255,255,255,0.8);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.testimonial-stars {
    color: #fbbf24;
    font-size: 14px;
    margin-bottom: 20px;
}

.testimonial-title {
    font-size: 20px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 15px;
    line-height: 1.3;
}

.testimonial-text {
    font-size: 14px;
    color: rgba(255,255,255,0.9);
    line-height: 1.6;
    margin-bottom: 30px;
}

.testimonial-badge {
    margin-top: auto;
    background: #22c55e;
    color: #fff;
    font-size: 11px;
    font-weight: 700;
    padding: 6px 16px;
    border-radius: 20px;
    text-transform: uppercase;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    box-shadow: 0 4px 10px rgba(34, 197, 94, 0.4);
}

.swiper-pagination-bullet {
    background-color: rgba(255,255,255,0.5);
}
.swiper-pagination-bullet-active {
    background-color: #fff;
}

.swiper-button-prev,
.swiper-button-next {
    background: rgba(37, 99, 235, 0.8);
    width: 40px;
    height: 40px;
    border-radius: 50%;
    color: #fff;
}
.swiper-button-prev::after,
.swiper-button-next::after {
    font-size: 18px;
    font-weight: bold;
}

@media (max-width: 768px) {
    .desktop-only { display: none !important; }
    .mobile-only { display: flex !important; }
    
    .mobile-toggle {
        display: block;
    }

    /* Claude Style Fullscreen Menu */
    .nav-links-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: #faf9f5;
        flex-direction: column;
        align-items: stretch;
        padding: 20px;
        z-index: 9999;
        transform: translateY(-100%);
        opacity: 0;
        transition: transform 0.4s ease, opacity 0.4s ease;
    }

    .nav-links-container.active {
        transform: translateY(0);
        opacity: 1;
    }

    .mobile-menu-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 40px;
    }

    .mobile-close {
        background: transparent;
        border: none;
        font-size: 28px;
        color: #111;
        cursor: pointer;
    }

    .nav-links {
        display: flex;
        flex-direction: column;
        gap: 20px;
        margin-bottom: auto;
    }

    .nav-links li {
        width: 100%;
        border-bottom: 1px solid rgba(0,0,0,0.05);
        padding-bottom: 15px;
    }

    .nav-links li a {
        font-size: 24px;
        font-weight: 600;
        color: #111;
    }

    .mobile-menu-footer {
        display: block;
        padding-top: 20px;
    }
}
'''

# Delete any existing .lang-switcher and .testimonials css blocks to avoid conflicts
css = re.sub(r'/\* Language Switcher \*/.*?/\* Buttons \*/', '/* Buttons */', css, flags=re.DOTALL)
css = re.sub(r'/\* Testimonials \*/.*?/\* CTA Section \*/', '/* CTA Section */', css, flags=re.DOTALL)
css = re.sub(r'\.mobile-toggle \{.*?\}(?=\n\n|\n/|\n@)', '', css, flags=re.DOTALL)
css = re.sub(r'@media \(max-width: 768px\) \{.*?\.nav-links\.active \{.*?\}\n    \}', '@media (max-width: 768px) {', css, flags=re.DOTALL)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css + '\n' + new_css)
