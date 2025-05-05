import pandas as pd

# Ruta del archivo
archivo = 'C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx'

# Cargar hoja correcta
df = pd.read_excel(archivo, sheet_name='Worksheet')

# Limpieza básica
df.columns = df.columns.str.strip()

# Asegurarse de que la columna sea numérica (por si hay errores de tipo)
df['Calificación'] = pd.to_numeric(df['Calificación'], errors='coerce')

# Calcular promedio, ignorando NaNs
calificacion_promedio = df['Calificación'].mean()

print(f"⭐ Calificación promedio de los clientes en Tienda 1: {calificacion_promedio:.2f}")
