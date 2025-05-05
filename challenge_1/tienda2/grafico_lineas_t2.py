import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel desde la hoja correcta
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda2/tienda_2.xlsx'
df = pd.read_excel(archivo, sheet_name='Worksheet', header=0)
df.columns = df.columns.str.strip()  # Elimina espacios en los nombres de columna

# Asegurar formato de fecha
#df['Fecha de Compra'] = pd.to_datetime(df['Fecha de Compra'], errors='coerce')
df['Fecha de Compra'] = pd.to_datetime(df['Fecha de Compra'], errors='coerce', dayfirst=True)

# Agrupar por fecha y sumar los ingresos
ventas_diarias = df.groupby(df['Fecha de Compra'].dt.date)['Precio'].sum()

# Gráfico de líneas
plt.figure(figsize=(12, 6))
ventas_diarias.plot(kind='line', marker='o', linestyle='-')
plt.title('Ventas diarias - Tienda 2')
plt.xlabel('Fecha')
plt.ylabel('Ingresos en $')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

