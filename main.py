from dotenv import load_dotenv
import google.generativeai as genai  
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TELEGRAM_API_KEY = os.getenv("TELEGRAM_BOT_TOKEN")

genai.configure(api_key=GEMINI_API_KEY)

class References:
    def __init__(self) -> None:
        self.response = ""

reference = References()
model = genai.GenerativeModel('gemini-1.5-flash')  

bot = Bot(token=TELEGRAM_API_KEY)
dp = Dispatcher(bot)

def clear_past():
    reference.response = ""

@dp.message_handler(commands=["clear"])
async def clear(message: types.Message):
    clear_past()
    await message.reply("Cleared past messages. You can start fresh now!")

@dp.message_handler(commands=["start"])
async def command_start_handler(message: types.Message):
    await message.reply(
        "Hello! I'm a bot that can help you with Gemini. "
        "Send me a message and I'll echo it back!"
    )

@dp.message_handler(commands=["help"])
async def command_help_handler(message: types.Message):
    help_command = """
    Hi there! I'm a Gemini bot created by Naresh! Here are some commands you can use:
    /start - Start the bot and get a welcome message
    /clear - to clear the past messages and start fresh
    /help - to get this help message
    /echo - to echo back your message
    """
    await message.reply(help_command)

@dp.message_handler()
async def gemini(message: types.Message):
    print(f">>> USER: \n\t{message.text}")
    response = model.generate_content(message.text)
    reference.response = response.text
    print(f">>> GEMINI: \n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id, text=reference.response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
