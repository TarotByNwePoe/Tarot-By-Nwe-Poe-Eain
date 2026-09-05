import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = "8604205173:AAH9Rjs0rsdAMDy1EEsgYnF1nQqGciF58O0"
BIN_ID = "6a9bbd0cda38895dfe3b586a"
API_KEY = "$2a$10$5eUPNJ5q3AqVn4CZ9imWoecZ/iqGOVjmPy48kAneG6P.YzdS0aTbm"

@app.route("/", methods=["GET"])
def home():
    return "Tarot Admin Bot is running!", 200

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = request.get_json()
    
    if "message" in update:
        msg = update["message"]
        chat_id = msg["chat"]["id"]
        
        text = msg.get("text", msg.get("caption", "ယနေ့အတွက် အထူးဟောကိန်း"))
        photo_url = "https://images.unsplash.com/photo-1518709268805-4e9042af9f23" # Default wallpaper
        
        # Admin က ပုံပါ ပို့လိုက်လျှင် Telegram Server မှ ပုံအမှန်ကို ဆွဲယူရန်
        if "photo" in msg:
            file_id = msg["photo"][-1]["file_id"]
            file_info_url = f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}"
            file_res = requests.get(file_info_url).json()
            if file_res.get("ok"):
                file_path = file_res["result"]["file_path"]
                photo_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

        # JSONbin.io သို့ စာသားရော ပုံပါ တစ်ခါတည်း အပ်ဒိတ်လုပ်မည်
        url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
        headers = {
            "Content-Type": "application/json",
            "X-Master-Key": API_KEY
        }
        
        payload = {
            "daily_update": text,
            "wallpaper_url": photo_url
        }
        
        response = requests.put(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            send_msg(chat_id, f"✅ Website သို့ အပ်ဒိတ်နှင့် Wallpaper အောင်မြင်စွာ တင်ပြီးပါပြီ!")
        else:
            send_msg(chat_id, "❌ အပ်ဒိတ်တင်ရာတွင် အမှားအယွင်း ရှိသွားပါသည်။")
            
    return "ok", 200

def send_msg(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
