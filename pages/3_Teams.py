import streamlit as st ## Import do streamlit

st.set_page_config( ## Configurações da página web do streamlit
    page_title="Teams - FIFA", ## Titulo da página
    layout="wide", ## Se a página irá carregar com o tamanho 100%
    initial_sidebar_state="expanded" ## Se a sidebar irá carregar aberta ou fechada
)

df_data = st.session_state["data"] ## Leitura dos dados no session state

clubes = df_data["Club"].unique() ## Pegar de forma unica os clubes
club = st.sidebar.selectbox("Clubes", clubes) ## Criar um selectbox para selecionar o clube que deseja ver os dados

df_filtered = df_data[df_data["Club"] == club].set_index("Name") ## Filtrar o DF apenas com os dados do clube selecionado

st.image(df_filtered.iloc[0]["Club Logo"]) ## Colocar a imagem do clube selecionado
st.markdown(f"## {club}") ## O nome do clube selecionado

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined", "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"] ## Colunas que serão utilizadas

st.dataframe( ## Um visual de tabela, que permite mudar o comportamento de determinada coluna, mudando o tipo de dado presente nela, como por exemplo, exibir uma imagem
    df_filtered[columns],
        column_config={
               "Overall": st.column_config.ProgressColumn(
                   "Overall", format= "%d" ,min_value= 0, max_value= 100
               ),
               "Wage(£)": st.column_config.ProgressColumn(
                   "Weekly Wage", format= "£%f" ,min_value= 0, max_value=df_filtered["Wage(£)"].max()
               ),
               "Photo": st.column_config.ImageColumn(),
               "Flag": st.column_config.ImageColumn("Country")
        }
)