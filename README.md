# 🚗 Análisis Interactivo de Vehículos Usados

Esta aplicación web interactiva permite a los usuarios explorar un conjunto de datos de **vehículos usados** a través de visualizaciones dinámicas e intuitivas 📊. Fue desarrollada con **Streamlit** y **Plotly Express** para ofrecer una experiencia visual atractiva y accesible.

---

## 🧾 Contexto

La aplicación analiza y visualiza datos del archivo `vehicles_us.csv`, que contiene información sobre anuncios de venta de vehículos usados en los Estados Unidos 🇺🇸.  
Incluye variables como:

- Kilometraje  
- Precio  
- Año del vehículo  
- Tipo de transmisión  
- Y más características relevantes

---

## ✨ Funcionalidades

### 📉 Visualización de Histogramas
Analiza la distribución del **kilometraje** de los vehículos.  
✅ Ideal para identificar rangos de uso comunes entre los autos disponibles.

### 🔁 Gráfico de Dispersión
Muestra la relación entre **kilometraje** y **precio**.  
✅ Permite observar la correlación entre ambas variables de manera visual.

### 🖱️ Interactividad
Los usuarios pueden seleccionar qué visualización mostrar mediante **casillas de verificación**.  
Los gráficos son **interactivos**, lo que facilita la exploración detallada de los datos.

---

## 🧰 Tecnologías Utilizadas

- ⚙️ **Streamlit**: Para la creación de la interfaz web interactiva.  
- 📈 **Plotly Express**: Para la generación de gráficos interactivos y personalizados.  
- 🐼 **Pandas**: Para la manipulación y análisis del dataset.

---

## 🚀 Uso de la Aplicación

### 📦 Requisitos

Asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install streamlit plotly pandas
