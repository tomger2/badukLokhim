from enum import Enum
from twilio.twiml.messaging_response import MessagingResponse

import api_calls

class CLOSE_REQUEST_STATE(Enum):
    ASK_ID = 1 
    ASK_DESCRIPTION = 2
    ASK_RATING = 3


CLOSE_REQUEST = dict()

def process_close_request(incoming_msg, STATE, SUB_STATE):
    response = MessagingResponse()
    responded = False
    
    if SUB_STATE is CLOSE_REQUEST_STATE.ASK_ID:
        req_id = incoming_msg
        req = api_calls.get_request(req_id)
        if req == []:
            msg = 'מספר הפנייה שהקלדת אינו תקין!'
            response.message(msg)
            STATE = None
            SUB_STATE = None
            responded = True
            return response, responded, STATE, SUB_STATE

        # request id is valid
        CLOSE_REQUEST['req_id'] = req_id
        CLOSE_REQUEST['req'] = req

        msg = 'הכנס תיאור כללי לשירות שניתן על ידי בעל המקצוע:'
        response.message(msg)
        SUB_STATE = CLOSE_REQUEST_STATE.ASK_DESCRIPTION
        responded = True

    elif SUB_STATE is CLOSE_REQUEST_STATE.ASK_DESCRIPTION:
        CLOSE_REQUEST['desc'] = incoming_msg

        # TODO Add desc to pro's descriptions

        msg = 'הכנס דירוג לעבודה שבוצעה (מספר בין 1 עד 10):'
        response.message(msg)
        SUB_STATE = CLOSE_REQUEST_STATE.ASK_RATING
        responded = True

    elif SUB_STATE is CLOSE_REQUEST_STATE.ASK_RATING:
        CLOSE_REQUEST['rating'] = incoming_msg
        # TODO update rating in DB
        
        # Close the request
        
        # TODO turn is_close in DB to True
        # TODO calculate opening & close timing for rating
        
        msg = 'מגניב, סגרנו את הפנייה!'
        response.message(msg)
        STATE = None
        SUB_STATE = None
        responded = True
        return response, responded, STATE, SUB_STATE 
    
    return response, responded, STATE, SUB_STATE
        
        
        