# 114 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. Luego, imprime la frase en pantalla.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Crea una variable con una frase
frase = "La programación en Python es divertida."

# Imprime la frase
print(frase)
