#6 - Escribe un programa que pida una fecha, especificando el día, mes y año, y determine si es válida para su análisis.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

import datetime

# Solicita la fecha al usuario
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

# Intenta crear la fecha
try:
    fecha = datetime.date(año, mes, dia)
    print(f"La fecha {fecha.strftime('%d/%m/%Y')} es válida.")
except ValueError:
    print("La fecha ingresada no es válida.")
