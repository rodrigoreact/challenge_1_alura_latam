# 17 - Crea un código que solicite una frase al usuario y luego imprima la misma frase ingresada pero en minúsculas.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita una frase al usuario
frase = input("Escribe una frase: ")

# Convierte la frase a minúsculas
frase_minusculas = frase.lower()

# Imprime la frase en minúsculas
print(f"La frase en minúsculas es: {frase_minusculas}")
