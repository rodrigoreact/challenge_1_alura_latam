import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet')
df.columns = df.columns.str.strip()

# Convertir columnas geográficas a numéricas (forzar errores como NaN)
df['latitud'] = pd.to_numeric(df['latitud'], errors='coerce')
df['longitud'] = pd.to_numeric(df['longitud'], errors='coerce')
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')

# Filtrar filas válidas
df_geo = df.dropna(subset=['latitud', 'longitud', 'Precio'])

# Normalizar precios para tamaños razonables
tamaño = df_geo['Precio'] / df_geo['Precio'].max() * 100

# Gráfico de dispersión
plt.figure(figsize=(12, 8))
plt.scatter(df_geo['longitud'], df_geo['latitud'], 
            s=tamaño,  # tamaño proporcional al precio
            alpha=0.5, 
            color='darkcyan', 
            edgecolors='k')

#plt.title('📍 Dispersión geográfica de las ventas (según Precio)')
plt.title('Dispersión geográfica de las ventas (según Precio)')

plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.grid(True)
plt.title('Dispersión geográfica de las ventas (seg n Precio)')
plt.tight_layout()
plt.show()

