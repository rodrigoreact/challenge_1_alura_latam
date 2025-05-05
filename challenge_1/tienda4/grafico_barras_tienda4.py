import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo Excel
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda4/tienda_4.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet')

# Limpiar nombres de columnas
df.columns = df.columns.str.strip()

# Calcular ventas por categoría
ventas_categoria = df['Categoría del Producto'].value_counts()

# Mostrar en consola
print("Ventas por categoría:\n", ventas_categoria)

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
ventas_categoria.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Ventas por Categoría de Producto Tienda 4', fontsize=14)
plt.xlabel('Categoría', fontsize=12)
plt.ylabel('Número de Ventas', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

