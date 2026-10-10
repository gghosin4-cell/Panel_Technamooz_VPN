# گزارش بازطراحی Panel Technamooz v2

## تغییرات اصلی

- رابط Login و Dashboard از پایه بازنویسی و با تم Dark Industrial Control Room مشکی/قرمز طراحی شد.
- مسیر مدیریت دیگر `/login` یا `/admin` نیست؛ از `ADMIN_PATH_SECRET` و HMAC مسیر پایدار `/control/<derived-token>` ساخته می‌شود.
- URL مدیریت در startup log ثبت می‌شود تا پس از Deploy قابل دریافت باشد.
- redirect ریشه به مسیر خصوصی جدید منتقل شد و مسیرهای قدیمی پاسخ 404 می‌دهند.
- نسخهٔ هسته به `2.0.0.0` ارتقا یافت.
- مدل ذخیره‌سازی دارای `schema_version=2` شد؛ state نسخهٔ قبلی بدون حذف داده بارگذاری می‌شود.
- cookie نشست در دامنهٔ عمومی Railway با `Secure` ساخته می‌شود.
- Dashboard جدید بخش‌های overview، کانفیگ‌ها، گروه‌های اشتراک، اتصال‌های زنده، تنظیمات حساب، Backup و Telegram را دارد.
- APIهای قبلی حفظ شدند تا لینک‌ها، subscriptionها و relayهای موجود از کار نیفتند.
- صفحهٔ public subscription نیز با قالب جدید و پشتیبانی از رمز اشتراک بازطراحی شد.
- صفحهٔ قدیمی برای reference در `legacy/pages_v1.py` نگهداری می‌شود و در runtime import نمی‌شود.

## تست‌های موفق

- `compileall` و `py_compile` تمام فایل‌ها
- `ruff check --select E9,F`: بدون خطا
- render و `node --check` برای Login و Dashboard جدید
- login با CAPTCHA روی مسیر مشتق‌شده
- 404 بودن `/login` و `/admin`
- dashboard خصوصی بعد از session
- ساخت گروه و کانفیگ با API
- دریافت `/api/links` و `/api/subs`
- status و enable/disable ربات Telegram
- Backup بدون token
- سازگاری state قدیمی و تولید schema version 2
- اجرای واقعی Uvicorn با `PORT` تزریق‌شده Railway
- `/health` در production: HTTP 200

## متغیرهای ضروری Railway

```text
ADMIN_USERNAME=Amirparsa
ADMIN_PASSWORD=<رمز قوی و یکتا>
SECRET_KEY=<secret ثابت و تصادفی>
ADMIN_PATH_SECRET=<کلید ثابت و محرمانه برای مسیر مدیریت>
DATA_DIR=/data
```

پس از Deploy، مسیر واقعی ورود در log سرویس با قالب زیر چاپ می‌شود:

```text
Technamooz Control Plane admin URL: /control/<derived-token>
```

> اگر `SECRET_KEY` یا `ADMIN_PATH_SECRET` را تغییر دهید، مسیر مدیریت نیز تغییر می‌کند. این دو مقدار را در Railway ثابت نگه دارید.
