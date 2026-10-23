import asyncio
import logging
import os
import sys
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()

# Render portini ochib turish uchun mini-server
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active!")

def start_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

# Serverni alohida oqimda ishga tushiramiz
threading.Thread(target=start_server, daemon=True).start()

@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer("Salom! Men Elbekning avtomatik biznes yordamchisiman. Hozir bandman, tez orada o'zim aloqaga chiqaman!")

@dp.message()
async def auto_reply_handler(message: types.Message) -> None:
    try:
        await message.answer("Xabaringiz uchun rahmat! Hozirda avtomatik rejimdaman, xabaringiz qayd etildi va tez orada o'zim javob yozaman.")
    except Exception as e:
        print(f"Xatolik: {e}")

async def main():
    if not TOKEN:
        print("Xato: BOT_TOKEN topilmadi!")
        return
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
