# -*- coding: utf-8 -*-
"""
Análisis de eficiencia de tiendas Alura Store
Recomendación de qué tienda vender basada en datos de ventas, reseñas y logística.
"""

# Importar librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de gráficos
plt.style.use("ggplot")
sns.set_palette("viridis")

# ======================
# 1. CARGAR DATOS (SIMULADOS SI NO EXISTE CSV)
# ======================
try:
    datos = pd.read_csv("alura_store_data.csv")
    print("✅ Datos cargados desde 'alura_store_data.csv'")
except FileNotFoundError:
    print("⚠️ No se encontró 'alura_store_data.csv'. Usando datos de ejemplo...")
    # Crear datos de muestra
    data = {
        "tienda": ["Tienda A", "Tienda B", "Tienda C", "Tienda D"] * 12,  # 12 meses
        "ingresos": [12000, 8000, 15000, 7000] * 12,
        "categoria": ["Electrónicos", "Ropa", "Hogar", "Electrónicos"] * 12,
        "producto_mas_vendido": ["Smartphone", "Camisa", "Sartén", "Tablet"] * 12,
        "reseña_promedio": [4.2, 3.8, 4.5, 3.2] * 12,
        "envio_promedio_dias": [2.5, 3.1, 2.8, 4.0] * 12,
        "unidades_vendidas": [1200, 800, 1500, 700] * 12,
    }
    datos = pd.DataFrame(data)

# ======================
# 2. ANÁLISIS INICIAL
# ======================
print("\n📊 RESUMEN ESTADÍSTICO:")
print(datos.describe())

# Agrupar datos por tienda
resumen_tiendas = datos.groupby("tienda").agg({
    "ingresos": "mean",
    "reseña_promedio": "mean",
    "envio_promedio_dias": "mean",
    "unidades_vendidas": "mean",
}).reset_index()

print("\n📌 DATOS POR TIENDA:")
print(resumen_tiendas)

# ======================
# 3. VISUALIZACIONES
# ======================
# Gráfico 1: Ingresos promedio (Barras)
plt.figure(figsize=(10, 5))
sns.barplot(x="tienda", y="ingresos", data=resumen_tiendas)
plt.title("Ingresos Promedio por Tienda (USD)")
plt.xlabel("Tienda")
plt.ylabel("Ingresos ($)")
plt.savefig("ingresos_tiendas.png", bbox_inches="tight")
plt.show()

# Gráfico 2: Reseñas vs. Tiempo de envío (Dispersión)
plt.figure(figsize=(10, 5))
sns.scatterplot(
    x="reseña_promedio",
    y="envio_promedio_dias",
    hue="tienda",
    data=resumen_tiendas,
    s=200,
)
plt.title("Relación: Reseñas vs. Tiempo de Envío")
plt.xlabel("Reseña Promedio (1-5)")
plt.ylabel("Días de Envío Promedio")
plt.grid(True)
plt.savefig("reseñas_vs_envio.png", bbox_inches="tight")
plt.show()

# Gráfico 3: Unidades vendidas (Barras horizontales)
plt.figure(figsize=(10, 4))
sns.barplot(x="unidades_vendidas", y="tienda", data=resumen_tiendas)
plt.title("Unidades Vendidas Promedio")
plt.xlabel("Ventas Totales")
plt.ylabel("Tienda")
plt.savefig("ventas_tiendas.png", bbox_inches="tight")
plt.show()

# ======================
# 4. RECOMENDACIÓN FINAL
# ======================
# Métrica compuesta: 40% ingresos, 30% reseñas, 30% logística
resumen_tiendas["puntaje_eficiencia"] = (
    0.4 * (resumen_tiendas["ingresos"] / resumen_tiendas["ingresos"].max())
    + 0.3 * (resumen_tiendas["reseña_promedio"] / 5)
    + 0.3 * (1 - resumen_tiendas["envio_promedio_dias"] / resumen_tiendas["envio_promedio_dias"].max())
)

peor_tienda = resumen_tiendas.loc[resumen_tiendas["puntaje_eficiencia"].idxmin(), "tienda"]

print("\n🔎 CONCLUSIÓN FINAL:")
print(f"La tienda menos eficiente es **{peor_tienda}**. Razones:")
print(f"- Ingresos más bajos (${resumen_tiendas[resumen_tiendas['tienda'] == peor_tienda]['ingresos'].values[0]:.0f})")
print(f"- Reseñas más bajas ({resumen_tiendas[resumen_tiendas['tienda'] == peor_tienda]['reseña_promedio'].values[0]:.1f}/5)")
print(f"- Envíos más lentos ({resumen_tiendas[resumen_tiendas['tienda'] == peor_tienda]['envio_promedio_dias'].values[0]:.1f} días)")

print("\n💡 RECOMENDACIÓN:")
print(f"Vender **{peor_tienda}** permitirá al Sr. João:")
print("✅ Liberar recursos para su nuevo emprendimiento.")
print("✅ Enfocarse en tiendas más rentables (ej: Tienda C).")
print("✅ Evitar pérdidas por baja eficiencia operativa.")

print("\n📌 Se han guardado los gráficos en PNG para revisión.")