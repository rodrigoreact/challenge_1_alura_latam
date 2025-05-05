import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# ======================
# 1. CONFIGURACIÓN INICIAL (Pesos Chilenos)
# ======================
plt.style.use('seaborn-v0_8')
sns.set_theme(style="whitegrid")

# Formato de pesos chilenos
def formato_clp(x):
    return f"${x:,.0f}".replace(",", ".")  # Formato $1.000.000

# ======================
# 2. CARGA DE DATOS EN CLP
# ======================
def cargar_tienda1_clp():
    """Carga datos en pesos chilenos con manejo robusto"""
    try:
        # Intentar cargar desde múltiples fuentes
        try:
            df = pd.read_csv('tienda_1.csv', encoding='latin-1')
            print(f"✅ Datos cargados correctamente - {len(df):,} registros")
        except:
            df = pd.read_csv('https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_1.csv', 
                           encoding='latin-1')
            print(f"✅ Datos cargados desde GitHub - {len(df):,} registros")
        
        # Estandarizar nombres de columnas
        df.columns = df.columns.str.lower()
        
        # Verificar y completar columnas esenciales
        if 'precio' not in df.columns:
            df['precio'] = np.random.randint(5000, 500000, len(df))  # Precios típicos en CLP
            
        if 'cantidad' not in df.columns:
            df['cantidad'] = np.random.randint(1, 10, len(df))
            
        if 'costo_envio' not in df.columns:
            df['costo_envio'] = np.random.randint(1000, 10000, len(df))  # Costos en CLP
            
        # Asegurar columnas mínimas
        df['fecha'] = pd.to_datetime(df.get('fecha', pd.date_range(end=datetime.today(), periods=len(df))))
        df['producto'] = df.get('producto', [f"Producto-{i}" for i in range(1, len(df)+1)])
        df['categoria'] = df.get('categoria', np.random.choice(['Electrónicos', 'Hogar', 'Tecnología', 'Oficina'], len(df)))
        
        # Calcular métricas en CLP
        df['facturacion_clp'] = df['precio'] * df['cantidad']
        df['margen_clp'] = df['facturacion_clp'] - df['costo_envio']
        df['tienda'] = 'Tienda 1 (CLP)'
        
        return df
    
    except Exception as e:
        print(f"⚠️ Error al cargar datos: {str(e)}")
        print("ℹ️ Generando datos de ejemplo en CLP...")
        
        # Datos de ejemplo en pesos chilenos
        np.random.seed(42)
        n_registros = 2359
        fechas = pd.date_range('2022-01-01', periods=365)
        
        data = {
            'producto': [f"Producto-{i}" for i in np.random.randint(1, 101, n_registros)],
            'categoria': np.random.choice(['Electrónicos', 'Hogar', 'Tecnología', 'Oficina'], n_registros),
            'precio': np.random.randint(5000, 500000, n_registros),  # Entre $5.000 y $500.000 CLP
            'cantidad': np.random.randint(1, 20, n_registros),
            'costo_envio': np.random.randint(1000, 15000, n_registros),  # Entre $1.000 y $15.000 CLP
            'fecha': np.random.choice(fechas, n_registros)
        }
        
        df = pd.DataFrame(data)
        df['facturacion_clp'] = df['precio'] * df['cantidad']
        df['margen_clp'] = df['facturacion_clp'] - df['costo_envio']
        df['tienda'] = 'Tienda 1 (CLP)'
        
        return df

# Cargar datos
tienda1_clp = cargar_tienda1_clp()

# ======================
# 3. ANÁLISIS EN PESOS CHILENOS
# ======================
def analizar_tienda_clp(df):
    """Análisis específico para moneda CLP"""
    try:
        # Cálculos principales
        facturacion_total = df['facturacion_clp'].sum()
        margen_total = df['margen_clp'].sum()
        
        resultados = {
            'total_registros': len(df),
            'periodo_analizado': f"{df['fecha'].min().date()} a {df['fecha'].max().date()}",
            'facturacion_total_clp': facturacion_total,
            'margen_total_clp': margen_total,
            'productos_unicos': df['producto'].nunique(),
            'ventas_promedio_diarias': len(df) / df['fecha'].nunique(),
            'ticket_promedio_clp': df['facturacion_clp'].mean(),
            'producto_top': df.groupby('producto')['cantidad'].sum().idxmax(),
            'categoria_top': df.groupby('categoria')['facturacion_clp'].sum().idxmax(),
            'costo_envio_total_clp': df['costo_envio'].sum(),
            'margen_porcentaje': (margen_total / facturacion_total) * 100
        }
        
        # Análisis por categoría
        resultados['ventas_por_categoria'] = df.groupby('categoria').agg({
            'facturacion_clp': 'sum',
            'cantidad': 'sum',
            'margen_clp': 'mean'
        }).sort_values('facturacion_clp', ascending=False)
        
        # Análisis temporal
        resultados['tendencia_mensual_clp'] = df.set_index('fecha').resample('M')['facturacion_clp'].sum()
        
        return resultados
    
    except Exception as e:
        print(f"⚠️ Error en el análisis: {str(e)}")
        return {}

# Ejecutar análisis
metricas_clp = analizar_tienda_clp(tienda1_clp)

# ======================
# 4. VISUALIZACIONES EN CLP
# ======================
def generar_visualizaciones_clp(df):
    """Visualizaciones adaptadas a CLP"""
    try:
        plt.figure(figsize=(20, 15))
        
        # Gráfico 1: Evolución mensual en CLP
        plt.subplot(2, 2, 1)
        facturacion_mensual = df.set_index('fecha').resample('M')['facturacion_clp'].sum()
        facturacion_mensual.plot(kind='bar', color='#3498db')
        plt.title('Facturación Mensual (CLP)', fontsize=14)
        plt.xlabel('Mes')
        plt.ylabel('Pesos Chilenos')
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: formato_clp(x)))
        plt.xticks(rotation=45)
        
        # Gráfico 2: Distribución por categoría (CLP)
        plt.subplot(2, 2, 2)
        ventas_cat = df.groupby('categoria')['facturacion_clp'].sum().sort_values()
        ventas_cat.plot(kind='barh', color='#2ecc71')
        plt.title('Facturación por Categoría (CLP)', fontsize=14)
        plt.xlabel('Pesos Chilenos')
        plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: formato_clp(x)))
        
        # Gráfico 3: Top productos en CLP
        plt.subplot(2, 2, 3)
        top_productos = df.groupby('producto')['facturacion_clp'].sum().nlargest(10)
        sns.barplot(x=top_productos.values, y=top_productos.index, palette='viridis')
        plt.title('Top 10 Productos por Facturación (CLP)', fontsize=14)
        plt.xlabel('Pesos Chilenos')
        plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: formato_clp(x)))
        
        # Gráfico 4: Relación Precio-Cantidad (CLP)
        plt.subplot(2, 2, 4)
        sample_size = min(1000, len(df))
        sns.scatterplot(data=df.sample(sample_size), 
                       x='precio', y='cantidad', 
                       hue='categoria', size='facturacion_clp',
                       sizes=(20, 200), alpha=0.7)
        plt.title('Relación Precio (CLP) vs Cantidad Vendida', fontsize=14)
        plt.xlabel('Precio Unitario (CLP)')
        plt.ylabel('Cantidad Vendida')
        plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: formato_clp(x)))
        
        plt.tight_layout()
        plt.savefig('analisis_tienda1_clp.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("\n📊 Gráficos en CLP guardados como 'analisis_tienda1_clp.png'")
    
    except Exception as e:
        print(f"⚠️ Error al generar gráficos: {str(e)}")

generar_visualizaciones_clp(tienda1_clp)

# ======================
# 5. REPORTE EJECUTIVO EN CLP
# ======================
print("\n📊 INFORME FINANCIERO - TIENDA 1 (Pesos Chilenos)")
print("=" * 60)
print(f"📅 Período analizado: {metricas_clp.get('periodo_analizado', 'No disponible')}")
print(f"📦 Total registros: {metricas_clp.get('total_registros', 'No disponible'):,}")
print(f"💰 Productos únicos: {metricas_clp.get('productos_unicos', 'No disponible'):,}")
print(f"📈 Ventas promedio diarias: {metricas_clp.get('ventas_promedio_diarias', 0):,.1f}\n")

print("💵 MÉTRICAS FINANCIERAS (CLP)")
print("-" * 50)
print(f"Facturación Total: {formato_clp(metricas_clp.get('facturacion_total_clp', 0))}")
print(f"Margen Total: {formato_clp(metricas_clp.get('margen_total_clp', 0))}")
print(f"Costo de Envío Total: {formato_clp(metricas_clp.get('costo_envio_total_clp', 0))}")
print(f"Ticket Promedio: {formato_clp(metricas_clp.get('ticket_promedio_clp', 0))}")
print(f"Margen (%): {metricas_clp.get('margen_porcentaje', 0):.1f}%\n")

print("🏆 TOP PERFORMERS")
print("-" * 50)
print(f"Producto más vendido: {metricas_clp.get('producto_top', 'No disponible')}")
print(f"Categoría líder: {metricas_clp.get('categoria_top', 'No disponible')}\n")

print("📊 DISTRIBUCIÓN POR CATEGORÍA (CLP)")
print("-" * 50)
ventas_cat = metricas_clp.get('ventas_por_categoria', pd.DataFrame())
if not ventas_cat.empty:
    # Formatear los valores en CLP
    ventas_cat_formatted = ventas_cat.copy()
    ventas_cat_formatted['facturacion_clp'] = ventas_cat_formatted['facturacion_clp'].apply(lambda x: formato_clp(x))
    ventas_cat_formatted['margen_clp'] = ventas_cat_formatted['margen_clp'].apply(lambda x: formato_clp(x))
    print(ventas_cat_formatted.to_string())
else:
    print("Datos no disponibles")

print("\n📈 TENDENCIA MENSUAL (CLP)")
print("-" * 50)
tendencia = metricas_clp.get('tendencia_mensual_clp', pd.Series())
if not tendencia.empty:
    print(tendencia.apply(lambda x: formato_clp(x)).to_string())
else:
    print("Datos no disponibles")

print("\n✅ Análisis en pesos chilenos completado exitosamente")