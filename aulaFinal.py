#item 2
import requests as req
import pandas as pd
import streamlit as st

#item 3

#identificando as mulheres
urlMulheres = "https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome"
resposta = req.get(urlMulheres)
dadosJSON = resposta.json()
dfMulheres = pd.DataFrame(dadosJSON['dados'])
dfMulheres['sexo'] = 'F'

#identificando os homens
urlHomens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta = req.get(urlHomens)
dadosJSON = resposta.json()
dfHomens = pd.DataFrame(dadosJSON['dados'])
dfHomens['sexo'] = 'M'

#unindo os dataframes
df = pd.concat([dfMulheres, dfHomens])

#item 5
opcao = st.selectbox(
    'Qual o sexo?',
    df['sexo'].unique()
)
dfFiltrado = df[df['sexo'] == opcao]
st.title('Deputados do sexo' + opcao)

#item 6
ocorrencias = dfFiltrado['siglaUf'].value_counts()
dfEstados = pd.DataFrame({
    'siglaUf':ocorrencias.index,
    'quantidade':ocorrencias.values}
)

#item 7
#total de homens
totalHomens = dfHomens['id'].count()
st.metric('Total de homens', totalHomens)

#total de homens
totalMulheres = dfMulheres['id'].count()
st.metric('Total de mulheres', totalMulheres)

st.bar_chart(dfEstados,
            x = 'siglaUf',
            y = 'quantidade',
            x_label = 'Siglas dos estados',
            y_label = 'Quantidade de deputados' 
      )        
st.dataframe(dfFiltrado)
