import pandas as pd
import matplotlib.pyplot as plt
import os

# Ruta base donde se encuentran los archivos
ruta_base = os.path.join(os.path.expanduser('~'), 'Desktop', 'challenge_1', 'challenge_1')

# Lista de archivos de tiendas
archivos_tiendas = [
    'tienda_1.xlsx',
    'tienda_2.xlsx',
    'tienda_3.xlsx',
    'tienda_4.xlsx'
]

# Diccionarios para almacenar resultados
ingresos = {}
ventas_por_categoria = {}
valoraciones = {}
productos_mas_vendidos = {}
productos_menos_vendidos = {}
costo_envio = {}

def cargar_datos(nombre_archivo):
    archivo = os.path.join(ruta_base, nombre_archivo)
    df = pd.read_excel(archivo, skiprows=1)
    df.columns = df.columns.str.strip()  # Limpiar nombres de columnas
    return df

for i, archivo in enumerate(archivos_tiendas, start=1):
    df = cargar_datos(archivo)
    nombre_tienda = f'Tienda {i}'

    # Ingreso total
    ingresos[nombre_tienda] = df['Precio'].sum()

    # Ventas por categoría
    ventas_por_categoria[nombre_tienda] = df['Categoría'].value_counts()

    # Valoración promedio
    valoraciones[nombre_tienda] = df['Calificación'].mean()

    # Producto más y menos vendido
    ventas_producto = df['Producto'].value_counts()
    productos_mas_vendidos[nombre_tienda] = ventas_producto.idxmax()
    productos_menos_vendidos[nombre_tienda] = ventas_producto.idxmin()

    # Costo de envío promedio
    costo_envio[nombre_tienda] = df['Valor del envío'].mean()

# --- VISUALIZACIONES ---

# Ingresos por tienda
plt.figure(figsize=(8, 5))
plt.bar(ingresos.keys(), ingresos.values(), color='skyblue')
plt.title('Ingresos Totales por Tienda')
plt.ylabel('Ingreso ($)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Ventas por categoría de la Tienda 1 (como ejemplo)
plt.figure(figsize=(8, 5))
ventas_por_categoria['Tienda 1'].plot(kind='bar', color='orange')
plt.title('Ventas por Categoría - Tienda 1')
plt.ylabel('Cantidad de Ventas')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Valoraciones promedio
plt.figure(figsize=(8, 5))
plt.bar(valoraciones.keys(), valoraciones.values(), color='green')
plt.title('Valoraciones Promedio por Tienda')
plt.ylabel('Calificación Promedio')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# --- RESULTADOS ---
print("\n--- INGRESOS TOTALES ---")
print(ingresos)

print("\n--- VENTAS POR CATEGORÍA (Tienda 1) ---")
print(ventas_por_categoria['Tienda 1'])

print("\n--- VALORACIONES PROMEDIO ---")
print(valoraciones)

print("\n--- PRODUCTOS MÁS VENDIDOS ---")
print(productos_mas_vendidos)

print("\n--- PRODUCTOS MENOS VENDIDOS ---")
print(productos_menos_vendidos)

print("\n--- COSTO DE ENVÍO PROMEDIO ---")
print(costo_envio)
