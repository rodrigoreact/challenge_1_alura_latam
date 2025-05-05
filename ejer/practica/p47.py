"""
Momento para los proyectos

10 - Un instituto de meteorología desea realizar un estudio de la temperatura media de cada mes del año. 
Para ello, debes crear un código que recoja y almacene esas temperaturas medias en una lista. 
Luego, calcula el promedio anual de las temperaturas y muestra todas las temperaturas por encima del promedio anual
y en qué mes ocurrieron, mostrando los meses por su nombre (Enero, Febrero, etc.).

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Lista con los nombres de los meses
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Lista para almacenar las temperaturas
temperaturas = []

# Recoger las temperaturas medias del año
print("Ingresa la temperatura media de cada mes del año:")
for mes in meses:
    temp = float(input(f"{mes}: "))
    temperaturas.append(temp)

# Calcular el promedio anual
promedio_anual = sum(temperaturas) / len(temperaturas)

# Mostrar el promedio anual
print(f"\nTemperatura promedio anual: {promedio_anual:.2f}°C")

# Mostrar meses con temperatura por encima del promedio
print("\nMeses con temperatura por encima del promedio anual:")
for i in range(12):
    if temperaturas[i] > promedio_anual:
        print(f"{meses[i]}: {temperaturas[i]:.2f}°C")
