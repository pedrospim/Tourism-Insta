# -*- coding: UTF-8 -*-

import json
from datetime import date
import funcoes as f
import unidecode
import math
from pprint import pprint
from collections import Counter
from prettytable import PrettyTable
    

table = PrettyTable()
colunas = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]


with open('1433292443399033.json', encoding="utf8") as f:
        data = json.load(f)

#pprint(json.dumps(data[0], indent='  '))

dias = { 0:{},
         1:{},
         2:{},
         3:{},
         4:{},
         5:{},
         6:{}}

for post in data:
    for palavra in post.get('tags',[]):
        dataDoPost = date.fromtimestamp(post.get('taken_at_timestamp'))
        if dias.get(dataDoPost.weekday()).get(palavra) is not None:
            dias.get(dataDoPost.weekday()).update({palavra:dias.get(dataDoPost.weekday()).get(palavra) + 1})
        else:
            dias.get(dataDoPost.weekday()).update({palavra:1})


for dia in dias:
    c = Counter(dias.get(dia))
    table.add_column(colunas[dia], c.most_common()[:5])

print(table)
