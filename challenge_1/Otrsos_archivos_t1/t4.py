import pandas as pd

# Cargar archivo y hoja correcta
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet', header=0)
df.columns = df.columns.str.strip()

# Filtrar productos válidos
df = df[df['Producto'].apply(lambda x: isinstance(x, str) and x.strip() not in ['Totales', 'Total productos:', 'Total de ceros:', ''])]
df['Producto'] = df['Producto'].str.strip()

# Contar productos vendidos
conteo_productos = df['Producto'].value_counts()

# Productos más vendidos
top_vendidos = conteo_productos.head(3)

# Productos menos vendidos: excluir productos con solo 1 venta y nombres extraños
menos_vendidos = conteo_productos[conteo_productos > 1].sort_values().head(3)

# Mostrar resultados
print("🔝 Productos más vendidos:")
for producto, cantidad in top_vendidos.items():
    print(f"- {producto}: {cantidad} ventas")

print("\n🔻 Productos menos vendidos:")
for producto, cantidad in menos_vendidos.items():
    print(f"- {producto}: {cantidad} ventas")

