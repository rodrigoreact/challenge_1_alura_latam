# 20 - Crea un código que solicite una frase al usuario y luego imprima la misma frase sin 
# espacios en blanco al principio entre medio y al final, además de convertirla a minúsculas.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita una frase al usuario
frase = input("Escribe una frase: ")

# Limpia la frase: elimina espacios y convierte a minúsculas
frase_procesada = frase.strip().lower().replace(" ", "")

# Imprime la frase procesada
print(f"Frase sin espacios y en minúsculas: '{frase_procesada}'")
