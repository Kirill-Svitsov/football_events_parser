from match_tv import match_tv_parse
from sporting import sporting_parse
from benfica import benfica_parse
from datetime import datetime, timedelta

if __name__ == "__main__":
    today = datetime.now()
    tomorrow = today + timedelta(days=1)

    match_tv_events = match_tv_parse()
    sporting_events = sporting_parse()
    benfica_events = benfica_parse()
