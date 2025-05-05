import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración visual segura
try:
    plt.style.use('seaborn-v0_8')  # Estilo moderno equivalente
except:
    plt.style.use('ggplot')  # Alternativa más compatible

sns.set_theme(style="whitegrid")  # Configuración moderna de Seaborn

# ======================
# 1. CARGA DE DATOS ROBUSTA
# ======================
def cargar_tienda2():
    """Carga datos con múltiples fuentes de respaldo"""
    fuentes = [
        # Fuente 1: URL de GitHub
        ("https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_2.csv", "GitHub"),
        # Fuente 2: Archivo local
        ("tienda_2.csv", "local"),
        # Fuente 3: Datos de ejemplo
        (None, "ejemplo")
    ]
    
    for fuente, tipo in fuentes:
        try:
            if tipo == "ejemplo":
                raise Exception("Usando datos de ejemplo")
                
            df = pd.read_csv(fuente)
            print(f"✅ Datos cargados desde {tipo}")
            df['Tienda'] = 'Tienda 2'  # Añadir columna identificadora
            return df
        except Exception as e:
            print(f"⚠️ No se pudo cargar desde {tipo}: {str(e)}")
            continue
    
    # Datos de ejemplo si todo falla
    print("ℹ️ Usando datos de ejemplo estructurados")
    return pd.DataFrame({
        'Producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor'],
        'Categoría': ['Electrónicos', 'Accesorios', 'Accesorios', 'Electrónicos'],
        'Precio': [2500, 80, 120, 450],
        'Costo_envío': [120, 15, 15, 30],
        'Calificación': [4.5, 4.0, 3.8, 4.2],
        'Fecha': pd.date_range(start='2023-01-01', periods=4)
    })

# Cargar datos
tienda2 = cargar_tienda2()

# ======================
# 2. ANÁLISIS CON VERIFICACIÓN DE COLUMNAS
# ======================
def analizar_tienda(df):
    """Análisis seguro con verificación de estructura"""
    resultados = {}
    
    # Encontrar columna de precio (insensible a mayúsculas)
    col_precio = next((col for col in df.columns if 'precio' in col.lower()), None)
    
    # 1. Facturación total
    if col_precio:
        resultados['Facturación Total'] = df[col_precio].sum()
    else:
        resultados['Facturación Total'] = 'Columna de precios no encontrada'
    
    # 2. Producto más común
    col_producto = next((col for col in df.columns if 'producto' in col.lower()), None)
    if col_producto:
        resultados['Producto Más Popular'] = df[col_producto].mode()[0]
    else:
        resultados['Producto Más Popular'] = 'Columna de productos no encontrada'
    
    # 3. Calificación promedio
    col_calificacion = next((col for col in df.columns if 'calif' in col.lower()), None)
    if col_calificacion:
        resultados['Calificación Promedio'] = df[col_calificacion].mean()
    else:
        resultados['Calificación Promedio'] = 'Columna de calificación no encontrada'
    
    return resultados, col_precio, col_calificacion

# Ejecutar análisis
metricas, col_precio, col_calificacion = analizar_tienda(tienda2)

# ======================
# 3. VISUALIZACIÓN CON VALIDACIÓN
# ======================
def generar_visualizaciones(df, precio_col, calif_col):
    """Genera gráficos con validación de datos"""
    try:
        plt.figure(figsize=(15, 5))
        
        # Gráfico 1: Distribución de categorías
        plt.subplot(1, 3, 1)
        col_categoria = next((col for col in df.columns if 'categ' in col.lower()), None)
        if col_categoria:
            df[col_categoria].value_counts().plot(
                kind='pie', 
                autopct='%1.1f%%', 
                colors=sns.color_palette("pastel")
            )
            plt.title('Distribución por Categoría')
        else:
            plt.text(0.5, 0.5, 'Datos de categoría\nno disponibles', ha='center')
            plt.title('Datos faltantes')
        
        # Gráfico 2: Precios de productos
        plt.subplot(1, 3, 2)
        col_producto = next((col for col in df.columns if 'producto' in col.lower()), None)
        if precio_col and col_producto:
            sns.barplot(
                data=df.sort_values(precio_col, ascending=False),
                x=col_producto,
                y=precio_col,
                palette="viridis"
            )
            plt.title('Precios de Productos')
            plt.xticks(rotation=45)
        else:
            plt.text(0.5, 0.5, 'Datos de precios\nno disponibles', ha='center')
            plt.title('Datos faltantes')
        
        # Gráfico 3: Relación Precio-Calificación
        plt.subplot(1, 3, 3)
        if precio_col and calif_col:
            sns.scatterplot(
                data=df,
                x=precio_col,
                y=calif_col,
                s=100,
                hue=col_categoria if col_categoria else None
            )
            plt.title('Relación Precio-Calificación')
        else:
            plt.text(0.5, 0.5, 'Datos insuficientes\npara comparación', ha='center')
            plt.title('Datos faltantes')
        
        plt.tight_layout()
        plt.savefig('analisis_tienda2.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("\n📊 Gráficos guardados como 'analisis_tienda2.png'")
    except Exception as e:
        print(f"⚠️ Error al generar gráficos: {str(e)}")

generar_visualizaciones(tienda2, col_precio, col_calificacion)

# ======================
# 4. REPORTE EJECUTIVO
# ======================
print("\n📈 REPORTE DE ANÁLISIS - TIENDA 2")
print("="*40)
for k, v in metricas.items():
    if isinstance(v, (int, float)):
        print(f"{k}: ${v:,.2f}" if 'Facturación' in k else f"{k}: {v:.2f}")
    else:
        print(f"{k}: {v}")

# Mostrar estilos disponibles para referencia
print("\n🎨 Estilos de gráficos disponibles:")
print(plt.style.available)