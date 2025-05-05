"""
$ py tienda_2.py
Este algoritmo responde todo esto:
******************************************
Ingresos totales: 1116343500
Costo de envío promedio: 25216.235693090293
Calificación promedio: 4.037303942348453
Productos más vendidos:
 Producto
Iniciando en programación    65
Microondas                   62
Batería                      61
Guitarra acústica            58
Pandereta                    58
Name: count, dtype: int64
Productos menos vendidos:
 Producto
Auriculares        37
Sillón             35
Mesa de comedor    34
Impresora          34
Juego de mesa      32
Name: count, dtype: int64
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


archivo =  'C:/Users/User/Desktop/challenge_1/challenge_1/tienda2/tienda_2.xlsx'
df = pd.read_excel(archivo, sheet_name="Worksheet")

df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")
df["Costo de envío"] = pd.to_numeric(df["Costo de envío"], errors="coerce")
df["Calificación"] = pd.to_numeric(df["Calificación"], errors="coerce")

print("Ingresos totales:", df["Precio"].sum())
print("Costo de envío promedio:", df["Costo de envío"].mean())
print("Calificación promedio:", df["Calificación"].mean())
print("Productos más vendidos:\n", df["Producto"].value_counts().head(5))
print("Productos menos vendidos:\n", df["Producto"].value_counts().tail(5))
