# -*- coding: utf-8 -*-
"""
ANÁLISIS DE TIENDAS ALURA STORE - CARGA DESDE URLS
Script para cargar y analizar datos de las 4 tiendas
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuración de estilos
plt.style.use('ggplot')
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def cargar_datos_desde_urls():
    """Carga los datos de las tiendas desde las URLs proporcionadas"""
    print("\n🔍 Cargando datos de tiendas desde URLs...")
    
    # URLs de los datos
    urls = {
        'Tienda 1': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv",
        'Tienda 2': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv",
        'Tienda 3': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv",
        'Tienda 4': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"
    }
    
    datos_tiendas = {}
    
    for nombre, url in urls.items():
        try:
            print(f"Cargando {nombre} desde URL...")
            df = pd.read_csv(url)
            
            # Verificar que hay datos
            if df.empty:
                raise ValueError(f"No se encontraron datos para {nombre}")
                
            # Asegurar que las columnas estén normalizadas
            df.columns = [col.strip() for col in df.columns]
            
            # Convertir precios a numéricos si es necesario
            if 'Precio' in df.columns:
                if df['Precio'].dtype == 'object':
                    df['Precio'] = pd.to_numeric(df['Precio'].str.replace('[$,]', '', regex=True), errors='coerce')
            
            # Añadir la columna de tienda
            df['tienda'] = nombre
            
            # Guardar el dataframe en el diccionario
            datos_tiendas[nombre] = df
            
            print(f"✅ {nombre} cargada | Registros: {len(df)} | Suma Precio: ${df['Precio'].sum():,.2f}")
            
        except Exception as e:
            print(f"❌ Error al cargar {nombre}: {str(e)}")
            datos_tiendas[nombre] = generar_datos_respaldo(nombre)
    
    return datos_tiendas

def generar_datos_respaldo(nombre_tienda, registros=5):
    """Genera datos de respaldo para una tienda si no se pudo cargar desde la URL"""
    print(f"Generando datos de respaldo para {nombre_tienda} ({registros} registros)")
    
    return pd.DataFrame({
        'Producto': [f'Producto {i}' for i in range(1, registros + 1)],
        'Precio': np.random.uniform(50, 500, registros),
        'Costo_envio': np.random.uniform(5, 25, registros),
        'Calificación': np.random.uniform(1, 5, registros),
        'tienda': nombre_tienda
    })

def combinar_y_analizar_datos(datos_tiendas):
    """Combina los datos de todas las tiendas y realiza el análisis"""
    # Verificar que hay datos para combinar
    if not datos_tiendas:
        print("❌ No hay datos disponibles para analizar")
        return None
    
    # Combinar todos los dataframes en uno solo
    dfs = list(datos_tiendas.values())
    datos_combinados = pd.concat(dfs, ignore_index=True)
    
    print(f"\n✅ Datos combinados | Total registros: {len(datos_combinados)}")
    
    # Análisis por tienda
    print("\n📊 RESUMEN DE FACTURACIÓN POR TIENDA:")
    for tienda in datos_combinados['tienda'].unique():
        df_tienda = datos_combinados[datos_combinados['tienda'] == tienda]
        print(f"{tienda}: {len(df_tienda)} registros | Facturación: ${df_tienda['Precio'].sum():,.2f}")
    
    # Análisis global
    total_facturacion = datos_combinados['Precio'].sum()
    print(f"\n💰 FACTURACIÓN TOTAL: ${total_facturacion:,.2f}")
    
    return datos_combinados

def generar_graficos(datos):
    """Genera gráficos para visualizar los datos"""
    if datos is None or datos.empty:
        print("❌ No hay datos disponibles para generar gráficos")
        return
    
    try:
        # 1. Gráfico de facturación por tienda
        plt.figure(figsize=(12, 6))
        facturacion = datos.groupby('tienda')['Precio'].sum().sort_values()
        ax = facturacion.plot(kind='barh', color='darkgreen')
        plt.title('Facturación por Tienda', fontsize=14)
        plt.xlabel('USD ($)', fontsize=12)
        plt.ylabel('Tienda', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        
        # Añadir las cantidades al final de cada barra
        for i, v in enumerate(facturacion):
            ax.text(v + 0.1, i, f"${v:,.2f}", va='center')
        
        plt.tight_layout()
        plt.savefig('facturacion_por_tienda.png', dpi=300)
        plt.close()
        print("✅ Gráfico de facturación guardado como 'facturacion_por_tienda.png'")
        
        # 2. Gráfico de cantidad de productos por tienda
        plt.figure(figsize=(12, 6))
        productos = datos.groupby('tienda').size().sort_values()
        ax = productos.plot(kind='barh', color='darkblue')
        plt.title('Cantidad de Productos por Tienda', fontsize=14)
        plt.xlabel('Cantidad de Productos', fontsize=12)
        plt.ylabel('Tienda', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        
        # Añadir las cantidades al final de cada barra
        for i, v in enumerate(productos):
            ax.text(v + 0.1, i, f"{v:,}", va='center')
        
        plt.tight_layout()
        plt.savefig('productos_por_tienda.png', dpi=300)
        plt.close()
        print("✅ Gráfico de productos guardado como 'productos_por_tienda.png'")
        
        # 3. Si hay datos de costo de envío, crear gráfico de costo promedio
        if 'Costo_envio' in datos.columns and datos['Costo_envio'].notna().any():
            plt.figure(figsize=(12, 6))
            costo_envio = datos.groupby('tienda')['Costo_envio'].mean().sort_values()
            ax = costo_envio.plot(kind='barh', color='darkred')
            plt.title('Costo de Envío Promedio por Tienda', fontsize=14)
            plt.xlabel('Costo Promedio ($)', fontsize=12)
            plt.ylabel('Tienda', fontsize=12)
            plt.grid(axis='x', linestyle='--', alpha=0.7)
            
            # Añadir las cantidades al final de cada barra
            for i, v in enumerate(costo_envio):
                ax.text(v + 0.01, i, f"${v:.2f}", va='center')
            
            plt.tight_layout()
            plt.savefig('costo_envio_promedio.png', dpi=300)
            plt.close()
            print("✅ Gráfico de costo de envío guardado como 'costo_envio_promedio.png'")
        
    except Exception as e:
        print(f"❌ Error al generar gráficos: {str(e)}")
        import traceback
        print(traceback.format_exc())

def guardar_datos_combinados(datos):
    """Guarda los datos combinados en un archivo CSV"""
    if datos is None or datos.empty:
        print("❌ No hay datos disponibles para guardar")
        return
    
    try:
        datos.to_csv('datos_combinados_tiendas.csv', index=False)
        print("✅ Datos combinados guardados como 'datos_combinados_tiendas.csv'")
        
        # También guardar un resumen de facturación
        resumen = datos.groupby('tienda')['Precio'].agg(['count', 'sum', 'mean'])
        resumen.columns = ['Cantidad_Productos', 'Facturacion_Total', 'Precio_Promedio']
        resumen.to_csv('resumen_facturacion_tiendas.csv')
        print("✅ Resumen de facturación guardado como 'resumen_facturacion_tiendas.csv'")
        
    except Exception as e:
        print(f"❌ Error al guardar datos: {str(e)}")

def main():
    """Función principal que ejecuta todo el proceso"""
    print("🚀 INICIANDO ANÁLISIS DE TIENDAS ALURA STORE\n")
    
    try:
        # 1. Cargar datos desde URLs
        datos_tiendas = cargar_datos_desde_urls()
        
        # 2. Combinar y analizar datos
        datos_combinados = combinar_y_analizar_datos(datos_tiendas)
        
        # 3. Generar gráficos
        generar_graficos(datos_combinados)
        
        # 4. Guardar datos combinados
        guardar_datos_combinados(datos_combinados)
        
        print("\n✅ ANÁLISIS COMPLETADO CON ÉXITO")
        
    except Exception as e:
        print(f"\n❌ ERROR IRRECUPERABLE: {str(e)}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    main()