import pandas as pd

# Ruta con raw string para evitar errores con las barras
archivo = r'C:\Users\User\Desktop\challenge_1\challenge_1\tienda_1.xlsx'

# Leer las primeras 10 filas sin encabezados
df = pd.read_excel(archivo, header=None)
print(df.head(2360))
