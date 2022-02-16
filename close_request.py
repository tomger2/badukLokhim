from enum import Enum

import api_calls

class CLOSE_REQUEST_STATE(Enum):
    ASK_ID = 2, 
    ASK_DESCRIPTION = 3,
    GIVE_RAITING = 4,
    UPDATE_RATING = 5
    

def process_close_request(incoming_msg, STATE, SUB_STATE):
    response = MessagingResponse()
    responded = False
    
    if SUB_STATE is CLOSE_REQUEST_STATE.ASK_ID:
        msg = 'הקלד את מספר הפנייה:'
        response.message(msg)
        SUB_STATE = CLOSE_REQUEST_STATE.ASK_DESCRIPTION
        responded = True
    elif SUB_STATE is CLOSE_REQUEST_STATE.ASK_DESCRIPTION:
        req_id = incoming_msg
        req = api_calls.get_request(req_id)
        if req == []:
            SUB_STATE = None
            return
        msg = 'הכנס תיאור כללי לשירות שניתן עי בעל המקצוע:'
        response.message(msg)
        SUB_STATE = CLOSE_REQUEST_STATE.GIVE_RAITING
        responded = True
    elif SUB_STATE is CLOSE_REQUEST_STATE.GIVE_RAITING:
        msg = 'הכנס דירוג לעבודה שבוצעה : '
        response.message(msg)
        responded = True
    elif SUB_STATE is CLOSE_REQUEST_STATE.UPDATE_RATING:
        
        
        
        