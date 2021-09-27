# -*- coding: utf-8 -*-
"""
@author: Alvaro Quisbert Mamani
"""

import pandas as pd
data = pd.read_csv("vino.csv",sep=",",header=[0])
print(data)

def moda(columna):
    #print(columna.value_counts())
    contarunicosindice=columna.value_counts().index.tolist()
    #contarunicosvalor=columna.value_counts().tolist()
    return contarunicosindice[0]

def media(columna):
    suma=columna.sum()
    return suma/len(columna)

def _ss(columna):
    c=media(columna)
    ss=sum((x-c)**2 for x in columna)
    return ss

def std(columna,d=0):
    n=len(columna)
    if (n>=2):
        ss=_ss(columna)
        pvar=ss/(n-d)
    return pvar**0.5
    
print("Moda[fixed acidity]=",moda(data["fixed acidity"]))
print("Moda[citric acid]=",moda(data["citric acid"]))
print("Moda[residual sugar]=",moda(data["residual sugar"]))
print("Moda[chlorides]=",moda(data["chlorides"]))
print("Moda[free sulfur dioxide]=",moda(data["free sulfur dioxide"]))
print("Moda[total sulfur dioxide]=",moda(data["total sulfur dioxide"]))
print("Moda[density]=",moda(data["density"]))
print("Moda[pH]=",moda(data["pH"]))
print("Moda[sulphates]=",moda(data["sulphates"]))
print("Moda[alcohol]=",moda(data["alcohol"]))
print("Moda[quality]=",moda(data["quality"]))

print("-------------------")

print("Media[fixed acidity]=",media(data["fixed acidity"]))
print("Media[citric acid]=",media(data["citric acid"]))
print("Media[residual sugar]=",media(data["residual sugar"]))
print("Media[chlorides]=",media(data["chlorides"]))
print("Media[free sulfur dioxide]=",media(data["free sulfur dioxide"]))
print("Media[total sulfur dioxide]=",media(data["total sulfur dioxide"]))
print("Media[density]=",media(data["density"]))
print("Media[pH]=",media(data["pH"]))
print("Media[sulphates]=",media(data["sulphates"]))
print("Media[alcohol]=",media(data["alcohol"]))
print("Media[quality]=",media(data["quality"]))

print("-------------------")

print("Desviacion[fixed acidity]=",std(data["fixed acidity"]))
print("Desviacion[citric acid]=",std(data["citric acid"]))
print("Desviacion[residual sugar]=",std(data["residual sugar"]))
print("Desviacion[chlorides]=",std(data["chlorides"]))
print("Desviacion[free sulfur dioxide]=",std(data["free sulfur dioxide"]))
print("Desviacion[total sulfur dioxide]=",std(data["total sulfur dioxide"]))
print("Desviacion[density]=",std(data["density"]))
print("Desviacion[pH]=",std(data["pH"]))
print("Desviacion[sulphates]=",std(data["sulphates"]))
print("Desviacion[alcohol]=",std(data["alcohol"]))
print("Desviacion[quality]=",std(data["quality"]))