#12 - Un establecimiento está vendiendo combustibles con descuentos variables.
#  Para el etanol, si la cantidad comprada es de hasta 15 litros, el descuento será del 2% por litro. 
# En caso contrario, será del 4% por litro. Para el diésel, si la cantidad comprada es de hasta 15 litros,
#  el descuento será del 3% por litro. En caso contrario, será del 5% por litro. El precio por litro de diésel es de R$ 2,00 y 
# el precio por litro de etanol es de R$ 1,70. Escribe un programa que lea la cantidad de litros vendidos y el tipo de combustible 
# (E para etanol y D para diésel) y calcule el valor a pagar por el cliente. Ten en cuenta algunas sugerencias:

"""
El valor del descuento será el producto del precio por litro, la cantidad de litros y el valor del descuento.
El valor a pagar por un cliente será el resultado de la multiplicación del precio por litro por la cantidad de litros
menos el valor del descuento resultante del cálculo.
"""
import os

# Limpia la pantalla (solo funciona en terminales compatibles)
os.system('cls' if os.name == 'nt' else 'clear')

# Precios por litro
precio_etanol = 1.70
precio_diesel = 2.00

# Solicita datos al usuario
litros = float(input("Ingrese la cantidad de litros vendidos: "))
tipo = input("Ingrese el tipo de combustible (E para etanol, D para diésel): ").strip().upper()

# Verifica tipo de combustible y calcula el valor
if tipo == 'E':
    precio_litro = precio_etanol
    descuento_porcentaje = 0.02 if litros <= 15 else 0.04
elif tipo == 'D':
    precio_litro = precio_diesel
    descuento_porcentaje = 0.03 if litros <= 15 else 0.05
else:
    print("Tipo de combustible inválido.")
    exit()

# Cálculos
valor_bruto = litros * precio_litro
descuento = valor_bruto * descuento_porcentaje
valor_final = valor_bruto - descuento

# Resultados
print(f"\nTipo de combustible: {'Etanol' if tipo == 'E' else 'Diésel'}")
print(f"Cantidad de litros: {litros} L")
print(f"Precio sin descuento: R$ {valor_bruto:.2f}")
print(f"Descuento aplicado: R$ {descuento:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
