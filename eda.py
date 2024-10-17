import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit.components.v1 as components
import os

# Função para listar arquivos na pasta datasets
def list_files_in_datasets():
    files = [f for f in os.listdir('./datasets') if f.endswith('.csv') or f.endswith('.xlsx')]
    return files

# Verificar se há arquivos disponíveis na pasta
files_available = sorted(list_files_in_datasets())

st.title("Exploratory Data Analysis (EDA)")
st.divider()

if not files_available:
    st.warning("No files available. Please upload the data before starting the analysis.")
else:
    # Selectbox para o usuário escolher o arquivo
    selected_file = st.selectbox("Select the file for analysis", files_available)

    # Carregar o DataFrame com base no arquivo selecionado
    try:
        if selected_file.endswith('.csv'):
            df = pd.read_csv(f'./datasets/{selected_file}')
        else:
            df = pd.read_excel(f'./datasets/{selected_file}')
    except Exception as e:
        st.error(f"Error loading the file: {e}")
        st.stop()  # Para o código caso haja um erro ao carregar o arquivo

    # Função para gerar e armazenar o relatório de EDA em cache
    @st.cache_data
    def generate_profile_report(dataframe):
        profile = ProfileReport(dataframe, title='Exploratory Data Analysis for the DataFrame', explorative=True)
        return profile.to_html()

    # Botão para iniciar a análise
    start_analysis = st.button("Start Data Analysis", use_container_width=True)

    if start_analysis:
        try:
            # Gerar o relatório de perfilamento e armazenar em cache
            profile_html = generate_profile_report(df)

            # Exibir o relatório no Streamlit
            components.html(profile_html, height=1000, width=1100, scrolling=True)

        except Exception as e:
            st.error(f"Error generating the profile report: {e}")

    # Verificar se o relatório já está gerado e exibir
    elif st.session_state.get("profile_html"):
        components.html(st.session_state["profile_html"], height=1000, width=1100, scrolling=True)
