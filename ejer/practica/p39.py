#2 - Con los mismos datos de la pregunta anterior, 
# determina cuántas compras se realizaron por encima de 3000 reales y calcula el porcentaje con respecto al total de compras.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Lista de gastos mensuales de la empresa
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

# Cuenta las compras por encima de R$ 3000
compras_mayores_3000 = [gasto for gasto in gastos if gasto > 3000]
cantidad_mayores_3000 = len(compras_mayores_3000)

# Calcula el porcentaje respecto al total
total_compras = len(gastos)
porcentaje = (cantidad_mayores_3000 / total_compras) * 100

# Muestra los resultados
print(f"Cantidad de compras mayores a R$ 3000: {cantidad_mayores_3000}")
print(f"Porcentaje respecto al total de compras: {porcentaje:.2f}%")
