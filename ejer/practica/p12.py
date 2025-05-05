# 12 - Crea un código que solicite las 3 notas de un estudiante e imprima el promedio de las notas.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita las tres notas del estudiante
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

# Calcula el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Muestra el resultado
print(f"El promedio de las notas es {promedio:.2f}")
