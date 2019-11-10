# -*- coding: UTF-8 -*-

import json
from datetime import date
import math
from pprint import pprint
from collections import Counter
import numpy as np
import pandas as pd

with open('pitangueiras.json', encoding="utf8") as f:
        data = json.load(f)

##likes = pd.Series([post.get('edge_liked_by').get('count') for post in data], [date.fromtimestamp(post.get('taken_at_timestamp')) for post in data])
##tagsSeries = pd.Series(tags, [post.get('id') for post in data])
##repetidas = tagsSeries.value_counts()[tagsSeries.value_counts() > 1]

#pprint(json.dumps(data[0], indent='  '))

## RETRIEVE TAGS FROM DATA
tags = []
tags += [tuple(post.get('tags',[])) for post in data]


# CREATE DATAFRAME
df = pd.DataFrame([post.get('edge_liked_by').get('count') for post in data], index=[post.get('id') for post in data], columns=['Likes'])
df['Date'] = [date.fromtimestamp(post.get('taken_at_timestamp')) for post in data]
df['Tags'] = tags

#### FILTERING #####

df = df.drop(df[df['Likes'] > 100].index)
#df = df.drop(df[df['Date'] < date(2019, 1, 5)].index)

#dfMore = [len(t) > 5 for t in df['Tags'].values]
#pprint(df[dfMore])

df = df.drop_duplicates(subset=['Tags'], keep='last')

#dfTags = pd.DataFrame(1, index=[t for t in l for l in df['Tags'].values], columns=['ID'])
dfTags = pd.DataFrame(columns=['ID', 'Likes', 'Date'])
    
for l in df['Tags'].index:
        temp = pd.DataFrame(l, index=[t for t in df.loc[l]['Tags']],columns=['ID'])
        temp['Likes'] = df.loc[l]['Likes']
        temp['Date'] =  df.loc[l]['Date']
        dfTags = dfTags.append(temp)
        
#dfTags = dfTags.append(pd.DataFrame([123], index=['abc'],columns=['ID']))


pprint(dfTags)
