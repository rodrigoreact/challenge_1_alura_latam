#3 - Escribe un programa que determine si una letra proporcionada por la persona usuaria es una vocal o una consonante.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita una letra al usuario
letra = input("Ingrese una letra: ").lower()

# Verifica si es una única letra del alfabeto
if len(letra) == 1 and letra.isalpha():
    if letra in 'aeiou':
        print("Es una vocal.")
    else:
        print("Es una consonante.")
else:
    print("Entrada inválida. Por favor, ingrese solo una letra.")
