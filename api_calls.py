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
def register_son(son):
    reg_son = {
        "name" : son.name,
        "age": son.age,
        "phone_number": son.phone,
        "elder" : son.elder
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
        "name": elder.name,
        "age" : elder.age,
        "city": elder.city,
        "address": elder.address,
        "private_home": elder.private,
        "apartment_num" : elder.apartment,
        "floor": elder.floor,       
        "phone": elder.phone
    }
    requests.post(URL_ELDERS, data=reg_elder)

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
    