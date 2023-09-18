[![GitHub](https://img.shields.io/badge/GitHub-Kirill--Svitsov-blue)](https://github.com/Kirill-Svitsov)

# Football Events Parser

## Purpose

This project consists of a set of scripts for parsing information about football events from various web sources.
The parser will collect daily data about upcoming matches, including teams, date and time,
as well as tournament details, and send them to a Telegram bot.

## Stack

- Python
- BeautifulSoup for parsing HTML code
- requests for HTTP requests
- datetime for working with dates and times
- python-telegram-bot for creating a Telegram bot

## Local Setup

1. Make sure you have Python 3.6 or higher installed on your system.
2. Clone the repository to your local machine.
3. Create a `.env` file in the project's root directory and add the following variables:

```plaintext
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID=YOUR_TELEGRAM_CHAT_ID
URL_SPORTING=https://www.sporting.pt/pt/bilhetes-e-gamebox/bilhetes
URL_MATCH_TV=https://matchtv.ru/tvguide
URL_BENFICA=https://www.sports.ru/benfica/calendar/
```
```
pip install -r requirements.txt
```
```
python main.py
```

## Additional Information
To use the script, you need to have Telegram bot tokens. Create your bot and obtain tokens from BotFather.

Also, make sure you have the python-dotenv module installed, which allows loading environment variables from the .env file.

Make sure to add .env to your .gitignore file to avoid exposing your sensitive data on GitHub.

## Author

**Kirill Svitsov**  
GitHub: [github.com/Kirill-Svitsov](https://github.com/Kirill-Svitsov)  
Email: svicovkirill@gmail.com
