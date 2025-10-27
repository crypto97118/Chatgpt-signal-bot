import os
import time
import requests

# می‌خونیم از Environment Variables که توی Render ست کردی
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"


def send_message(text):
    try:
        resp = requests.post(
            TELEGRAM_API,
            data={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "Markdown"
            },
            timeout=10,
        )
        # برای دیباگ، استاتوس‌کد رو چاپ می‌کنیم توی لاگ Render
        print("Telegram response code:", resp.status_code, "body:", resp.text)
    except Exception as e:
        print("Error sending message:", e)


def main():
    # پیام شروع: همین الان باید تو تلگرام برسه اگه همه چی اوکی باشه
    send_message("✅ Bot is LIVE on Render and connected successfully.")

    # هر 2 دقیقه یه پیام وضعیت می‌فرسته. فقط برای تست پایداری.
    # بعد از تست، این قسمت رو در نسخه نهایی یا کامنت می‌کنیم یا تغییرش می‌دیم.
    counter = 1
    while True:
        heartbeat_text = f"💓 Heartbeat #{counter}: bot is still running."
        send_message(heartbeat_text)
        counter += 1
        time.sleep(120)  # هر 120 ثانیه = هر دو دقیقه


if __name__ == "__main__":
    main()
