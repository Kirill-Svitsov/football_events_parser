import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url_sporting = os.getenv("URL_SPORTING")
headers = {
    'Accept': os.getenv("HEADER_ACCEPT"),
    'User-Agent': os.getenv("USER_AGENT")
}


def sporting_parse():
    req_sporting = requests.get(url_sporting, headers=headers)
    src_sporting = req_sporting.text
    soup_sporting = BeautifulSoup(src_sporting, 'lxml')
    # Находим все блоки с информацией о билетах
    bilhetes_blocks = soup_sporting.find_all('div', class_='mmsubmenu__title')
    football_events = []
    # Перебираем каждый блок с билетами
    for block in bilhetes_blocks:
        if 'bilhetes futebol' in block.text.lower():
            # Найден блок с билетами на футбол
            matches_info = block.find_next('ul', class_='mmproximojogo')
            # Находим каждую отдельную игру
            matches = matches_info.find_all('li', class_='mmproximojogo__item')
            # Перебираем информацию о каждой игре
            for match in matches:
                # Извлекаем дату и время
                date_time = match.find('div', class_='item__date').text.strip()
                # Извлекаем названия команд
                teams = match.find_all('div', class_='equipa')
                home_team = teams[0].text.strip()
                away_team = teams[1].text.strip()
                event_info = f'{date_time} - {home_team} - {away_team}'
                football_events.append(event_info)
    if len(football_events) == 0:
        football_events.append('Спортинг на этой неделе не играет')
        print(football_events[0])
    return football_events


if __name__ == "__main__":
    sporting_parse()
