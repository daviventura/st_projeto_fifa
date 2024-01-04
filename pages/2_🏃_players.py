import streamlit as st
import pandas as pd
import time

st.set_page_config(
    layout='wide',
    page_title='FIFA'
)

df_data=pd.read_csv('../CLEAN_FIFA23_official_data.csv',index_col=0)

clubes=df_data['Club'].unique()
club=st.sidebar.selectbox('Clube',clubes)

df_players=df_data[df_data['Club']==club]
jogadores=df_players['Name'].unique()
jogador=st.sidebar.selectbox('Jogador',jogadores)


jogador_stats=df_data[df_data['Name']==jogador].iloc[0]

st.image(jogador_stats['Photo'])
st.title(jogador_stats['Name'])

st.markdown(f"**Clube:**  {jogador_stats['Club']}")
st.markdown(f"**Posição:**  {jogador_stats['Position']}")

col1,col2,col3,col4=st.columns(4)

col1.markdown(f"**Idade:**  {jogador_stats['Age']}")
col2.markdown(f"**Altura:**  {jogador_stats['Height(cm.)']/100}")
col3.markdown(f"**Peso:**  {jogador_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {jogador_stats['Overall']}")

overall_bar=st.progress(0,text='Overall do Jogador')
atributo=jogador_stats['Overall']

for overall in range(atributo):
    time.sleep(0.005)
    overall_bar.progress(overall+1,text='Overall Player')


col1,col2,col3,col4=st.columns(4)

time.sleep(0.1)
col1.metric('Valor de Mercado',value=f"£ {jogador_stats['Value(£)']:,.2f}")
time.sleep(0.1)
col2.metric('Remuneração/Semana',value=f"£ {jogador_stats['Wage(£)']:,.2f}")
time.sleep(0.1)
col3.metric('Cláusula de Rescisão',value=f"£ {jogador_stats['Release Clause(£)']:,.2f}")
