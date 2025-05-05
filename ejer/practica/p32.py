#8 - Escribe un programa que solicite un número entero a la persona usuaria y
#  determine si es par o impar. Pista: Puedes usar el operador módulo (%).

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita un número entero
numero = int(input("Ingrese un número entero: "))

# Verifica si es par o impar usando el operador módulo
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
