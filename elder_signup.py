from enum import Enum

class ELDER_SIGNUP_STATE(Enum):
    ASK_NAME = 1
    ASK_AGE = 2
    ASK_PHONE = 3
    ASK_ELDER_NAME = 4
    ASK_ELDER_AGE = 5
    ASK_ELDER_CITY = 6
    ASK_ELDER_ADDRESS = 7
    ASK_ELDER_APT_NUM = 8
    ASK_ELDER_PHONE = 9

GRANDSON = {}

def process_elder_signup(incoming_msg, response, responded):
    global STATE, SUB_STATE
    if SUB_STATE is ELDER_SIGNUP_STATE.ASK_NAME:
        GRANDSON['name'] = incoming_msg
        msg = 'הקלד את הגיל שלך:'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_AGE
        responded = True
    
    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_AGE:
        GRANDSON['age'] = incoming_msg
        msg = 'הקלד את מספר הפלאפון שלך:'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_PHONE
        responded = True
    
    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_PHONE:
        GRANDSON['phone'] = incoming_msg
        msg = 'הקלד את שם המבוגר עליו אתה אחראי:'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_ELDER_NAME
        GRANDSON['elder'] = {}
        responded = True
        
    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_ELDER_NAME:
        GRANDSON['elder']['name'] = incoming_msg
        msg = 'הקלד את הגיל של ' + GRANDSON['elder']['name'] + ':'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_ELDER_AGE
        responded = True

    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_ELDER_AGE:
        GRANDSON['elder']['age'] = incoming_msg
        msg = 'הקלד את עיר המגורים של ' + GRANDSON['elder']['name'] + ':'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_ELDER_CITY
        responded = True

    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_ELDER_CITY:
        GRANDSON['elder']['city'] = incoming_msg
        msg = 'הקלד את שם הרחוב (כולל מספר בית):'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_ELDER_ADDRESS
        responded = True
    
    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_ELDER_ADDRESS:
        GRANDSON['elder']['address'] = incoming_msg
        msg = 'הקלד את מספר הדירה. (אם מדובר בבית פרטי, הקלד 0):'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_ELDER_APT_NUM
        responded = True
            
    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_ELDER_APT_NUM:
        GRANDSON['elder']['private_home'] = True if (int(incoming_msg) == 0) else False
        GRANDSON['elder']['apt_num'] = incoming_msg
        msg = 'הקלד את מספר הפלאפון של ' + GRANDSON['elder']['name'] + ':'
        response.message(msg)
        SUB_STATE = ELDER_SIGNUP_STATE.ASK_ELDER_PHONE
        responded = True
        
    elif SUB_STATE is ELDER_SIGNUP_STATE.ASK_ELDER_PHONE:
        GRANDSON['elder']['phone'] = incoming_msg
        response.message(incoming_msg)
        msg = 'מגניב, נרשמתם בהצלחה!'
        response.message(msg)
        STATE = None
        SUB_STATE = None
        responded = True
        response.message('הנה הפרטים שלכם:')
        response.message(GRANDSON)
        return GRANDSON, response, responded
    
    return response, responded
    