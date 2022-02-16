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