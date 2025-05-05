"""
Momento para los proyectos

15 - El departamento de Recursos Humanos de tu empresa te pidió ayuda para analizar las edades de los colaboradores de 4 sectores de la empresa.
Para ello, te proporcionaron los siguientes datos:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

Dado que cada sector tiene 10 colaboradores, construye un código que calcule la media de edad de cada sector,
la edad media general entre todos los sectores y cuántas personas están por encima de la edad media general.

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Datos de edades por sector
edades = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

# Calcular y mostrar la media por sector
media_por_sector = {}
total_edades = []

for sector, lista in edades.items():
    media = sum(lista) / len(lista)
    media_por_sector[sector] = media
    total_edades.extend(lista)

# Calcular media general
media_general = sum(total_edades) / len(total_edades)

# Contar cuántas personas están por encima de la media general
por_encima_media = sum(1 for edad in total_edades if edad > media_general)

# Mostrar resultados
print("Media de edad por sector:")
for sector, media in media_por_sector.items():
    print(f"{sector}: {media:.2f} años")

print(f"\nMedia de edad general: {media_general:.2f} años")
print(f"Número de personas por encima de la media general: {por_encima_media}")
