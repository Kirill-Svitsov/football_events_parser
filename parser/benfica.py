import os
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url_benfica = os.getenv("URL_BENFICA")
headers = {
    'Accept': os.getenv("HEADER_ACCEPT"),
    'User-Agent': os.getenv("USER_AGENT")
}


def benfica_parse():
    req_benfica = requests.get(url_benfica, headers=headers)
    src_benfica = req_benfica.text
    soup_benfica = BeautifulSoup(src_benfica, 'lxml')
    calendar_table = soup_benfica.find('table', class_='stat-table')
    benfica_events = calendar_table.findAll('tr')
    # Определение начальной и конечной даты для ближайшей недели
    today = datetime.now()
    next_week = today + timedelta(days=7)
    football_events = []
    for event in benfica_events[1:]:
        date_time = event.find('a').text
        event_date = datetime.strptime(
            date_time.split('|')[0].strip(),
            "%d.%m.%Y"
        )
        # Проверяем, попадает ли событие в ближайшую неделю
        if today <= event_date < next_week:
            tournament = event.find('div', class_='hide-field').text.strip()
            teams = event.find_all('a', title=True)
            home_team = teams[1]['title']
            away_team = teams[2]['title']
            event_info = (
                f'{date_time} -'
                f' {home_team} -'
                f' {away_team} -'
                f' {tournament}'
            )
            football_events.append(event_info)
    if not football_events:
        football_events.append('Бенфика на этой неделе не играет')
    return football_events


if __name__ == "__main__":
    benfica_parse()
