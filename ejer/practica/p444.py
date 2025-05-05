"""
Momento para los proyectos

7 - Para un estudio sobre la multiplicación de bacterias en una colonia, se recopiló el número de bacterias 
multiplicadas por día y se puede observar a continuación: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. 
Con estos valores, crea un código que genere una lista que contenga el porcentaje de crecimiento de bacterias por día, comparando el número de bacterias en cada día con el número de bacterias del día anterior. Sugerencia: para calcular el porcentaje de crecimiento, utiliza la siguiente ecuación: 100 * (muestra_actual - muestra_anterior) / muestra_anterior.

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')


# Lista con número de bacterias por día
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

# Lista para porcentajes de crecimiento, iniciamos con 0 para el Día 1
crecimientos = [0.0]  # Día 1 no tiene día anterior, así que el crecimiento es 0

# Calcular crecimiento desde el Día 2 en adelante
for i in range(1, len(bacterias)):
    anterior = bacterias[i - 1]
    actual = bacterias[i]
    crecimiento = 100 * (actual - anterior) / anterior
    crecimientos.append(crecimiento)

# Mostrar resultados
print("Porcentaje de crecimiento por día:")
for i, porcentaje in enumerate(crecimientos, start=1):
    print(f"Día {i}: {porcentaje:.2f}%")
