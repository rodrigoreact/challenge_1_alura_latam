# 9 - Crea un programa que solicite dos valores numéricos, un operador y una potencia, y realice la exponenciación entre estos dos valores.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita la base y el exponente
base = float(input("Ingresa la base: "))
exponente = float(input("Ingresa el exponente: "))

# Calcula la potencia
resultado = base ** exponente

# Muestra el resultado
print(f"{base} elevado a la potencia {exponente} es {resultado}.")
