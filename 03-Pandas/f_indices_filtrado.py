#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:32:31 2020

@author: dev-11
"""
# f_indices_filtrado.py


import pandas as pd

path_guardado = "/home/dev-11/Documents/Github/py-eguez-sarzosa-vicente-adrian/03 - Pandas/data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas)) # Numpy Array

print(artistas.size)
print(len(artistas))

blake = df['artist'] == 'Blake, William' # Serie

print(blake.value_counts())

df_blake = df[blake] # DataFrame



















