#questao 3
import streamlit as st


numero = st.slider('Selecione um número', min_value=0, max_value=100)
st.text('Seu número é ' + str(numero))
