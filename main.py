import os
import requests
from flask import Flask, request

app = Flask(__name__)

# သင်ပေးထားတဲ့ Bot Token နဲ့ JSONbin အချက်အလက်များ
TOKEN = "8604205173:AAH9Rjs0rsdAMDy1EEsgYnF1nQqGciF58O0"
BIN_ID = "6a9bbd0cda38895dfe3b586a"
API_KEY = "$2a$10$5eUPNJ5q3AqVn4CZ9imWoecZ/iqGOVjmPy48kAneG6P.YzdS0aTbm"

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"


@app.route("/", methods=["GET"])
def home():
  return "Tarot Admin Bot is running 24/7!", 200


@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
  update = request.get_json()

  if "message" in update and "text" in update["message"]:
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"]

    # JSONbin.io ကို အပ်ဒိတ်လုပ်ခြင်း
    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
    headers = {"Content-Type": "application/json", "X-Master-Key": API_KEY}

    payload = {
        "daily_update": text,
        "wallpaper_url": (
            "https://images.unsplash.com/photo-1518709268805-4e9042af9f23"
        ),
    }

    response = requests.put(url, json=payload, headers=headers)

    # Telegram ကနေ Admin ဆီကို အကြောင်းပြန်ရန်
    if response.status_code == 200:
      send_telegram_message(
          chat_id, f"✅ Website သို့ အောင်မြင်စွာ အပ်ဒိတ်တင်ပြီးပါပြီ:\n{text}"
      )
    else:
      send_telegram_message(
          chat_id, "❌ အပ်ဒိတ်တင်ရာတွင် အမှားအယွင်း ရှိသွားပါသည်။"
      )

  return "ok", 200


def send_telegram_message(chat_id, text):
  url = f"{TELEGRAM_API_URL}/sendMessage"
  data = {"chat_id": chat_id, "text": text}
  requests.post(url, json=data)


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)
