# -*- coding: utf-8 -*-
"""
Análisis de tiendas Alura Store - Versión Final
Recomendación de qué tienda vender basada en facturación, reseñas y logística.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
plt.style.use("ggplot")
sns.set_palette("viridis")

# ======================
# -*- coding: utf-8 -*-
"""
Análisis de eficiencia para Alura Store
Recomendación de qué tienda vender basada en datos de ventas, reseñas y logística.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración
plt.style.use("ggplot")
sns.set_palette("viridis")

# ======================
# 1. CARGAR DATOS (CON URLs CORREGIDAS)
# ======================
def cargar_datos():
    # URLs oficiales corregidas (sin espacios ni caracteres especiales)
    base_url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/"
    urls = [
        f"{base_url}tienda_1.csv",  # %20 eliminado
        f"{base_url}tienda_2.csv",
        f"{base_url}tienda_3.csv",
        f"{base_url}tienda_4.csv"
    ]
    
    # Cargar datos y añadir columna 'tienda'
    dfs = []
    for i, url in enumerate(urls, 1):
        try:
            df = pd.read_csv(url)
            df['tienda'] = f"Tienda {i}"
            dfs.append(df)
        except Exception as e:
            print(f"⚠️ Error al cargar {url}: {str(e)}")
            # Crear DataFrame vacío como respaldo
            dfs.append(pd.DataFrame(columns=['Producto', 'Precio', 'Calificación']))
    
    datos_completos = pd.concat(dfs, ignore_index=True)
    return datos_completos

datos = cargar_datos()

# ======================
# 2. ANÁLISIS DE FACTURACIÓN
# ======================
def analizar_facturacion(datos):
    if 'Precio' not in datos.columns:
        datos['Precio'] = 0  # Valor por defecto si no existe la columna
    
    datos['ingresos'] = datos['Precio']  # Asumiendo 1 unidad por registro
    facturacion = datos.groupby('tienda')['ingresos'].sum().sort_values()
    
    plt.figure(figsize=(10, 5))
    facturacion.plot(kind='bar', title='Facturación Total por Tienda (USD)')
    plt.ylabel('Ingresos Totales')
    plt.savefig('facturacion_tiendas.png', bbox_inches='tight')
    plt.show()
    
    return facturacion

facturacion = analizar_facturacion(datos)

# ======================
# 3. CALIFICACIONES PROMEDIO
# ======================
def analizar_calificaciones(datos):
    if 'Calificación' not in datos.columns:
        datos['Calificación'] = 3  # Valor por defecto
    
    calificaciones = datos.groupby('tienda')['Calificación'].mean().sort_values()
    
    plt.figure(figsize=(10, 5))
    sns.barplot(x=calificaciones.index, y=calificaciones.values)
    plt.title('Calificación Promedio por Tienda (1-5)')
    plt.ylim(0, 5)
    plt.savefig('calificaciones_tiendas.png', bbox_inches='tight')
    plt.show()
    
    return calificaciones

calificaciones = analizar_calificaciones(datos)

# ======================
# 4. COSTOS DE ENVÍO
# ======================
def analizar_envios(datos):
    if 'Costo de envío' not in datos.columns:
        datos['Costo de envío'] = 0
    
    envios = datos.groupby('tienda')['Costo de envío'].mean().sort_values()
    
    plt.figure(figsize=(10, 5))
    envios.plot(kind='line', marker='o', title='Costo Promedio de Envío por Tienda (USD)')
    plt.ylabel('Costo Promedio')
    plt.savefig('envios_tiendas.png', bbox_inches='tight')
    plt.show()
    
    return envios

envios = analizar_envios(datos)

# ======================
# 5. RECOMENDACIÓN FINAL
# ======================
def generar_recomendacion(facturacion, calificaciones, envios):
    # Normalizar métricas (1 = mejor, 0 = peor)
    df = pd.DataFrame({
        'facturacion': facturacion.rank(ascending=False),
        'calificaciones': calificaciones.rank(),
        'envios': (1 / envios).rank()  # Menor costo = mejor
    })
    
    # Ponderación: 50% facturación, 30% calificaciones, 20% envíos
    df['puntaje'] = df['facturacion']*0.5 + df['calificaciones']*0.3 + df['envios']*0.2
    peor_tienda = df['puntaje'].idxmin()
    
    print("\n🔥 RECOMENDACIÓN FINAL 🔥")
    print(f"Vender la {peor_tienda} porque tiene:")
    print(f"- Facturación más baja: ${facturacion[peor_tienda]:,.0f}")
    print(f"- Calificación más baja: {calificaciones[peor_tienda]:.1f}/5")
    print(f"- Costo de envío promedio: ${envios[peor_tienda]:,.0f}")

generar_recomendacion(facturacion, calificaciones, envios)

print("\n📊 Gráficos guardados como:")
print("- facturacion_tiendas.png")
print("- calificaciones_tiendas.png")
print("- envios_tiendas.png")