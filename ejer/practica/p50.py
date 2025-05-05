"""
Momento para los proyectos

13 - Los empleados de un departamento de tu empresa recibirán una bonificación del 10% de su salario debido a un excelente rendimiento del equipo. 
El departamento de finanzas ha solicitado tu ayuda para verificar las consecuencias financieras de esta bonificación en los recursos. 
Se te ha enviado una lista con los salarios que recibirán la bonificación: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. 
La bonificación de cada empleado no puede ser inferior a 200. 
En el código, convierte cada uno de los salarios en claves de un diccionario y la bonificación de cada salario en el valor correspondiente.
Luego, informa el gasto total en bonificaciones, cuántos empleados recibieron la bonificación mínima y cuál fue el valor más alto de la bonificación proporcionada.

"""

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Lista de salarios
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

# Crear diccionario con bonificaciones
bonificaciones = {}
for salario in salarios:
    bonificacion = salario * 0.10
    if bonificacion < 200:
        bonificacion = 200
    bonificaciones[salario] = bonificacion

# Calcular total de bonificaciones
total_bonificaciones = sum(bonificaciones.values())

# Contar empleados con bonificación mínima
bonificacion_minima = 200
empleados_con_minima = sum(1 for b in bonificaciones.values() if b == bonificacion_minima)

# Obtener la mayor bonificación
bonificacion_mayor = max(bonificaciones.values())

# Mostrar resultados
print("Bonificaciones por salario:", bonificaciones)
print(f"\nGasto total en bonificaciones: R$ {total_bonificaciones:.2f}")
print(f"Cantidad de empleados con bonificación mínima (R$200): {empleados_con_minima}")
print(f"Mayor bonificación otorgada: R$ {bonificacion_mayor:.2f}")
