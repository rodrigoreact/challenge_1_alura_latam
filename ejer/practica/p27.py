#4 - Escribe un programa que lea valores promedio de precios de un modelo de automóvil 
# durante 3 años consecutivos y muestre el valor más alto y más bajo entre esos tres años.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita los promedios de precios durante 3 años
precio1 = float(input("Ingrese el promedio de precio del primer año: "))
precio2 = float(input("Ingrese el promedio de precio del segundo año: "))
precio3 = float(input("Ingrese el promedio de precio del tercer año: "))

# Guarda los valores en una lista para facilitar el análisis
precios = [precio1, precio2, precio3]

# Encuentra el valor más alto y más bajo
precio_max = max(precios)
precio_min = min(precios)

# Muestra los resultados
print(f"\nEl valor más alto es: {precio_max}")
print(f"El valor más bajo es: {precio_min}")
