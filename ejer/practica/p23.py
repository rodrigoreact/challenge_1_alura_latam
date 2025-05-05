#23 - Crea un código que solicite una frase al usuario y 
# luego imprima la misma frase con todas las consonantes "s" reemplazadas por el carácter "$".

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita una frase al usuario
frase = input("Escribe una frase: ")

# Reemplaza todas las 's' por '$'
frase_modificada = frase.replace("s", "$")

# Imprime la frase modificada
print(f"Frase con 's' reemplazadas por '$': {frase_modificada}")
