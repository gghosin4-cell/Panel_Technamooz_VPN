# Panel Technamooz v2.0.0 Stable

نسخهٔ دوم stable با control plane کاملاً جدید، صفحهٔ ورود خصوصی، layout واکنش‌گرا، inventory کانفیگ‌ها، subscription groups، activity stream، live connections، security center و Telegram center آماده شد.

- قرارداد APIها، state JSON، لینک‌های subscription و transportهای VLESS/Trojan/XHTTP حفظ شده‌اند.
- مسیر عمومی قابل‌حدس `/login` در production غیرفعال شد و مسیر مدیریت اختصاصی با HMAC/`ADMIN_PANEL_PATH` ارائه می‌شود.
- خطای runtime در parser ورودی XHTTP اصلاح شد.
- backup از export کردن hash رمز گروه و token ربات جلوگیری می‌کند.
