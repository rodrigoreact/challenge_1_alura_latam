"""
Momento para los proyectos

14 - Un equipo de científicos de datos está estudiando la diversidad biológica en un bosque. 
El equipo recopiló información sobre el número de especies de plantas y animales en cada área del bosque y almacenó estos datos en un diccionario.
En él, la clave describe el área de los datos y los valores en las listas corresponden a las especies de plantas y animales en esas áreas, respectivamente.

{'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}

Escribe un código para calcular el promedio de especies por área e identificar el área con la mayor diversidad biológica.
Sugerencia: utiliza las funciones incorporadas sum() y len().

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Datos de diversidad biológica
diversidad = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

# Diccionario para guardar los promedios por área
promedios = {}
mayor_diversidad = ''
mayor_total = 0

# Cálculo de promedios y búsqueda de la mayor diversidad
for area, especies in diversidad.items():
    total = sum(especies)  # plantas + animales
    promedio = total / 2
    promedios[area] = promedio
    
    if total > mayor_total:
        mayor_total = total
        mayor_diversidad = area

# Mostrar los promedios por área
print("Promedio de especies por área:")
for area, promedio in promedios.items():
    print(f"{area}: {promedio:.2f} especies")

# Mostrar el área con mayor diversidad
print(f"\nÁrea con mayor diversidad biológica: {mayor_diversidad} ({mayor_total} especies en total)")
