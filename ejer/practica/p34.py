#10 - Un programa debe ser escrito para leer dos números y luego preguntar a la persona usuaria qué operación desea realizar. 
# El resultado de la operación debe incluir información sobre el número, si es par o impar, positivo o negativo, e entero o decimal.

import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Solicita dos números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Muestra las operaciones disponibles
print("\nOperaciones disponibles:")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")

# Solicita la operación deseada
opcion = input("Seleccione el número de la operación que desea realizar: ")

# Realiza la operación seleccionada
if opcion == "1":
    resultado = num1 + num2
    operacion = "Suma"
elif opcion == "2":
    resultado = num1 - num2
    operacion = "Resta"
elif opcion == "3":
    resultado = num1 * num2
    operacion = "Multiplicación"
elif opcion == "4":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
        exit()
    resultado = num1 / num2
    operacion = "División"
else:
    print("Opción inválida.")
    exit()

# Muestra el resultado de la operación
print(f"\nResultado de la {operacion}: {resultado}")

# Clasificaciones:
# Par o impar (solo aplica si es número entero)
if resultado.is_integer():
    if int(resultado) % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
else:
    print("El número es decimal (no se evalúa par/impar).")

# Positivo o negativo
if resultado > 0:
    print("El número es positivo.")
elif resultado < 0:
    print("El número es negativo.")
else:
    print("El número es cero (ni positivo ni negativo).")

# Entero o decimal
if resultado.is_integer():
    print("El número es entero.")
else:
    print("El número es decimal.")









