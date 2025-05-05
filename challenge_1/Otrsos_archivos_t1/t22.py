import pandas as pd

# Ruta del archivo
archivo = "C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx"

# Cargar los datos desde la hoja 'Worksheet', encabezado en la primera fila (índice 0)
df = pd.read_excel(archivo, sheet_name='Worksheet', header=0)

# Limpiar nombres de columnas (por si tienen espacios)
df.columns = df.columns.str.strip()

# Mostrar columnas para verificar
print("Columnas disponibles:", df.columns)

# Calcular ingresos totales
if 'Precio' in df.columns:
    ingresos = df['Precio'].sum()
    print(f"Ingresos totales: {ingresos}")
else:
    print("La columna 'Precio' no se encuentra.")

# Agrupar por categoría y contar la cantidad de productos vendidos
ventas_por_categoria = df['Categoría del Producto'].value_counts()

# Mostrar los resultados
print("Ventas por categoría:")
print(ventas_por_categoria)
# Convertir la columna Calificación a valores numéricos (forzando y omitiendo errores)
df['Calificación'] = pd.to_numeric(df['Calificación'], errors='coerce')

# Ahora sí, calcular la calificación promedio ignorando NaNs
calificacion_promedio = df['Calificación'].mean()

# Mostrar el resultado
print(f"Calificación promedio: {calificacion_promedio:.2f}")

# Agrupar por producto y contar la cantidad de ventas
ventas_por_producto = df['Producto'].value_counts()

# Contar cuántas veces se vendió cada producto
ventas_por_producto = df['Producto'].value_counts()

# Obtener los 3 productos más vendidos
productos_mas_vendidos = ventas_por_producto.head(3)
print("🔝 Productos más vendidos:")
print(productos_mas_vendidos)

# Contar ventas por producto
ventas_por_producto = df['Producto'].value_counts()

# Más vendidos
productos_mas_vendidos = ventas_por_producto.head(3)
print("🔝 Productos más vendidos:")
print(productos_mas_vendidos)

# Menos vendidos (todos con la mínima cantidad de ventas)
min_ventas = ventas_por_producto.min()
productos_con_min_ventas = ventas_por_producto[ventas_por_producto == min_ventas]

print(f"\n🔻 Hay {len(productos_con_min_ventas)} productos con solo {min_ventas} venta(s).")
print("Ejemplos de productos menos vendidos:")
print(productos_con_min_ventas.head(3))




