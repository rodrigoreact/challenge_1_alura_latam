"""
Momento para los proyectos

12 - Se realizó una encuesta de mercado para decidir cuál diseño de marca infantil es más atractivo para los niños. Los votos de la encuesta se pueden ver a continuación:

Tabla de votos de la marca
Diseño 1 - 1334 votos
Diseño 2 - 982 votos
Diseño 3 - 1751 votos
Diseño 4 - 210 votos
Diseño 5 - 1811 votos
Copia el código
Adapta los datos proporcionados a una estructura de diccionario. A partir de ello, informa el diseño ganador y el porcentaje de votos recibidos.

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Diccionario con los votos de cada diseño
votos = {
    'Diseño 1': 1334,
    'Diseño 2': 982,
    'Diseño 3': 1751,
    'Diseño 4': 210,
    'Diseño 5': 1811
}

# Calcular el total de votos
total_votos = sum(votos.values())

# Identificar el diseño ganador
ganador = max(votos, key=votos.get)
votos_ganador = votos[ganador]

# Calcular el porcentaje de votos del diseño ganador
porcentaje = (votos_ganador / total_votos) * 100

# Mostrar resultados
print(f"Diseño ganador: {ganador}")
print(f"Votos recibidos: {votos_ganador}")
print(f"Porcentaje de votos: {porcentaje:.2f}%")
