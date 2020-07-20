# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 21:02:22 2020

@author: Jeff
"""


import numpy as np
from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt

image = misc.face()
divY = 0
divX = 0

def cutPuzzle(image_to_cut):
    vertical_slices = np.array_split(image_to_cut, divY)
    handler = 0
    image_slices = np.zeros([int(image_pieces), int(image.shape[0] / divY), int(image.shape[1] / divX), 3], dtype=int)
    for slice in vertical_slices:
        horizontal_slices = np.hsplit(slice, divX)
        for h_slice in horizontal_slices:
            image_slices[handler] = h_slice
            handler += 1
    return image_slices

def getMinPrime(number, factor):
    if(number / factor == 1):
        return factor
    elif(number % factor == 0):
        return getMinPrime(number / factor, 2)
    else:
        return getMinPrime(number, factor + 1)
        
def generatePuzzle(image_pieces):
    global divX
    global divY
    divY = getMinPrime(int(image_pieces), 2)
    divX = int(int(image_pieces) / divY)
    image_slices = cutPuzzle(image)
    np.random.shuffle(image_slices)
    return rebuildPuzzle(image_slices)

def rebuildPuzzle(image_slices):
    puzzle = np.zeros([divY, int(image.shape[0] / divY), image.shape[1], 3], dtype=int)
    for i in range(1, divY + 1):
        puzzle[i - 1] = np.concatenate(image_slices[(i -1) * divX: i * divX], 1)
    puzzle_final = np.concatenate(puzzle, 0)
    return puzzle_final

def showPuzzle():
    plt.figure(1)
    plt.subplot(121)
    plt.imshow(puzzle)
    plt.subplot(122)
    plt.imshow(image)
    plt.show()

def movement_menu():
    print("Seleccione el desplazamiento de la pieza:")
    print("1. Arriba")
    print("2. Abajo")
    print("3. Izquierda")
    print("4. Derecha")
    return int(input("Seleccione una opción: "))

def movement(piece, order):
    actual_puzzle = cutPuzzle(puzzle)
    if(order == 1):
        toMove = (piece - divX) % int(image_pieces)
    elif(order == 2):
        toMove = (piece + divX) % int(image_pieces)
    elif(order == 3):
        toMove = (piece - 1) % int(image_pieces)
    else:
        toMove = (piece + 1) % int(image_pieces)
    actual_puzzle[[toMove, piece]] = actual_puzzle[[piece,toMove]] 
    return rebuildPuzzle(actual_puzzle)

def completed(puzzle):
    return np.array_equal(image, puzzle)

image_pieces = input("Ingrese el número de piezas: ")

puzzle = generatePuzzle(image_pieces)

while(not completed(puzzle)):
    showPuzzle()
    print("E.g:"+"\n"+
            "1 | 2"+"\n"+
            "3 | 4"+"\n")
    selected_piece = input(f"Seleccione una pieza del 1 al {image_pieces}: ")
    selected_movement = movement_menu()
    puzzle = movement(int(selected_piece) - 1, selected_movement)

showPuzzle()