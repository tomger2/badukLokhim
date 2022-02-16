from enum import Enum
from unittest.mock import DEFAULT

class BotState(Enum):
    START = 1
    ELDER_SIGNUP = 2
    HANDYMAN_SIGNUP = 3
    ELDER_REQUEST = 4
    HANDYMAN_RATING = 5
    MAIN_ACTION = 6

class ELDER_SIGNUP_STATE(Enum):
    START = 1
    ASK_NAME = 2
    ASK_AGE = 3
    ASK_CITY = 4
    ASK_PHONE = 5
    ASK_ELDER_NAME = 6
    ASK_ELDER_CITY = 7
    ASK_ELDER_PHONE = 8
    
    
# conversation = {
#     BotState.ELDER_SIGNUP : [('שם', 'הכנס את השם המלא שלך'), ('פלאפון', 'הכנס את מספר הפלאפון שלך')] 
# }

