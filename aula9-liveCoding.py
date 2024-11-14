import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'nomeServidor':['Adriana', 'Thais', 'Samara'],
    'salario':[10000,25000,20000]
}   
)
st.write('Criando uma tabela')
st.write(df)

st.selectbox('Qual servidor você gostaria de selecionar?',
             df['nomeServidor'])
