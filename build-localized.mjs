import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const root = process.cwd();
const baseUrl = 'https://usta24uz.netlify.app';

function read(relativePath) {
  return fs.readFileSync(path.join(root, relativePath), 'utf8');
}

function write(relativePath, content) {
  const target = path.join(root, relativePath);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.writeFileSync(target, content.replace(/\r?\n/g, '\n'), 'utf8');
}

function replaceAllExact(content, replacements) {
  let result = content;
  for (const [source, target] of replacements.sort((a, b) => b[0].length - a[0].length)) {
    result = result.split(source).join(target);
  }
  return result;
}

function localizeDataNodes(html, dictionary) {
  return html.replace(
    /<([a-z][a-z0-9-]*)([^>]*\sdata-i18n="([^"]+)"[^>]*)>([\s\S]*?)<\/\1>/gi,
    (match, tag, attributes, key) => dictionary[key] === undefined
      ? match
      : `<${tag}${attributes}>${dictionary[key]}</${tag}>`
  );
}

function localizeCounterSuffixes(html, dictionary) {
  return html.replace(
    /data-suffix="[^"]*"\s+data-i18n-suffix="([^"]+)"/g,
    (match, key) => dictionary[key] === undefined
      ? match
      : `data-suffix="${dictionary[key]}" data-i18n-suffix="${key}"`
  );
}

const translationContext = {};
vm.runInNewContext(`${read('translations.js')}\nglobalThis.__translations = translations;`, translationContext);
const ru = translationContext.__translations.ru;

function russianHomeSchema(sourceHtml) {
  return sourceHtml.replace(
    /<script type="application\/ld\+json">([\s\S]*?)<\/script>/,
    (match, rawJson) => {
      const data = JSON.parse(rawJson);
      for (const item of data['@graph']) {
        if (item['@type'] === 'WebPage') {
          item['@id'] = `${baseUrl}/ru/#webpage`;
          item.url = `${baseUrl}/ru/`;
          item.name = 'Сантехник и электрик в Ургенче 24/7 — Usta24';
          item.description = 'Услуги сантехника и электрика в Ургенче: связь 24/7, согласованная заранее цена и гарантия на выполненную работу.';
          item.inLanguage = 'ru';
        }
        if (item['@type'] === 'ImageObject') {
          item.caption = 'Usta24 — услуги сантехника и электрика в Ургенче';
        }
        if (Array.isArray(item['@type']) && item['@type'].includes('HomeAndConstructionBusiness')) {
          item.description = 'Usta24 оказывает услуги сантехника и электрика в Ургенче с возможностью обращения 24/7. Цена согласуется до начала работ, на выполненную работу предоставляется гарантия.';
          item.address.addressLocality = 'Ургенч';
          item.address.addressRegion = 'Хорезмская область';
          item.areaServed[0].name = 'Ургенч';
          item.areaServed[1].name = 'Хорезмская область';
          item.hasOfferCatalog.name = 'Услуги Usta24';
          item.hasOfferCatalog.itemListElement[0].url = `${baseUrl}/ru/santehnik-urgench/`;
          item.hasOfferCatalog.itemListElement[0].itemOffered.name = 'Услуги сантехника в Ургенче';
          item.hasOfferCatalog.itemListElement[0].itemOffered.areaServed.name = 'Ургенч';
          item.hasOfferCatalog.itemListElement[1].url = `${baseUrl}/ru/elektrik-urgench/`;
          item.hasOfferCatalog.itemListElement[1].itemOffered.name = 'Услуги электрика в Ургенче';
          item.hasOfferCatalog.itemListElement[1].itemOffered.areaServed.name = 'Ургенч';
        }
        if (item['@type'] === 'FAQPage') {
          item['@id'] = `${baseUrl}/ru/#faq-schema`;
          item.mainEntity.forEach((question, index) => {
            const number = index + 1;
            question.name = ru[`faq-q${number}`];
            question.acceptedAnswer.text = ru[`faq-a${number}`];
          });
        }
      }
      return `    <script type="application/ld+json">\n${JSON.stringify(data, null, 8)}\n    </script>`;
    }
  );
}

function buildRussianHome() {
  let html = read('index.html');
  html = localizeDataNodes(html, ru);
  html = localizeCounterSuffixes(html, ru);
  html = russianHomeSchema(html);
  html = replaceAllExact(html, [
    ['<html lang="uz">', '<html lang="ru">'],
    ['href="style.css?v=20260720-4"', 'href="/style.css?v=20260720-4"'],
    ['href="images/', 'href="/images/'],
    ['src="images/', 'src="/images/'],
    ['<title>Urganchda Santexnik va Elektrik 24/7 — Usta24</title>', '<title>Сантехник и Электрик в Ургенче 24/7 — Usta24</title>'],
    ["Urganchda santexnik yoki elektrik kerakmi? Usta24 bilan 24/7 bog'laning. Narx ish boshlanishidan oldin kelishiladi, bajarilgan ishga kafolat beriladi.", 'Нужен сантехник или электрик в Ургенче? Свяжитесь с Usta24 круглосуточно. Цена согласуется до начала работ, на выполненную работу предоставляется гарантия.'],
    ['Urganchda Santexnik va Elektrik 24/7 — Usta24', 'Сантехник и Электрик в Ургенче 24/7 — Usta24'],
    ['Usta24 — Urganchda 24/7 santexnik va elektrik chaqirish. Tez yetib borish, kelishilgan narx va kafolatli ish.', 'Usta24 — вызов сантехника и электрика в Ургенче 24/7. Быстрый выезд, согласованная цена и гарантия.'],
    ['Usta24 - Urganchda santexnik va elektrik xizmatlari', 'Usta24 — услуги сантехника и электрика в Ургенче'],
    ['Usta24 — Urganchda santexnik va elektrik xizmatlari', 'Usta24 — услуги сантехника и электрика в Ургенче'],
    ['Urganchda Usta24 santexnik va elektrik xizmatlari: 24/7 aloqa, tezkor chaqiruv va kafolatli ish.', 'Услуги сантехника и электрика Usta24 в Ургенче: связь 24/7, быстрый вызов и гарантия.'],
    ['<meta property="og:locale" content="uz_UZ">', '<meta property="og:locale" content="ru_RU">\n    <meta property="og:locale:alternate" content="uz_UZ">'],
    ['<link rel="canonical" href="https://usta24uz.netlify.app/">', '<link rel="canonical" href="https://usta24uz.netlify.app/ru/">'],
    ['<meta property="og:url" content="https://usta24uz.netlify.app/">', '<meta property="og:url" content="https://usta24uz.netlify.app/ru/">'],
    ['"priceRange": "100 000–150 000 UZS dan"', '"priceRange": "от 100 000 до 150 000 UZS"'],
    ['href="/santexnik-urganch/"', 'href="/ru/santehnik-urgench/"'],
    ['href="/elektrik-urganch/"', 'href="/ru/elektrik-urgench/"'],
    ['href="/#', 'href="/ru/#'],
    ['href="/" class="logo"', 'href="/ru/" class="logo"'],
    ['<a class="lang-btn active" href="/" lang="uz" hreflang="uz" aria-current="page">UZ</a>\n                        <a class="lang-btn" href="/ru/" lang="ru" hreflang="ru">RU</a>', '<a class="lang-btn" href="/" lang="uz" hreflang="uz">UZ</a>\n                        <a class="lang-btn active" href="/ru/" lang="ru" hreflang="ru" aria-current="page">RU</a>'],
    ['aria-label="Usta24 bosh sahifa"', 'aria-label="Главная страница Usta24"'],
    ['aria-label="Asosiy navigatsiya"', 'aria-label="Основная навигация"'],
    ['aria-label="Menyuni ochish"', 'aria-label="Открыть меню"'],
    ['aria-label="Menyuni yopish"', 'aria-label="Закрыть меню"'],
    ['aria-label="Xizmat turi"', 'aria-label="Вид услуги"'],
    ["'Menyuni yopish'", "'Закрыть меню'"],
    ["'Menyuni ochish'", "'Открыть меню'"],
    ['<span class="cta-card-name">Xamro</span>', '<span class="cta-card-name">Хамро</span>'],
    ['<span class="cta-card-name">Shoxruh</span>', '<span class="cta-card-name">Шохрух</span>'],
    ['(Shoxruh)', '(Шохрух)'],
    ['(Xamro)', '(Хамро)'],
    ['alt="Santexnik Urganch - tiqilishni tozalash"', 'alt="Сантехник в Ургенче — прочистка засора"'],
    ['alt="Santexnik Urganch - santexnika o\'rnatish"', 'alt="Сантехник в Ургенче — установка сантехники"'],
    ['alt="Santexnik Urganch - suv oqishini bartaraf etish"', 'alt="Сантехник в Ургенче — устранение протечки"'],
    ['alt="Santexnik Urganch - unitaz o\'rnatish"', 'alt="Сантехник в Ургенче — установка унитаза"'],
    ['alt="Santexnik Urganch - katyol o\'rnatish"', 'alt="Сантехник в Ургенче — установка котла"'],
    ['alt="Santexnik Urganch - kanalizatsiya tozalash"', 'alt="Сантехник в Ургенче — прочистка канализации"'],
    ['alt="Elektrik Urganch - rozetka almashtirish"', 'alt="Электрик в Ургенче — замена розетки"'],
    ['alt="Elektrik Urganch - qandil o\'rnatish"', 'alt="Электрик в Ургенче — установка люстры"'],
    ['alt="Elektrik Urganch - hisoblagich almashtirish"', 'alt="Электрик в Ургенче — замена счётчика"'],
    ['alt="Elektrik Urganch - chiroq o\'rnatish"', 'alt="Электрик в Ургенче — установка светильника"'],
    ['alt="Elektrik Urganch - avtomat almashtirish"', 'alt="Электрик в Ургенче — замена автомата"'],
    ['alt="Elektrik Urganch - qandil demontaj qilish"', 'alt="Электрик в Ургенче — демонтаж люстры"'],
    ['alt="Santexnik Urganch va Elektrik Urganch - Usta24 ish jarayoni"', 'alt="Работа сантехника и электрика Usta24 в Ургенче"']
  ]);
  html = html.replace(
    /alt="Usta24 mijozi ([^"]+) fikri"/g,
    'alt="Отзыв клиента Usta24 $1"'
  );
  write('ru/index.html', html);
}

const sharedServiceReplacements = [
  ['<html lang="uz">', '<html lang="ru">'],
  ['aria-label="Usta24 bosh sahifa"', 'aria-label="Главная страница Usta24"'],
  ['aria-label="Asosiy navigatsiya"', 'aria-label="Основная навигация"'],
  ["aria-label=\"Sahifa yo'li\"", 'aria-label="Навигационная цепочка"'],
  ['Barcha huquqlar himoyalangan.', 'Все права защищены.'],
  ['Urganchda santexnik va elektrik xizmatlari.', 'Услуги сантехника и электрика в Ургенче.'],
  ['Usta24 bosh sahifasi', 'Главная страница Usta24'],
  ['Bosh sahifa', 'Главная'],
  ['Xizmatlar', 'Услуги'],
  ['Aloqa', 'Контакты'],
  ["Qo'ng'iroq qilish", 'Позвонить'],
  ['Telegramdan yozish', 'Написать в Telegram'],
  ['Savol-javob', 'Вопросы и ответы'],
  ['Ish jarayoni', 'Порядок работы'],
  ['Narx kelishiladi', 'Цена согласуется'],
  ['24/7 aloqa', 'Связь 24/7'],
  ['Urganch va yaqin Xorazm hududlari', 'Ургенч и ближайшие районы Хорезма'],
  ['Urganchda santexnik', 'Сантехник в Ургенче'],
  ['Urganchda elektrik', 'Электрик в Ургенче'],
  ['Urganch shahri', 'город Ургенч'],
  ['Xorazm viloyati', 'Хорезмская область'],
  ['Urganch', 'Ургенч'],
  ['Santexnik', 'Сантехник'],
  ['Elektrik', 'Электрик']
];

const plumberReplacements = [
  ['Santexnik Urganch — 24/7 Usta Chaqirish | Usta24', 'Сантехник в Ургенче — вызов мастера 24/7 | Usta24'],
  ["Urganchda santexnik chaqiring: quvur va kanalizatsiya tiqilishi, suv oqishi, unitaz, kran, dush va isitish tizimi. 24/7 aloqa, kelishilgan narx va kafolat.", 'Вызов сантехника в Ургенче: засоры труб и канализации, протечки, установка унитаза, крана, душа и системы отопления. Связь 24/7, согласованная цена и гарантия.'],
  ['Santexnik Urganch — 24/7 Usta Chaqirish', 'Сантехник в Ургенче — вызов мастера 24/7'],
  ["Urganchda quvur, kanalizatsiya, suv oqishi va santexnika jihozlari bo'yicha 24/7 yordam.", 'Круглосуточная помощь в Ургенче с трубами, канализацией, протечками и сантехническим оборудованием.'],
  ['Santexnik Urganch — Usta24', 'Сантехник в Ургенче — Usta24'],
  ["Urganchda 24/7 santexnik chaqirish, oldindan kelishilgan narx va bajarilgan ishga kafolat.", 'Вызов сантехника в Ургенче 24/7, заранее согласованная цена и гарантия на выполненную работу.'],
  ['Usta24 — Urganchda santexnik xizmati', 'Usta24 — услуги сантехника в Ургенче'],
  ['Santexnik Urganch — 24/7 usta chaqirish', 'Сантехник в Ургенче — вызов мастера 24/7'],
  ["Urganchda quvur, kanalizatsiya, suv oqishi va santexnika jihozlari bo'yicha xizmatlar.", 'Услуги в Ургенче по ремонту труб, канализации, устранению протечек и установке сантехники.'],
  ['Santexnik Urganch', 'Сантехник в Ургенче'],
  ["Urganchda santexnik xizmati", 'Услуги сантехника в Ургенче'],
  ["Santexnika ta'miri va o'rnatish", 'Ремонт и установка сантехники'],
  ['Santexnik xizmatlari', 'Сантехнические услуги'],
  ['Quvur tiqilishini bartaraf qilish', 'Устранение засоров труб'],
  ['Suv oqishini aniqlash va tuzatish', 'Поиск и устранение протечек'],
  ["Unitaz, kran va dush o'rnatish", 'Установка унитаза, крана и душа'],
  ['Kanalizatsiya tozalash', 'Прочистка канализации'],
  ["Urganchda santexnik chaqirish narxi qancha?", 'Сколько стоит вызов сантехника в Ургенче?'],
  ["Ko'rsatilgan santexnik xizmatlari 150 000 so'mdan boshlanadi. Yakuniy narx muammo va ish hajmi ko'rilgach, ish boshlanishidan oldin kelishiladi.", 'Стоимость указанных сантехнических услуг начинается от 150 000 сум. Окончательная цена согласуется до начала работ после осмотра проблемы и оценки объёма.'],
  ['Santexnik qancha vaqtda yetib boradi?', 'Как быстро приедет сантехник?'],
  ["Usta24 90 foiz holatda Urganchdagi manzilga 30 daqiqa ichida yetib borishga harakat qiladi. Aniq vaqt usta joylashuvi va manzilga bog'liq.", 'В 90 процентах случаев Usta24 старается прибыть по адресу в Ургенче в течение 30 минут. Точное время зависит от местоположения мастера и адреса.'],
  ['Santexnikni kechasi ham chaqirish mumkinmi?', 'Можно ли вызвать сантехника ночью?'],
  ["Ha, Usta24 bilan santexnik masalalari bo'yicha 24/7 bog'lanish mumkin.", 'Да, по вопросам сантехники с Usta24 можно связаться круглосуточно.'],
  ['Bajarilgan santexnika ishiga kafolat bormi?', 'Есть ли гарантия на сантехнические работы?'],
  ["Ha, bajarilgan ishga bir yilgacha kafolat beriladi. Kafolat shartlari bajarilgan ish turiga qarab tushuntiriladi.", 'Да, на выполненную работу предоставляется гарантия до одного года. Условия гарантии объясняются в зависимости от вида работ.'],
  ['Santexnik Urganch — 24/7 tezkor yordam', 'Сантехник в Ургенче — срочная помощь 24/7'],
  ["Quvur yoki kanalizatsiya tiqildimi, suv oqyaptimi, unitaz, kran yoki dush o'rnatish kerakmi? Muammoni ayting — usta kelish vaqti hamda taxminiy ish tartibini tushuntiradi.", 'Засорилась труба или канализация, появилась протечка, нужно установить унитаз, кран или душ? Опишите проблему — мастер сообщит ориентировочное время приезда и порядок работы.'],
  ['24/7 telefon va Telegram orqali aloqa', 'Связь по телефону и в Telegram 24/7'],
  ['Ish boshlanishidan oldin kelishilgan narx', 'Цена согласуется до начала работ'],
  ['Bajarilgan ishga bir yilgacha kafolat', 'Гарантия на выполненную работу до одного года'],
  ["Xizmatlar 150 000 so'mdan boshlanadi. Yakuniy narx muammo va ish hajmiga qarab oldindan kelishiladi.", 'Услуги начинаются от 150 000 сум. Окончательная цена заранее согласуется с учётом проблемы и объёма работ.'],
  ["Uy va ofislar uchun santexnika ta'miri va o'rnatish", 'Ремонт и установка сантехники для дома и офиса'],
  ['Santexnika xizmatlari', 'Сантехнические услуги'],
  ['Urganchda qaysi santexnik ishlarini bajaramiz?', 'Какие сантехнические работы мы выполняем в Ургенче?'],
  ["Muammo sababini tekshirib, zarur ish va materiallarni tushuntiramiz. Quyidagi xizmatlar uy, kvartira va ofislar uchun ko'rsatiladi.", 'Мы определяем причину проблемы и объясняем, какие работы и материалы потребуются. Услуги оказываются в домах, квартирах и офисах.'],
  ['Quvur tiqilishini tozalash', 'Прочистка засоров труб'],
  ['Rakovina, vanna yoki oshxona quvuridagi suv sekin ketishi va tiqilish sababini bartaraf etish.', 'Устранение засоров и причин медленного слива воды в раковине, ванной или кухонной трубе.'],
  ['Suv oqishini tuzatish', 'Устранение протечек'],
  ["Kran, ulanish joyi va quvurlardagi oqishni tekshirish, nosoz qismni ta'mirlash yoki almashtirish.", 'Проверка протечек в кране, соединениях и трубах, ремонт или замена неисправной детали.'],
  ["Unitaz o'rnatish", 'Установка унитаза'],
  ["Eski unitazni almashtirish, yangi jihozni o'rnatish, suv va kanalizatsiyaga to'g'ri ulash.", 'Замена старого унитаза, установка нового оборудования и правильное подключение к воде и канализации.'],
  ['Kran, rakovina va dush', 'Кран, раковина и душ'],
  ["Yangi santexnika jihozlarini o'rnatish, ulanishlarni tekshirish va ishlashini sinab ko'rish.", 'Установка новой сантехники, проверка соединений и тестирование работы.'],
  ['Kanalizatsiya tozalash xizmati', 'Услуга прочистки канализации'],
  ['Kanalizatsiya tozalash', 'Прочистка канализации'],
  ["Uy ichidagi kanalizatsiya tiqilishi va noxush hidga olib kelayotgan muammolarni tekshirish.", 'Проверка засоров внутренней канализации и причин неприятного запаха.'],
  ['Isitish tizimi', 'Система отопления'],
  ["Qozon o'rnatish va mavjud isitish tizimidagi ulanishlarni sozlash bo'yicha yordam.", 'Помощь в установке котла и настройке подключений существующей системы отопления.'],
  ["Qachon usta chaqirish kerak?", 'Когда нужно вызвать мастера?'],
  ["Muammoni kechiktirmaslik kerak bo'lgan belgilar", 'Признаки, при которых не стоит откладывать ремонт'],
  ["Suv sizishi mebel, devor va polga zarar yetkazishi mumkin. Quvurdan g'alati tovush kelishi, bosim pasayishi, suvning sekin ketishi yoki doimiy namlik sezilsa, sababini erta tekshirtirish keyingi katta ta'mirning oldini olishga yordam beradi.", 'Протечка может повредить мебель, стены и пол. Необычный шум в трубах, снижение давления, медленный слив или постоянная сырость — повод проверить причину заранее и избежать более серьёзного ремонта.'],
  ["Favqulodda oqish bo'lsa, imkon qadar asosiy suv kranini yoping va elektr jihozlarini nam joydan uzoqlashtiring. Keyin ustaga manzil va muammo haqida aniq ma'lumot bering.", 'При аварийной протечке по возможности перекройте основной кран и уберите электроприборы от воды. Затем сообщите мастеру точный адрес и характер проблемы.'],
  ["Ustaga yozishda nimalarni yuborish kerak?", 'Что сообщить мастеру?'],
  ["Muammo qayerda va qachondan boshlanganini", 'Где и когда возникла проблема'],
  ["Imkon bo'lsa, foto yoki qisqa videoni", 'По возможности фото или короткое видео'],
  ["Urganchdagi aniq mo'ljal va aloqa raqamini", 'Точный ориентир в Ургенче и контактный номер'],
  ["Telegram orqali ma'lumot yuborish →", 'Отправить информацию в Telegram →'],
  ['Santexnik chaqirish qanday ishlaydi?', 'Как проходит вызов сантехника?'],
  ["Bog'lanasiz", 'Вы связываетесь с нами'],
  ['Telefon yoki Telegram orqali muammo va manzilni aytasiz.', 'По телефону или в Telegram сообщаете проблему и адрес.'],
  ['Usta tekshiradi', 'Мастер проводит осмотр'],
  ["Manzilga kelgach, muammo sababi va bajariladigan ish aniqlanadi.", 'После приезда мастер определяет причину проблемы и необходимые работы.'],
  ["Ish boshlanishidan oldin xizmat narxi siz bilan kelishiladi.", 'Стоимость услуги согласуется с вами до начала работ.'],
  ['Ish topshiriladi', 'Работа сдаётся'],
  ["Ta'mir yoki o'rnatish yakunlangach, natija tekshiriladi va kafolat sharti tushuntiriladi.", 'После ремонта или установки результат проверяется, а условия гарантии объясняются клиенту.'],
  ['Urganchda santexnik chaqirish haqida savollar', 'Вопросы о вызове сантехника в Ургенче'],
  ['Urganchdan tashqariga ham chiqasizmi?', 'Выезжаете ли вы за пределы Ургенча?'],
  ["Asosiy xizmat hududi Urganch shahri. Yaqin Xorazm hududlariga chiqish imkonini telefon orqali manzilni aytib aniqlashtirish mumkin.", 'Основная зона обслуживания — город Ургенч. Возможность выезда в ближайшие районы Хорезма можно уточнить по телефону, сообщив адрес.'],
  ['Urganchda santexnik kerakmi?', 'Нужен сантехник в Ургенче?'],
  ['Muammoni qisqacha ayting. Usta kelish tartibi va keyingi qadamni tushuntiradi.', 'Кратко опишите проблему. Мастер объяснит порядок выезда и дальнейшие действия.'],
  ["Urganchda santexnika jihozini o'rnatayotgan usta", 'Мастер устанавливает сантехнику в Ургенче'],
  ['Quvur tiqilishini tozalash xizmati', 'Услуга прочистки засора трубы'],
  ['Suv oqishini aniqlash va tuzatish', 'Поиск и устранение протечки'],
  ["Unitaz o'rnatish xizmati", 'Услуга установки унитаза'],
  ["Kran, rakovina va dush o'rnatish", 'Установка крана, раковины и душа'],
  ["Isitish tizimi va qozon o'rnatish", 'Установка системы отопления и котла'],
  ['Urganchda santexnik', 'Сантехник в Ургенче'],
  ['Santexnik', 'Сантехник']
];

const electricianReplacements = [
  ['Elektrik Urganch — 24/7 Usta Chaqirish | Usta24', 'Электрик в Ургенче — вызов мастера 24/7 | Usta24'],
  ["Urganchda elektrik chaqiring: rozetka, avtomat, hisoblagich, qandil va yoritish tizimini o'rnatish yoki almashtirish. 24/7 aloqa, kelishilgan narx va kafolat.", 'Вызов электрика в Ургенче: установка и замена розеток, автоматов, счётчиков, люстр и освещения. Связь 24/7, согласованная цена и гарантия.'],
  ['Elektrik Urganch — 24/7 Usta Chaqirish', 'Электрик в Ургенче — вызов мастера 24/7'],
  ["Urganchda rozetka, avtomat, hisoblagich, qandil va yoritish tizimi bo'yicha 24/7 elektrik yordami.", 'Круглосуточная помощь электрика в Ургенче с розетками, автоматами, счётчиками, люстрами и освещением.'],
  ['Elektrik Urganch — Usta24', 'Электрик в Ургенче — Usta24'],
  ["Urganchda 24/7 elektrik chaqirish, oldindan kelishilgan narx va bajarilgan ishga kafolat.", 'Вызов электрика в Ургенче 24/7, заранее согласованная цена и гарантия на выполненную работу.'],
  ['Usta24 — Urganchda elektrik xizmati', 'Usta24 — услуги электрика в Ургенче'],
  ['Elektrik Urganch — 24/7 usta chaqirish', 'Электрик в Ургенче — вызов мастера 24/7'],
  ["Urganchda rozetka, avtomat, hisoblagich, qandil va yoritish tizimi bo'yicha elektrik xizmatlari.", 'Услуги электрика в Ургенче: розетки, автоматы, счётчики, люстры и системы освещения.'],
  ['Elektrik Urganch', 'Электрик в Ургенче'],
  ['Urganchda elektrik xizmati', 'Услуги электрика в Ургенче'],
  ["Elektr jihozlarini o'rnatish va almashtirish", 'Установка и замена электрооборудования'],
  ['Elektrik xizmatlari', 'Услуги электрика'],
  ["Rozetka o'rnatish va almashtirish", 'Установка и замена розеток'],
  ['Avtomat almashtirish', 'Замена автомата'],
  ["Qandil va chiroq o'rnatish", 'Установка люстр и светильников'],
  ["Elektr hisoblagichini ulash va almashtirish", 'Подключение и замена электросчётчика'],
  ['Urganchda elektrik chaqirish narxi qancha?', 'Сколько стоит вызов электрика в Ургенче?'],
  ["Ko'rsatilgan elektrik xizmatlari 100 000 so'mdan boshlanadi. Yakuniy narx nosozlik, ish hajmi va kerakli materiallar aniqlangach, ish boshlanishidan oldin kelishiladi.", 'Стоимость указанных услуг электрика начинается от 100 000 сум. Окончательная цена согласуется до начала работ после определения неисправности, объёма и необходимых материалов.'],
  ['Elektrik qancha vaqtda yetib boradi?', 'Как быстро приедет электрик?'],
  ["Usta24 90 foiz holatda Urganchdagi manzilga 30 daqiqa ichida yetib borishga harakat qiladi. Aniq vaqt usta joylashuvi va manzilga bog'liq.", 'В 90 процентах случаев Usta24 старается прибыть по адресу в Ургенче в течение 30 минут. Точное время зависит от местоположения мастера и адреса.'],
  ['Elektrikni kechasi ham chaqirish mumkinmi?', 'Можно ли вызвать электрика ночью?'],
  ["Ha, Usta24 bilan elektr nosozligi va o'rnatish ishlari bo'yicha 24/7 bog'lanish mumkin.", 'Да, по вопросам электрических неисправностей и установки с Usta24 можно связаться круглосуточно.'],
  ['Bajarilgan elektrik ishiga kafolat bormi?', 'Есть ли гарантия на работы электрика?'],
  ["Ha, bajarilgan ishga bir yilgacha kafolat beriladi. Kafolat shartlari bajarilgan ish turiga qarab tushuntiriladi.", 'Да, на выполненную работу предоставляется гарантия до одного года. Условия гарантии объясняются в зависимости от вида работ.'],
  ['Elektrik Urganch — 24/7 tezkor yordam', 'Электрик в Ургенче — срочная помощь 24/7'],
  ["Rozetka ishlamayaptimi, avtomat tez-tez o'chadimi, qandil, chiroq yoki hisoblagichni ulash kerakmi? Muammoni ayting — elektrik kelish vaqti va bajariladigan ish tartibini tushuntiradi.", 'Не работает розетка, часто отключается автомат, нужно подключить люстру, светильник или счётчик? Опишите проблему — электрик сообщит ориентировочное время приезда и порядок работ.'],
  ['24/7 telefon va Telegram orqali aloqa', 'Связь по телефону и в Telegram 24/7'],
  ['Ish boshlanishidan oldin kelishilgan narx', 'Цена согласуется до начала работ'],
  ['Bajarilgan ishga bir yilgacha kafolat', 'Гарантия на выполненную работу до одного года'],
  ["Xizmatlar 100 000 so'mdan boshlanadi. Yakuniy narx nosozlik, ish hajmi va materialga qarab oldindan kelishiladi.", 'Услуги начинаются от 100 000 сум. Окончательная цена заранее согласуется с учётом неисправности, объёма работ и материалов.'],
  ["Uy va ofislar uchun elektr jihozlarini o'rnatish va almashtirish", 'Установка и замена электрооборудования для дома и офиса'],
  ['Urganchda qaysi elektrik ishlarini bajaramiz?', 'Какие электромонтажные работы мы выполняем в Ургенче?'],
  ["Nosozlikni tekshirib, xavfsiz yechim, zarur ish va materiallarni tushuntiramiz. Quyidagi xizmatlar uy, kvartira va ofislar uchun ko'rsatiladi.", 'Мы проверяем неисправность и объясняем безопасное решение, необходимые работы и материалы. Услуги оказываются в домах, квартирах и офисах.'],
  ['Rozetka va kalitlar', 'Розетки и выключатели'],
  ["Eski yoki qizib ketayotgan rozetka va kalitlarni tekshirish, almashtirish va yangi nuqta o'rnatish.", 'Проверка и замена старых или нагревающихся розеток и выключателей, установка новых точек.'],
  ["Avtomatni almashtirish", 'Замена автомата'],
  ["Tez-tez o'chayotgan yoki nosoz himoya avtomatini tekshirish va mos qurilmaga almashtirish.", 'Проверка часто отключающегося или неисправного защитного автомата и замена на подходящее устройство.'],
  ["Qandil o'rnatish", 'Установка люстры'],
  ["Qandilni yig'ish, mustahkam o'rnatish, elektr tarmog'iga ulash va ishlashini tekshirish.", 'Сборка люстры, надёжный монтаж, подключение к электросети и проверка работы.'],
  ['Chiroq va yoritish', 'Светильники и освещение'],
  ["Devor yoki shift chiroqlarini o'rnatish, ulash va mavjud yoritish nuqtalarini sozlash.", 'Установка и подключение настенных или потолочных светильников, настройка существующих точек освещения.'],
  ['Hisoblagichni ulash', 'Подключение счётчика'],
  ["Elektr hisoblagichi ulanishini tekshirish, almashtirish va ishga tushirish bo'yicha yordam.", 'Проверка подключения электросчётчика, помощь в замене и запуске.'],
  ["Demontaj va qayta o'rnatish", 'Демонтаж и повторная установка'],
  ["Eski qandil yoki chiroqni ehtiyotkorlik bilan yechish va yangi joyga qayta o'rnatish.", 'Аккуратный демонтаж старой люстры или светильника и повторная установка на новом месте.'],
  ['Elektr xavfsizligi', 'Электробезопасность'],
  ["Nosozlikni kechiktirmaslik kerak bo'lgan belgilar", 'Признаки, при которых нельзя откладывать ремонт'],
  ["Rozetka yoki simdan kuygan hid kelishi, uchqun chiqishi, rozetkaning qizishi, chiroqlarning sababsiz lipillashi yoki avtomatning qayta-qayta o'chishi xavfsizlik muammosidan darak berishi mumkin.", 'Запах гари от розетки или провода, искры, нагрев розетки, беспричинное мерцание света или повторное отключение автомата могут указывать на проблему безопасности.'],
  ["Bunday holatda nosoz jihozdan foydalanmang. Agar xavfsiz va qanday qilishni bilsangiz, tegishli liniya yoki asosiy avtomatni o'chiring. Ochiq simlarga tegmang va tekshiruvni elektrikka topshiring.", 'В таком случае не пользуйтесь неисправным оборудованием. Если это безопасно и вы знаете как, отключите соответствующую линию или главный автомат. Не прикасайтесь к открытым проводам и поручите проверку электрику.'],
  ['Elektrikka yozishda nimalarni yuborish kerak?', 'Что сообщить электрику?'],
  ['Qaysi jihoz yoki xonada muammo borligini', 'В каком приборе или помещении возникла проблема'],
  ["Avtomat o'chishi, hid yoki uchqun kabi belgilarni", 'Такие признаки, как отключение автомата, запах или искры'],
  ["Urganchdagi aniq mo'ljal va aloqa raqamini", 'Точный ориентир в Ургенче и контактный номер'],
  ['Telegram orqali ma\'lumot yuborish →', 'Отправить информацию в Telegram →'],
  ['Elektrik chaqirish qanday ishlaydi?', 'Как проходит вызов электрика?'],
  ["Bog'lanasiz", 'Вы связываетесь с нами'],
  ['Telefon yoki Telegram orqali nosozlik belgilari va manzilni aytasiz.', 'По телефону или в Telegram сообщаете признаки неисправности и адрес.'],
  ['Elektrik tekshiradi', 'Электрик проводит проверку'],
  ["Manzilga kelgach, muammo manbai va xavfsiz bajariladigan ish aniqlanadi.", 'После приезда определяется источник проблемы и безопасный порядок работ.'],
  ["Ish boshlanishidan oldin xizmat va kerakli materiallar narxi siz bilan kelishiladi.", 'Стоимость услуги и необходимых материалов согласуется с вами до начала работ.'],
  ["Natija sinovdan o'tadi", 'Результат проверяется'],
  ["O'rnatish yoki almashtirishdan so'ng jihoz ishlashi tekshiriladi va kafolat sharti tushuntiriladi.", 'После установки или замены работа оборудования проверяется, а условия гарантии объясняются клиенту.'],
  ['Urganchda elektrik chaqirish haqida savollar', 'Вопросы о вызове электрика в Ургенче'],
  ['Urganchdan tashqariga ham chiqasizmi?', 'Выезжаете ли вы за пределы Ургенча?'],
  ["Asosiy xizmat hududi Urganch shahri. Yaqin Xorazm hududlariga chiqish imkonini telefon orqali manzilni aytib aniqlashtirish mumkin.", 'Основная зона обслуживания — город Ургенч. Возможность выезда в ближайшие районы Хорезма можно уточнить по телефону, сообщив адрес.'],
  ['Urganchda elektrik kerakmi?', 'Нужен электрик в Ургенче?'],
  ['Nosozlikni qisqacha ayting. Elektrik kelish tartibi va keyingi qadamni tushuntiradi.', 'Кратко опишите неисправность. Электрик объяснит порядок выезда и дальнейшие действия.'],
  ["Urganchda qandil o'rnatayotgan elektrik", 'Электрик устанавливает люстру в Ургенче'],
  ["Rozetka o'rnatish va almashtirish", 'Установка и замена розетки'],
  ["Elektr avtomatini almashtirish", 'Замена электрического автомата'],
  ["Qandilni o'rnatish va ulash", 'Установка и подключение люстры'],
  ["Chiroq va yoritish tizimini o'rnatish", 'Установка светильника и системы освещения'],
  ["Elektr hisoblagichini almashtirish", 'Замена электросчётчика'],
  ["Qandilni demontaj qilish", 'Демонтаж люстры'],
  ['Urganchda elektrik', 'Электрик в Ургенче'],
  ['Elektrik', 'Электрик']
];

function buildRussianService(sourcePath, outputPath, sourceCanonical, russianCanonical, replacements, activeType) {
  let html = read(sourcePath);
  html = replaceAllExact(html, [
    [sourceCanonical, russianCanonical],
    ...replacements,
    ...sharedServiceReplacements
  ]);
  html = html.replace('<meta property="og:locale" content="uz_UZ">', '<meta property="og:locale" content="ru_RU">\n    <meta property="og:locale:alternate" content="uz_UZ">');
  html = html.split('href="/"').join('href="/ru/"');
  html = html.split('href="/santexnik-urganch/"').join('href="/ru/santehnik-urgench/"');
  html = html.split('href="/elektrik-urganch/"').join('href="/ru/elektrik-urgench/"');
  html = html.split('https://usta24uz.netlify.app/#website').join('https://usta24uz.netlify.app/#website');
  html = html.split('https://usta24uz.netlify.app/#business').join('https://usta24uz.netlify.app/#business');
  html = html.replace(
    /<a class="lang-btn active" href="[^"]+" lang="uz" hreflang="uz" aria-current="page">UZ<\/a>\s*<a class="lang-btn" href="([^"]+)" lang="ru" hreflang="ru">RU<\/a>/,
    `<a class="lang-btn" href="${sourceCanonical.replace(baseUrl, '')}" lang="uz" hreflang="uz">UZ</a>\n                    <a class="lang-btn active" href="$1" lang="ru" hreflang="ru" aria-current="page">RU</a>`
  );
  html = html
    .replace(`<link rel="alternate" hreflang="uz" href="${russianCanonical}">`, `<link rel="alternate" hreflang="uz" href="${sourceCanonical}">`)
    .replace(`<link rel="alternate" hreflang="x-default" href="${russianCanonical}">`, `<link rel="alternate" hreflang="x-default" href="${sourceCanonical}">`);
  html = html.replace(
    /<script type="application\/ld\+json">([\s\S]*?)<\/script>/,
    (match, rawJson) => {
      const data = JSON.parse(rawJson);
      for (const item of data['@graph']) {
        if (item['@type'] === 'WebPage') item.inLanguage = 'ru';
        if (item['@type'] === 'BreadcrumbList') item.itemListElement[0].item = `${baseUrl}/ru/`;
      }
      return `    <script type="application/ld+json">\n${JSON.stringify(data, null, 8)}\n    </script>`;
    }
  );
  html = html.replace(`href="/ru/${activeType}/" aria-current="page"`, `href="/ru/${activeType}/" aria-current="page"`);
  write(outputPath, html);
}

buildRussianHome();
buildRussianService(
  'santexnik-urganch/index.html',
  'ru/santehnik-urgench/index.html',
  `${baseUrl}/santexnik-urganch/`,
  `${baseUrl}/ru/santehnik-urgench/`,
  plumberReplacements,
  'santehnik-urgench'
);
buildRussianService(
  'elektrik-urganch/index.html',
  'ru/elektrik-urgench/index.html',
  `${baseUrl}/elektrik-urganch/`,
  `${baseUrl}/ru/elektrik-urgench/`,
  electricianReplacements,
  'elektrik-urgench'
);

console.log('Built Russian pages: /ru/, /ru/santehnik-urgench/, /ru/elektrik-urgench/');
