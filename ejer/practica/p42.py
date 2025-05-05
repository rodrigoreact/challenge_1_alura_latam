#5 - Crea un programa que, al ingresar un número cualquiera, genere una lista que contenga todos los números primos entre 1 y el número ingresado.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita un número al usuario
limite = int(input("Ingrese un número: "))

# Genera la lista de números primos entre 1 y el número ingresado
primos = [num for num in range(1, limite + 1) if es_primo(num)]

# Muestra el resultado
print(f"Números primos entre 1 y {limite}:")
print(primos)
