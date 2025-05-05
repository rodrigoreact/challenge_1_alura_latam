#1 - 3 - Crea un programa que solicite al usuario que escriba su nombre, edad y altura en metros, 
# y luego imprima "Hola, [nombre], tienes [edad] años y mides [altura] metros."

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita al usuario su nombre, edad y altura
nombre = input("Por favor, escribe tu nombre: ")
edad = input("Por favor, escribe tu edad: ")
altura = input("Por favor, escribe tu altura en metros (por ejemplo, 1.75): ")

# Imprime el mensaje personalizado
print(f"Hola, {nombre}, tienes {edad} años y mides {altura} metros.")
