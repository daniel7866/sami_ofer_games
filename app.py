from bs4 import BeautifulSoup
import requests
import re

URL = 'https://www.haifa-stadium.co.il/לוח_המשחקים_באצטדיון/'

# date is dd/mm/yy
DATE_FORMAT = re.compile('[0-9][0-9]/[0-9][0-9]/[0-9][0-9]')

# time is hh:mm
TIME_FORMAT = re.compile('[0-9][0-9]:[0-9][0-9]')

# allow only spaces and letters, but no rows containing only white space
GAME_DETAILS_FORMAT = re.compile('^(?! +$)[א-ת ]+$')

# div with this classname contains rows which contains the games (but could be other row elements too)
CLASS_NAME = 'elementor-container elementor-column-gap-default'


result = requests.get(URL)
doc = BeautifulSoup(result.text, "html.parser")
row_containers = doc.find_all("div", {'class' : CLASS_NAME})

for row in row_containers:
    next_game_day = row.find(string=DATE_FORMAT)
    next_game_time = row.find(string=TIME_FORMAT)
    
    # if we've found this format it means it is a row containing a game
    if next_game_day and next_game_time:
        details = row.find_all(string=GAME_DETAILS_FORMAT)
        print(next_game_day)
        print(next_game_time)
        for detail in details:
            print(detail)
        
        # we only care for the next game
        break


