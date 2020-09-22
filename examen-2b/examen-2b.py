#  Examen

import numpy as np
import pandas as pd
import random
import string

## 1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros


ej_1 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

df_primeros = ej_1.head(5)

df_ultimos = ej_1.tail(5)


print(df_primeros)
print("\n")
print(df_primeros)
print("\n")

## 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico

'''
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401
2013-01-06 -0.673690  0.113648 -1.478427  0.524988

'''

arreglo_6_4 = np.random.uniform(0,1000,size=(6, 4))

columnas_fechas = pd.date_range('2020-01-24', '2030-01-24', 6)

ej_2 = pd.DataFrame(arreglo_6_4, columns=list('ABCD'), index=columnas_fechas)

print(ej_2)
print("\n")

## 4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.


ej_4 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

columnas_4 = ej_4.columns
print(columnas_4)

valores_4 = ej_4.values
print(valores_4)


print("\n")

## 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe

ej_5 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

estadisticas = ej_5.describe()

print(estadisticas)
print("\n")

## 6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos


ej_6 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

transpuesta = ej_6.transpose()

print(transpuesta)
print("\n")

## 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente

ej_7 = pd.DataFrame(np.random.randint(0,1000,size=(10, 6)), columns=list('ABCDEF'))

ej_7_per_A_asc = ej_7.sort_values('A')
ej_7_per_A_desc = ej_7.sort_values('A', ascending=False)
print(ej_7_per_A_asc)

ej_7_per_B_asc = ej_7.sort_values('B')
ej_7_per_B_desc = ej_7.sort_values('B', ascending=False)
print(ej_7_per_B_desc)

ej_7_per_C_asc = ej_7.sort_values('C')
ej_7_per_C_desc = ej_7.sort_values('C', ascending=False)
print(ej_7_per_C_desc)

ej_7_per_D_asc = ej_7.sort_values('D')
ej_7_per_D_desc = ej_7.sort_values('D', ascending=False)
print(ej_7_per_D_desc)

ej_7_per_E_asc = ej_7.sort_values('E')
ej_7_per_E_desc = ej_7.sort_values('E', ascending=False)
print(ej_7_per_E_desc)

ej_7_per_F_asc = ej_7.sort_values('F')
ej_7_per_F_desc = ej_7.sort_values('F', ascending=False)
print(ej_7_per_F_desc)

print("\n")

## 8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7

ej_8 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_filtered = ej_8.where(ej_8> 7)

print(df_filtered)
print("\n")

## 9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.

ej_9 = pd.DataFrame(np.random.randint(1,100,size=(10, 6)), columns=list('ABCDEF'))

ej_9 = ej_9.where(ej_9 < 90)

ej_9 = ej_9.fillna(0)

print(ej_9)
print("\n")

## 10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio

ej_10 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_mean = ej_10.mean().mean()
print(df_mean)

df_median = ej_10.median().median()
print(df_median)

print("\n")

## 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe

ej_11 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_11_2 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_result = ej_11.append(df_11_2)

print(df_result)
print("\n")
## 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.

lista_strings = []

for i in range(60):
    lista_strings.append(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)))

ej_12 = pd.DataFrame(np.array(lista_strings).reshape(10,6), columns=list('ABCDEF'))

df_result_12 = pd.DataFrame()

df_result_12['A'] = ej_12['A'] + ej_12['B'] 

df_result_12['B'] = ej_12['C'] + ej_12['D']

df_result_12['C'] = ej_12['E'] + ej_12['F']

print(df_result_12)
print("\n")
## 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna


ej_13 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df_freq_A = ej_13['A'].value_counts()
df_freq_B = ej_13['B'].value_counts()
df_freq_C = ej_13['C'].value_counts()
df_freq_D = ej_13['D'].value_counts()
df_freq_E = ej_13['E'].value_counts()
df_freq_F = ej_13['F'].value_counts()

print(df_freq_F)
print("\n")
## 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C

ej_14 = pd.DataFrame(np.random.randint(1,10,size=(10, 3)), columns=list('ABC'))

ej_14['D'] = ej_14['A'] * ej_14['B'] / ej_14['C']

print(ej_14)
print("\n")