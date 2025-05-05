# 5 - Crea un programa que solicite tres valores numéricos al usuario y luego imprima la suma de los tres valores.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')


# Solicita tres valores numéricos al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

# Calcula la suma
suma = num1 + num2 + num3

# Muestra el resultado
print(f"La suma de {num1}, {num2} y {num3} es {suma}.")
