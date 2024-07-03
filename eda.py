import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests
import os

# Função para carregar animações Lottie a partir de uma URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL da animação Lottie específica
lottie_url = "https://lottie.host/e1a2656b-a71d-4ff0-8ba8-005922673a4e/rIESHPrdJe.json"
lottie_animation = load_lottie_url(lottie_url)

# Placeholder para a animação
placeholder = st.empty()

# Verificar se o arquivo de dados existe
if not os.path.exists('dados.csv'):
    st.warning("Por favor, faça o upload dos dados na aba 'Upload de Arquivo' antes de iniciar a análise.")
else:
    # Carregar o DataFrame
    df = pd.read_csv('dados.csv')

    # Função para gerar e armazenar o relatório de EDA em cache
    @st.cache_data
    def generate_profile_report(dataframe):
        profile = ProfileReport(dataframe, title='Exploratory Data Analysis for the DataFrame', explorative=True)
        return profile.to_html()

    # Botão para iniciar a análise
    start_analysis = st.button("Iniciar Análise de Dados")

    if start_analysis:
        # Exibir a animação enquanto o relatório está carregando
        with placeholder.container():
            if lottie_animation:
                st_lottie(lottie_animation, height=200, key="loading")

        # Gerar o relatório de perfilamento e armazenar em cache
        profile_html = generate_profile_report(df)

        # Remover a animação de carregamento
        placeholder.empty()

        # Exibir o relatório no Streamlit
        components.html(profile_html, height=900, width=900, scrolling=True)

    # Verificar se o relatório já está gerado e exibir
    elif st.session_state.get("profile_html"):
        components.html(st.session_state["profile_html"], height=900, width=900, scrolling=True)
