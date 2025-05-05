# 8 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador,
# y realice la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita el numerador
numerador = float(input("Ingresa el numerador: "))

# Solicita el denominador, asegurándose de que no sea 0
denominador = float(input("Ingresa el denominador: "))
while denominador == 0:
    print("El denominador no puede ser 0. Intenta nuevamente.")
    denominador = float(input("Ingresa el denominador: "))

# Realiza la división
resultado = numerador / denominador

# Muestra el resultado
print(f"La división de {numerador} entre {denominador} es {resultado}.")
