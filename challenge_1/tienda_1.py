import pandas as pd

# Cargar el archivo Excel
archivo =  'C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx'

df = pd.read_excel(archivo)

# Vista general del DataFrame (opcional para revisión)
# print(df.head())

# Ventas totales
ventas_totales = df['Valor Venta'].sum()

# Cantidad total de productos vendidos
productos_vendidos = len(df)

# Calificación promedio
calificacion_promedio = df['Calificación'].mean()

# Top 5 productos más vendidos
productos_mas_vendidos = df['Producto'].value_counts().head(5)

# Top 5 productos menos vendidos
productos_menos_vendidos = df['Producto'].value_counts().tail(5)

# Valor promedio del envío
envio_promedio = df['Valor Envío'].mean()

# Mostrar resultados
print(f"Ventas totales: R$ {ventas_totales:,.2f}")
print(f"Cantidad de productos vendidos: {productos_vendidos}")
print(f"Calificación promedio: {calificacion_promedio:.2f}")
print("\nProductos más vendidos:\n", productos_mas_vendidos)
print("\nProductos menos vendidos:\n", productos_menos_vendidos)
print(f"\nValor promedio de envío: R$ {envio_promedio:.2f}")
