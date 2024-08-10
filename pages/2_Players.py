import streamlit as st ## Import do streamlit

st.set_page_config( ## Configurações da página web do streamlit
    page_title="Players - FIFA", ## Titulo da página
    layout="wide", ## Se a página irá carregar com o tamanho 100%
    initial_sidebar_state="expanded" ## Se a sidebar irá carregar aberta ou fechada
)

df_data = st.session_state["data"] ## Leitura dos dados no session state

clubes = df_data["Club"].unique() ## Pegar de forma unica os clubes
club = st.sidebar.selectbox("Clubes", clubes) ## Criar um selectbox para selecionar o clube que deseja ver os dados

df_players = df_data[df_data["Club"] == club] ## Selecionar os jogadores do clube selecionado no passo acima
players = df_players["Name"].unique() ## Pegar os jogadores de forma única
player = st.sidebar.selectbox("Players", players) ## Criar um selectbox para selecionar o jogador que deseja ver os dados

player_stats = df_data[df_data["Name"] == player].iloc[0] ## Pegar do df os dados ja tratados do o clube + os dados do jogador escolhido

st.image(player_stats["Photo"]) ## Colocar a foto do joogador escolhido
st.title(player_stats["Name"]) ## Nome do jogador

st.markdown(f"**Clube:** {player_stats['Club']}") ## O clube desse jogador
st.markdown(f"**Posição:** {player_stats['Position']}") ## A posição que ele joga

col1, col2, col3, col4 = st.columns(4) ## Criação de um grid de 4 colunas

col1.write(f"**Idade:** {player_stats['Age']}") ## Idade do jogador
col2.write(f"**Altura:** {player_stats['Height(cm.)'] / 100}") ## Altura do jogador, foi necessário dividir por 100, pois veio em CM
col3.write(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.433:.2f}") ## Peso do jogador, foi feito um cálculo para converter em kg
st.divider() ## Uma linha de divisória entre os dados apresetados

st.subheader(f"Overall {player_stats['Overall']}") ## Um subtitulo
st.progress(int(player_stats["Overall"])) ## uma linha de progressão, utilizando o overall como base, já que vai de 0 a 100

col1, col2, col3, col4 = st.columns(4) ## Um novo grid de 4 posições

col1.metric("Valor de mercado", f"£ {player_stats["Value(£)"]:,}") ## Um visual de métrica
col2.metric("Remuneração semanal", f"£ {player_stats["Wage(£)"]:,}") ## Um visual de métrica
col3.metric("Cláusula de rescisão", f"£ {player_stats["Release Clause(£)"]:,}") ## Um visual de métrica