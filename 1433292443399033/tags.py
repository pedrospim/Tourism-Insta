# -*- coding: UTF-8 -*-

import json
from datetime import date
import unidecode
import math
from pprint import pprint
from collections import Counter
from prettytable import PrettyTable
    

table = PrettyTable()
table.field_names = ["Hashtag", "Qnt.", "Total Likes", "Med. Likes", "Data", "Temp. Máx.", "Temp. Mín."]

tempo = open("dados.txt","r")
dados = tempo.read()
dados = dados.split("<br>")


with open('1433292443399033.json', encoding="utf8") as f:
        data = json.load(f)

def getTempMaxima(data1):

    soma = 0
    qnt = 0
    
    for linha in dados:
        li = linha.split(",")
        lin = []
        if len(li) > 1: 
            lin = li[1].split("/")

        if len(lin) > 2:       
            data2 = date(int(lin[2]),int(lin[1]),int(lin[0]))
            if data1 == data2:
                qnt = qnt + 1
                if float(li[4]) > soma:
                    soma = float(li[4])
            
    if qnt > 0:       
        return soma
    else:
        return 0

def getTempMinima(data1):

    soma = 100
    qnt = 0
    
    for linha in dados:
        li = linha.split(",")
        lin = []
        if len(li) > 1: 
            lin = li[1].split("/")

        if len(lin) > 2:       
            data2 = date(int(lin[2]),int(lin[1]),int(lin[0]))
            if data1 == data2:
                qnt = qnt + 1
                if float(li[5]) < soma:
                    soma = float(li[5])
            
    if qnt > 0:       
        return soma
    else:
        return 0
    

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
                w = date.fromtimestamp(post.get('taken_at_timestamp'))

                tagsInfo[formatar(palavra)] = [z + 1, x+y ,math.floor((x + y)/(z+1)), w]

            else:
                x = post.get('edge_liked_by').get('count')
                w = date.fromtimestamp(post.get('taken_at_timestamp'))
                
                tagsInfo[formatar(palavra)] = [1, x, x, w]

    return tagsInfo

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
c = Counter(gerarDados('1433292443399033.json'))
for linha in c.most_common()[:30]:
    table.add_row([linha[0],
                   linha[1][0],
                   linha[1][1],
                   linha[1][2],
                   linha[1][3],
                   getTempMaxima(linha[1][3]),
                   getTempMinima(linha[1][3])])

print(table)    
##pprint(c.most_common()[:50])
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
