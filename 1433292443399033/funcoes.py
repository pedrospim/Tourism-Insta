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
