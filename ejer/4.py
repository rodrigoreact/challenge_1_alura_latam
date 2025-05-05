import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ======================
# 1. CONFIGURACIÓN INICIAL  
# ======================
# Estilo de gráficos (compatible con versiones recientes)
try:
    plt.style.use('seaborn-v0_8')  # Estilo moderno equivalente a 'seaborn'
except:
    plt.style.use('ggplot')  # Alternativa más compatible

sns.set_theme(style="whitegrid")  # Configuración profesional de Seaborn

# ======================
# 2. CARGA DE DATOS (TIENDA 4)  
# ======================
def cargar_tienda4():
    """Carga datos de Tienda 4 desde múltiples fuentes con respaldo"""
    FUENTES = [
        # Prioridad 1: URL GitHub
        ("https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_4.csv", "GitHub"),
        # Prioridad 2: Archivo local
        ("tienda_4.csv", "Archivo local"),
        # Prioridad 3: Datos de ejemplo
        (None, "Datos de ejemplo")
    ]
    
    for fuente, tipo in FUENTES:
        try:
            if tipo == "Datos de ejemplo":
                raise Exception("Generando datos de ejemplo")
                
            df = pd.read_csv(fuente)
            print(f"✅ Datos cargados desde {tipo}")
            df['Tienda'] = 'Tienda 4'  # Columna identificadora
            return df
        except Exception as e:
            print(f"⚠️ No se pudo cargar desde {tipo}: {str(e)}")
            continue
    
    # Datos de ejemplo estructurados (si todo falla)
    print("ℹ️ Usando datos de ejemplo predefinidos")
    return pd.DataFrame({
        'Producto': ['Impresora', 'Monitor 4K', 'SSD 1TB', 'Webcam'],
        'Categoría': ['Oficina', 'Electrónicos', 'Componentes', 'Accesorios'],
        'Precio': [300, 600, 120, 90],
        'Costo_envío': [40, 80, 15, 10],
        'Calificación': [3.8, 4.5, 4.7, 4.2],
        'Fecha': pd.date_range(start='2023-03-01', periods=4)
    })

# Cargar datos
tienda4 = cargar_tienda4()

# ======================
# 3. ANÁLISIS DE DATOS (CON VERIFICACIÓN DE COLUMNAS)  
# ======================
def analizar_tienda(df):
    """Calcula métricas clave con validación robusta"""
    # Encontrar columnas relevantes (insensible a mayúsculas/acentos)
    col_precio = next((col for col in df.columns if 'precio' in col.lower()), None)
    col_calif = next((col for col in df.columns if 'calif' in col.lower() or 'rating' in col.lower()), None)
    col_producto = next((col for col in df.columns if 'producto' in col.lower() or 'item' in col.lower()), None)
    col_categoria = next((col for col in df.columns if 'categ' in col.lower()), None)
    
    # Diccionario de resultados
    resultados = {
        'Productos analizados': len(df),
        'Facturación Total': df[col_precio].sum() if col_precio else 'No disponible',
        'Producto Más Vendido': df[col_producto].mode()[0] if col_producto else 'No disponible',
        'Calificación Promedio': df[col_calif].mean() if col_calif else 'No disponible',
        'Margen Estimado': (df[col_precio].sum() - df['Costo_envío'].sum()) if all([col_precio, 'Costo_envío' in df.columns]) else 'No disponible'
    }
    
    # Distribución por categoría (si existe)
    if col_categoria:
        resultados['Distribución por Categoría'] = df[col_categoria].value_counts(normalize=True).to_dict()
    
    return resultados, col_precio, col_calif, col_categoria

# Ejecutar análisis
metricas, col_precio, col_calif, col_categoria = analizar_tienda(tienda4)

# ======================
# 4. VISUALIZACIONES PROFESIONALES  
# ======================
def generar_visualizaciones(df, precio_col, calif_col, categoria_col):
    """Genera gráficos con validación de datos"""
    try:
        plt.figure(figsize=(16, 5))
        
        # Gráfico 1: Distribución de categorías (si existe)
        plt.subplot(1, 3, 1)
        if categoria_col:
            df[categoria_col].value_counts().plot(
                kind='pie',
                autopct='%1.1f%%',
                colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'],
                explode=(0.05, 0.05, 0.05, 0.05)
            )
            plt.title('Distribución por Categoría', pad=20)
        else:
            plt.text(0.5, 0.5, 'Datos de categoría\nno disponibles', ha='center', va='center')
            plt.title('Datos faltantes', pad=20)
        
        # Gráfico 2: Comparativa de precios
        plt.subplot(1, 3, 2)
        col_producto = next((col for col in df.columns if 'producto' in col.lower()), None)
        if all([precio_col, col_producto]):
            df_sorted = df.sort_values(precio_col, ascending=False)
            sns.barplot(
                data=df_sorted,
                x=col_producto,
                y=precio_col,
                palette="viridis"
            )
            plt.title('Comparativa de Precios', pad=20)
            plt.xticks(rotation=45, ha='right')
        else:
            plt.text(0.5, 0.5, 'Datos de precios\nno disponibles', ha='center', va='center')
            plt.title('Datos faltantes', pad=20)
        
        # Gráfico 3: Relación Precio-Calificación
        plt.subplot(1, 3, 3)
        if all([precio_col, calif_col]):
            sns.regplot(
                data=df,
                x=precio_col,
                y=calif_col,
                scatter_kws={'s': 100, 'alpha': 0.7},
                line_kws={'color': 'red'}
            )
            plt.title('Relación Precio-Calificación', pad=20)
            plt.ylim(0, 5.5)
        else:
            plt.text(0.5, 0.5, 'Datos insuficientes\npara comparación', ha='center', va='center')
            plt.title('Datos faltantes', pad=20)
        
        plt.tight_layout()
        plt.savefig('analisis_tienda4.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("\n📊 Gráficos guardados como 'analisis_tienda4.png'")
    except Exception as e:
        print(f"⚠️ Error al generar gráficos: {str(e)}")

generar_visualizaciones(tienda4, col_precio, col_calif, col_categoria)

# ======================
# 5. REPORTE EJECUTIVO  
# ======================
print("\n📈 INFORME DE RENDIMIENTO - TIENDA 4")
print("=" * 45)

# Formatear valores numéricos
for k, v in metricas.items():
    if isinstance(v, float):
        print(f"{k}: ${v:,.2f}" if 'Facturación' in k or 'Margen' in k else f"{k}: {v:.2f}")
    elif isinstance(v, dict):
        print(f"\n{k}:")
        for subk, subv in v.items():
            print(f"  - {subk}: {subv:.1%}")
    else:
        print(f"{k}: {v}")

# Mostrar resumen de calidad de datos
print("\n🔍 METADATOS:")
print(f"- Columnas encontradas: {list(tienda4.columns)}")
print(f"- Filas analizadas: {len(tienda4)}")
print(f"- Rango de fechas: {tienda4['Fecha'].min().date()} a {tienda4['Fecha'].max().date()}" if 'Fecha' in tienda4.columns else "- Datos de fecha no disponibles")

print("\n✅ Análisis completado exitosamente")