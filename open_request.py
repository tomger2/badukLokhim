from enum import Enum
from twilio.twiml.messaging_response import MessagingResponse

import matching

class OPEN_REQUEST_STATE(Enum):
    ASK_PHONE = 1
    ASK_PROFESSION = 2
    ASK_HANDYMAN = 3

REQUEST = dict()

def process_elder_signup(incoming_msg, STATE, SUB_STATE):
    response = MessagingResponse()
    responded = False
    
    if SUB_STATE is OPEN_REQUEST_STATE.ASK_PHONE:
        grandson_phone = incoming_msg

        # Check if there is such grandson
        grandson = api_calls.get_son(grandson_phone)
        if grandson == []:
            msg = 'נראה שאינך רשום במערכת.. הירשם תחילה ותחזור אלינו'
            response.message(msg)
            STATE = BotState.START
            SUB_STATE = None
            responded = True
            return response, responded, STATE, SUB_STATE

        REQUEST['grandson'] = grandson
        REQUEST['elder'] = grandson['elder']
        REQUEST['phone'] = grandson_phone

        msg = 'הקלד את המקצוע הנדרש עבורך מבין האופציות הבאות:\n'        
        index = 1
        profession_list = api_calls.get_profession_list()
        for pro in profession_list:
            msg += str(index) + '. ' + pro + "\n"
            index += 1

        response.message(msg)
        SUB_STATE = OPEN_REQUEST_STATE.ASK_PROFESSION
        responded = True
    
    elif SUB_STATE is OPEN_REQUEST_STATE.ASK_PROFESSION:
        REQUEST['profession'] = incoming_msg
        pros_list = matching.get_pros(REQUEST['profession'], REQUEST['grandson']['elder'])
        
        if pros_list == []:
            msg = 'לצערנו לא נמצאה לך התאמה לבעל מקצוע.. נקווה לחדש את המלאי בקרוב'
            response.message(msg)
            STATE = None
            SUB_STATE = None
            responded = True
            return REQUEST, response, responded, STATE, SUB_STATE
        
        REQUEST['pros_list'] = pros_list
        msg = 'בחר את בעל המקצוע המועדף עליך. הקלד את הספרה המתאימה עבורו:'
        index = 1
        for pro in pros_list:
            msg += str(index) + '. ' + pro + "\n"
            index += 1
            
        response.message(msg)
        SUB_STATE = OPEN_REQUEST_STATE.ASK_HANDYMAN
        responded = True
        
    elif SUB_STATE is OPEN_REQUEST_STATE.ASK_HANDYMAN:
        handyman_index = int(incoming_msg)
        REQUEST['handyman'] = REQUEST['pros_list'][handyman_index - 1]

        msg = 'מגניב, פתחנו את הפנייה שלכם!'
        response.message(msg)
        STATE = None
        SUB_STATE = None
        responded = True
        return REQUEST, response, responded, STATE, SUB_STATE

    return REQUEST, response, responded, STATE, SUB_STATE
    