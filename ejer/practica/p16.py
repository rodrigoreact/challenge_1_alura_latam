#16 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en mayúsculas.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita una frase al usuario
frase = input("Escribe una frase: ")

# Convierte la frase a mayúsculas
frase_mayusculas = frase.upper()

# Imprime la frase en mayúsculas
print(f"La frase en mayúsculas es: {frase_mayusculas}")
