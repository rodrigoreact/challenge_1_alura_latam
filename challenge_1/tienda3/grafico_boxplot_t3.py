import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo Excel
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda3/tienda_3.xlsx'

# Leer la hoja "Worksheet"
df = pd.read_excel(archivo, sheet_name='Worksheet')

# Limpieza: eliminar filas sin categoría o precio
df = df[['Categoría del Producto', 'Precio']].dropna()

# Crear el gráfico boxplot
plt.figure(figsize=(12, 6))
df.boxplot(column='Precio', by='Categoría del Producto', grid=False, rot=90)

# Títulos y etiquetas
plt.title('Distribución de precios por categoría de producto - Tienda 3')
plt.suptitle('')  # Elimina el título automático que pone pandas
plt.xlabel('Categoría del Producto')
plt.ylabel('Precio')

# Mejor presentación
plt.tight_layout()
plt.show()
