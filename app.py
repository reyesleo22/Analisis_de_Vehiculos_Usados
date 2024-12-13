import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Análisis de Vehículos",
    page_icon="🚗",
    layout="centered"
)

st.title("📊 Análisis Interactivo de Vehículos Usados")
st.write(
    "Explora el conjunto de datos de anuncios de venta de coches. "
    "Selecciona una opción para visualizar la distribución del kilometraje o la relación entre kilometraje y precio."
)

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.checkbox('Mostrar histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Distribución del Kilometraje")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.checkbox('Mostrar gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión mostrando la relación entre el precio y el kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre Kilometraje y Precio")
    st.plotly_chart(fig, use_container_width=True)
