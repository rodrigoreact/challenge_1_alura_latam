#6 - Escribe un programa que lea tres números y los muestre en orden descendente.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Coloca los números en una lista
numeros = [num1, num2, num3]

# Ordena la lista en orden descendente
numeros.sort(reverse=True)

# Muestra los números ordenados
print("\nNúmeros en orden descendente:")
for num in numeros:
    print(num)
