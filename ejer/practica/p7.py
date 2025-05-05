# 7 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la multiplicación de los dos valores.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita dos valores numéricos al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Calcula la multiplicación
multiplicacion = num1 * num2

# Muestra el resultado
print(f"La multiplicación de {num1} por {num2} es {multiplicacion}.")
