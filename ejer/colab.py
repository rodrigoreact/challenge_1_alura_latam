# 📦 Instalar fpdf si es necesario


# 📦 Librerías
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from fpdf import FPDF

# 🎯 Enlaces corregidos
url1 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/main/base-de-datos-challenge1-latam/tienda_4.csv"

# 📊 Cargar los datos
tienda1 = pd.read_csv(url1)
tienda1['Tienda'] = 'Tienda 1'
tienda2 = pd.read_csv(url2)
tienda2['Tienda'] = 'Tienda 2'
tienda3 = pd.read_csv(url3)
tienda3['Tienda'] = 'Tienda 3'
tienda4 = pd.read_csv(url4)
tienda4['Tienda'] = 'Tienda 4'

# 🔗 Unir
df = pd.concat([tienda1, tienda2, tienda3, tienda4], ignore_index=True)
df['Precio'] = pd.to_numeric(df['Precio'], errors='coerce')
df['Costo de envío'] = pd.to_numeric(df['Costo de envío'], errors='coerce')

# 🔍 Análisis
facturacion = df.groupby('Tienda')['Precio'].sum()
ventas_categoria = df['Categoría del Producto'].value_counts()
calificacion_promedio = df.groupby('Tienda')['Calificación'].mean()
productos_mas = df['Producto'].value_counts().head(3)
productos_menos = df['Producto'].value_counts().tail(3)
envio_prom = df.groupby('Tienda')['Costo de envío'].mean()

# 🖼 Guardar gráficos en PDF
with PdfPages("analisis_tiendas.pdf") as pdf:
    plt.figure(figsize=(12, 8))
    
    plt.subplot(1, 3, 1)
    facturacion.plot(kind='bar', color='skyblue')
    plt.title('Facturación por Tienda')
    plt.ylabel('Total')
    
    plt.subplot(1, 3, 2)
    ventas_categoria.plot(kind='barh', color='salmon')
    plt.title('Ventas por Categoría')

    plt.subplot(1, 3, 3)
    calificacion_promedio.plot(kind='bar', color='lightgreen')
    plt.title('Calificación Promedio')
    plt.ylim(0, 5)

    plt.tight_layout()
    pdf.savefig()  # Guardar gráfica
    plt.close()

# 📄 Crear PDF de resultados con FPDF
pdf_doc = FPDF()
pdf_doc.add_page()
pdf_doc.set_font("Arial", size=12)
pdf_doc.cell(200, 10, "Resumen de Análisis de Tiendas", ln=True, align="C")
pdf_doc.ln(10)

# Insertar textos
def write_section(title, content):
    pdf_doc.set_font("Arial", 'B', size=12)
    pdf_doc.cell(200, 10, title, ln=True)
    pdf_doc.set_font("Arial", size=11)
    for line in content.split('\n'):
        pdf_doc.multi_cell(0, 8, line)
    pdf_doc.ln(5)

write_section("Facturación por Tienda", facturacion.to_string())
write_section("Ventas por Categoría", ventas_categoria.to_string())
write_section("Calificación Promedio por Tienda", calificacion_promedio.to_string())
write_section("Productos Más Vendidos", productos_mas.to_string())
write_section("Productos Menos Vendidos", productos_menos.to_string())
write_section("Costo de Envío Promedio por Tienda", envio_prom.to_string())

# Guardar PDF
pdf_doc.output("resumen_tiendas.pdf")

# 📎 Mostrar enlaces para descarga
from IPython.display import FileLink
print("📁 Haz clic para descargar:")
display(FileLink("analisis_tiendas.pdf"))
display(FileLink("resumen_tiendas.pdf"))
