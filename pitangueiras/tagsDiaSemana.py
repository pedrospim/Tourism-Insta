# -*- coding: UTF-8 -*-

import json
from datetime import date
import funcoes
import unidecode
import math
from pprint import pprint
from collections import Counter
from prettytable import PrettyTable


def normalizar(palavras, tags):
    for p in palavras:
        if p in tags:
            return False

    return True

table = PrettyTable()
colunas = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]


with open('pitangueiras.json', encoding="utf8") as f:
        data = json.load(f)

#pprint(json.dumps(data[0], indent='  '))

palavrasNorm = ['ribeiraopreto','vilasdoatlantico']

hashfiltrada = 0;
hashnaofiltrada = 0;

qntDias = { 0:0,
         1:0,
         2:0,
         3:0,
         4:0,
         5:0,
         6:0}

dias = { 0:{},
         1:{},
         2:{},
         3:{},
         4:{},
         5:{},
         6:{}}

for post in data:
    dataDoPost = date.fromtimestamp(post.get('taken_at_timestamp'))
    qntDias.update({dataDoPost.weekday(): qntDias.get(dataDoPost.weekday()) + 1})
   #print(dataDoPost)
    for palavra in post.get('tags',[]):
        if normalizar(palavrasNorm,post.get('tags',[])):
            hashnaofiltrada += 1
            if dias.get(dataDoPost.weekday()).get(funcoes.formatar(palavra)) is not None:
                dias.get(dataDoPost.weekday()).update({funcoes.formatar(palavra):dias.get(dataDoPost.weekday()).get(funcoes.formatar(palavra)) + 1})
            else:
                dias.get(dataDoPost.weekday()).update({funcoes.formatar(palavra):1})
        else:
            hashfiltrada += 1
            


for dia in dias:
    c = Counter(dias.get(dia))
    table.add_column(colunas[dia], c.most_common()[:10])

print(table)
print("Hashs filtradas: " + str(hashfiltrada))
print("Hahs nao filtradas: " + str(hashnaofiltrada))
print(qntDias)
