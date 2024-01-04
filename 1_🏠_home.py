import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.markdown('# FIFA 2023 OFICIAL DATASET ⚽')
st.sidebar.markdown('Dados disponíveis no [Kaggle](https://www.youtube.com/)')

btn=st.button('Acesse os dados no Kaggle',type='secondary')
if btn:
    webbrowser.open_new_tab('https://www.youtube.com/')

st.markdown(
    ''' O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.'''
)
