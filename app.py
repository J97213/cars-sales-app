import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('notebooks/vehicles_us.csv')

st.header('Venta de carros')

hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')

if disp_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    st.write('Creación de un histograma para la columna "odometer"')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, key='histogram', use_container_width=True)

build_dispersion = st.checkbox('Construir gráfico de dispersión')

if build_dispersion:
    st.write(
        'Creación de un gráfico de dispersión para las columnas "odometer" y "price"')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, key='dispersion', use_container_width=True)
