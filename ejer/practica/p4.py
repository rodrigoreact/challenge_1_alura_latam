# 4 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la suma de ambos valores.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')



# Solicita dos valores numéricos al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Calcula la suma
suma = num1 + num2

# Muestra el resultado
print(f"La suma de {num1} y {num2} es {suma}.")


