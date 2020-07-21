# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:23:29 2020

@author: Jeff
"""


lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(
    lista_numeros)

series_b = pd.Series(
    tupla_numeros)

series_c = pd.Series(
    np_numeros)

series_d = pd.Series(
    [True,
    False,
    12,
    12.12,
    "Adrian",
    None,
    (1),
    [2],
    {"nombre":"Adrian"}
    ])

print(series_d[3])