#21 - Crea un código que solicite una frase al usuario y luego imprima la misma frase con todas las vocales "e" reemplazadas por la letra "f".

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')



# Solicita una frase al usuario
frase = input("Escribe una frase: ")

# Reemplaza todas las 'e' por 'f'
frase_modificada = frase.replace("e", "f")

# Imprime la frase modificada
print(f"Frase con 'e' reemplazadas por 'f': {frase_modificada}")
