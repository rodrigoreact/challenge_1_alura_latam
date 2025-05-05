# -*- coding: utf-8 -*-
"""
ANÁLISIS DE TIENDAS ALURA STORE - VERSIÓN EXCEL (.xlsx)
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de estilos (actualizada para matplotlib moderno)
try:
    plt.style.use('seaborn-v0_8')  # Estilo similar al antiguo 'seaborn'
except:
    plt.style.use('ggplot')  # Fallback seguro

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# ======================================
# 1. CARGA DE DATOS DESDE ARCHIVOS EXCEL
# ======================================
def cargar_datos_excel():
    """Carga datos desde archivos .xlsx con manejo de errores"""
    
    # Nombres de los archivos Excel locales
    archivos = {
        'Tienda 1': 'xls/tienda_1.xlsx',
        'Tienda 2': 'xls/tienda_2.xlsx',
        'Tienda 3': 'xls/tienda_3.xlsx',
        'Tienda 4': 'xls/tienda_4.xlsx'
    }
    
    datos_tiendas = []
    
    for nombre, archivo in archivos.items():
        try:
            if not os.path.exists(archivo):
                raise FileNotFoundError(f"Archivo {archivo} no encontrado")
            
            print(f"📂 Cargando {nombre} desde {archivo}...")
            
            # Leer Excel (usando la primera hoja por defecto)
            df = pd.read_excel(archivo, engine='openpyxl')  # Requiere pip install openpyxl
            df['tienda'] = nombre  # Añadir columna identificadora
            
            datos_tiendas.append(df)
            print(f"✅ {nombre} cargada correctamente (Registros: {len(df)})")
            
        except Exception as e:
            print(f"⚠️ Error en {nombre}: {str(e)}")
            print("🔧 Usando datos de ejemplo...")
            # Datos de respaldo
            datos_tiendas.append(pd.DataFrame({
                'Producto': [f'Producto {i}' for i in range(1, 6)],
                'Precio': [100, 200, 150, 300, 250],
                'Costo_envio': [10, 15, 12, 20, 18],
                'Calificación': [4.0, 3.5, 4.2, 3.8, 4.5],
                'tienda': nombre
            }))
    
    return pd.concat(datos_tiendas, ignore_index=True)

# ======================================
# 2. PROCESAMIENTO DE DATOS
# ======================================
def procesar_datos(df):
    """Limpieza y cálculo de métricas clave"""
    
    # Columnas numéricas (manejo seguro)
    numeric_cols = ['Precio', 'Costo_envio', 'Calificación']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        else:
            df[col] = 0  # Columna por defecto si no existe
    
    # Métricas por tienda
    analisis = df.groupby('tienda').agg({
        'Precio': ['sum', 'mean'],
        'Calificación': 'mean',
        'Costo_envio': 'mean'
    })
    
    # Renombrar columnas
    analisis.columns = ['Facturación_Total', 'Precio_Promedio', 
                       'Calificación_Promedio', 'Costo_Envío_Promedio']
    
    return analisis

# ======================================
# 3. VISUALIZACIÓN CON SEABORN
# ======================================
def generar_visualizaciones(analisis):
    """Crea dashboard interactivo con los resultados"""
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Dashboard de Rendimiento - Alura Store', fontsize=16)
    
    # Gráfico 1: Facturación Total
    sns.barplot(
        x=analisis.index,
        y=analisis['Facturación_Total'],
        ax=axes[0, 0],
        palette='Blues_d'
    )
    axes[0, 0].set_title('Facturación por Tienda (USD)')
    axes[0, 0].ticklabel_format(style='plain', axis='y')
    
    # Gráfico 2: Calificación Promedio
    sns.barplot(
        x=analisis.index,
        y=analisis['Calificación_Promedio'],
        ax=axes[0, 1],
        palette='Greens_d'
    )
    axes[0, 1].set_title('Satisfacción del Cliente (1-5)')
    axes[0, 1].set_ylim(0, 5)
    
    # Gráfico 3: Costos de Envío
    sns.barplot(
        x=analisis.index,
        y=analisis['Costo_Envío_Promedio'],
        ax=axes[1, 0],
        palette='Reds_d'
    )
    axes[1, 0].set_title('Costo Promedio de Envío (USD)')
    
    # Gráfico 4: Relación Precio-Calificación
    sns.scatterplot(
        x=analisis['Precio_Promedio'],
        y=analisis['Calificación_Promedio'],
        size=analisis['Facturación_Total'],
        sizes=(100, 500),
        ax=axes[1, 1],
        hue=analisis.index,
        palette='viridis',
        legend=False
    )
    axes[1, 1].set_title('Relación Precio-Calificación')
    
    plt.tight_layout()
    plt.savefig('dashboard_alura.png', dpi=300, bbox_inches='tight')
    plt.close()

# ======================================
# 4. RECOMENDACIÓN AUTOMATIZADA
# ======================================
def generar_recomendacion(analisis):
    """Sistema de scoring para identificar la tienda menos eficiente"""
    
    # Normalización de métricas (0-1)
    metrics = analisis.copy()
    metrics['Facturación_Norm'] = metrics['Facturación_Total'] / metrics['Facturación_Total'].max()
    metrics['Calificación_Norm'] = metrics['Calificación_Promedio'] / 5
    metrics['Costo_Norm'] = 1 - (metrics['Costo_Envío_Promedio'] / metrics['Costo_Envío_Promedio'].max())
    
    # Ponderación (ajustable)
    weights = {
        'Facturación': 0.5,
        'Calificación': 0.3,
        'Costo': 0.2
    }
    
    metrics['Puntaje_Final'] = (
        metrics['Facturación_Norm'] * weights['Facturación'] +
        metrics['Calificación_Norm'] * weights['Calificación'] +
        metrics['Costo_Norm'] * weights['Costo']
    )
    
    peor_tienda = metrics['Puntaje_Final'].idxmin()
    
    print("\n" + "="*60)
    print("   INFORME DE RECOMENDACIÓN - ALURA STORE")
    print("="*60)
    
    print("\n📊 MÉTRICAS CLAVE:")
    print(analisis.sort_values('Facturación_Total', ascending=False))
    
    print("\n🔍 DETALLE DEL ANÁLISIS:")
    print(metrics[['Facturación_Norm', 'Calificación_Norm', 'Costo_Norm', 'Puntaje_Final']].sort_values('Puntaje_Final'))
    
    print(f"\n🚨 RECOMENDACIÓN: La tienda con menor rendimiento es {peor_tienda}")
    print("Principales motivos:")
    print(f"- Facturación más baja: ${metrics.loc[peor_tienda, 'Facturación_Total']:,.2f}")
    print(f"- Calificación más baja: {metrics.loc[peor_tienda, 'Calificación_Promedio']:.2f}/5")
    print(f"- Costo de envío más alto: ${metrics.loc[peor_tienda, 'Costo_Envío_Promedio']:.2f}")

# ======================================
# EJECUCIÓN PRINCIPAL
# ======================================
if __name__ == "__main__":
    print("🚀 INICIANDO ANÁLISIS CON ARCHIVOS EXCEL...")
    
    # Paso 1: Cargar datos
    datos = cargar_datos_excel()
    
    # Paso 2: Procesar y analizar
    analisis = procesar_datos(datos)
    
    # Paso 3: Visualización
    generar_visualizaciones(analisis)
    
    # Paso 4: Recomendación
    generar_recomendacion(analisis)
    
    print("\n✅ ANÁLISIS COMPLETADO")
    print("📊 Dashboard guardado como 'dashboard_alura.png'")