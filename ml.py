########################### Bibliotecas ###########################
import streamlit as st
import pandas as pd
import time
import os
import json
import papermill as pm
from sklearn.metrics import accuracy_score

########################### FUNÇÕES ###########################
# Função para listar arquivos na pasta datasets
def list_files_in_datasets():
    files = [f for f in os.listdir('./datasets') if f.endswith('.csv') or f.endswith('.xlsx')]
    return files

def ensure_models_folder():
    if not os.path.exists('models'):
        os.makedirs('models')

# Função para salvar as configurações em um arquivo JSON
def save_configurations(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)

# Função utilitária para verificar a existência de arquivos
def check_file_exists(filepath, error_message=None):
    if os.path.exists(filepath):
        return True
    else:
        if error_message:
            st.error(error_message)
        return False

# Função para rodar o notebook com papermill e esperar até que o arquivo seja gerado, com barra de progresso
def run_notebook():
    st.info("Training the models, please wait...")
    notebook_path = './train_models.ipynb'
    output_notebook_path = './models/train_models_output.ipynb'
    progress_bar = st.progress(0)  # Inicializa a barra de progresso

    try:
        # Executa o notebook com papermill
        pm.execute_notebook(notebook_path, output_notebook_path)
        for i in range(100):
            time.sleep(0.05)  # Simulando progresso
            progress_bar.progress(i + 1)
        st.success("Model training completed! Results saved in the 'models' folder.")
    except Exception as e:
        st.error(f"Error during model training: {e}")

    # Verifica continuamente se o arquivo results.csv foi gerado
    for i in range(30):  # Máximo de 30 segundos de espera
        if check_file_exists('models/results.csv'):
            break
        time.sleep(1)  # Aguarda 1 segundo antes de checar novamente
    else:
        st.error("Training completed, but results.csv was not found.")

    # Carregar e exibir os parâmetros do treinamento
    if check_file_exists('./models/setup_summary.csv'):
        setup_summary = pd.read_csv('./models/setup_summary.csv')
        st.write("### Training Parameters Summary")
        st.dataframe(setup_summary, use_container_width=True)

# Limpar o cache e deletar os arquivos config.json, results.csv and others
def clear_data():
    st.cache_data.clear()  # Limpar o cache
    files_to_remove = [
        'models/results.csv', 'models/predictions.csv',
        'models/best_model.pkl', 'models/best_model_params.json',
        'models/train_models_output.ipynb'
    ]
    for filepath in files_to_remove:
        if os.path.exists(filepath):
            os.remove(filepath)

    time.sleep(2)
    st.success("All data cleared successfully!")

# Função para carregar os resultados de treinamento
def load_results():
    if check_file_exists('./models/results.csv', "No results found. Please train the models first."):
        return pd.read_csv('./models/results.csv')
    return None

# Função para permitir download de JSON
def download_json(data, filename):
    json_data = json.dumps(data)
    st.download_button(label="Download Best Model Configurations (JSON)", data=json_data, file_name=filename, mime='application/json')

# Verifica se a pasta models existe
ensure_models_folder()

########################### INTERFACE ###########################

# Inicializar o estado da aplicação
if 'setup_completed' not in st.session_state:
    st.session_state.setup_completed = False

# Título da página
st.title("Machine Learning Models Analysis")
st.write("---")

# Seção de seleção do Dataset
st.markdown("### Selecting the Dataset")

# Listar os arquivos disponíveis para seleção
files_available = sorted(list_files_in_datasets())

if not files_available:
    st.warning("No files available. Please upload the data before starting the analysis.")
else:
    selected_file = st.selectbox("Select the file for the ML analysis", files_available)

    if selected_file:
        try:
            if selected_file.endswith('.csv'):
                df = pd.read_csv(f'./datasets/{selected_file}')
            else:
                df = pd.read_excel(f'./datasets/{selected_file}')

            # Exibir uma breve visualização do DataFrame
            st.write("#### Dataset Preview")
            st.dataframe(df.head(), use_container_width=True)

        except Exception as e:
            st.error(f"Error loading the file: {e}")
            st.stop()
        st.write("---")

# Seção de Configurações do Setup de Machine Learning
st.header("Setup Machine Learning Models")

# Variável alvo, semente e percentual do conjunto de teste em três colunas
col1, col2, col3 = st.columns(3)
with col1:
    target_variable = st.selectbox("Select the target:", df.columns, index=0) if selected_file else ""
with col2:
    session_id = st.number_input("Session ID (Seed):", min_value=1, step=1, value=1245)
with col3:
    test_size = st.slider('Test dataset percentage:', 0.05, 0.50, step=0.05, value=0.20)

# Configuração de normalização
normalize_data = st.checkbox("Normalize Data", value=False)
if normalize_data:
    normalization_method = st.selectbox("Normalization Method:", ["None", "zscore", "minmax", "maxabs", "robust"], index=0)
else:
     normalization_method = False

# Opção para remover multicolinearidade
remove_multicollinearity = st.checkbox("Remove Multicollinearity", value=False)
if remove_multicollinearity:
    multicollinearity_threshold = st.slider('Multicollinearity Threshold:', 0.1, 1.0, step=0.05, value=0.95)
else:
    multicollinearity_threshold = False

# Opção de fold strategy
use_fold_strategy = st.checkbox("Use Fold Strategy", value=False)
if use_fold_strategy:
    fold_strategy = st.selectbox("Fold Strategy:", ["kfold", "stratifiedkfold", "groupkfold", "timeseries"], index=1)
    fold_number = st.slider('Fold Number:', 1, 20, step=1, value=10)
else:
    fold_strategy = 'kfold'
    fold_number = 2

# Opção para corrigir desbalanceamento
fix_imbalance = st.checkbox("Fix Data Imbalance", value=False)
if fix_imbalance:
    st.info("Using SMOTE as the default method for fixing data imbalace.")
else:
    fix_imbalance = False

# Opção para aplicar PCA
apply_pca = st.checkbox("Apply PCA to Reduce Dimensionality", value=False)
if apply_pca:
    pca_method = st.selectbox("PCA Method:", ["linear", "kernel", "incremental"], index=0)
    pca_components = st.slider('Number of PCA Components:', 1, 10, step=1, value=5)
else:
    pca_method = None
    pca_components = None

# Opção para seleção de características
feature_selection = st.checkbox("Apply Feature Selection", value=False)
if feature_selection:
    st.info("Using classic feature selection with LightGBM as the default estimator.")
    n_features_to_select = st.slider('Number of Features to Select (fraction):', 0.2, 0.9, step=0.1, value=0.5)
else:
    n_features_to_select = None

# Botão de Setup para salvar as configurações
if st.button("Setup"):
    config = {
        "file": selected_file,
        "target": target_variable,
        "session_id": session_id,
        "normalize": normalize_data,
        "normalization_method": normalization_method,
        "test_size": test_size,
        "remove_multicollinearity": remove_multicollinearity,
        "multicollinearity_threshold": multicollinearity_threshold,
        "fold_strategy": fold_strategy,
        "fold_number": fold_number,
        "fix_imbalance": fix_imbalance,
        "pca": apply_pca,
        "pca_method": pca_method,
        "pca_components": pca_components,
        "feature_selection": feature_selection,
        "n_features_to_select": n_features_to_select
    }

    save_configurations(config)
    st.session_state.setup_completed = True
    st.success("Setup completed! Now, you can proceed to train the models.")

########################### BOTÕES DE AÇÃO ###########################
# Se o setup foi completado, exibir os botões de ação
if st.session_state.setup_completed:
    st.write("---")

    st.header("Action buttons")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        clear_button = st.button("Clear All Data")
    with col2:
        train_button = st.button("Training the Models")
    with col3:
        show_results_button = st.button("Training Results")
    with col4:
        hyperparam_button = st.button("Best Model")
    with col5:
        predict_button = st.button("Prediction - Testing data")

    # Ações associadas aos botões
    if train_button:
        run_notebook()

    if show_results_button:
        results = load_results()
        if results is not None:
            st.write("### Model Comparison Results")
            st.dataframe(results, use_container_width=True)

    if hyperparam_button:
        if check_file_exists('./models/best_model_params.json', "Best model hyperparameters not found."):
            try:
                with open('./models/best_model_params.json', 'r') as f:
                    best_model_params = json.load(f)
                st.write("### Best Model Hyperparameters")
                st.json(best_model_params)

                # Adicionar opção de download em JSON
                download_json(best_model_params, "best_model_params.json")

            except Exception as e:
                st.error(f"Error loading the best model hyperparameters: {e}")

    if predict_button:
        if check_file_exists('models/predictions.csv', "Predictions file not found."):
            with open('config.json', 'r') as f:
                config = json.load(f)
            predictions = pd.read_csv('models/predictions.csv')
            st.write("### Predictions on Testing Data")
            st.dataframe(predictions, use_container_width=True)

            accuracy = accuracy_score(predictions[config["target"]], predictions['prediction_label'])
            model_name = config.get("model_name", "Unknown Model")
            st.write(f"**Model Analyzed:** {model_name}")
            st.write(f"**Accuracy:** {accuracy * 100:.2f}%")

    if clear_button:
        clear_data()