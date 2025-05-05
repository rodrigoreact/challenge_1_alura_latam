#5 - Escribe un programa que pregunte sobre el precio de tres productos e indique cuál es el producto más barato para comprar.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita los precios de tres productos
precio1 = float(input("Ingrese el precio del producto 1: "))
precio2 = float(input("Ingrese el precio del producto 2: "))
precio3 = float(input("Ingrese el precio del producto 3: "))

# Verifica cuál es el más barato
if precio1 < precio2 and precio1 < precio3:
    print("Debe comprar el producto 1, es el más barato.")
elif precio2 < precio1 and precio2 < precio3:
    print("Debe comprar el producto 2, es el más barato.")
elif precio3 < precio1 and precio3 < precio2:
    print("Debe comprar el producto 3, es el más barato.")
else:
    print("Hay dos o más productos con el mismo precio más barato.")
