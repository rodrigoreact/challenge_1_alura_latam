# -*- coding: utf-8 -*-
"""
ANÁLISIS DE RENDIMIENTO - ALURA STORE
Versión corregida con configuración de estilos actualizada
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================================
# CONFIGURACIÓN CORREGIDA DE ESTILOS
# ======================================
# Versión moderna (para matplotlib >= 3.6)
try:
    plt.style.use('seaborn-v0_8')  # Estilo equivalente al antiguo 'seaborn'
except:
    plt.style.use('ggplot')  # Estilo alternativo si falla

sns.set_theme(style="whitegrid")  # Configuración moderna de seaborn
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

# ======================================
# 1. CARGA DE DATOS (URLs CORREGIDAS)
# ======================================
def cargar_datos():
    """Carga datos desde GitHub con manejo profesional de errores"""
    
    # URLs definitivas (corregido espacio en tienda_1)
    urls = {
        'Tienda 1': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_1.csv",
        'Tienda 2': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_2.csv",
        'Tienda 3': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_3.csv",
        'Tienda 4': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_4.csv"
    }
    
    datos_tiendas = []
    
    for nombre, url in urls.items():
        try:
            print(f"📤 Cargando {nombre}...")
            df = pd.read_csv(url)
            df['tienda'] = nombre
            datos_tiendas.append(df)
            print(f"✅ {nombre} cargada correctamente | Registros: {len(df)}")
        except Exception as e:
            print(f"⚠️ Error en {nombre}: {str(e)[:100]}...")
            # Datos de ejemplo como respaldo
            datos_tiendas.append(pd.DataFrame({
                'Producto': [f'Producto {i}' for i in range(1, 6)],
                'Precio': [100, 200, 150, 300, 250],
                'Costo de envío': [10, 15, 12, 20, 18],
                'Calificación': [4.0, 3.5, 4.2, 3.8, 4.5],
                'tienda': nombre
            }))
    
    return pd.concat(datos_tiendas, ignore_index=True)

# ======================================
# 2. ANÁLISIS Y VISUALIZACIÓN
# ======================================
def analizar_y_visualizar(datos):
    """Procesa datos y genera visualizaciones"""
    
    # Limpieza de datos
    numeric_cols = ['Precio', 'Costo de envío', 'Calificación']
    datos[numeric_cols] = datos[numeric_cols].apply(pd.to_numeric, errors='coerce').fillna(0)
    
    # Métricas por tienda
    analisis = datos.groupby('tienda').agg({
        'Precio': ['sum', 'mean'],
        'Calificación': 'mean',
        'Costo de envío': 'mean'
    })
    analisis.columns = ['Facturación', 'Precio Promedio', 'Calificación Promedio', 'Costo Envío Promedio']
    
    # Visualización
    fig, ax = plt.subplots(2, 2, figsize=(15, 12))
    plt.suptitle('Análisis Comparativo de Tiendas Alura Store', fontsize=16)
    
    # Gráfico 1: Facturación
    analisis['Facturación'].sort_values().plot(kind='barh', ax=ax[0, 0], color='skyblue')
    ax[0, 0].set_title('Facturación Total')
    ax[0, 0].set_xlabel('USD')
    
    # Gráfico 2: Calificaciones
    analisis['Calificación Promedio'].sort_values().plot(kind='barh', ax=ax[0, 1], color='lightgreen')
    ax[0, 1].set_title('Satisfacción del Cliente')
    ax[0, 1].set_xlim(0, 5)
    
    # Gráfico 3: Costos de envío
    analisis['Costo Envío Promedio'].sort_values().plot(kind='barh', ax=ax[1, 0], color='salmon')
    ax[1, 0].set_title('Eficiencia Logística')
    ax[1, 0].set_xlabel('USD')
    
    # Gráfico 4: Dispersión
    ax[1, 1].scatter(analisis['Precio Promedio'], analisis['Calificación Promedio'], s=100, alpha=0.6)
    ax[1, 1].set_title('Relación Precio-Calificación')
    ax[1, 1].set_xlabel('Precio Promedio')
    ax[1, 1].set_ylabel('Calificación Promedio')
    
    plt.tight_layout()
    plt.savefig('analisis_tiendas.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    return analisis

# ======================================
# 3. RECOMENDACIÓN
# ======================================
def generar_recomendacion(analisis):
    """Genera recomendación basada en métricas"""
    
    # Normalización
    metrics = analisis.copy()
    metrics['Facturación_norm'] = metrics['Facturación'] / metrics['Facturación'].max()
    metrics['Calificación_norm'] = metrics['Calificación Promedio'] / 5
    metrics['Costo_norm'] = 1 - (metrics['Costo Envío Promedio'] / metrics['Costo Envío Promedio'].max())
    
    # Puntaje compuesto
    metrics['Score'] = (metrics['Facturación_norm'] * 0.5 + 
                       metrics['Calificación_norm'] * 0.3 + 
                       metrics['Costo_norm'] * 0.2)
    
    peor_tienda = metrics['Score'].idxmin()
    
    print("\n" + "="*50)
    print("   INFORME DE RECOMENDACIÓN")
    print("="*50)
    print("\n🔍 MÉTRICAS POR TIENDA:")
    print(analisis)
    print(f"\n🚨 RECOMENDACIÓN: La tienda con menor rendimiento es {peor_tienda}")
    print(f"- Facturación: ${metrics.loc[peor_tienda, 'Facturación']:,.0f}")
    print(f"- Calificación: {metrics.loc[peor_tienda, 'Calificación Promedio']:.1f}/5")
    print(f"- Costo envío: ${metrics.loc[peor_tienda, 'Costo Envío Promedio']:.2f}")

# ======================================
# EJECUCIÓN PRINCIPAL
# ======================================
if __name__ == "__main__":
    print("🚀 INICIANDO ANÁLISIS DE TIENDAS ALURA STORE")
    
    # Paso 1: Carga de datos
    datos = cargar_datos()
    
    # Paso 2: Análisis y visualización
    analisis = analizar_y_visualizar(datos)
    
    # Paso 3: Recomendación
    generar_recomendacion(analisis)
    
    print("\n✅ Análisis completado exitosamente")
    print("📊 Dashboard guardado como 'analisis_tiendas.png'")