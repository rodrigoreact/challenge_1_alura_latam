# 13 - Crea un código que calcule e imprima el promedio ponderado de los números 5, 12, 20 y 15 con pesos respectivamente iguales a 1, 2, 3 y 4.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Valores y sus pesos
valores = [5, 12, 20, 15]
pesos = [1, 2, 3, 4]

# Calcula el promedio ponderado
suma_ponderada = sum(valor * peso for valor, peso in zip(valores, pesos))
suma_pesos = sum(pesos)
promedio_ponderado = suma_ponderada / suma_pesos

# Muestra el resultado
print(f"El promedio ponderado es {promedio_ponderado:.2f}")
