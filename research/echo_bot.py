import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def command_start_handler(message: types.Message):
    await message.reply(
        "Hello! I'm a bot that can help you with Gemini. "
        "Send me a message and I'll echo it back!"
    )

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == "_main_":
    executor.start_polling(dp, skip_updates=True)