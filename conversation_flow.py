from enum import Enum
from unittest.mock import DEFAULT

class BotState(Enum):
    START = 1
    ELDER_SIGNUP = 2
    HANDYMAN_SIGNUP = 3
    ELDER_REQUEST = 4
    HANDYMAN_RATING = 5
    MAIN_ACTION = 6
    

# conversation = {
#     BotState.ELDER_SIGNUP : [('שם', 'הכנס את השם המלא שלך'), ('פלאפון', 'הכנס את מספר הפלאפון שלך')] 
# }

