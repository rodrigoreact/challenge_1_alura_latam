import pandas as pd
import matplotlib.pyplot as plt

# Cargar archivo Excel
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda2/tienda_2.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet')

# Convertir coordenadas a valores numéricos
df['lat'] = pd.to_numeric(df['lat'], errors='coerce')
df['lon'] = pd.to_numeric(df['lon'], errors='coerce')

# Eliminar filas con coordenadas faltantes
df = df.dropna(subset=['lat', 'lon'])

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df['lon'], df['lat'], alpha=0.5, c='green')
plt.title('Distribución geográfica de ventas - Tienda 2')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid(True)
plt.tight_layout()
plt.show()

