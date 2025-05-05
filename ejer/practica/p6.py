# 6 - Crea un programa que solicite dos valores numéricos al usuario y luego imprima la resta del primero menos el segundo valor.
import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita dos valores numéricos al usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Calcula la resta
resta = num1 - num2

# Muestra el resultado
print(f"La resta de {num1} menos {num2} es {resta}.")
