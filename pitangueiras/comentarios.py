# -*- coding: UTF-8 -*-

import json
from pprint import pprint
from collections import Counter

with open('pitangueiras.json', encoding="utf8") as f:
    data = json.load(f)

#pprint(json.dumps(data[:5], indent='  '))

frases = [
    palavra.get('text').encode('UTF-8')
    for post in data
    for palavra in post.get('edge_media_to_comment').get('data', [])
    ]

qntComments = [
    post.get('edge_media_to_comment').get('count')
    for post in data
    ]

#palavras = set( [data[0].get('edge_media_to_caption').get('data',[])

#]

#)

#palavras = palavras.encode('UTF-8')

wordcount = 0;
commentCount = 0;
psoltas = []
palavras = [
    p.split()
    for p in frases
    ]

for frases in palavras:
    for p in frases:
            psoltas.append(p.lower())
            wordcount = wordcount + 1

for qnt in qntComments:
    commentCount = commentCount + qnt
    

c = Counter(psoltas)
pprint(c.most_common()[:30])
pprint(wordcount)
pprint(commentCount)

#pprint(palavras)
