from enum import Enum
from twilio.twiml.messaging_response import MessagingResponse
import api_calls

class HANDYMAN_SIGNUP_STATE(Enum):
    ASK_NAME = 1
    ASK_PHONE = 2
    ASK_CITIES = 3
    ASK_PROFESSION = 4

HANDYMAN = dict()

def process_handyman_signup(incoming_msg, STATE, SUB_STATE):
    response = MessagingResponse()
    responded = False
    
    if SUB_STATE is HANDYMAN_SIGNUP_STATE.ASK_NAME:
        HANDYMAN['name'] = incoming_msg
        msg = 'הקלד את מספר הפלאפון שלך:'
        response.message(msg)
        SUB_STATE = HANDYMAN_SIGNUP_STATE.ASK_PHONE
        responded = True
    
    elif SUB_STATE is HANDYMAN_SIGNUP_STATE.ASK_PHONE:
        HANDYMAN['phone'] = incoming_msg
        msg = 'הקלד את הערים בהן אתה פועל. אם קיימת יותר מעיר אחת, הפרד בינהן בפסיק. \n'
        msg += 'לדוגמא: \n'
        msg += 'תל אביב, כפר סבא \n'
        response.message(msg)
        SUB_STATE = HANDYMAN_SIGNUP_STATE.ASK_CITIES
        responded = True
    
    elif SUB_STATE is HANDYMAN_SIGNUP_STATE.ASK_CITIES:
        HANDYMAN['cities'] = incoming_msg.split(",")
        msg = 'הקלד את המקצוע שלך מבין האופציות הבאות:\n'
        
        index = 1
        profession_list = api_calls.get_profession_list()
        for pro in profession_list:
            msg += str(index) + '. ' + pro + "\n"
            index += 1

        response.message(msg)
        SUB_STATE = HANDYMAN_SIGNUP_STATE.ASK_PROFESSION
        responded = True
        
    elif SUB_STATE is HANDYMAN_SIGNUP_STATE.ASK_PROFESSION:
        HANDYMAN['profession'] = incoming_msg
        msg = 'מגניב, נרשמת בהצלחה!'
        response.message(msg)
        STATE = None
        SUB_STATE = None
        responded = True
        return HANDYMAN, response, responded, STATE, SUB_STATE

    return HANDYMAN, response, responded, STATE, SUB_STATE
    