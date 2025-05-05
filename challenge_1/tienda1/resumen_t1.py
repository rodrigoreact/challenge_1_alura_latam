import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from fpdf import FPDF
from fpdf.enums import XPos, YPos

# Cargar datos
archivo = "tienda_1.xlsx"
df = pd.read_excel(archivo, sheet_name="Worksheet")

# Asegurar tipos correctos
df["Calificación"] = pd.to_numeric(df["Calificación"], errors="coerce")
df["Precio"] = pd.to_numeric(df["Precio"], errors="coerce")

# Análisis de datos
ingresos_totales = df["Precio"].sum()
ventas_por_categoria = df["Categoría del Producto"].value_counts()
calificacion_promedio = df["Calificación"].mean()
productos_mas_vendidos = df["Producto"].value_counts().head(5)
productos_menos_vendidos = df["Producto"].value_counts().tail(5)

# Gráfica: Ventas por categoría
plt.figure(figsize=(8, 5))
ventas_por_categoria.plot(kind="bar", color="skyblue")
plt.title("Ventas por Categoría")
plt.ylabel("Cantidad de Ventas")
plt.tight_layout()
plt.savefig("ventas_categoria_1.png")
plt.close()

# Gráfica: Productos más vendidos
plt.figure(figsize=(8, 5))
productos_mas_vendidos.plot(kind="bar", color="green")
plt.title("Top 5 Productos Más Vendidos")
plt.ylabel("Cantidad de Ventas")
plt.tight_layout()
plt.savefig("productos_mas_vendidos_1.png")
plt.close()

# Boxplot de calificaciones
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Calificación"])
plt.title("Distribución de Calificaciones")
plt.savefig("calificaciones_boxplot_1.png")
plt.close()

# Mapa geográfico si hay coordenadas
if "lat" in df.columns and "lon" in df.columns:
    plt.figure(figsize=(6, 6))
    plt.scatter(df["lon"], df["lat"], alpha=0.5)
    plt.title("Distribución Geográfica de Ventas")
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    plt.savefig("mapa_geografico_1.png")
    plt.close()

# Crear informe PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(0, 10, "Informe de Análisis - Tienda 1", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.set_font("helvetica", "", 12)
pdf.cell(0, 10, f"Ingresos totales: ${ingresos_totales:,.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
pdf.cell(0, 10, f"Calificación promedio: {calificacion_promedio:.2f}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.cell(0, 10, "Ventas por categoría:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
for cat, val in ventas_por_categoria.items():
    pdf.cell(0, 10, f" - {cat}: {val}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

pdf.image("ventas_categoria_1.png", w=170)
pdf.image("productos_mas_vendidos_1.png", w=170)
pdf.image("calificaciones_boxplot_1.png", w=120)

if "lat" in df.columns and "lon" in df.columns:
    pdf.image("mapa_geografico_1.png", w=120)

# Guardar el PDF
pdf.output("informe_tienda_1.pdf")
print("✅ Informe generado: informe_tienda_1.pdf")
print("Precio máximo:", df["Precio"].max())
print("Precio mínimo:", df["Precio"].min())
print("Precio promedio:", df["Precio"].mean())

