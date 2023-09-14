from bs4 import BeautifulSoup
import requests

url_sporting = 'https://www.sporting.pt/pt/bilhetes-e-gamebox/bilhetes'
headers = {
    'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
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

                print(f'Дата и время: {date_time}')
                print(f'Команда хозяев: {home_team}')
                print(f'Команда гостей: {away_team}')

                football_events.append({
                    'Дата и время': date_time,
                    'Команда хозяев': home_team,
                    'Команда гостей': away_team
                })
    return


if __name__ == "__main__":
    sporting_parse()
