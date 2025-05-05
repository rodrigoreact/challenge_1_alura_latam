# 118 - Crea una variable llamada "frase" y asígnale una cadena de texto de tu elección. 
# Luego, imprime la frase sin espacios en blanco al principio y al final.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Crea una variable con espacios al principio y al final
frase = "   Aprender Python es útil.   "

# Elimina los espacios en blanco al principio y al final
frase_sin_espacios = frase.strip()

# Imprime la frase sin espacios
print(f"Frase sin espacios al inicio y al final: '{frase_sin_espacios}'")
