# -*- coding: utf-8 -*-
"""
Análisis de Rendimiento de Tiendas Alura Store
Script completo para evaluar y comparar el rendimiento de 4 tiendas
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.error import HTTPError

# Configuración de visualización
plt.style.use('ggplot')
sns.set_palette('viridis')

# ======================
# 1. CARGA DE DATOS CON MANEJO DE ERRORES
# ======================
def cargar_datos():
    # URLs corregidas de los archivos CSV
    urls = {
        'Tienda 1': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_1.csv",
        'Tienda 2': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_2.csv",
        'Tienda 3': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_3.csv",
        'Tienda 4': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_4.csv"
    }
    
    dataframes = []
    
    for nombre, url in urls.items():
        try:
            print(f"Cargando datos de {nombre}...")
            df = pd.read_csv(url)
            df['tienda'] = nombre  # Añadir columna identificadora
            dataframes.append(df)
            print(f"✅ {nombre} cargada exitosamente")
        except HTTPError as e:
            print(f"⚠️ Error al cargar {nombre}: {e}")
            print("Usando datos de ejemplo para esta tienda...")
            # Crear dataframe de ejemplo con estructura similar
            df_ejemplo = pd.DataFrame({
                'Producto': ['Producto Ejemplo'],
                'Categoría del Producto': ['Electrónicos'],
                'Precio': [0],
                'Costo de envío': [0],
                'Calificación': [3],
                'tienda': [nombre]
            })
            dataframes.append(df_ejemplo)
        except Exception as e:
            print(f"⚠️ Error inesperado con {nombre}: {e}")
            dataframes.append(pd.DataFrame({'tienda': [nombre]}))
    
    # Combinar todos los dataframes
    try:
        datos_completos = pd.concat(dataframes, ignore_index=True)
        return datos_completos
    except Exception as e:
        print(f"Error al combinar datos: {e}")
        return pd.DataFrame()

# Cargar los datos
datos = cargar_datos()

# Verificación básica de datos
if datos.empty:
    print("\n🚨 No se pudieron cargar datos. Creando dataset de ejemplo completo...")
    datos = pd.DataFrame({
        'Producto': ['Smartphone', 'Laptop', 'Tablet', 'Monitor'],
        'Categoría del Producto': ['Electrónicos', 'Electrónicos', 'Electrónicos', 'Electrónicos'],
        'Precio': [1500, 3000, 800, 500],
        'Costo de envío': [50, 80, 30, 25],
        'Calificación': [4.5, 4.2, 3.8, 4.0],
        'tienda': ['Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4']
    })

print("\n📋 Vista previa de los datos:")
print(datos.head())

# ======================
# 2. ANÁLISIS DE DATOS
# ======================
def analizar_datos(df):
    # Verificar columnas esenciales
    columnas_requeridas = ['Precio', 'Costo de envío', 'Calificación', 'tienda']
    for col in columnas_requeridas:
        if col not in df.columns:
            df[col] = 0  # Asignar valor por defecto si falta la columna
    
    # Convertir a numérico
    df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce').fillna(0)
    df['Costo de envío'] = pd.to_numeric(df['Costo de envío'], errors='coerce').fillna(0)
    df['Calificación'] = pd.to_numeric(df['Calificación'], errors='coerce').fillna(0)
    
    # 2.1. Análisis de Facturación
    facturacion = df.groupby('tienda')['Precio'].sum().sort_values()
    
    # 2.2. Análisis de Calificaciones
    calificaciones = df.groupby('tienda')['Calificación'].mean().sort_values()
    
    # 2.3. Análisis de Costos de Envío
    costos_envio = df.groupby('tienda')['Costo de envío'].mean().sort_values()
    
    return facturacion, calificaciones, costos_envio

facturacion, calificaciones, costos_envio = analizar_datos(datos)

# ======================
# 3. VISUALIZACIÓN DE DATOS
# ======================
def generar_graficos(facturacion, calificaciones, costos_envio):
    # Gráfico de Facturación
    plt.figure(figsize=(12, 6))
    facturacion.plot(kind='bar', color=sns.color_palette())
    plt.title('Facturación Total por Tienda')
    plt.ylabel('Total de Ventas ($)')
    plt.xlabel('Tienda')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('facturacion_tiendas.png')
    plt.close()
    
    # Gráfico de Calificaciones
    plt.figure(figsize=(12, 6))
    calificaciones.plot(kind='bar', color=sns.color_palette())
    plt.title('Calificación Promedio por Tienda')
    plt.ylabel('Calificación (1-5)')
    plt.xlabel('Tienda')
    plt.ylim(0, 5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('calificaciones_tiendas.png')
    plt.close()
    
    # Gráfico de Costos de Envío
    plt.figure(figsize=(12, 6))
    costos_envio.plot(kind='bar', color=sns.color_palette())
    plt.title('Costo Promedio de Envío por Tienda')
    plt.ylabel('Costo de Envío ($)')
    plt.xlabel('Tienda')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('costos_envio_tiendas.png')
    plt.close()

generar_graficos(facturacion, calificaciones, costos_envio)

# ======================
# 4. RECOMENDACIÓN FINAL
# ======================
def generar_recomendacion(facturacion, calificaciones, costos_envio):
    # Crear DataFrame comparativo
    comparacion = pd.DataFrame({
        'Facturación': facturacion,
        'Calificación': calificaciones,
        'Costo_Envio': costos_envio
    })
    
    # Normalizar los datos (1 = mejor, 0 = peor)
    comparacion['Facturación_norm'] = comparacion['Facturación'] / comparacion['Facturación'].max()
    comparacion['Calificación_norm'] = comparacion['Calificación'] / 5  # Escala 1-5
    comparacion['Costo_Envio_norm'] = 1 - (comparacion['Costo_Envio'] / comparacion['Costo_Envio'].max())
    
    # Ponderación (40% facturación, 40% calificación, 20% costos envío)
    comparacion['Puntaje_Final'] = (comparacion['Facturación_norm'] * 0.4 + 
                                   comparacion['Calificación_norm'] * 0.4 + 
                                   comparacion['Costo_Envio_norm'] * 0.2)
    
    # Identificar la tienda con peor puntaje
    peor_tienda = comparacion['Puntaje_Final'].idxmin()
    
    print("\n🔍 ANÁLISIS COMPARATIVO:")
    print(comparacion)
    
    print("\n🔥 RECOMENDACIÓN FINAL:")
    print(f"La tienda con menor rendimiento es: {peor_tienda}")
    print(f"- Facturación total: ${comparacion.loc[peor_tienda, 'Facturación']:,.2f}")
    print(f"- Calificación promedio: {comparacion.loc[peor_tienda, 'Calificación']:.2f}/5")
    print(f"- Costo promedio de envío: ${comparacion.loc[peor_tienda, 'Costo_Envio']:,.2f}")
    
    print("\n📊 Los gráficos se han guardado como:")
    print("- facturacion_tiendas.png")
    print("- calificaciones_tiendas.png")
    print("- costos_envio_tiendas.png")

generar_recomendacion(facturacion, calificaciones, costos_envio)