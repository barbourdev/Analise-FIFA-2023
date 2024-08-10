import streamlit as st
import pandas as pd
from datetime import datetime

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
