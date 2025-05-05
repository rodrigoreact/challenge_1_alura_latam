#1 - Escribe un programa que pida a la persona usuaria que proporcione dos números y muestre el número más grande.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita dos números al usuario
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Compara los números y muestra el mayor
if numero1 > numero2:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1:
    print(f"El número mayor es: {numero2}")
else:
    print("Ambos números son iguales.")
