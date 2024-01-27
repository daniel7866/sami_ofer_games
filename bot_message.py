from dotenv import load_dotenv
import os
from telegram import Bot
from telegram.error import TelegramError

import asyncio

loop = asyncio.get_event_loop()

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
API_KEY = os.getenv("API_KEY")
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")

async def bot_message(message):
    bot = Bot(token=API_KEY)
    async with bot:
        try:
            await bot.send_message(chat_id=GROUP_CHAT_ID, text=message)
        except TelegramError as e:
            print(f"Error sending message: {e}")

