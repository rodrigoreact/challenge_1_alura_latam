#2 - Escribe un programa que solicite el porcentaje de crecimiento de producción de una empresa e 
# informe si hubo un crecimiento (porcentaje positivo) o una disminución (porcentaje negativo).

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita el porcentaje de crecimiento de producción
porcentaje = float(input("Ingrese el porcentaje de crecimiento de la producción: "))

# Verifica si fue crecimiento, disminución o sin cambio
if porcentaje > 0:
    print("Hubo un crecimiento en la producción.")
elif porcentaje < 0:
    print("Hubo una disminución en la producción.")
else:
    print("La producción se mantuvo sin cambios.")
