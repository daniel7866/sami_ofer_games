from sami_ofer import *
from bot_message import *

next_game = To_String(Get_Next_Games(False)[0])
loop.run_until_complete(bot_message(next_game))