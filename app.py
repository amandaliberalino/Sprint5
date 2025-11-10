# Importando bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly_express as px


# Importando os dados
df_cars = pd.read_csv('data/vehicles.csv')

# Cabeçalho do frontend
st.header('Dashboard para análises de de anúncios de carros', divider= 'blue')
st.subheader('Desenvolvido para avaliação como projeto referente à _SPRINT 5_: Ferramentas de engenharia de software.')

# Botão para criação do histograma
#hist_button = st.button('Criar histograma')

# Checkbox para histograma
hist = st.checkbox('Histograma')

if hist:
    st.write('Criando histograma para o conjunto de anúncios de vendas de carro.')

    # histograma
    fig = px.histogram(df_cars, x='odometer',title='Classificação por quilometragem')

    # Gráfico iterativo
    st.plotly_chart(fig)

# Botão para criação do grafico de dispersão
#disp_button = st.button('Criar dispersão')

# Checkbox para gráfico de dispersão
disp = st.checkbox('Gráfico de dispersão')

if disp:
    st.write('Criando gráfico de dispersão para conjunto de anúncios de vendas de carro.')

    # Gráfico de dispersão
    fig = px.scatter(df_cars, x="odometer", y="price", title='Valorização dos carros em função da quilometragem')

    # Gráfico iterativo
    st.plotly_chart(fig)
