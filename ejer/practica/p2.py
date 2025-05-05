#1 - 2 - Crea un programa que solicite al usuario que escriba su nombre y edad, y luego imprima "Hola, [nombre], tienes [edad] años."

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita al usuario su nombre y edad
nombre = input("Por favor, escribe tu nombre: ")
edad = input("Por favor, escribe tu edad: ")

# Imprime un saludo con la edad
print(f"Hola, {nombre}, tienes {edad} años.")