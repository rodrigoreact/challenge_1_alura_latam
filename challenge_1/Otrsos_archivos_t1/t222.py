import pandas as pd

# Cargar archivo Excel y seleccionar la hoja correcta
archivo = "C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx"
df = pd.read_excel(archivo, sheet_name="Worksheet")

# Limpiar columnas
df.columns = df.columns.str.strip()

# Filtrar filas con nombres válidos de producto
df_productos = df[df['Producto'].apply(lambda x: isinstance(x, str) and len(x.strip()) > 1)]

# Contar ventas por producto
ventas_por_producto = df_productos['Producto'].value_counts()

# Mostrar top 3 más vendidos
productos_mas_vendidos = ventas_por_producto.head(3)
print("🔝 Productos más vendidos:")
for producto, cantidad in productos_mas_vendidos.items():
    print(f"- {producto}: {cantidad} ventas")

# Mostrar productos con solo una venta (mínimo)
productos_con_min_ventas = ventas_por_producto[ventas_por_producto == 1]
print(f"\n🔻 Hay {len(productos_con_min_ventas)} productos con solo 1 venta.")
print("Ejemplos de productos menos vendidos:")
for producto in productos_con_min_ventas.head(3).index:
    print(f"- {producto}")
