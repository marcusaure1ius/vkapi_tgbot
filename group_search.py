import requests
import os
import logging
from dotenv import load_dotenv
load_dotenv()

VK_TOKEN = os.getenv('VK_TOKEN')
URL = 'https://api.vk.com/method/'
VERS = '5.126'

def GetCleanData(group):
    try:
        group_id = group['id']
    except:
        group_id = 'group_id_is_null'

    try:
        group_name = group['name']
    except:
        group_name = 'group_name_is_null'

    return_data = {
        'group_id':group_id,
        'group_name':group_name,
    }

    return return_data

def SearchGroup():
    raw_groups_array=[]
    clean_groups_array=[]
    count = 2
    sort = 1
    q='Рифмы'
    r = requests.get(url=URL+'groups.search', params={
        'access_token':VK_TOKEN,
        'v':VERS,
        'count':count,
        'sort':sort,
        'q':q
    })
    
    raw_groups = r.json()['response']['items']
    raw_groups_array.extend(raw_groups)

    for group in raw_groups_array:
        clean_groups = GetCleanData(group)
        clean_groups_array.append(clean_groups)
    
    print (clean_groups_array)

def main():
    SearchGroup()


if __name__ == '__main__':
    main()