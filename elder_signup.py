from enum import Enum

class ELDER_SIGNUP_STATE(Enum):
    ASK_NAME = 2
    ASK_AGE = 3
    ASK_CITY = 4
    ASK_PHONE = 5
    ASK_ELDER_NAME = 6
    ASK_ELDER_CITY = 7
    ASK_ELDER_PHONE = 8

class Grandson():
    def __init__(self):
        self.sub_state = ELDER_SIGNUP_STATE.ASK_NAME

class Elder():
    def __init__(self):
        pass

GRANDSON = Grandson()      

def process_elder_signup(incoming_msg, response, responded):
    global STATE
    if GRANDSON.sub_state is ELDER_SIGNUP_STATE.ASK_NAME:
        GRANDSON.name = incoming_msg
        msg = 'הקלד את הגיל שלך:'
        response.message(msg)
        GRANDSON.sub_state = ELDER_SIGNUP_STATE.ASK_AGE
        responded = True
    
    elif GRANDSON.sub_state is ELDER_SIGNUP_STATE.ASK_AGE:
        GRANDSON.age = incoming_msg
        msg = 'הקלד את עיר המגורים שלך:'
        response.message(msg)
        GRANDSON.sub_state = ELDER_SIGNUP_STATE.ASK_CITY
        responded = True
    
    elif GRANDSON.sub_state is ELDER_SIGNUP_STATE.ASK_CITY:
        GRANDSON.city = incoming_msg
        msg = 'הקלד את מספר הפלאפון שלך:'
        response.message(msg)
        GRANDSON.sub_state = ELDER_SIGNUP_STATE.ASK_PHONE
        responded = True
    
    elif GRANDSON.sub_state is ELDER_SIGNUP_STATE.ASK_PHONE:
        GRANDSON.phone = incoming_msg
        msg = 'הקלד את שם המבוגר עליו אתה אחראי:'
        response.message(msg)
        GRANDSON.sub_state = ELDER_SIGNUP_STATE.ASK_ELDER_NAME
        GRANDSON.elder = Elder()
        responded = True
        
    elif GRANDSON.sub_state is ELDER_SIGNUP_STATE.ASK_ELDER_NAME:
        GRANDSON.elder.name = incoming_msg
        msg = 'הקלד את עיר המגורים של ' + GRANDSON.elder.name + ':'
        response.message(msg)
        GRANDSON.sub_state = ELDER_SIGNUP_STATE.ASK_ELDER_CITY
        responded = True
    
    elif GRANDSON.sub_state is ELDER_SIGNUP_STATE.ASK_ELDER_CITY:
        GRANDSON.elder.city = incoming_msg
        msg = 'הקלד את מספר הפלאפון של ' + GRANDSON.elder.name + ':'
        response.message(msg)
        GRANDSON.sub_state = ELDER_SIGNUP_STATE.ASK_ELDER_PHONE
        responded = True
        
    elif GRANDSON.sub_state is ELDER_SIGNUP_STATE.ASK_ELDER_PHONE:
        GRANDSON.elder.phone = incoming_msg
        response.message(incoming_msg)
        msg = 'מגניב, נרשמתם בהצלחה!'
        response.message(msg)
        STATE = None
        GRANDSON.sub_state = None
        responded = True
        return GRANDSON, response, responded
    
    return response, responded
    