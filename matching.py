import requests
import json
import pandas as pd
import numpy as np
from pandas import json_normalize

def resolve_prof(url):
    x = requests.get(url)
    data = json.loads(x.text)
    prof = json_normalize(data)
    return prof['title'].iloc[0]

# the actual function
def get_pros(wanted_profession_str, elder_url):
    # get elder
    data = json.loads(requests.get(elder_url).text)
    elder = json_normalize(data)
    # get elder city (address, lat and long)
    elder_city = elder.city.values[0]
    # get all possible professionals
    pro_list_url = 'http://baduk-lokhim-git-group6.apps.cluster-9cdf.9cdf.sandbox537.opentlc.com/pro/'
    pro_data = json.loads(requests.get(pro_list_url).text)
    pro_list = json_normalize(pro_data)
    # match city
    city_match = pro_list.apply(lambda x: elder_city in x['active_cities'], axis=1)
    # match wanted profession
    resolved_profs = pro_list.apply(lambda x: [resolve_prof(url) for url in x.profession], axis=1)
    prof_match = resolved_profs.apply(lambda x: wanted_profession_str in x)
    match = city_match & prof_match
    match_id = pro_list[match].id.to_list()
    index = pro_list[match].index.to_list()
    relevant_pro_list = np.array(pro_data)[index].tolist()
    return relevant_pro_list

#example (returns empty, no match)
elder_url='http://baduk-lokhim-git-group6.apps.cluster-9cdf.9cdf.sandbox537.opentlc.com/elders/581277b3-c0db-4899-95a0-21c48ad712a1'
relevant_pro_list = get_pros('אינסטלטור', elder_url)
relevant_pro_list