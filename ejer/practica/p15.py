# 15 - Crea un código que solicite una frase y luego imprima la frase en pantalla.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita una frase al usuario
frase = input("Escribe una frase: ")

# Imprime la frase
print(f"La frase ingresada es: {frase}")
