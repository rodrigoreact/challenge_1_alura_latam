import pandas as pd
import matplotlib.pyplot as plt

# Ruta y carga
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda3/tienda_3.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet')
df.columns = df.columns.str.strip()

# Asegurar tipo numérico
df['Calificación'] = pd.to_numeric(df['Calificación'], errors='coerce')

# Histograma de calificaciones
plt.figure(figsize=(10, 6))
plt.hist(df['Calificación'].dropna(), bins=20, color='orange', edgecolor='black')
plt.title('Distribución de Calificaciones de Clientes - Tienda 3')
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
