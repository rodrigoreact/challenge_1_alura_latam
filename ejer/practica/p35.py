#11 - Escribe un programa que pida a la persona usuaria tres números que representan los lados de un triángulo. El programa debe informar si los valores pueden utilizarse para formar un triángulo y, en caso afirmativo, si es equilátero, isósceles o escaleno. Ten en cuenta algunas sugerencias:
"""
Tres lados forman un triángulo cuando la suma de cualesquiera dos lados es mayor que el tercero;
Triángulo Equilátero: tres lados iguales;
Triángulo Isósceles: dos lados iguales;
Triángulo Escaleno: tres lados diferentes..
"""
import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita los tres lados al usuario
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))

# Verifica si pueden formar un triángulo
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("\nLos lados pueden formar un triángulo.")
    
    # Clasifica el tipo de triángulo
    if lado1 == lado2 == lado3:
        print("Tipo de triángulo: Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Tipo de triángulo: Isósceles")
    else:
        print("Tipo de triángulo: Escaleno")
else:
    print("\nLos lados NO pueden formar un triángulo.")
