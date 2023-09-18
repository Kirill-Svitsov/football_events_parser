import os

from dotenv import load_dotenv
from telegram import Bot, ParseMode

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message):
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(
        chat_id=TELEGRAM_CHAT_ID,
        text=message,
        parse_mode=ParseMode.MARKDOWN
    )
