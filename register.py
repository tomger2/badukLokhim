import requests


url_sons = 'http://85.65.48.228:8080/sons/'
url_elders = 'http://85.65.48.228:8080/elders/'
url_pro = 'http://85.65.48.228:8080/pro/'


'''
register_son
input : new son details : name, city, phone, elder information

the function register the son in the database 

'''
def register_son(son):
    reg_son = {
        "name" : son.name,
        "age": son.age,
        "city": son.city,
        "phone_number": son.phone,
        "elder" : son.elder
    }
    requests.post(url_sons, data=reg_son)


'''
register_pro
input : new pro details : name, city, phone, profession information

the function register the pro in the database 

'''
def register_pro(pro):
    reg_pro = {
        "name" : pro.name,
        "age": pro.age,
        "city": pro.city,
        "phone_number": pro.phone,
        "profession" : pro.profession
    }
    requests.post(url_sons, data=reg_pro)
    


def register_elder(elder):
    reg_elder = {
        "name": elder.name,
        "city": elder.city,
        "phone_number": elder.phone
    }
    requests.post(url_elders, data=reg_elder)

'''
get elder information using name
input : new pro details : first name, last name

the function get elder information link using fname lname

'''    
def get_son(phone):
    sons_list = requests.get(url_sons).content
    for son in sons_list:
        print(son.first_name)  



get_son('00000')