import streamlit as st
import pandas as pd
import os

# Verifica se a pasta datasets existe, caso contrário, cria a pasta
if not os.path.exists('datasets'):
    os.makedirs('datasets')

# Custom CSS to change button size
st.markdown("""
    <style>
    .stButton > button {
        height: 2em;
        width: 100%;
        font-size: 1.5em;
    }
    </style>
    """, unsafe_allow_html=True)

# Page title and description
st.markdown("<h1 style='text-align: center;'>Upload your Data</h1>", unsafe_allow_html=True)

df = None  # Initializing df as None

# File type selection
file_type = st.selectbox("Select the file type", ["None", "CSV", "XLSX"], index=0,
                         help="Choose the file type you want to upload")

if file_type != "None":
    st.divider()

    with st.form("Upload"):
        # File upload widget
        file = st.file_uploader("Upload your data here", type=["csv"] if file_type == "CSV" else ["xlsx"])

        if file_type == "CSV":
            # Option to choose the CSV delimiter
            delimiter = st.selectbox("Select the CSV delimiter", [",", ";"], index=0,
                                     help="Choose ',' for comma and ';' for semicolon")
        else:
            delimiter = None

        # Campo para nome do arquivo
        file_name = st.text_input("Enter a name for the file (optional)", value="")

        submit_button = st.form_submit_button("Submit File", )

        if submit_button and file is not None:
            try:
                # Verifica se o usuário deu um nome ou usa o nome original
                if file_name == "":
                    file_name = file.name.split(".")[0]

                # Salva o arquivo com a extensão correta e salva o nome na sessão
                if file_type == 'CSV':
                    df = pd.read_csv(file, index_col=None, sep=delimiter)
                    file_path = f"datasets/{file_name}.csv"
                    df.to_csv(file_path, index=None)
                elif file_type == 'XLSX':
                    df = pd.read_excel(file, index_col=None)
                    file_path = f"datasets/{file_name}.xlsx"
                    df.to_excel(file_path, index=None)

                # Salva o caminho do arquivo na sessão
                st.session_state['file_path'] = file_path
                st.session_state['file_uploaded'] = True
                st.success(f"File successfully uploaded as {file_name}.{file_type.lower()}!")

            except Exception as e:
                st.error(f"Error processing the file: {e}")
        elif submit_button and file is None:
            st.warning("Please upload a file before submitting.")

# Botão "Display Dataframe" aparece somente após o upload bem-sucedido
if 'file_uploaded' in st.session_state and st.session_state['file_uploaded']:
    if st.button("Display Dataframe"):
        try:
            # Recupera o caminho do arquivo salvo na sessão
            if 'file_path' in st.session_state:
                file_path = st.session_state['file_path']
                # Carrega o arquivo com base no caminho salvo
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path)
                else:
                    df = pd.read_excel(file_path)

                st.markdown("<h3 style='text-align:center;'>Dataframe for EDA and ML Analysis</h3>", unsafe_allow_html=True)
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("No file uploaded yet.")
        except Exception as e:
            st.error(f"Error displaying the file: {e}")
