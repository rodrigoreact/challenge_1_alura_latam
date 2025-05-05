import pandas as pd

# Ruta corregida usando raw string para evitar errores con las barras
archivo = r'C:\Users\User\Desktop\challenge_1\challenge_1\tienda_1.xlsx'

# Cargar el archivo Excel
df = pd.read_excel(archivo)

# Mostrar los nombres reales de las columnas
print("Columnas disponibles en el archivo:")
print(df.columns)

# 👇 Reemplaza 'Valor Venta' por el nombre correcto según lo que imprima la línea anterior
# Por ejemplo: 'Total', 'Total Venta', etc.
# ventas_totales = df['Valor Venta'].sum()

# Si identificas la columna correcta, por ejemplo 'Total', haz esto:
# ventas_totales = df['Total'].sum()
# print(f"Ventas totales: {ventas_totales}")
