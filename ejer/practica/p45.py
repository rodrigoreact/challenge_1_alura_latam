"""
Momento para los proyectos

8 - Para una selección de productos alimenticios, debemos separar el conjunto de IDs proporcionados por números enteros, 
sabiendo que los productos con ID par son dulces y los que tienen ID impar son amargos. Crea un código que recoja 10 IDs.
Luego, calcula y muestra la cantidad de productos dulces y amargos.

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Inicializar contadores
dulces = 0
amargos = 0

# Recoger 10 IDs del usuario
print("Ingresa 10 IDs de productos (números enteros):")
for i in range(10):
    id_producto = int(input(f"ID {i+1}: "))
    if id_producto % 2 == 0:
        dulces += 1
    else:
        amargos += 1

# Mostrar resultados
print(f"\nCantidad de productos dulces: {dulces}")
print(f"Cantidad de productos amargos: {amargos}")
