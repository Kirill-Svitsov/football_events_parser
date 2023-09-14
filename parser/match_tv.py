from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

url_match_tv = 'https://matchtv.ru/tvguide'

headers = {
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}


def match_tv_parse():
    req_match_tv = requests.get(url_match_tv, headers=headers)
    src_match_tv = req_match_tv.text

    soup_match_tv = BeautifulSoup(src_match_tv, 'lxml')
    match_tv_container = soup_match_tv.find('li',
                                            class_='tv-programm__chanels-item col-lg-4 col-md-6 col-sm-6 col-xs-12')
    match_tv_events = match_tv_container.findAll('li', class_='tv-programm__tvshows-item')
    football_events = []

    found_football = False

    for event in match_tv_events:
        time_str = event.find('div', class_='tv-programm__tvshow-time').text.strip()
        time_obj = datetime.strptime(time_str, '%H:%M')
        time_difference = timedelta(hours=2)
        actual_time = time_obj + time_difference
        title = event.find('div', class_='tv-programm__tvshow-title').text.strip()

        if 'футбол' in title.lower():
            found_football = True
            print(f'Время: {actual_time.strftime("%H:%M")}, Название: {title}')
            football_events.append(f'Время: {actual_time.strftime("%H:%M")}, Название: {title}')

    if not found_football:
        print("Сегодня нет футбола по ТВ")

    return football_events


if __name__ == "__main__":
    match_tv_parse()
