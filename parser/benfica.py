from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

url_benfica = 'https://www.sports.ru/benfica/calendar/'
headers = {
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
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
        event_date = datetime.strptime(date_time.split('|')[0].strip(), "%d.%m.%Y")

        # Проверяем, попадает ли событие в ближайшую неделю
        if today <= event_date < next_week:
            tournament = event.find('div', class_='hide-field').text.strip()
            teams = event.find_all('a', title=True)
            home_team = teams[1]['title']
            away_team = teams[2]['title']
            print(f'{date_time} - {home_team} - {away_team} - {tournament}')
            football_events.append({
                'Дата и время': date_time,
                'Команда хозяев': home_team,
                'Команда гостей': away_team,
                'Турнир': tournament
            })
    return football_events


if __name__ == "__main__":
    benfica_parse()

