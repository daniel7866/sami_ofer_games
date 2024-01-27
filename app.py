from sami_ofer import *
from bot_message import *
from datetime import datetime

next_game = Get_Next_Games(False)[0]

if next_game['date'] == datetime.now().strftime("%d/%m/%y"):
    loop.run_until_complete(bot_message(next_game))
