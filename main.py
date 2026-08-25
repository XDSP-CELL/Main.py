import os
import asyncio
from pyrogram import Client, filters
from telegram import Bot
from googletrans import Translator

# Environment Variables से डिटेल्स अपने आप लोड होंगी
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
TARGET_CHAT = os.getenv("TARGET_CHAT")
SESSION_STRING = os.getenv("SESSION_STRING")  # Render के लिए जरूरी

ORIGINAL_BOT = "BloxFruitsStock_Robot"

translator = Translator()
bot = Bot(token=BOT_TOKEN)

# String Session का इस्तेमाल करके Pyrogram कनेक्ट होगा
app = Client("my_stock_session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

@app.on_message(filters.chat(ORIGINAL_BOT))
async def forward_and_translate(client, message):
    original_text = message.text or message.caption
    
    if not original_text:
        return

    try:
        translated = translator.translate(original_text, dest='en')
        english_text = translated.text
        
        final_message = "🍍 **BLOX FRUITS LIVE STOCK** 🍎\n\n"
        final_message += english_text
        final_message += "\n\n✨ Powered by @bloxfruitstock_trackerbot"

        if message.photo:
            await bot.send_photo(
                chat_id=TARGET_CHAT,
                photo=message.photo.file_id,
                caption=final_message,
                parse_mode="Markdown"
            )
        else:
            await bot.send_message(
                chat_id=TARGET_CHAT,
                text=final_message,
                parse_mode="Markdown"
            )
            
        print("✅ Live stock forwarded and translated successfully!")

    except Exception as e:
        print(f"❌ Error: {e}")

print("🚀 Blox Fruits Tracker Bot is running on Render...")
app.run()
