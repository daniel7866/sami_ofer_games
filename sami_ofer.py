from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime, timedelta

#######################
###### constants ######
#######################
URL = 'https://www.haifa-stadium.co.il/לוח_המשחקים_באצטדיון/'

# date is dd/mm/yy
DATE_FORMAT = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9]')

# time is hh:mm
TIME_FORMAT = re.compile('[0-9][0-9]:[0-9][0-9]')

# allow only spaces and letters, but no rows containing only white space
GAME_DETAILS_FORMAT = re.compile('^(?! +$)[א-ת ]+$')

# div with this classname contains rows which contains the games (but could be other row elements too)
CLASS_NAME = 'elementor-container elementor-column-gap-default'
#######################
#######################


def Get_Next_Games(allGames = True) -> list:
    request = requests.get(URL)
    doc = BeautifulSoup(request.text, "html.parser")
    row_containers = doc.find_all("div", {'class' : CLASS_NAME})

    res = []

    for row in row_containers:
        next_game_date = row.find(string=DATE_FORMAT)
        next_game_time = row.find(string=TIME_FORMAT)
        
        # if we've found this format it means it is a row containing a game
        if next_game_date and next_game_time:
            details = row.find_all(string=GAME_DETAILS_FORMAT)
            game = {}
            game['date'] = next_game_date
            game['time'] = next_game_time

            # traffic is usually a mess 3 hours before
            time_to_run_away = (datetime.strptime(next_game_time, "%H:%M") - timedelta(hours=3)).strftime("%H:%M")
            game['time_to_run_away'] = 'חסימת כבישים:' + time_to_run_away
            game['details'] = ''

            for detail in details:
                game['details'] += detail + '\n'
            
            res.insert(0,game)

            # we only care for the next game
            if not allGames:
                break
    return res


def To_String(game : map) -> str:
    res = ''

    res += game['date'] + '\n'
    res += game['time'] + '\n'
    res += game['time_to_run_away'] + '\n'
    res += game['details'] + '\n'

    return res

