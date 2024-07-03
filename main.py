import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from PIL import Image
from pydantic import BaseModel, Field, PrivateAttr
from pydantic_settings import BaseSettings


## Configuracoes da pagina
st.set_page_config(
    page_icon="robot", #https://icons.getbootstrap.com/
    page_title="Auto Machine Learning with Streamlit",
    layout="wide",
    initial_sidebar_state="auto",
)

##### 0.Side bar #####
with st.sidebar:
    logoHeader = Image.open("img/image4.png")
    st.image(logoHeader, use_column_width=True)
    st.header('ML `version 1.1`')

    selected = option_menu(
        #https://icons.getbootstrap.com/
        menu_icon="cast",
        menu_title="Main Menu",
        options=['Home', 'Upload', 'EDA', 'Machine Learning'],
        icons=['house-check-fill', 'cloud-arrow-up-fill', 'bar-chart-steps', 'robot'],
        default_index=0,
        orientation="vertical",
    )
    
    st.markdown("Desenvolvido por [Daniel Hilário](https://www.instagram.com/prof.danielhilario/)")

##### 1. Interacao com a Side bar #####
if selected == "Home":
    ## Abrir a página home.py
    with open("home.py", "r") as f:
        exec(f.read())
elif selected == "Upload":
    # Abrir o arquivo upload para submissao do arquivo
    with open("upload.py", "r") as f:
        exec(f.read())
elif selected == "EDA":
    # Abrir o arquivo EDA para análise estatística
    with open("eda.py", "r") as f:
        exec(f.read())
elif selected == "Machine Learning":
    # Abrir a página para análise usando os modelos de ML
    with open("ml.py", "r") as f:
        exec(f.read())
