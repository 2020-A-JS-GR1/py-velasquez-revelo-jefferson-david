import numpy as np
from scipy import misc
import pandas as pd
import os

# 1) Examen

## 2) Crear un vector de ceros de tamaño 10

vector_zeros_2 = np.zeros(10)
print('2) --> ', vector_zeros_2)

## 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1

vector_zeros_3 = np.zeros(10)
vector_zeros_3[5] = 1

print('3) --> ', vector_zeros_3)

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.

vector_zeros_4 = np.arange(50)
vector_zeros_4 = vector_zeros_4[::-1]

print('4) --> ', vector_zeros_4)

## 5) Crear una matriz de 3 x 3 con valores del cero al 8

matriz = np.arange(9)
matriz = matriz.reshape((3,3))

print('5) --> ', matriz)

## 6) Encontrar los indices que no sean cero en un arreglo

arreglo_indices = [1,2,0,0,4,0]
arreglo_indices = np.array(arreglo_indices)

resultado = np.where(arreglo_indices != 0)[0]

print('6) --> ', resultado)

## 7) Crear una matriz de identidad 3 x 3 

matriz_identidad = np.eye(3)
print('7) --> ', matriz_identidad)

## 8) Crear una matriz 3 x 3 x 3 con valores randomicos

matriz_randomica = np.random.randint(27, size=27).reshape(3,3,3)
print('8) --> ', matriz_randomica)

## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor

matriz_diez = np.arange(100).reshape(10,10)

menor_valor = matriz_diez.min()
mayor_valor = matriz_diez.max()

print('9) menor --> ', menor_valor)
print('9) mayor --> ', mayor_valor)

## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)

imagen = misc.face()

resultado = len(np.unique(imagen, axis=0))
print('10) --> ', resultado)


## 11) ¿Como crear una serie de una lista, diccionario o arreglo?


mylist = list('abcdefghijklmnsopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie = pd.Series(mylist)
serie_diccionario = pd.Series(mydict)
serie_arreglo = pd.Series(myarr)


print('11) --> Serie de lista: ', serie, '\n')
print('11) --> Serie de diccionario: ', serie_diccionario, '\n')
print('11) --> Serie de arreglo ', serie_arreglo, '\n')


## 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 

df = pd.DataFrame(ser).reset_index()

# Transformar la serie en dataframe y hacer una columna indice

df1 = pd.DataFrame(ser, index=['a'])


## 13) ¿Como combinar varias series para hacer un DataFrame?


ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df_combinado = pd.concat([ser1, ser2], axis = 1)
df_combinado = pd.DataFrame(df_combinado)

print('13) --> ', df_combinado)

## 14) ¿Como obtener los items que esten en una serie A y no en una serie B?


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

items_diferencia = np.setdiff1d(ser1, ser2)
print('14) --> ', items_diferencia)

## 15) ¿Como obtener los items que no son comunes en una serie A y serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

items_conjuncion = set(ser1) ^ set(ser2)
items_conjuncion = list(items_conjuncion)
items_conjuncion = pd.Series(items_conjuncion)

print('15) --> ', items_conjuncion, '\n')

## 16) ¿Como obtener el numero de veces que se repite un valor en una serie?

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

repeticiones, contador = np.unique(ser, return_counts=True)
repeticiones = dict(zip(repeticiones, contador))

print(repeticiones)
print(contador)

print('16) --> ', repeticiones, '\n')


## 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

valores_repetidos, contador = np.unique(ser, return_counts=True)

print('serie --> ', ser)
print('contador --> ', ser)
indice = np.argsort(-contador)
print('indice --> ', indice)
valores_repetidos = valores_repetidos[indice]

valores_repetidos[2:] = 0

print('17) --> Valores repetidos', valores_repetidos)

## 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?

ser = pd.Series(np.random.randint(1, 10, 35))

df_shape = pd.DataFrame(ser.values.reshape(7,5))

print('18) --> ', df_shape)

## 19) ¿Obtener los valores de una serie conociendo la posicion por indice?

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u

resultado = ser[pos]

print('19) --> ', resultado)

## 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

#Verical
df1 = pd.concat([pd.DataFrame(),ser2], ignore_index = True)

#Horizontal
df2 = pd.DataFrame().append(ser1, ignore_index=True)

print('20) Vertical --> ', df1)
print('21) Horizontal --> ', df2)

## 21)¿Obtener la media de una serie agrupada por otra serie?

#`groupby` tambien esta disponible en series.

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64

media_agrupada = pd.concat([frutas, pesos], axis = 1)
media_agrupada = media_agrupada.groupby(media_agrupada[0], as_index=False)[1].mean()

print('21) --> \n', media_agrupada)


## 22)¿Como importar solo columnas especificas de un archivo csv?

#https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.

path = "./archivo.csv"

data_csv = pd.read_csv(
    path, 
    nrows = 10)

columnas = ['crim', 'zn', 'indus']

data_tres_columnas = pd.read_csv(path, nrows=10, usecols=columnas)

print('22) --> ', data_tres_columnas)

