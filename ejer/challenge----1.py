# -*- coding: utf-8 -*-
"""
ANÁLISIS DE RENDIMIENTO - ALURA STORE
Script completo con URLs corregidas y manejo robusto de datos
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.error import HTTPError

# Configuración de estilos
plt.style.use('seaborn')
sns.set_palette('pastel')
plt.rcParams['figure.figsize'] = (12, 6)

# ======================================
# 1. CARGA DE DATOS CON URLs CORREGIDAS
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
            
            # Verificación básica de estructura
            columnas_requeridas = ['Producto', 'Precio', 'Calificación']
            if not all(col in df.columns for col in columnas_requeridas):
                raise ValueError(f"Estructura incorrecta en {nombre}")
                
            df['tienda'] = nombre
            datos_tiendas.append(df)
            print(f"✅ {nombre} cargada correctamente | Registros: {len(df)}")
            
        except HTTPError as e:
            print(f"⚠️ Error 404 en {nombre}. Usando datos de respaldo...")
            datos_tiendas.append(datos_respaldo(nombre))
        except Exception as e:
            print(f"⚠️ Error en {nombre}: {str(e)[:100]}...")
            datos_tiendas.append(datos_respaldo(nombre))
    
    return pd.concat(datos_tiendas, ignore_index=True)

def datos_respaldo(nombre_tienda):
    """Genera datos de ejemplo para tiendas con problemas"""
    return pd.DataFrame({
        'Producto': [f'Producto Ejemplo {i}' for i in range(1, 6)],
        'Precio': [100, 200, 150, 300, 250],
        'Costo de envío': [10, 15, 12, 20, 18],
        'Calificación': [4.0, 3.5, 4.2, 3.8, 4.5],
        'tienda': nombre_tienda
    })

# ======================================
# 2. PROCESAMIENTO Y ANÁLISIS
# ======================================
def procesar_datos(df):
    """Limpieza y transformación de datos"""
    
    # Convertir campos numéricos
    numeric_cols = ['Precio', 'Costo de envío', 'Calificación']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    # Imputación de valores faltantes
    df['Precio'] = df['Precio'].fillna(df['Precio'].median())
    df['Costo de envío'] = df['Costo de envío'].fillna(df['Costo de envío'].mean())
    df['Calificación'] = df['Calificación'].clip(1, 5)  # Asegurar rango 1-5
    
    # Cálculo de métricas por tienda
    analisis = df.groupby('tienda').agg({
        'Precio': ['sum', 'mean', 'count'],
        'Calificación': 'mean',
        'Costo de envío': 'mean'
    })
    
    analisis.columns = ['Facturación', 'Precio Promedio', 'Ventas', 
                       'Calificación Promedio', 'Costo Envío Promedio']
    
    return df, analisis

# ======================================
# 3. VISUALIZACIÓN PROFESIONAL
# ======================================
def generar_visualizaciones(analisis):
    """Genera dashboard completo de métricas"""
    
    fig, ax = plt.subplots(2, 2, figsize=(15, 12))
    plt.suptitle('Análisis Comparativo de Tiendas', fontsize=16)
    
    # Gráfico 1: Facturación
    analisis['Facturación'].sort_values().plot(
        kind='barh', ax=ax[0, 0], title='Facturación Total', color='skyblue')
    ax[0, 0].set_xlabel('USD')
    
    # Gráfico 2: Calificaciones
    analisis['Calificación Promedio'].sort_values().plot(
        kind='barh', ax=ax[0, 1], title='Satisfacción del Cliente', color='lightgreen')
    ax[0, 1].set_xlim(0, 5)
    
    # Gráfico 3: Costos de envío
    analisis['Costo Envío Promedio'].sort_values().plot(
        kind='barh', ax=ax[1, 0], title='Eficiencia Logística', color='salmon')
    ax[1, 0].set_xlabel('USD')
    
    # Gráfico 4: Relación Precio-Calificación
    ax[1, 1].scatter(
        analisis['Precio Promedio'], 
        analisis['Calificación Promedio'],
        s=analisis['Ventas']*10, alpha=0.6)
    
    ax[1, 1].set_title('Relación Precio-Calificación')
    ax[1, 1].set_xlabel('Precio Promedio')
    ax[1, 1].set_ylabel('Calificación')
    
    plt.tight_layout()
    plt.savefig('dashboard_tiendas.png', dpi=300, bbox_inches='tight')
    plt.close()

# ======================================
# 4. RECOMENDACIÓN BASADA EN DATOS
# ======================================
def generar_recomendacion(analisis):
    """Sistema de scoring para recomendación"""
    
    # Normalización de métricas
    metrics = analisis.copy()
    metrics['Facturación_norm'] = metrics['Facturación'] / metrics['Facturación'].max()
    metrics['Calificación_norm'] = metrics['Calificación Promedio'] / 5
    metrics['Costo_norm'] = 1 - (metrics['Costo Envío Promedio'] / metrics['Costo Envío Promedio'].max())
    
    # Ponderación estratégica
    weights = {
        'Facturación': 0.5,
        'Calificación': 0.3,
        'Costo': 0.2
    }
    
    metrics['Score'] = (
        metrics['Facturación_norm'] * weights['Facturación'] +
        metrics['Calificación_norm'] * weights['Calificación'] +
        metrics['Costo_norm'] * weights['Costo']
    )
    
    peor_tienda = metrics['Score'].idxmin()
    
    print("\n" + "="*50)
    print("   INFORME DE RECOMENDACIÓN - ALURA STORE")
    print("="*50)
    
    print("\n🔍 MÉTRICAS POR TIENDA:")
    print(analisis.sort_values('Facturación'))
    
    print("\n📊 SCORING ESTRATÉGICO:")
    print(metrics[['Score']].sort_values('Score'))
    
    print(f"\n🚨 RECOMENDACIÓN: La tienda con menor rendimiento es {peor_tienda}")
    print("Motivos principales:")
    print(f"- Facturación: ${metrics.loc[peor_tienda, 'Facturación']:,.0f} ({(metrics.loc[peor_tienda, 'Facturación_norm']*100):.1f}% del máximo)")
    print(f"- Calificación: {metrics.loc[peor_tienda, 'Calificación Promedio']:.1f}/5")
    print(f"- Costo envío: ${metrics.loc[peor_tienda, 'Costo Envío Promedio']:.2f}")
    
    print("\n💡 SUGERENCIAS:")
    print("- Evaluar estrategias comerciales para mejorar ventas")
    print("- Revisar procesos logísticos para reducir costos")
    print("- Implementar encuestas de satisfacción para identificar áreas de mejora")

# ======================================
# EJECUCIÓN PRINCIPAL
# ======================================
if __name__ == "__main__":
    print("🚀 INICIANDO ANÁLISIS DE TIENDAS ALURA STORE")
    
    # Paso 1: Carga de datos
    datos = cargar_datos()
    
    # Paso 2: Procesamiento
    datos, analisis = procesar_datos(datos)
    
    # Paso 3: Visualización
    generar_visualizaciones(analisis)
    
    # Paso 4: Recomendación
    generar_recomendacion(analisis)
    
    print("\n✅ Análisis completado exitosamente")
    print("📊 Dashboard guardado como 'dashboard_tiendas.png'")