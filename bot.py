import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():

    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN not found in .env")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    @dp.message(CommandStart())
    async def start_handler(message: Message):
        await message.answer("Бот запущен ✅")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())