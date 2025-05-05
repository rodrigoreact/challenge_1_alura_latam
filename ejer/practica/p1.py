import os
#1 - Crea un programa que solicite al usuario que escriba su nombre y luego imprima "Hola, [nombre].

# Limpia la pantalla
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita al usuario que escriba su nombre
nombre = input("Por favor, escribe tu nombre: ")

# Imprime un saludo personalizado
print(f"Hola, {nombre}.")
