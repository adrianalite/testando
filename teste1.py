import requests as rq
import pandas as pd
import streamlit as st

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/74646/despesas?ordem=ASC&ordenarPor=ano'

resposta = rq.get(url)
dadosJSON = resposta.json()
df = pd.DataFrame(dadosJSON['dados'])
#calculando os gastos
gastos = df['valorLiquido'].sum()
nomeDeputado = "Aécio Neves"

st.title('Gastos do deputado ' + nomeDeputado + nomeDeputado)
st.metric('Gastos do deputado', gastos)
