#9 - Escribe un programa que pida un número a la persona usuaria y le informe si es entero o decimal.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita un número al usuario
numero = input("Ingrese un número: ")

# Intenta convertir a número flotante
try:
    numero_float = float(numero)
    
    # Verifica si es entero
    if numero_float.is_integer():
        print("El número es entero.")
    else:
        print("El número es decimal.")

except ValueError:
    print("Entrada inválida. Por favor, ingrese un número válido.")
