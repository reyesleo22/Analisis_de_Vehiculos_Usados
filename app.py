import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:  # Al hacer clic en el botón
    st.write('Creación de un gráfico de dispersión mostrando la relación entre el precio y el kilometraje')
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre kilometraje y precio")
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)
