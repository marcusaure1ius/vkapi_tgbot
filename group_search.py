import requests
import logging

from config import config

VK_TOKEN = config.VK_TOKEN
URL = 'https://api.vk.com/method/'
VERS = '5.126'

def text_slice(text):
    def utf8len(s):
        return len(s.encode('utf-8'))

    k = 70

    while utf8len(text)>64:
        
        text = text[0:k]+'...'
        k -= 1
    
    return text

def GetCleanData(group):
    try:
        group_id = group['id']
    except:
        group_id = 'group_id_is_null'

    try:
        group_name = str(group['name']).replace(':','')
    except:
        group_name = 'group_name_is_null'

    # group_name = text_slice(group_name)

    return_data = {
        'group_id':group_id,
        'group_name':group_name,
    }

    return return_data

def SearchGroup(search_message):
    raw_groups_array=[]
    clean_groups_array=[]
    count = 3
    sort = 1
    q=search_message
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
    
    return clean_groups_array

def main():
    print(SearchGroup('клуб'))

if __name__ == '__main__':
    main()