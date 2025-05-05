#3 - Crea un código que recoja en una lista 5 números enteros aleatorios e imprima la lista. Ejemplo: [1, 4, 7, 2, 4].

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

import random

# Generar una lista con 5 números enteros aleatorios entre 1 y 10 (puedes ajustar el rango)
numeros_aleatorios = [random.randint(1, 10) for _ in range(7)]

# Imprimir la lista
print("Lista de números aleatorios:", numeros_aleatorios)
