#1Vamos practicar el uso de estructuras de datos, como listas y diccionarios, a través de algunas actividades.
# Ahora que estamos avanzando en el contenido, podemos hacer los desafíos más interesantes. ¡Para ello, trabajaremos con proyectos de código!
""""
Primero, resolveremos algunos problemas para calentar y prepararnos para los proyectos.

Entrenando la programación

1 - Crea un programa que tenga la siguiente lista con los gastos de una empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Con estos valores, crea un programa que calcule el promedio de gastos. Sugerencia: usa las funciones integradas sum() y len().
"""
import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Lista de gastos mensuales de la empresa
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Calcula el total y el promedio
total_gastos = sum(gastos)
promedio_gastos = total_gastos / len(gastos)

# Muestra el promedio
print(f"El promedio de gastos es: R$ {promedio_gastos:.2f}")
