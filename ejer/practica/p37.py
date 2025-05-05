#13 - En una empresa de venta de bienes raíces, debes crear un código que analice los datos de ventas anuales
#  para ayudar a la dirección en la toma de decisiones. 
# El código debe recopilar los datos de cantidad de ventas durante los años 2022 y 2023 y calcular la variación porcentual.
#  A partir del valor de la variación, se deben proporcionar las siguientes sugerencias:

"""
Para una variación superior al 20%: bonificación para el equipo de ventas.
Para una variación entre el 2% y el 20%: pequeña bonificación para el equipo de ventas.
Para una variación entre el 2% y el -10%: planificación de políticas de incentivo a las ventas.
Para bonificaciones inferiores al -10%: recorte de gastos.
"""
import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita las cantidades de ventas para cada año
ventas_2022 = int(input("Ingrese la cantidad de ventas en 2022: "))
ventas_2023 = int(input("Ingrese la cantidad de ventas en 2023: "))

# Verifica que ventas_2022 no sea cero para evitar división por cero
if ventas_2022 == 0:
    print("No se puede calcular la variación porque las ventas de 2022 son cero.")
else:
    # Calcula la variación porcentual
    variacion = ((ventas_2023 - ventas_2022) / ventas_2022) * 100

    # Muestra la variación
    print(f"\nVariación porcentual: {variacion:.2f}%")

    # Evalúa y da una sugerencia basada en la variación
    if variacion > 20:
        print("Sugerencia: Bonificación para el equipo de ventas.")
    elif 2 < variacion <= 20:
        print("Sugerencia: Pequeña bonificación para el equipo de ventas.")
    elif -10 <= variacion <= 2:
        print("Sugerencia: Planificación de políticas de incentivo a las ventas.")
    else:
        print("Sugerencia: Recorte de gastos.")
