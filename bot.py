import re
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

from conversation_flow import BotState

STATE = None
SUB_STATE = None

from elder_signup import *
from handyman_signup import *
from close_request import *

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    global STATE, SUB_STATE
    incoming_msg = request.values.get('Body', '')
    response = MessagingResponse()
    responded = False
    
    # Display welcome message after user's first message
    if STATE is None:
        response.message('ברוך הבא')
        msg = 'הקלד בבקשה את הפעולה הרצויה: \n'
        msg += '1. הרשמה \n'
        msg += '2. פתיחת פנייה \n'
        msg += '3. דירוג בעל מקצוע \n'
        response.message(msg)
        STATE = BotState.START
        responded = True
            
    elif STATE is BotState.START:
        if incoming_msg == 'הרשמה':
            msg = '1. נכד דיגיטלי \n'
            msg += '2. בעל מקצוע \n'
            response.message(msg)
            STATE = BotState.MAIN_ACTION
            responded = True
            
        # elif incoming_msg == 'פתיחת פנייה':
            
        elif incoming_msg == 'דירוג בעל מקצוע':
            msg = 'הכנס מספר פנייה לדירוג : '
            response.message(msg)
            STATE = BotState.HANDYMAN_RATING
            responded = True

    elif STATE is BotState.MAIN_ACTION:
        if incoming_msg == 'נכד דיגיטלי':
            response.message('ברוך הבא, נכד דיגיטלי יקר')
            msg = 'הקלד את שמך המלא:'
            response.message(msg)
            STATE = BotState.ELDER_SIGNUP
            SUB_STATE = ELDER_SIGNUP_STATE.ASK_NAME
            responded = True
        
        if incoming_msg == 'בעל מקצוע':
            response.message('ברוך הבא, בעל מקצוע יקר')
            msg = 'הקלד את שמך המלא:'
            response.message(msg)
            STATE = BotState.HANDYMAN_SIGNUP
            SUB_STATE = HANDYMAN_SIGNUP_STATE.ASK_NAME
            responded = True
            
    elif STATE is BotState.ELDER_SIGNUP:
        grandson, response, responded, STATE, SUB_STATE = process_elder_signup(incoming_msg, STATE, SUB_STATE)
    
    elif STATE is BotState.HANDYMAN_SIGNUP:
        handyman, response, responded, STATE, SUB_STATE = process_handyman_signup(incoming_msg, STATE, SUB_STATE)

    elif STATE is BotState.HANDYMAN_RATING:
        response, responded = process_close_request(incoming_msg, response, responded)
        
    if not responded:
       response.message('נסה בבקשה להיצמד לפורמט המבוקש :)')
    
    return str(response)


if __name__ == '__main__':
    app.run()
