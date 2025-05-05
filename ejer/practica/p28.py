#4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil 
# durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita los precios promedio para cada año
precio1 = float(input("Ingrese el promedio de precio del año 1: "))
precio2 = float(input("Ingrese el promedio de precio del año 2: "))
precio3 = float(input("Ingrese el promedio de precio del año 3: "))

# Guardar precios en una lista
precios = [precio1, precio2, precio3]

# Encontrar el precio más alto y más bajo
precio_max = max(precios)
precio_min = min(precios)

# Encontrar el año correspondiente (índice + 1 para año humano)
anio_max = precios.index(precio_max) + 1
anio_min = precios.index(precio_min) + 1

# Mostrar resultados
print(f"\nEl valor más alto fue {precio_max} en el año {anio_max}")
print(f"El valor más bajo fue {precio_min} en el año {anio_min}")
