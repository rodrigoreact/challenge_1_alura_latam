"""
Momento para los proyectos

11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos.
Los datos de ventas se han almacenado en un diccionario:

{'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

Escribe un código que calcule el total de ventas y el producto más vendido.

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Diccionario con datos de ventas
ventas = {
    'Producto A': 300,
    'Producto B': 80,
    'Producto C': 60,
    'Producto D': 200,
    'Producto E': 250,
    'Producto F': 30
}

# Calcular el total de ventas
total_ventas = sum(ventas.values())

# Identificar el producto más vendido
producto_mas_vendido = max(ventas, key=ventas.get)

# Mostrar resultados
print(f"Total de ventas: {total_ventas} unidades")
print(f"Producto más vendido: {producto_mas_vendido} ({ventas[producto_mas_vendido]} unidades)")
