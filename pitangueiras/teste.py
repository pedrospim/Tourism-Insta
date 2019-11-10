# -*- coding: UTF-8 -*-

import json
import unidecode
import math
from pprint import pprint
from collections import Counter

def formatar(p):

    pF = p
    pF = pF.lower()

    pF = unidecode.unidecode(pF)



    return pF

def gerarDados(nomeDoArquivo):
    with open(nomeDoArquivo, encoding="utf8") as f:
        data = json.load(f)

    tagsInfo = {}
    
    for post in data:
        for palavra in post.get('tags',[]):
            if formatar(palavra) in tagsInfo.keys():
                y = tagsInfo.get(formatar(palavra))[1]
                x = post.get('edge_liked_by').get('count')
                z = tagsInfo.get(formatar(palavra))[0]

                tagsInfo[formatar(palavra)] = [z + 1, x+y ,math.floor((x + y)/(z+1))]

            else:
                x = post.get('edge_liked_by').get('count')

                tagsInfo[formatar(palavra)] = [1, x, x]

    return tagsInfo

with open('pitangueiras.json', encoding="utf8") as f:
    data = json.load(f)

##pprint(json.dumps(data[0], indent='  '))


##tagsLikes = {}
##tagsQnt = {}
##tagsMedia = {}
##
##tagsInfo = {}
##
##for post in data:
##    for palavra in post.get('tags',[]):
##        if tagsInfo.get(palavra.lower()) is not None:
##            y = tagsInfo.get(palavra.lower())[0]
##            x = post.get('edge_liked_by').get('count')
##            z = tagsInfo.get(palavra.lower())[1]
##
##            tagsInfo[palavra.lower()] = [x+y, z + 1 , math.floor((x + y)/(z+1))]
##
##        else:
##            x = post.get('edge_liked_by').get('count')
##            tagsInfo[palavra.lower()] = [x, 1, x]         
##            
##
##
##tags = [
##    palavra.lower()
##    for post in data
##    for palavra in post.get('tags', [])
##   ]


##
##qntComments = [
##    post.get('edge_media_to_comment').get('count')
##    for post in data
##    ]

#palavras = set( [data[0].get('edge_media_to_caption').get('data',[])

#]

#)

#palavras = palavras.encode('UTF-8')

#######
c = Counter(gerarDados('pitangueiras.json'))
pprint("HASHTAGS MAIS USADAS")
pprint(c.most_common()[:50])
########
##c = Counter(tagsLikes)
##pprint("MAIS LIKEADAS")
##pprint(c.most_common()[:15])
########
##c = Counter(tagsMedia)
##pprint("COM MAIORES MEDIA DE LIKE POR HASHTAG")
##pprint(c.most_common()[:15])
##         
#pprint(palavras)
