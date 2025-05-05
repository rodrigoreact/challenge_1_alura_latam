"""
Momento para los proyectos

11 - Una empresa de comercio electrónico está interesada en analizar las ventas de sus productos.
Los datos de ventas se han almacenado en un diccionario:

{'Producto A': 300, 'Producto B': 80, 'Producto C': 60, 'Producto D': 200, 'Producto E': 250, 'Producto F': 30}

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

# Mostrar ventas por producto
print("Ventas por producto:")
for producto, cantidad in ventas.items():
    print(f"{producto}: {cantidad} unidades")

# Calcular total de ventas
total_ventas = sum(ventas.values())
print(f"\nTotal de ventas: {total_ventas} unidades")

# Identificar producto más y menos vendido
producto_mas_vendido = max(ventas, key=ventas.get)
producto_menos_vendido = min(ventas, key=ventas.get)

print(f"\nProducto más vendido: {producto_mas_vendido} ({ventas[producto_mas_vendido]} unidades)")
print(f"Producto menos vendido: {producto_menos_vendido} ({ventas[producto_menos_vendido]} unidades)")
