import pandas as pd

# Ver qué hojas tiene el archivo
archivo = "C:/Users/User/Desktop/challenge_1/challenge_1/tienda_1.xlsx"
hojas = pd.ExcelFile(archivo).sheet_names
print("Hojas disponibles:", hojas)

# Leer la primera hoja
df = pd.read_excel(archivo, sheet_name=hojas[0])
print(df.head())