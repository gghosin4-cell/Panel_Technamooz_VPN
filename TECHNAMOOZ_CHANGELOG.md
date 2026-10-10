# Panel Technamooz v2.0.0.0 Control Plane

نسخهٔ بازطراحی‌شدهٔ Technamooz با shell عملیاتی جدید، تم مشکی/قرمز، مسیر مدیریت خصوصی مشتق‌شده، احراز هویت سخت‌شده، Dashboard responsive، مدیریت Telegram، migration سازگار state و تنظیمات Railway آماده شد.

## v2.0.0.0

- صفحه ورود و Dashboard از پایه بازطراحی شدند.
- مسیر `/login` و `/admin` حذف و مسیر `/control/<derived-token>` جایگزین شد.
- `ADMIN_PATH_SECRET` برای ثابت و خصوصی‌بودن URL مدیریت اضافه شد.
- session cookie در استقرار عمومی با `Secure` تنظیم می‌شود.
- state دارای `schema_version=2` شد و state نسخه قبلی بدون حذف داده load می‌شود.
- قرارداد وضعیت Telegram با Frontend کامل و lifecycle فعال/غیرفعال‌سازی اصلاح شد.
- نسخه برنامه به `2.0.0.0` ارتقا یافت.
