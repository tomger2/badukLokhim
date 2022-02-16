from enum import Enum


class CLOSE_REQUEST_STATE(Enum):
    ASK_ID = 2, 
    ASK_DESCRIPTION = 3,
    GIVE_RAITING = 4,
    

def process_close_request(incoming_msg, response, responded):
    global STATE, SUB_STATE
    
    if SUB_STATE is CLOSE_REQUEST_STATE.ASK_ID:
        msg = 'הקלד את מספר הפנייה:'
        response.message(msg)
        SUB_STATE = CLOSE_REQUEST_STATE.ASK_DESCRIPTION
        responded = True
    elif SUB_STATE is CLOSE_REQUEST_STATE.ASK_DESCRIPTION:
        msg = 'הכנס תיאור כללי לשירות שניתן עי בעל המקצוע:'
        response.message(msg)
        SUB_STATE = CLOSE_REQUEST_STATE.GIVE_RAITING
        responded = True
    elif SUB_STATE is CLOSE_REQUEST_STATE.GIVE_RAITING:
        msg = 'הכנס דירוג לעבודה שבוצעה : '
        response.message(msg)
        responded = True
        SUB_STATE = None
        
        