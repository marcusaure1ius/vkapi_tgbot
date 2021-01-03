import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from vk_fetching import GetGroupInfoById

post_data = GetGroupInfoById()

df = pd.DataFrame(post_data)

df['post_dt'] = pd.to_datetime(df['post_dt'])
df['post_date'] = df['post_dt'].map(lambda x: x.strftime('%Y-%m-%d'))
df['post_ym'] = df['post_dt'].map(lambda x: x.strftime('%Y-%m'))

mean_day_posts = round(df.groupby(['post_date'])['post_id'].count().mean())
mean_month_posts = round(df.groupby(['post_ym'])['post_id'].count().mean())
mean_likes = round(df['post_likes'].mean())
mean_reposts = round(df['post_reposts'].mean())
mean_comments = round(df['post_comments'].mean())
mean_views = round(df['post_views'].mean())
conv_views_to_likes = round((mean_likes/mean_views)*100, 2)

print('------------------------')
print('Среднее кол-во постов в день:',mean_day_posts)
print('Среднее кол-во постов в месяц:',mean_month_posts)
print('Среднее кол-во лайков под постом:',mean_likes)
print('Среднее кол-во репостов под постом:',mean_reposts)
print('Среднее кол-во комментариев под постом:',mean_comments)
print('Среднее кол-во просмотров под постом:',mean_views)
print('Конверсия просмотров к лайкам:',conv_views_to_likes)

l = df.groupby(['post_ym']).agg({'post_views':['sum', 'mean'], 'post_likes':['sum', 'mean'], 'post_comments':['sum', 'mean'], 'post_reposts':['sum', 'mean']})

def GetBarPlot(measure, agg):
    fig, ax = plt.subplots()
    ax.bar(l.index, l[measure][agg], color = 'red')
    fig.set_figwidth(16)
    fig.set_figheight(6)
    ax.set_xlabel('Месяцы')
    if measure == 'post_views':
        if agg == 'mean':
            ax.set_ylabel('Среднее кол-во просмотров')
        else:
            ax.set_ylabel('Суммарное кол-во просмотров')
    elif measure == 'post_likes':
        if agg == 'mean':
            ax.set_ylabel('Среднее кол-во лайков')
        else:
            ax.set_ylabel('Суммарное кол-во лайков')
    elif measure == 'post_comments':
        if agg == 'mean':
            ax.set_ylabel('Среднее кол-во комментариев')
        else:
            ax.set_ylabel('Суммарное кол-во комментариев')
    else:
        if agg == 'mean':
            ax.set_ylabel('Среднее кол-во репостов')
        else:
            ax.set_ylabel('Суммарное кол-во репостов')
    plt.savefig('png/'+measure+agg+'.png')
    # plt.show(block=False)

GetBarPlot('post_views', 'mean')
GetBarPlot('post_views', 'sum')
GetBarPlot('post_comments', 'mean')
GetBarPlot('post_comments', 'sum')
GetBarPlot('post_likes', 'mean')
GetBarPlot('post_likes', 'sum')
GetBarPlot('post_reposts', 'mean')
GetBarPlot('post_reposts', 'sum')
print('Графики сохранены в папку png/')