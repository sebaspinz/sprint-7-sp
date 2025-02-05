import pandas as pd
import plotly.express as px
import streamlit as st

#car_data = pd.read_csv(r"C:\Users\poveds3\TRIPLETEN\Proyectos-git\Sprint-7\vehicles_us.csv") # leer los datos
car_data = pd.read_csv("vehicles_us.csv")
car_data.info()

st.header(":blue[Anuncios de coches]")
st.subheader('Proyecto sprint 7',divider="red")

# Construcion histograma
hist_button = st.checkbox('Construir histograma')
if hist_button: # al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", title="Histograma del conjunto de datos odometro",color_discrete_sequence=['indianred'])
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    fig.show()

# Construccon diagrama de dispersion
scatter_button = st.checkbox('Construir grafico de dispersion')
if scatter_button: # al hacer clic en el botón
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price", title="Grafico de dispersion de los datos de odometro con respecto a price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    fig.show()
    