import pandas as pd

# Cargar el archivo
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx'
df = pd.read_excel(archivo, sheet_name="Worksheet")
df.columns = df.columns.str.strip()

# Filtrar solo las filas válidas (por ejemplo, productos no vacíos)
df = df[df['Producto'].apply(lambda x: isinstance(x, str) and len(x.strip()) > 1)]

# Agrupar por categoría y contar las ventas
ventas_categoria = df['Categoría del Producto'].value_counts()

# Mostrar los resultados ordenados
print("🛍️ Ventas por categoría:")
for categoria, cantidad in ventas_categoria.items():
    print(f"- {categoria}: {cantidad} ventas")
