from datetime import datetime
import webbrowser as wb 
import streamlit as st
import pandas as pd

st.set_page_config( ## Configurações da página web do streamlit
    page_title="Home - FIFA", ## Titulo da página
    layout="wide", ## Se a página irá carregar com o tamanho 100%
    initial_sidebar_state="expanded", ## Se a sidebar irá carregar aberta ou fechada
)

## Verificar se meu dataframe já está presente no session state, caso não esteja, ler e colocar ele lá, para compartilhar dados com as outras páginas

if "data" not in st.session_state:
    df_data = pd.read_csv("fonts/CLEAN_FIFA23_official_data.csv", index_col=0) ## Ler o dataframe com a biblioteca pandas
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year] ## Filtrar o df pelos contratos que estão ativos na data atual
    df_data = df_data[df_data["Value(£)"] > 0] ## Filtrar por valores acima de 0
    df_data = df_data.sort_values(by="Overall", ascending=False) ## Ordenar por ordem de overall
    st.session_state["data"] = df_data ## Colocar o df filtrado e "tratado" no session state

st.title("DADOS OFICIAIS DA FIFA ⚽️!")
st.sidebar.write("Desenvolvido por [Felipe Barbour](https://www.linkedin.com/in/felipebarbour/)")

btn = st.button("Acesse os dados no Kaggle")

if btn:
    wb.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    
st.write("Este conjunto de dados cobre uma ampla gama de informações sobre jogadores de futebol profissional de 2017 a 2023. Ele inclui dados demográficos, características físicas, estatísticas de desempenho em jogos, detalhes contratuais e afiliações a clubes. Com mais de 17.000 registros, este recurso é valioso para analistas, pesquisadores e entusiastas do futebol que desejam explorar e estudar diversos aspectos do esporte, desde atributos individuais dos jogadores até métricas de desempenho coletivo.")