# 19 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin espacios en blanco al principio y al final.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita una frase al usuario
frase = input("Escribe una frase: ")

# Elimina los espacios al principio y al final
frase_limpia = frase.strip()

# Imprime la frase limpia
print(f"La frase sin espacios al inicio y al final es: '{frase_limpia}'")
