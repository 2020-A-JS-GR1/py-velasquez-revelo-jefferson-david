# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:51:05 2020

@author: Jeff
"""


#c_dataframes.py

import numpy as np
import pandas as pd

s2 = df[1]

s3 = df1[2]

df1[3] = s1

df1[4] = s1*s2

datos_fisicos_uno = pd.DataFrame(
        arr_pnd,
        columns = [
            'Estatura (cm)',
            'Peso (kg)',
            'Edad (anios)'])


datos_fisicos_dos = pd.DataFrame(
        arr_pnd,
        columns = [
            'Estatura (cm)',
            'Peso (kg)',
            'Edad (anios)'],
        index = ['Jeff', 'David'])

serie_peso = datos_fisicos_dos['Peso (kg)']
datos_jeff = serie_peso['Jeff']

print(serie_peso)
print(datos_jeff)

df1.index = ['Jeff', 'David']
df1.index = ['Nombre1', 'Apellido1']

df1.columns = ['A', 'B', 'C', 'D', 'E']





















