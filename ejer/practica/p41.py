#4 - Recoge nuevamente 5 números enteros e imprime la lista en orden inverso al enviado.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

import random

# Generar una lista con 5 números enteros aleatorios entre 1 y 10
numeros = [random.randint(1, 10) for _ in range(5)]

# Imprimir la lista original
print("Lista original:", numeros)

# Imprimir la lista en orden inverso
print("Lista en orden inverso:", numeros[::-1])
