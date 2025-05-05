"""
$ py tienda_3.py
Ingresos totales: 2196039200
Costo de envío promedio: 49590.338983050846
Calificación promedio: 4.048325561678677
Productos más vendidos:
Producto
Kit de bancas      57
Mesa de comedor    56
Cama king          56
Mesa de noche      55
Set de ollas       55
Name: count, dtype: int64
Productos menos vendidos:
Producto
Set de vasos               36
Mochila                    36
Microondas                 36
Bloques de construcción    35
Totales                     1
Name: count, dtype: int64
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


archivo =  'C:/Users/User/Desktop/challenge_1/challenge_1/tienda3/tienda_3.xlsx'
df = pd.read_excel(archivo, sheet_name="Worksheet")

df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
df["Costo de envío"] = pd.to_numeric(df["Costo de envío"], errors="coerce")
df["Calificación"] = pd.to_numeric(df["Calificación"], errors="coerce")

print("Ingresos totales:", df["Precio"].sum())
print("Costo de envío promedio:", df["Costo de envío"].mean())
print("Calificación promedio:", df["Calificación"].mean())
print("Productos más vendidos:\n", df["Producto"].value_counts().head(5))
print("Productos menos vendidos:\n", df["Producto"].value_counts().tail(5))
