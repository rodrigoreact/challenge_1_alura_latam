import pandas as pd

# Cargar archivo (ajusta la ruta y hoja si es necesario)
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet', header=0)
df.columns = df.columns.str.strip()  # Limpieza de columnas

# Asegurarse que 'Producto' está limpio
df = df[df['Producto'].apply(lambda x: isinstance(x, str) and len(x.strip()) > 1)]

# Contar productos vendidos
conteo_productos = df['Producto'].value_counts()

# Productos más vendidos
top_vendidos = conteo_productos.head(3)

# Productos menos vendidos (mínimos mayores que cero)
# Filtramos productos con más de 0 ventas y ordenamos por cantidad
menos_vendidos = conteo_productos.sort_values().head(3)

# Mostrar resultados
print("🔝 Productos más vendidos:")
for producto, cantidad in top_vendidos.items():
    print(f"- {producto}: {cantidad} ventas")

print("\n🔻 Productos menos vendidos:")
for producto, cantidad in menos_vendidos.items():
    print(f"- {producto}: {cantidad} ventas")
