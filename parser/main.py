import os
import time
from datetime import datetime, timedelta

from benfica import benfica_parse
from dotenv import load_dotenv
from match_tv import match_tv_parse
from sporting import sporting_parse

from telegram_bot.telegram_module import send_message

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
RETRY_PERIOD = 86400  # 24 часа в секундах

if TELEGRAM_BOT_TOKEN is None or TELEGRAM_CHAT_ID is None:
    print("Ошибка: Токены для телеграма не заданы в файле .env.")
    exit()

while True:
    today = datetime.now()
    tomorrow = today + timedelta(days=1)

    try:
        match_tv_events = match_tv_parse()
    except Exception as e:
        print(f"Ошибка при получении данных с Match TV: {str(e)}")
        send_message(
            TELEGRAM_BOT_TOKEN,
            TELEGRAM_CHAT_ID,
            f"Ошибка при получении данных с Match TV: {str(e)}"
        )
        match_tv_events = []

    try:
        sporting_events = sporting_parse()
    except Exception as e:
        print(f"Ошибка при получении данных с сайта Sporting: {str(e)}")
        send_message(
            TELEGRAM_BOT_TOKEN,
            TELEGRAM_CHAT_ID,
            f"Ошибка при получении данных с сайта Sporting: {str(e)}"
        )
        sporting_events = []

    try:
        benfica_events = benfica_parse()
    except Exception as e:
        print(f"Ошибка при получении данных с сайта Benfica: {str(e)}")
        send_message(
            TELEGRAM_BOT_TOKEN,
            TELEGRAM_CHAT_ID,
            f"Ошибка при получении данных с сайта Benfica: {str(e)}"
        )
        benfica_events = []

    # Разделительное сообщение
    daily_message = (
        f'⚽⚽⚽⚽️ Сводка сегодняшних событий по футболу,'
        f' за {today.strftime("%d.%m.%Y")}⚽⚽⚽⚽'
    )
    send_message(
        TELEGRAM_BOT_TOKEN,
        TELEGRAM_CHAT_ID,
        daily_message.upper()
    )

    # Матч ТВ
    massage = f'Футбол по Матч ТВ  на сегодня, {today.strftime("%d.%m.%Y")}: '
    send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, massage)
    for event in match_tv_events:
        send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, event)

    # Спортинг
    massage = 'Футбол на стадионе Спортинга в ближайшее время: '
    send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, massage)
    for event in sporting_events:
        send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, event)

    # Бенфика
    massage = 'Матчи Бенфики на этой неделе: '
    send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, massage)
    for event in benfica_events:
        send_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, event)

    time.sleep(RETRY_PERIOD)  # Ожидаем 24 часа перед следующей итерацией
