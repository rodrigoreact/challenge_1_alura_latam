import pandas as pd

archivo = "C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx"
df = pd.read_excel(archivo, sheet_name="Worksheet")
df.columns = df.columns.str.strip()

# Filtrar productos válidos
def es_producto_valido(nombre):
    if not isinstance(nombre, str):
        return False
    nombre = nombre.strip().lower()
    palabras_invalidas = ['total', 'resumen', 'verificar', 'nan', 'productos', 'ceros']
    if any(palabra in nombre for palabra in palabras_invalidas):
        return False
    return len(nombre) > 1

df_productos = df[df['Producto'].apply(es_producto_valido)]

# Contar ventas por producto
ventas_por_producto = df_productos['Producto'].value_counts()

# Top 3 más vendidos
productos_mas_vendidos = ventas_por_producto.head(3)
print("🔝 Productos más vendidos:")
for producto, cantidad in productos_mas_vendidos.items():
    print(f"- {producto}: {cantidad} ventas")

# Productos menos vendidos (solo 1 venta)
productos_con_min_ventas = ventas_por_producto[ventas_por_producto == 1]
print(f"\n🔻 Hay {len(productos_con_min_ventas)} productos con solo 1 venta.")
print("Ejemplos de productos menos vendidos:")
for producto in productos_con_min_ventas.head(3).index:
    print(f"- {producto}")
