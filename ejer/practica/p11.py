# 11 - Crea un programa que solicite dos valores numéricos, un numerador y un denominador, 
# y devuelva el resto de la división entre los dos valores. Asegúrate de que el valor del denominador no sea igual a 0.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita el numerador
numerador = int(input("Ingresa el numerador (entero): "))

# Solicita el denominador, asegurándose de que no sea 0
denominador = int(input("Ingresa el denominador (entero): "))
while denominador == 0:
    print("El denominador no puede ser 0. Intenta nuevamente.")
    denominador = int(input("Ingresa el denominador (entero): "))

# Calcula el resto (módulo)
resto = numerador % denominador

# Muestra el resultado
print(f"El resto de dividir {numerador} entre {denominador} es {resto}.")
