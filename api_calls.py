import requests
import json

URL_SONS = 'http://baduk-lokhim-git-group6.apps.cluster-9cdf.9cdf.sandbox537.opentlc.com/sons/'
URL_ELDERS = 'http://baduk-lokhim-git-group6.apps.cluster-9cdf.9cdf.sandbox537.opentlc.com/elders/'
URL_PRO = 'http://baduk-lokhim-git-group6.apps.cluster-9cdf.9cdf.sandbox537.opentlc.com/pro/'
URL_REQ = 'http://baduk-lokhim-git-group6.apps.cluster-9cdf.9cdf.sandbox537.opentlc.com/call/'
URL_PROF = 'http://baduk-lokhim-git-group6.apps.cluster-9cdf.9cdf.sandbox537.opentlc.com/professions/'
'''
register_son
input : new son details 

the function register the son in the database 

'''
def register_son(son, elder_phone):
    reg_son = {
        "name" : son['name'],
        "phone": son['phone'],
        "elder" : URL_ELDERS + get_elder_id(elder_phone) + '/'
    }
    requests.post(URL_SONS, data=reg_son)



'''
register_pro
input : new pro details 

the function register the pro in the database 

'''
def register_pro(pro):
    reg_pro = {
        "name" : pro.name,
        "active_cities" : pro.active_cities,
        "phone_number": pro.phone,
        "profession" : pro.profession
    }
    requests.post(URL_PRO, data=reg_pro)
    


def register_elder(elder):
    reg_elder = {
        "name": elder['name'],
        "age" : elder['age'],
        "city": elder['city'],
        "address": elder['address'],
        "private_home": elder['private_home'],
        "apartment_num" : elder['apartment_num'],
        "floor": elder['floor'],       
        "phone": elder['phone']
    }
    r = requests.post(URL_ELDERS, data=reg_elder)



'''
def register_call(son, description, handyman, start_date, destination):
    
'''



'''
get elder information using name
input : new pro details : first name, last name

the function get elder information link using fname lname

'''    
def get_son(phone):
    sons_list = json.loads(requests.get(URL_SONS).content)
    for son in sons_list:
        son_phone = son['phone']
        if son_phone == phone : 
            return son          
    return []

def get_pro(phone):
    pros_list = json.loads(requests.get(URL_PRO).content)
    for pro in pros_list:
        pro_phone = pro['phone']
        if pro_phone == phone : 
            return pro          
    return []


def get_son_url(phone):
    son = get_son(phone)
    return URL_SONS + son['id'] + '/'


def get_open_calls_for_son(phone):
    res = []
    son_url = get_son_url(phone)
    call_list = json.loads(requests.get(URL_REQ).content)
    for call in call_list:
        if call['grandson'] == son_url:
            res = res + [call]
    return res

def get_elder_id(phone):
    elders_list = json.loads(requests.get(URL_ELDERS).content)
    for elder in elders_list:
        elder_phone = elder['phone']
        if elder_phone == phone : 
            return elder['id']          
    return ''
    

def get_request(id):
    requests_list = json.loads(requests.get(URL_REQ).content)
    for req in requests_list:
        req_id = req['id']
        if req_id == id:
            return req 
    return []


def get_profession_list():
    prof_list = json.loads(requests.get(URL_PROF).content)
    prof_string_list = [] 
    for prof in prof_list:
        prof_string_list = prof_string_list + [prof['title']]
    return prof_string_list

'''
def push_rating(rate, request):
 '''   

def get_profession_by_id(id):
    return json.loads(requests.get(id))

def display_pro(pro):
    return 'שם  : ' + pro['name'] + '\n' + 'ערים:' \
        + pro['active_cities'] + '\n' + 'טלפון: ' +  '\n' + \
            + ':מקצוע' + get_profession_by_id(pro['id']) + '\n' + 'דירוג:' + pro['rank'] + '\n' +\
                + 'ביקורות:' + pro['reviews']


def display_call_child(call):
    if call['is_occupied']:
        handy_json = json.loads(requests.get(call['handy_man']).content)
        return 'עובד מבצע'+ handy_json + 'תיאור:' + call['description'] + '\n' + 'תאריך לביצוע:' + call['destination']
    else:
        return 'תיאור:' + call['description'] + '\n' + 'תאריך לביצוע:' + call['destination']

def display_call_handyman(call):
    son_json = json.loads(requests.get(call['grandson']).content)
    elder_json = json.loads(requests.get(call['elder']).content)
    return 'ילד:'+ son_json + '\n' + 'קשיש:' + elder_json + '\n' + 'תיאור:' + call['description'] + '\n' + 'תאריך לביצוע:' + call['destination']


def close_call(call):
    id = call['id']
    url = URL_REQ + id + '/'
    r = requests.patch(url , data={"is_open": False})
    print(r)
    

def update_ranking(pro, rank):
    curr_id = pro['id']
    curr_ranking = pro['rank']
    num_of_calls = pro['num_of_calls']
    
    new_rank = ((curr_ranking * num_of_calls) + rank)  / (num_of_calls + 1)
    
    url = URL_PRO + curr_id + '/'
    r = requests.patch(url, data={"num_of_calls" : num_of_calls + 1 , "rank" : new_rank})  




def calls_by_handyman_phone(phone):
    handy_calls = []
    call_list = json.loads(requests.get(URL_REQ).content)
    for call in call_list:
        call_handymans = call["handy_man_pool"]
        for hcall in call_handymans:
            handymans_call = json.loads(requests.get(hcall).content)
            if handymans_call['phone'] == phone:
                if call['is_occupied'] == False:
                    handy_calls = handy_calls + [call]

    return handy_calls


def calls_by_son_phone(phone):
    son_calls = []
    call_list = json.loads(requests.get(URL_REQ).content)
    for call in call_list:
        call_son = call["grandson"]
        son_call = json.loads(requests.get(call_son).content)
        if son_call['phone'] == phone:
            son_calls = son_calls + [call]

    return son_calls


def is_son_exist(phone):
    son = get_son(phone)
    if son == []:
        return False
    return True

def is_handyman_exist(phone):
    pro = get_pro(phone)
    if pro == []:
        return False
    return True


def handy_url_list_create(handymans):
    url_list = []
    for handyman in handymans:
        url_list = url_list + [URL_REQ + handyman['id'] + '/']
    
    return url_list
    
'''
def get_call_id_from_json(call_json):
   ''' 

def occupy_call(call):
    occ_id = call['id']
    url = URL_REQ + occ_id + '/'
    r = requests.patch(url , data={"is_occupied": True})
    
    
    
'''register_elder({
        "name": "2יוסי",
        "age" : 5,
        "city": "ראשון לציון",
        "address": " 10 הנוקמים",
        "private_home": False,
        "apartment_num" : None,
        "floor": None,       
        "phone": "052-222223"
    })

register_son({"name" : "דני",
        "phone": "00000"}, '052-222223')
        
        '''
        
