"""
$ py tienda_4.py
Ingresos totales: 2076751400.0
Costo de envío promedio: 23459.457167090754
Calificación promedio: 3.9957591178965224
Productos más vendidos:
 Producto
Cama box                     62
Cubertería                   59
Dashboards con Power BI      56
Cama king                    56
Carrito de control remoto    55
Name: count, dtype: int64
Productos menos vendidos:
 Producto
Refrigerador                   38
Ciencia de datos con Python    38
Guitarra acústica              37
Armario                        34
Guitarra eléctrica             33
Name: count, dtype: int64
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


archivo =  'C:/Users/User/Desktop/challenge_1/challenge_1/tienda4/tienda_4.xlsx'
df = pd.read_excel(archivo, sheet_name="Worksheet")

df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
df["Costo de envío"] = pd.to_numeric(df["Costo de envío"], errors="coerce")
df["Calificación"] = pd.to_numeric(df["Calificación"], errors="coerce")

print("Ingresos totales:", df["Precio"].sum())
print("Costo de envío promedio:", df["Costo de envío"].mean())
print("Calificación promedio:", df["Calificación"].mean())
print("Productos más vendidos:\n", df["Producto"].value_counts().head(5))
print("Productos menos vendidos:\n", df["Producto"].value_counts().tail(5))
