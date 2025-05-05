import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.error import HTTPError

# Configuración de visualización
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 6)
sns.set_palette('viridis')

def cargar_datos():
    """Carga datos desde GitHub con manejo robusto de errores"""
    urls = {
        'Tienda 1': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_1.csv",
        'Tienda 2': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_2.csv",
        'Tienda 3': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_3.csv",
        'Tienda 4': "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_4.csv"
    }
    
    datos_tiendas = []
    
    for nombre, url in urls.items():
        try:
            print(f"Cargando {nombre}...")
            df = pd.read_csv(url)
            df['tienda'] = nombre
            datos_tiendas.append(df)
            print(f"✅ {nombre} cargada correctamente")
        except HTTPError as e:
            print(f"⚠️ Error 404 al cargar {nombre}. Usando datos de ejemplo...")
            datos_ejemplo = pd.DataFrame({
                'Producto': ['Producto Ejemplo'],
                'Precio': [0],
                'Costo de envío': [0],
                'Calificación': [3],
                'tienda': [nombre]
            })
            datos_tiendas.append(datos_ejemplo)
        except Exception as e:
            print(f"⚠️ Error inesperado en {nombre}: {e}")
            datos_tiendas.append(pd.DataFrame({'tienda': [nombre]}))
    
    return pd.concat(datos_tiendas, ignore_index=True)

# Cargar y preparar datos
datos = cargar_datos()

# Verificación de columnas esenciales
for col in ['Precio', 'Costo de envío', 'Calificación']:
    if col not in datos.columns:
        datos[col] = 0

# Convertir a numérico
datos['Precio'] = pd.to_numeric(datos['Precio'], errors='coerce').fillna(0)
datos['Costo de envío'] = pd.to_numeric(datos['Costo de envío'], errors='coerce').fillna(0)
datos['Calificación'] = pd.to_numeric(datos['Calificación'], errors='coerce').fillna(3)

# Análisis básico
analisis = datos.groupby('tienda').agg({
    'Precio': 'sum',
    'Calificación': 'mean',
    'Costo de envío': 'mean'
}).rename(columns={
    'Precio': 'Facturación Total',
    'Calificación': 'Calificación Promedio',
    'Costo de envío': 'Costo Envío Promedio'
})

# Visualización
fig, ax = plt.subplots(3, 1, figsize=(12, 15))

analisis['Facturación Total'].plot(kind='bar', ax=ax[0], title='Facturación por Tienda')
ax[0].set_ylabel('USD')

analisis['Calificación Promedio'].plot(kind='bar', ax=ax[1], title='Calificación Promedio', ylim=(0, 5))
ax[1].set_ylabel('Puntos')

analisis['Costo Envío Promedio'].plot(kind='bar', ax=ax[2], title='Costo de Envío Promedio')
ax[2].set_ylabel('USD')

plt.tight_layout()
plt.savefig('analisis_tiendas.png')
plt.close()

# Recomendación basada en métricas normalizadas
analisis_normalizado = analisis.copy()
for col in analisis.columns:
    if 'Facturación' in col:
        analisis_normalizado[col] = analisis[col] / analisis[col].max()
    elif 'Costo' in col:
        analisis_normalizado[col] = 1 - (analisis[col] / analisis[col].max())  # Invertir para que menor costo sea mejor
    else:
        analisis_normalizado[col] = analisis[col] / 5  # Calificación de 1-5

analisis_normalizado['Puntaje'] = (
    analisis_normalizado['Facturación Total'] * 0.5 +
    analisis_normalizado['Calificación Promedio'] * 0.3 +
    analisis_normalizado['Costo Envío Promedio'] * 0.2
)

peor_tienda = analisis_normalizado['Puntaje'].idxmin()

# Resultados
print("\n📊 Análisis Comparativo:")
print(analisis)

print("\n🔍 Métricas Normalizadas:")
print(analisis_normalizado)

print(f"\n🚨 Recomendación: Considerar cerrar {peor_tienda} por:")
print(f"- Facturación más baja: ${analisis.loc[peor_tienda, 'Facturación Total']:,.2f}")
print(f"- Calificación más baja: {analisis.loc[peor_tienda, 'Calificación Promedio']:.2f}/5")
print(f"- Costo de envío: ${analisis.loc[peor_tienda, 'Costo Envío Promedio']:,.2f}")

print("\n📈 Gráfico guardado como 'analisis_tiendas.png'")