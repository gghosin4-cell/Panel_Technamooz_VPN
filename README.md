# Panel Technamooz `v2.0.0` <span style="color:#10b981;font-weight:bold;font-size:0.7em;">STABLE</span>

> پنل فوق‌حرفه‌ای و یکپارچه ساخت، توزیع و مدیریت کانفیگ‌های ابری VPN بر پایهٔ پایتون و FastAPI  
> توسعه‌یافته توسط **تیم Technamooz** با مدیریت **amirparsa**  
> نسخه: `technamooz-version-2.0.0 stable`

---

## 🌟 معرفی پروژه (Overview)
**Panel Technamooz** یک control plane مدرن، پرسرعت و کم‌مصرف برای ساخت و کنترل ترافیک کانفیگ‌های امن است که با **Python/FastAPI** توسعه داده شده و برای استقرار پایدار روی **Railway** آماده است. نسخهٔ ۲ علاوه بر بازطراحی کامل پنل و صفحهٔ ورود، قراردادهای دادهٔ قبلی را می‌خواند و APIهای موجود را حفظ می‌کند.

---

## 🚀 قابلیت‌های کلیدی نسخه Ultra 3.0 Stable

### 🛡️ پروتکل‌های پشتیبانی‌شده
- **VLESS WebSocket (WS)** با پشتیبانی از TLS / Reality
- **Trojan WebSocket (WS)** با احراز هویت SHA-224 و بازپخش مستقیم به هسته
- **XHTTP Packet-Up** (فناوری عبور از شدیدترین محدودیت‌ها)
- **XHTTP Stream-Up** با مدیریت بهینه جریان داده و مالتی‌پلکسینگ

### 📡 فرمت‌های اشتراک نوین و هوشمند
- **Clash Meta / Mihomo (YAML)**: خروجی کامل و استاندارد پروکسی با Ruleها و تنظیمات DNS
- **Sing-box (JSON)**: سازگار با نسخه 1.8+ برای کلاینت‌های Android، iOS، Windows و Linux
- **V2Ray / Xray URI**: لینک‌های استاندارد سازگار با v2rayNG, Streisand, FoXray, Nekobox, Shadowrocket
- **صفحات سابسکریپشن وب**: پنل عمومی زیبا برای هر مشترک با QR Code و نمایش حجم/انقضا

### 🎯 مسیریابی با آی‌پی تمیز (Clean IP / CDN Domain)
- پشتیبانی مستقیم از درج Clean IP مخصوص اپراتورهای ایرانسل، همراه‌اول، رایتل و مخابرات
- امکان تعیین دامنه CDN مجزا برای Host و SNI به منظور دور زدن مسدودسازی‌های SNI-based

### 🎨 رابط کاربری گلاسمورفیسم نوین (Glassmorphism UI/UX)
- **دو زبانه کامل**: انگلیسی (پیش‌فرض) و فارسی با سوئیچ آنی بدون رفرش
- **دو تم رنگی اختصاصی**:
  - **تم تاریک (Dark Mode)**: مشکی متالیک و قرمز آتشین (`#07070a` + `#ef233c`)
  - **تم روشن (Light Mode)**: سفید ابریشمی، بنفش نئونی و قرمز (`#f8fafc` + `#7209b7` + `#ef233c`)
- **لوگوی اختصاصی Technamooz**: تعبیه‌شده به‌صورت وکتور و پایدار در تمام صفحات
- **ویترین شبکه‌های اجتماعی تکناموز**: دسترسی ۱-کلیک به یوتیوب، تلگرام، اینستاگرام، توییتر، گیت‌هاب، وبسایت رسمی و پشتیبانی
- **Control plane جدید v2**: داشبورد عملیاتی، inventory کانفیگ‌ها، subscription groups، activity stream، live connections، security و Telegram در یک پوستهٔ یکپارچه
- **ورودی مدیریت خصوصی**: مسیر `/login` در production عمومی نیست؛ مسیر مدیریت از `SECRET_KEY` به‌صورت پایدار مشتق می‌شود یا با `ADMIN_PANEL_PATH` تعیین می‌گردد.

### ⚙️ امنیت و کنترل ترافیک سازمانی
- **محدودیت تعداد کاربر همزمان (IP Limiter)**: جلوگیری از اشتراک‌گذاری اکانت‌ها با TTL دقیق
- **محدودکننده نرخ سرعت (Token Bucket Limiter)**: اعمال سقف پهنای باند بر حسب مگابیت (Mbps)
- **تمدید ۱-کلیک (+۳۰ روز)** و **ریست ترافیک مصرفی**
- **ورود دو مرحله‌ای با کد امنیتی (CAPTCHA)** جهت محافظت در برابر حملات Brute-Force
- **امکان تغییر نام کاربری و رمز عبور** از درون پنل و اعمال لحظه‌ای در هش امنیتی PBKDF2

### 🤖 ربات تلگرام پیشرفته Technamooz
- نظارت لحظه‌ای بر سلامت سرور، مصرف پردازنده، رم و ترافیک (`/status`)
- ساخت و صدور سریع کانفیگ‌های VLESS و Trojan
- ارسال لینک‌های مستقیم اشتراک Clash و Sing-box به کاربران
- دستورات تمدید و ریست اکانت برای ادمین

---

## 🔑 دسترسی مدیر و مسیر خصوصی

- **نام کاربری**: `Amirparsa`
- **رمز عبور توسعه محلی**: `Technamooz` (در production حتماً مقدار امن تنظیم کنید)
- **کد امنیتی (کپچا)**: کد تصادفی ۵ رقمی نمایش داده‌شده در صفحه
- **مسیر پنل**: مقدار `ADMIN_PANEL_PATH` را به یک segment تصادفی و طولانی تنظیم کنید؛ اگر تنظیم نشود از `SECRET_KEY` مسیر پایدار `/pnl-...` ساخته می‌شود.

*(پس از اولین ورود می‌توانید از منوی تنظیمات یا آیکون پروفایل، نام کاربری و رمز عبور را به دلخواه خود تغییر دهید)*

---

## ☁️ راهنمای استقرار روی Railway (Deployment Guide)

این پروژه دارای فایل‌های `railway.json` و `Procfile` است و برای اجرای مستقیم روی Railway طراحی شده است. `railway.json` از schema رسمی Railway استفاده می‌کند و `startCommand` را صریحاً روی اجرای Uvicorn تنظیم می‌کند تا تشخیص خودکار builder/start command باعث خطا نشود.

### مراحل نصب:
1. مخزن گیت‌هاب پروژه را در حساب Railway خود **Import** کنید:
   ```
   https://github.com/technamooz/Panel_Technamooz_VPN
   ```
2. در تنظیمات سرویس Railway، یک **Volume** ایجاد کرده و مسیر Mount آن را برابر با `/data` قرار دهید (جهت ذخیره دائمی دیتابیس کانفیگ‌ها و ساب‌ها).
3. متغیرهای محیطی اختیاری (Environment Variables):
   - `ADMIN_USERNAME`: نام کاربری ادمین (پیش‌فرض: `Amirparsa`)
   - `ADMIN_PASSWORD`: رمز عبور ادمین (در محیط production الزامی و بدون مقدار پیش‌فرض امن)
   - `DATA_DIR`: مسیر ذخیره داده‌ها (پیش‌فرض: `/data` در Railway و `./data` در محیط محلی)
   - `TELEGRAM_BOT_TOKEN`: توکن ربات تلگرام (اختیاری)
   - `TELEGRAM_ADMIN_IDS`: شناسه‌های عددی تلگرام ادمین‌ها با کاما (اختیاری)
   - `ADMIN_PANEL_PATH`: مسیر اختصاصی پنل بدون `/` ابتدایی، ترجیحاً یک مقدار تصادفی ۳۲ تا ۶۴ کاراکتری
   - `ALLOW_LEGACY_LOGIN_PATH`: فقط برای local development مقدار `true`؛ در production باید `false` بماند
4. پلتفرم Railway به صورت خودکار متغیر `PORT` را تزریق کرده و سرویس از طریق دستور زیر راه‌اندازی می‌شود:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
5. هلث‌چک پروژه روی آدرس `/health` به صورت فعال نظارت می‌کند.

> در صورت استفاده از Deploy from GitHub، فایل `railway.json` باید در root repository باشد؛ نیازی به تنظیم دستی Start Command نیست. `Procfile` نیز به‌عنوان fallback باقی مانده است.

### سازگاری داده و API در نسخهٔ ۲

- فایل state قبلی `technamooz_state.json` بدون حذف قابلیت‌های قبلی بارگذاری می‌شود.
- کل APIهای `/api/*`، مسیرهای subscription، WebSocket و XHTTP حفظ شده‌اند.
- hash رمز گروه‌ها و token ربات در backup جدید export نمی‌شوند؛ restore بکاپ‌های قدیمی همچنان آن‌ها را نادیده می‌گیرد.
- برای جلوگیری از قطع session پشت reverse proxy، cookie در Railway با `Secure`, `HttpOnly` و `SameSite=Lax` صادر می‌شود.

### الزامات امنیتی نسخهٔ hardened

- در محیط Railway، متغیر `ADMIN_PASSWORD` اجباری است و برنامه بدون آن اجرا نمی‌شود. تشخیص محیط با متغیرهای Railway مانند `RAILWAY_ENVIRONMENT_NAME` انجام می‌شود؛ رمز توسعهٔ `Technamooz` فقط برای اجرای محلی است.
- برای تولید URL صحیح، `RAILWAY_PUBLIC_DOMAIN` یا `ALLOWED_PUBLIC_HOSTS` را تنظیم کنید. مقدار `TRUST_PROXY_HEADERS` فقط زمانی فعال شود که برنامه پشت reverse proxy مورد اعتماد است.
- CORS به‌صورت پیش‌فرض غیرفعال است؛ در صورت نیاز، originهای دقیق را در `CORS_ORIGINS` با کاما جدا کنید و از wildcard استفاده نکنید.
- relay به مقصدهای private/loopback/link-local متصل نمی‌شود. فقط در شبکهٔ کاملاً کنترل‌شده و با آگاهی از ریسک، `ALLOW_PRIVATE_TARGETS=true` را فعال کنید.

---

## 💻 راه‌اندازی محلی (Local Development)

```bash
# کلون پروژه
git clone https://github.com/technamooz/Panel_Technamooz_VPN.git
cd Panel_Technamooz_VPN

# ساخت و فعال‌سازی محیط مجازی
python3 -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate

# نصب پیش‌نیازها
pip install -r requirements.txt

# اجرای سرور
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

سپس مرورگر خود را باز کرده و به آدرس زیر مراجعه نمایید:
```
http://localhost:8000/login
```

---

## 🌐 شبکه‌های اجتماعی و جامعه کاربری Technamooz

- 📺 **YouTube**: [@technamooz](https://youtube.com/@technamooz)
- 📢 **Telegram Channel**: [@technamooz](https://t.me/technamooz)
- 📸 **Instagram**: [@technamooz](https://instagram.com/technamooz)
- 🐦 **Twitter / X**: [@technamooz](https://twitter.com/technamooz)
- 🐙 **GitHub**: [github.com/technamooz](https://github.com/technamooz)
- 🌍 **Official Website**: [technamooz.ir](https://technamooz.ir)
- 💬 **Telegram Support**: [@technamooz_support](https://t.me/technamooz_support)

---

## 📄 لایسنس و حقوق نشر
این پروژه تحت لایسنس MIT منتشر شده است.  
توسعه‌یافته با افتخار توسط **تیم Technamooz** با مدیریت **amirparsa**.
