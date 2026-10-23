import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()

# Botning o'ziga /start bosilganda javob berish uchun
@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer("Salom! Men Elbekning avtomatik biznes yordamchisiman.")

# Telegram Business orqali keladigan xabarlarga avtomatik javob berish uchun
@dp.business_message()
async def business_auto_reply(message: types.Message):
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
