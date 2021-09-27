# -*- coding: utf-8 -*-
"""
@author: Alvaro Quisbert Mamani
"""

import pandas as pd
data = pd.read_csv("feminicidio.csv",sep=",",header=[0])
print(data)

def moda(columna):
    #print(columna.value_counts())
    contarunicosindice=columna.value_counts().index.tolist()
    #contarunicosvalor=columna.value_counts().tolist()
    return contarunicosindice[0]
    

print("Moda[Departamento]=",moda(data["Departamento"]))
print("Moda[Area]=",moda(data["Area"]))
print("Moda[Relación]=",moda(data["Relación"]))
print("Moda[Hijos]=",moda(data["Hijos"]))
print("Moda[Victima]=",moda(data["Victima"]))
print("Moda[Denunciado]=",moda(data["Denunciado"]))
