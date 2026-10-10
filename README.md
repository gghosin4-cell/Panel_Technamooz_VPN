# Panel Technamooz v2 — Secure Control Plane

پنل بازطراحی‌شدهٔ ساخت و مدیریت کانفیگ با هستهٔ FastAPI، رابط کنترل عملیاتی مشکی/قرمز، مسیر مدیریت خصوصی و استقرار آمادهٔ Railway.

## تغییرات نسخه 2

- رابط ورود و Dashboard کاملاً بازطراحی شده‌اند.
- مسیر مدیریت در `/admin` یا `/login` نیست؛ مسیر از secret مشتق می‌شود.
- VLESS WebSocket، Trojan WebSocket، XHTTP Packet-Up و XHTTP Stream-Up حفظ شده‌اند.
- خروجی VLESS URI، Clash/Mihomo، Sing-box و Subscription حفظ شده‌اند.
- گروه‌های اشتراک، محدودیت حجم/سرعت/IP، انقضا، تمدید و reset حفظ شده‌اند.
- state قبلی حذف نشده و در همان فایل JSON قابل استفاده است.
- Telegram اختیاری است و secret آن در backup export نمی‌شود.
- Railway با `PORT`، health check و Volume روی `/data` پشتیبانی می‌شود.

## اجرای محلی

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export ADMIN_USERNAME=Amirparsa
export ADMIN_PASSWORD='یک-رمز-قوی'
export SECRET_KEY='یک-secret-ثابت-و-طولانی'
export ADMIN_PATH_SECRET='یک-کلید-خصوصی-برای-مسیر-مدیریت'
export DATA_DIR=./data

uvicorn main:app --host 0.0.0.0 --port 8000
```

پس از اجرا، مسیر ورود را از log برنامه بردار یا توکن را با همان `ADMIN_PATH_SECRET` محاسبه کن. شکل مسیر:

```text
/control/<derived-token>
```

`/login` و `/admin` عمداً 404 هستند.

## تنظیمات Railway

در Variables سرویس:

```text
ADMIN_USERNAME=Amirparsa
ADMIN_PASSWORD=<رمز قوی و یکتا>
SECRET_KEY=<secret ثابت و تصادفی>
ADMIN_PATH_SECRET=<کلید خصوصی ثابت برای URL مدیریت>
DATA_DIR=/data
```

اختیاری:

```text
RAILWAY_PUBLIC_DOMAIN=<دامنه عمومی بدون https://>
ALLOWED_PUBLIC_HOSTS=<دامنه‌ها با کاما>
TRUST_PROXY_HEADERS=false
CORS_ORIGINS=<originهای دقیق با کاما>
TELEGRAM_BOT_TOKEN=<اختیاری>
TELEGRAM_ADMIN_IDS=<شناسه‌ها با کاما>
```

یک Railway Volume با Mount Path زیر بساز:

```text
/data
```

Start command پروژه:

```text
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Health check:

```text
GET /health
```

## ورود و امنیت

- در production نبود `ADMIN_PASSWORD` باعث توقف امن برنامه می‌شود.
- مسیر مدیریت به `ADMIN_PATH_SECRET` وابسته است؛ این مقدار را ثابت و محرمانه نگه دار.
- `SECRET_KEY` را بعد از استقرار تغییر نده، چون session و مسیر مشتق‌شده به آن وابسته‌اند.
- رمز پیش‌فرض `Technamooz` فقط برای local development است و در Railway استفاده نمی‌شود.
- فایل state روی Volume با mode محدود ذخیره می‌شود.
- توکن Telegram هرگز داخل backup قرار نمی‌گیرد.
- مسیرهای عمومی رایج `/login` و `/admin` وجود ندارند.

## APIهای اصلی

| حوزه | مسیرها |
|---|---|
| سلامت | `/health` |
| احراز هویت | `/api/captcha`, `/api/login`, `/api/logout`, `/api/me` |
| کانفیگ | `/api/links`, `/api/links/{uuid}`, `/api/links/{uuid}/renew`, `/api/links/{uuid}/reset` |
| گروه اشتراک | `/api/subs`, `/api/subs/{id}`, `/api/subs/{id}/links` |
| خروجی | `/sub/{uuid}`, `/sub/{uuid}/clash`, `/sub/{uuid}/singbox` |
| اشتراک گروهی | `/sub-group/{key}`, `/sub-group/{key}/clash`, `/sub-group/{key}/singbox` |
| relay | `/ws/{uuid}`, `/trojan/{uuid}`, مسیرهای XHTTP |
| عملیات | `/api/backup`, `/api/restore`, `/api/system`, `/api/activity`, `/api/connections` |

## تست‌های پیشنهادی قبل از انتشار

```bash
python3 -m compileall -q .
ruff check --select E9,F *.py
python3 -m json.tool railway.json >/dev/null
```

سپس `/health`، مسیر خصوصی مشتق‌شده، login، ساخت کانفیگ، خروجی Clash/Sing-box و subscription را بررسی کن.

## ساختار

- `main.py`: application و endpointهای سازگار فعلی
- `pages.py`: UI جدید Login، Dashboard و public subscription
- `relay_vless.py`: VLESS/Trojan WebSocket relay
- `xhttp_siz10.py`: XHTTP relay
- `speed_limit.py`: محدودیت سرعت و IP
- `telegram_bot.py`: ربات اختیاری Telegram
- `legacy/pages_v1.py`: snapshot قالب قدیم برای reference، در runtime import نمی‌شود
- `plan.md`: طرح معماری و تصمیم‌های نسخه 2
