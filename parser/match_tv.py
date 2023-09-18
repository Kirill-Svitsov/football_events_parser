import os
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

url_match_tv = os.getenv("URL_MATCH_TV")
headers = {
    'Accept': os.getenv("HEADER_ACCEPT"),
    'User-Agent': os.getenv("USER_AGENT")
}


def match_tv_parse():
    req_match_tv = requests.get(url_match_tv, headers=headers)
    src_match_tv = req_match_tv.text
    soup_match_tv = BeautifulSoup(src_match_tv, 'lxml')
    match_tv_container = soup_match_tv.find(
        'li',
        class_='tv-programm__chanels-item col-lg-4 col-md-6 col-sm-6 col-xs-12'
    )
    match_tv_events = match_tv_container.findAll(
        'li',
        class_='tv-programm__tvshows-item'
    )
    football_events = []
    found_football = False
    for event in match_tv_events:
        time_str = event.find(
            'div',
            class_='tv-programm__tvshow-time'
        ).text.strip()
        time_obj = datetime.strptime(time_str, '%H:%M')
        time_difference = timedelta(hours=2)
        actual_time = time_obj + time_difference
        title = event.find(
            'div',
            class_='tv-programm__tvshow-title'
        ).text.strip()
        if 'футбол' in title.lower():
            found_football = True
            football_events.append(
                (f'Время: {actual_time.strftime("%H:%M")},'
                 f' Название: {title}'))
    if not found_football:
        football_events.append("Сегодня нет футбола по ТВ")
    return football_events


if __name__ == "__main__":
    match_tv_parse()
