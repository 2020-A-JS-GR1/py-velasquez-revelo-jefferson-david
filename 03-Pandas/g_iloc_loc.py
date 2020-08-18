#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:59:24 2020

@author: dev-11
"""
# g_iloc_loc.py

import pandas as pd

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

# loc

# primero = df.loc[1035]
# segundo = df.loc[1035, 'artist']

filtrado_horizontal = df.loc[1035] # Serie
print(filtrado_horizontal)
print(filtrado_horizontal['artist'])
print(filtrado_horizontal.index) # Indices columnas

serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index) # Indices son los Indices

# Filtrado por indice
df_1035 = df[df.index == 1035]

# loc -> acceder grupo filas y columnas x LABEL (ARR TRUE FALSE)

segundo = df.loc[1035]  # Filtrar por indice (1)
segundo = df.loc[[1035,1036]] # Filtrar por arr indices

segundo = df.loc[3:5] # Filtrando desde x indice
                      # hasta y indice
segundo = df.loc[df.index == 1035] # Filtrar por 
                                   # Arreglo-> True False


segundo = df.loc[1035, 'artist'] # 1 Indice
segundo = df.loc[1035, ['artist', 'medium']] # Varios indices
segundo = df.loc[1035, ['artist', 'medium']]

# print(df.loc[0]) # Indice dentro del DataFrame X ERROR
# print(df[0]) # Indice dentro del DataFrame X ERROR

# iloc -> acceder grupo filas y columnas indices en 0

tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]


tercero = df.iloc[0:10, 0:4] # Filtrado indices
                             # Por rango de indice 0:4


###########
datos = {
    "nota_1":{
            "Pepito": 7,
            "Juanita": 9,
            "Maria":8
        },
    "nota_2":{
            "Pepito": 7,
            "Juanita": 9,
            "Maria":8
        },
    "disciplina":{
        
            "Pepito": 4,
            "Juanita": 9,
            "Maria": 2
        }
    }

notas = pd.DataFrame(datos)

condicion_nota = notas["nota_1"] <= 7
condicion_nota_2 = notas["nota_2"] <= 7
condicion_disciplina = notas["disciplina"] <= 7

mayores_siete = notas.loc[condicion_nota, ["nota_1"]]

no_pasaron = notas.loc[condicion_nota][condicion_nota_2][condicion_disciplina]
 
notas.loc["Maria", "disciplina"] = 7
notas.loc[:, "disciplina"] = 7

#### PROMEDIO DE LAS NOTAS (nota_1+nota_2+disciplina)/3
print("las notas")
print(notas)
promedio = (notas["nota_1"] + notas["nota_2"] + notas["disciplina"]) /3

print("El promedio es: ")
print(promedio)



















