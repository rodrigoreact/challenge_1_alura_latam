"""
Momento para los proyectos

9 - Desarrolla un programa que informe la puntuación de un estudiante de acuerdo con sus respuestas. 
Debe pedir la respuesta del estudiante para cada pregunta y verificar si la respuesta coincide con el resultado.
Cada pregunta vale un punto y hay opciones A, B, C o D.

Resultado del examen:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Respuestas correctas del examen
respuestas_correctas = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

# Inicializar contador de puntuación
puntuacion = 0

print("Responde a las 10 preguntas con A, B, C o D:")

# Ciclo para obtener las respuestas del estudiante
for i in range(10):
    respuesta = input(f"Pregunta {i+1}: ").strip().upper()
    if respuesta == respuestas_correctas[i]:
        puntuacion += 1

# Mostrar resultado final
print(f"\nPuntuación total del estudiante: {puntuacion}/10")
