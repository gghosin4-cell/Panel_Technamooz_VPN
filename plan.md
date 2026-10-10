# طرح بازطراحی کامل Panel Technamooz — نسخه 2

## هدف

ساخت یک پنل مستقل، پایدار و آمادهٔ Railway با حفظ قابلیت‌های اصلی نسخهٔ فعلی، بازطراحی کامل تجربهٔ کاربری، ارتقای هسته و API، لایهٔ دادهٔ مقاوم‌تر و امنیت بالاتر برای مسیر ورود.

## نیازمندی‌های قطعی

- بازطراحی کامل قالب پنل و صفحهٔ ورود با هویت بصری مشکی/قرمز Technamooz.
- حفظ و ارتقای ساخت کانفیگ‌های VLESS، Trojan و XHTTP.
- حفظ خروجی VLESS URI، Clash/Mihomo YAML، Sing-box JSON و صفحات اشتراک.
- حفظ مدیریت گروه‌های اشتراک، محدودیت حجم/سرعت/IP، انقضا، تمدید و Reset مصرف.
- حفظ Telegram Bot به‌صورت اختیاری و کنترل‌شده.
- آماده‌سازی برای Railway با `PORT`، Volume روی `/data`، health-check و متغیرهای secrets.
- مسیر ورود عمومی نباید `/admin` یا مسیر قابل حدس باشد؛ مسیر خصوصی از متغیر `ADMIN_PATH_SECRET` یا مقدار تصادفی امن ساخته می‌شود و مسیرهای عمومی رایج پاسخ 404 می‌گیرند.
- ارتقای احراز هویت: رمز PBKDF2، session امن، rate limit ورود، CSRF برای عملیات cookie-based و عدم لو رفتن secrets.
- حفظ سازگاری state نسخهٔ قبلی و امکان migration به ساختار جدید بدون حذف اطلاعات.

## تصمیم معماری

- Backend: FastAPI با ساختار ماژولار به‌جای تمرکز تمام منطق در یک فایل.
- Core: مدل‌های دامنه و سرویس‌های خالص برای لینک، گروه، quota، اشتراک، احراز هویت و migration.
- API: routerهای جدا برای auth، links، subscriptions، settings، backup و health؛ پاسخ‌های یکنواخت و validation مشخص.
- Data: لایهٔ repository با فایل state اتمیک در v2 و schema version؛ طراحی آماده برای مهاجرت به SQLite/PostgreSQL در مرحلهٔ بعد. برای سازگاری با Railway، Volume روی `/data` مرجع است.
- Frontend: HTML/CSS/JS مستقل با RTL/LTR، responsive layout، sidebar، command/search bar، کارت‌های وضعیت، جدول کانفیگ، drawer/modal و toastهای استاندارد. بدون وابستگی CDN برای اجرای پایدار.
- Assets: لوگوی inline SVG و tokens مرکزی CSS؛ فایل‌های asset از `/static` سرو می‌شوند.
- Deployment: `Procfile`، `railway.json`، health endpoint و startup guardهای production.

## طراحی محصول

- **Design Movement:** Dark Industrial Control Room با رگه‌های cyberpunk کنترل‌شده، نه neon شلوغ.
- **Core Principles:** خوانایی عملیاتی، کنتراست قوی، سلسله‌مراتب روشن، بازخورد فوری.
- **Color Philosophy:** مشکی زغالی برای تمرکز و عمق؛ قرمز Technamooz برای اقدام، هشدار و identity؛ خاکستری گرم برای سطوح ثانویه.
- **Layout Paradigm:** shell دو ناحیه‌ای با sidebar ثابت، workspace سیال و پنل جزئیات کشویی؛ موبایل با bottom navigation.
- **Signature Elements:** خط قرمز status، کارت‌های metric با نوار سلامت، لوگوی T هندسی و chipهای protocol.
- **Interaction:** عملیات حساس با confirmation، عملیات سریع با keyboard shortcut، خطاها inline و قابل اصلاح.
- **Animation:** فقط transitionهای 150–220ms، pulse محدود برای وضعیت live، بدون حرکت تزئینی سنگین.
- **Typography:** سیستم فونت محلی/سیستمی با خوانایی فارسی؛ وزن 700 برای عنوان، 500 برای label، 400 برای متن.
- **Brand Essence:** اتاق کنترل امن و سریع برای مدیریت کانفیگ‌های Technamooz؛ دقیق، قدرتمند، قابل اعتماد.
- **Brand Voice:** کوتاه، عملیاتی و مطمئن؛ نمونه: «کانفیگ آمادهٔ انتشار است.» و «دسترسی این نشست منقضی شد؛ دوباره وارد شوید.»
- **Signature Brand Color:** `#E11D48` با accent قرمز روشن `#FB2C36`.

## ساختار پیشنهادی

```text
app/
  main.py
  config.py
  core/
    security.py
    errors.py
    models.py
    state.py
    migration.py
  repositories/
    state_repository.py
  services/
    links.py
    subscriptions.py
    exports.py
    telegram.py
  api/
    auth.py
    links.py
    subscriptions.py
    settings.py
    system.py
  web/
    routes.py
    templates/
    static/
      css/
      js/
      assets/
  relays/
    vless.py
    xhttp.py
    speed_limit.py
scripts/
  migrate_state.py
requirements.txt
Procfile
railway.json
README.md
SECURITY.md
```

## برنامهٔ اجرا

1. استخراج و ممیزی نسخهٔ فعلی و قراردادهای API.
2. ساخت shell جدید و صفحهٔ ورود با مسیر خصوصی تصادفی و fallback امن.
3. جداکردن مدل‌های دامنه و repository بدون شکستن state قبلی.
4. پیاده‌سازی routerهای API و validation یکنواخت.
5. پیاده‌سازی dashboard جدید و اتصال کامل به API.
6. تکمیل migration و backup/restore نسخه‌دار.
7. بازبینی relayها و اعمال guardهای resource/SSRF.
8. تست static، unit، API، migration، خروجی‌ها، frontend syntax و Railway runtime.
9. تولید ZIP نسخهٔ Stable و گزارش تغییرات.

## فرض‌های اجرایی

- قابلیت‌های پروتکل فعلی حفظ می‌شوند و redesign به معنای حذف relayها نیست.
- برای جلوگیری از شکستن نصب موجود، مسیر پیش‌فرض ورود از `ADMIN_PATH_SECRET` ساخته می‌شود؛ اگر تنظیم نشده باشد، برنامه در production مسیر تصادفی را فقط در log اولیه ثبت می‌کند و endpoint `/login` عمومی نیست.
- state فعلی قبل از migration هرگز overwrite نمی‌شود؛ فایل backup قبل از تبدیل ساخته می‌شود.
- استفادهٔ production از relay باید با قوانین سرویس میزبان سازگار باشد.
