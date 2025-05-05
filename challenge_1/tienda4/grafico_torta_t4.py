import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo Excel
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda4/tienda_4.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet')

# Limpiar nombres de columnas
df.columns = df.columns.str.strip()

# Calcular ventas por categoría
ventas_categoria = df['Categoría del Producto'].value_counts()

# Crear gráfico de torta
plt.figure(figsize=(8, 8))
plt.pie(
    ventas_categoria,
    labels=ventas_categoria.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Paired.colors
)
plt.title('Distribución de Ventas por Categoría de Producto - Tienda 4', fontsize=14)
plt.axis('equal')  # Para que sea un círculo perfecto
plt.tight_layout()
plt.show()
