import requests
import json
import csv
import logging
import os
from datetime import datetime
from datetime import timedelta
from time import sleep

from config import config

VK_TOKEN = config.VK_TOKEN
URL = 'https://api.vk.com/method/'
VERS = '5.126'

if not os.path.exists('csv'):
    os.mkdir('csv')
if not os.path.exists('png'):
    os.mkdir('png')

def GetCleanData(post, group_name, group):
    try:
        post_id = post['id']
    except:
        post_id = 'post_id_is_null'

    try:
        post_dt = datetime.fromtimestamp(post['date']).strftime('%Y-%m-%d %H:%M:%S')
    except:
        post_dt = 'post_dt_is_null'

    try:
        post_comments = post['comments']['count']
    except:
        post_comments = 'post_comments_is_null'

    try:
        post_likes = post['likes']['count']
    except:
        post_likes = 'post_likes_is_null'

    try:
        post_reposts = post['reposts']['count']
    except:
        post_reposts = 'post_reposts_is_null'
    
    try:
        post_views = post['views']['count']
    except:
        post_views = 'post_views_is_null'
        
    post_link = 'https://vk.com/'+str(group_name)+'?w=wall'+str(group)+'_'+str(post_id)

    return_data = {
        'post_id':post_id,
        'post_dt':post_dt,
        'post_comments':post_comments,
        'post_likes':post_likes,
        'post_reposts':post_reposts,
        'post_views':post_views,
        'post_link':post_link
    }

    return return_data

def WriteCSV(data):
    keys = data[0].keys()
    with open ('csv/posts_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

def GetGroupMetricsInfo(group):
    count = 1
    offset = 0
    group_size = []
    group_name = []
    group_sz = 0
    group_nm = 0
    metrics = {}
    r = requests.get(url=URL+'wall.get', params={
        'access_token':VK_TOKEN, 
        'owner_id':group, 
        'v':VERS, 
        'count':count, 
        'offset':offset,
        'extended':1,
        'fields':'members_count'
    })

    group_size_fetch = r.json()['response']['groups']
    group_size.extend(group_size_fetch)
    for group in group_size:
        group_sz = group['members_count']
    
    group_name_fetch = r.json()['response']['groups']
    group_name.extend(group_name_fetch)
    for group in group_name:
        group_nm = group['screen_name']

    posts_count_fetch = r.json()['response']['count']

    metrics = {'size':group_sz, 'posts_count': posts_count_fetch, 'group_name': group_nm}
    return metrics

def GetGroupInfoById(group):
    group_prefix = '-'
    group_id = group_prefix+group
    start = datetime.now()
    count = 100
    offset = 0
    clean_post_data = []
    all_posts = []
    to_date = round(datetime.timestamp(datetime.now()-timedelta(days=365)))

    group_metrics_info = GetGroupMetricsInfo(group_id)

    while True:
        sleep(1)
        r = requests.get(url=URL+'wall.get', params={
            'access_token':VK_TOKEN, 
            'owner_id':group_id, 
            'v':VERS, 
            'count':count, 
            'offset':offset
        })
        
        posts = r.json()['response']['items']

        all_posts.extend(posts)

        oldest_post_dt = posts[-1]['date']

        offset += 100

        # print('Загружено {} постов...'.format(len(all_posts)))

        if oldest_post_dt <= 1606850938:
            break
        

    for post in all_posts:
        clean_post = GetCleanData(post, group_metrics_info['group_name'], group_id)
        clean_post_data.append(clean_post)
    
    WriteCSV(clean_post_data)

    end = datetime.now()
    total_time = end - start

    # print('---------------------------------')
    # print('Время выполнения:', total_time)
    # print('Всего загружено постов:', len(clean_post_data))
    # print('Число подписчиков:', group_metrics_info['size'])
    # print('Общее кол-во постов', group_metrics_info['posts_count'])
    # print('CSV файл сохранен в папку csv/')
    # print(clean_post_data)
    # add 
    return clean_post_data


def main():
    post_data = GetGroupInfoById('22781583')


if __name__ == '__main__':
    main()