import pandas as pd

# Ruta correcta sin comillas internas
df = pd.read_excel("C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx", header=0)

# Limpiar espacios de los encabezados
df.columns = df.columns.str.strip()

# Verifica columnas
print(df.columns)

# Cálculo del ingreso
ingresos = df['Precio'].sum()
print(f"Ingresos totales: {ingresos}")
