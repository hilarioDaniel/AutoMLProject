import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

## Configuracoes da pagina
st.set_page_config(
    page_icon="robot", #https://icons.getbootstrap.com/
    page_title="EDA and Machine Learning with Python and Streamlit",
    layout="wide",
    initial_sidebar_state="auto",
)

##### 0.Side bar #####
with st.sidebar:
    logoHeader = Image.open("img/niats.png")
    st.image(logoHeader, use_column_width=True)
    st.header('EDA and ML `version 1.0`')

    selected = option_menu(
        menu_icon="cast",
        menu_title="Main Menu",
        options=['Home', 'Upload', 'EDA', 'Machine Learning'],
        icons=['house-check-fill', 'cloud-arrow-up-fill', 'bar-chart-steps', 'robot'],
        default_index=0,
        orientation="vertical",
    )
    
    st.markdown("Developed by: [Silva, D.H.](https://www.instagram.com/prof.danielhilario/) and [Ribeiro, C.T](https://www.instagram.com/caiotonus/)")

##### 1. Side bar interaction #####
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