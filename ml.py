# import streamlit as st
# import pandas as pd
# from pycaret.classification import setup, compare_models, pull, predict_model, save_model, load_model
# import os
#
# # Função para listar arquivos na pasta datasets
# def list_files_in_datasets():
#     return [f for f in os.listdir('./datasets') if f.endswith(('.csv', '.xlsx'))]
#
# # Title and description of the initial page
# st.title("Machine Learning Models Analysis")
# st.divider()
#
# st.markdown('#### Choose the file for ML Classification Analysis')
# # Listar os arquivos disponíveis para seleção
# files_available = list_files_in_datasets()
#
# if not files_available:
#     st.warning("No files available. Please upload the data before starting the analysis.")
# else:
#     # Selectbox para o usuário escolher o arquivo para a análise
#     selected_file = st.selectbox("Select the file for analysis", files_available)
#
#     # Carregar o DataFrame com base no arquivo selecionado
#     file_path = f'./datasets/{selected_file}'
#
#     try:
#         df = pd.read_csv(file_path) if selected_file.endswith('.csv') else pd.read_excel(file_path)
#     except Exception as e:
#         st.error(f"Error loading the file: {e}")
#         st.stop()
#
#     st.divider()
#
#     # Se o DataFrame foi carregado corretamente
#     with st.form("Basic Settings"):
#         st.subheader("Training models for classifying problems")
#
#         # Definir as variáveis de configuração
#         target_variable = st.selectbox("Select the target variable:", df.columns, index=2)
#         test_size = st.slider('Test dataset percentage:', 0.05, 1.00, step=0.05, value=0.20)
#         fold_strategy = st.selectbox("Select the fold strategy:", ["kfold", "stratifiedkfold"])
#         folds_number = st.number_input('Number of Folds', min_value=2, max_value=10, value=5)
#         normalization_method = st.selectbox("Normalization method:", ["None", "minmax", "zscore"], index=0)
#         multicollinearity_threshold = st.slider('Multicollinearity Threshold (1 to disable):', 0.00, 1.00, step=0.05,
#                                                 value=0.00)
#         train_models = st.form_submit_button("Train the ML Models", use_container_width=True)
#
#     if train_models:
#         # PyCaret setup
#         setup_params = {
#             'data': df,
#             'target': target_variable,
#             'session_id': 1245,
#             'normalize': normalization_method != "None",
#             'remove_multicollinearity': multicollinearity_threshold > 0,
#             'fold_strategy': fold_strategy,
#             'fold': folds_number,
#             'train_size': 1 - test_size
#         }
#
#         if normalization_method != "None":
#             setup_params['normalize_method'] = normalization_method
#         if multicollinearity_threshold > 0:
#             setup_params['multicollinearity_threshold'] = multicollinearity_threshold
#
#         setup(**setup_params)
#         setup_df = pull()
#
#         st.markdown("### Training setup parameters")
#         st.dataframe(setup_df, use_container_width=True)
#
#         # Model Training
#         best_model = compare_models()
#         compare_df = pull()
#
#         st.markdown("### Model comparison results")
#         st.dataframe(compare_df, use_container_width=True)
#
#         st.markdown("### Hyperparameters for the best model")
#         st.json(best_model.get_params(), expanded=False)
#
#         # Saving the best model
#         save_model(best_model, 'best_model')
#         st.success("Best model saved!")
#
#     # Seção de predição
#     with st.form("Model Evaluation"):
#         st.subheader("Model Evaluation")
#         testing_models = st.form_submit_button("Predictions with the Best Model", use_container_width=True)
#
#     if testing_models:
#         try:
#             best_model = load_model('best_model')
#             st.markdown("### Predictions on the test dataset")
#             test_predictions = predict_model(best_model)
#             st.dataframe(test_predictions, use_container_width=True)
#
#             st.markdown("### Evaluation metrics")
#             metrics = pull()
#             st.dataframe(metrics, use_container_width=True)
#         except Exception as e:
#             st.error(f"Error making predictions: {e}")

# import streamlit as st
# import pandas as pd
# from pycaret.classification import setup, compare_models, predict_model, save_model, load_model
# import os
#
#
# # Função para listar arquivos na pasta datasets
# def list_files_in_datasets():
#     return [f for f in os.listdir('./datasets') if f.endswith(('.csv', '.xlsx'))]
#
#
# # Title and description of the initial page
# st.title("Machine Learning Models Analysis")
#
# # Listar os arquivos disponíveis para seleção
# files_available = list_files_in_datasets()
#
# if not files_available:
#     st.warning("No files available. Please upload the data before starting the analysis.")
# else:
#     # Selectbox para o usuário escolher o arquivo para a análise
#     selected_file = st.selectbox("Select the file for analysis", files_available)
#
#     # Carregar o DataFrame com base no arquivo selecionado
#     file_path = f'./datasets/{selected_file}'
#     try:
#         df = pd.read_csv(file_path) if selected_file.endswith('.csv') else pd.read_excel(file_path)
#     except Exception as e:
#         st.error(f"Error loading the file: {e}")
#         st.stop()
#
#     # Se o DataFrame foi carregado corretamente
#     with st.form("Basic Settings"):
#         st.subheader("Training models for classifying problems")
#
#         # Definir as variáveis de configuração
#         target_variable = st.selectbox("Select the target variable:", df.columns, index=2)
#         test_size = st.slider('Test dataset percentage:', 0.05, 1.00, step=0.05, value=0.20)
#         normalization_method = st.selectbox("Normalization method:", ["minmax", "zscore"], index=0)
#         train_models = st.form_submit_button("Train the ML Models", use_container_width=True)
#
#     if train_models:
#         # PyCaret setup exatamente como no Jupyter Notebook
#         clf = setup(
#             data=df,
#             target=target_variable,
#             session_id=123,  # Igual ao notebook
#             normalize=True,  # Normalização sempre ativada
#             normalize_method=normalization_method,  # Método de normalização selecionado
#             train_size=1 - test_size  # Proporção do conjunto de treinamento
#         )
#
#
#         # Model Training - compare_models retorna o melhor modelo diretamente
#         try:
#             best_model = compare_models(sort='AUC')  # Ordenar por AUC
#
#             st.markdown("### Model comparison results")
#             st.write(best_model)  # Exibir o melhor modelo selecionado
#
#             st.markdown("### Hyperparameters for the best model")
#             st.json(best_model.get_params(), expanded=False)
#
#             # Saving the best model
#             save_model(best_model, 'best_model')
#             st.success("Best model saved!")
#
#         except Exception as e:
#             st.error(f"Error during model training or comparison: {e}")
#
#     # Seção de predição
#     with st.form("Model Evaluation"):
#         st.subheader("Model Evaluation")
#         testing_models = st.form_submit_button("Predictions with the Best Model", use_container_width=True)
#
#     if testing_models:
#         try:
#             best_model = load_model('best_model')
#             st.markdown("### Predictions on the test dataset")
#             test_predictions = predict_model(best_model)
#             st.dataframe(test_predictions, use_container_width=True)
#
#         except Exception as e:
#             st.error(f"Error making predictions: {e}")

# import streamlit as st
# import pandas as pd
# import json
# import os
#
#
# # Função para listar arquivos na pasta datasets
# def list_files_in_datasets():
#     return [f for f in os.listdir('./datasets') if f.endswith(('.csv', '.xlsx'))]
#
#
# # Página do Streamlit para configurar
# st.title("Machine Learning Configuration")
#
# files_available = list_files_in_datasets()
#
# if not files_available:
#     st.warning("No files available.")
# else:
#     # Escolher o arquivo
#     selected_file = st.selectbox("Select the file for analysis", files_available)
#
#     # Carregar o DataFrame com base no arquivo selecionado
#     file_path = f'./datasets/{selected_file}'
#     try:
#         df = pd.read_csv(file_path) if selected_file.endswith('.csv') else pd.read_excel(file_path)
#         st.write("### Data Preview:")
#         # Expandir o dataframe para usar toda a largura da tela
#         st.dataframe(df.head(), use_container_width=True)
#     except Exception as e:
#         st.error(f"Error loading the file: {e}")
#         st.stop()
#
#     # Organizar a variável alvo e o session_id em duas colunas
#     col1, col2 = st.columns(2)
#
#     with col1:
#         # Selecionar a variável alvo como selectbox com base nas colunas do dataset carregado
#         target_variable = st.selectbox("Target variable (coluna do alvo)", df.columns)
#
#     with col2:
#         # Campo para inserir a semente
#         session_id = st.number_input("Session ID", value=123)
#
#     # Configuração da normalização
#     normalize = st.checkbox("Normalize data", value=False)
#     normalization_method = None
#
#     if normalize:
#         # Exibir a escolha do método de normalização se a normalização estiver marcada
#         normalization_method = st.selectbox("Normalization method", ["", "zscore", "minmax", "maxabs", "robust"])
#
#     test_size = st.slider("Test dataset percentage", 0.05, 1.0, value=0.2)
#
#     # Botão para salvar as configurações e rodar o pycaret_clf.py
#     if st.button("Run Analysis"):
#         config = {
#             "file": selected_file,
#             "target": target_variable,
#             "normalize": normalize,
#             "normalization_method": normalization_method,
#             "session_id": session_id,
#             "test_size": test_size
#         }
#
#         # Salvar configurações em um arquivo JSON
#         with open('config.json', 'w') as f:
#             json.dump(config, f)
#
#         # Rodar o arquivo pycaret_clf.py
#         os.system('python pycaret_clf.py')  # Executa o arquivo pycaret_clf.py
#
#         st.success(
#             "Configurations saved! The machine learning models are being processed. Please wait for the results.")

#
# import streamlit as st
# import subprocess
# import pandas as pd
# import json
# import os
#
#
# # Função para listar arquivos na pasta datasets
# def list_files_in_datasets():
#     files = [f for f in os.listdir('./datasets') if f.endswith('.csv') or f.endswith('.xlsx')]
#     return files
#
# def ensure_models_folder():
#     if not os.path.exists('models'):
#         os.makedirs('models')
#
# #Verifica se a pasta models existe
# ensure_models_folder()
#
# # Função para salvar as configurações em um arquivo JSON
# def save_configurations(config):
#     with open('config.json', 'w') as f:
#         json.dump(config, f)
#
#
# # Inicializar o estado da aplicação
# if 'setup_completed' not in st.session_state:
#     st.session_state.setup_completed = False
#
# # Title and description of the initial page
# st.title("Machine Learning Models Analysis")
# st.write("---")
#
# # Seção de seleção do Dataset
# st.markdown("### Selecting the Dataset")
#
# # Listar os arquivos disponíveis para seleção
# files_available = list_files_in_datasets()
#
# if not files_available:
#     st.warning("No files available. Please upload the data before starting the analysis.")
# else:
#     selected_file = st.selectbox("Select the file for the ML analysis", files_available)
#
#     if selected_file:
#         try:
#             if selected_file.endswith('.csv'):
#                 df = pd.read_csv(f'./datasets/{selected_file}')
#             else:
#                 df = pd.read_excel(f'./datasets/{selected_file}')
#
#             # Exibir uma breve visualização do DataFrame
#             st.write("#### Dataset Preview")
#             st.dataframe(df.head(), use_container_width=True)
#
#         except Exception as e:
#             st.error(f"Error loading the file: {e}")
#             st.stop()
#         st.write("---")
#
# # Seção de Configurações do Setup de Machine Learning
# st.header("Setup Machine Learning Models")
#
# # Variável alvo, semente e percentual do conjunto de teste em três colunas
# col1, col2, col3 = st.columns(3)
# with col1:
#     target_variable = st.selectbox("Select the target variable:", df.columns, index=0) if selected_file else ""
# with col2:
#     session_id = st.number_input("Session ID (Random State):", min_value=1, step=1, value=1245)
# with col3:
#     test_size = st.slider('Test dataset percentage:', 0.05, 0.50, step=0.05, value=0.20)
#
# # Configuração de normalização
# normalize_data = st.checkbox("Normalize Data", value=False)
# if normalize_data:
#     normalization_method = st.selectbox("Normalization Method:", ["None", "zscore", "minmax", "maxabs", "robust"], index=0)
# else:
#     normalization_method = None
#
# # Opção para remover multicolinearidade
# remove_multicollinearity = st.checkbox("Remove Multicollinearity", value=False)
# if remove_multicollinearity:
#     multicollinearity_threshold = st.slider('Multicollinearity Threshold:', 0.1, 1.0, step=0.1, value=0.9)
# else:
#     multicollinearity_threshold = None
#
# # Opção de fold strategy
# use_fold_strategy = st.checkbox("Use Fold Strategy", value=False)
# if use_fold_strategy:
#     fold_strategy = st.selectbox("Fold Strategy:", ["kfold", "stratifiedkfold", "groupkfold", "timeseries"], index=1)
#     fold_number = st.slider('Fold Number:', 2, 20, step=1, value=10)
# else:
#     fold_strategy = None
#     fold_number = None
#
# # Botão de Setup para salvar as configurações
# if st.button("Setup"):
#     config = {
#         "file": selected_file,
#         "target": target_variable,
#         "session_id": session_id,
#         "normalize": normalize_data,
#         "normalization_method": normalization_method,
#         "test_size": test_size,
#         "remove_multicollinearity": remove_multicollinearity,
#         "multicollinearity_threshold": multicollinearity_threshold,
#         "fold_strategy": fold_strategy,
#         "fold_number": fold_number
#     }
#
#     save_configurations(config)
#     st.session_state.setup_completed = True
#     st.success("Setup completed! Now, you can proceed to train the models.")
#
# # Se o setup foi completado, exibir os botões de ação
# if st.session_state.setup_completed:
#     st.write("---")  # Outro separador visual
#
#     st.header("Action buttons")
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         train_button = st.button("Training the Models")
#     with col2:
#         hyperparam_button = st.button("Show the Best Model")
#     with col3:
#         predict_button = st.button("Prediction with the best model - Testing data")
#
#     # Ações associadas aos botões
#     if train_button:
#         st.info("Training the models, please wait...")
#         # Rodar o arquivo .ipynb para treinar os modelos
#         try:
#             subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "train_models.ipynb"], check=True)
#             st.success("Model training completed! Results saved in the 'models' folder.")
#         except subprocess.CalledProcessError as e:
#             st.error(f"Error during model training: {e}")
#
#         # Verificar se o arquivo results.csv foi criado
#         if os.path.exists('models/results.csv'):
#             # Carregar e exibir os resultados
#             results = pd.read_csv('models/results.csv')
#             st.write("### Model Comparison Results")
#             st.dataframe(results)
#         else:
#             st.warning("No results found. Please check if the training was successful.")
#
#     if hyperparam_button:
#         st.info("Showing hyperparameters... (To be implemented)")
#
#     if predict_button:
#         st.info("Predicting with the best model... (To be implemented)")


import streamlit as st
import subprocess
import pandas as pd
import json
import os
import papermill as pm

# Função para listar arquivos na pasta datasets
def list_files_in_datasets():
    files = [f for f in os.listdir('./datasets') if f.endswith('.csv') or f.endswith('.xlsx')]
    return files

def ensure_models_folder():
    if not os.path.exists('models'):
        os.makedirs('models')

# Verifica se a pasta models existe
ensure_models_folder()

# Função para salvar as configurações em um arquivo JSON
def save_configurations(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)

# Função para rodar o notebook com papermill
def run_notebook():
    st.info("Training the models, please wait...")

    # Path do notebook que será executado
    notebook_path = './train_models.ipynb'

    # Path do notebook de saída gerado após a execução
    output_notebook_path = './models/train_models_output.ipynb'

    # Executar o notebook com papermill
    try:
        pm.execute_notebook(notebook_path, output_notebook_path)
        st.success("Model training completed! Results saved in the 'models' folder.")
    except Exception as e:
        st.error(f"Error during model training: {e}")

# Inicializar o estado da aplicação
if 'setup_completed' not in st.session_state:
    st.session_state.setup_completed = False

# Title and description of the initial page
st.title("Machine Learning Models Analysis")
st.write("---")

# Seção de seleção do Dataset
st.markdown("### Selecting the Dataset")

# Listar os arquivos disponíveis para seleção
files_available = list_files_in_datasets()

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
    target_variable = st.selectbox("Select the target variable:", df.columns, index=0) if selected_file else ""
with col2:
    session_id = st.number_input("Session ID (Random State):", min_value=1, step=1, value=1245)
with col3:
    test_size = st.slider('Test dataset percentage:', 0.05, 0.50, step=0.05, value=0.20)

# Configuração de normalização
normalize_data = st.checkbox("Normalize Data", value=False)
if normalize_data:
    normalization_method = st.selectbox("Normalization Method:", ["None", "zscore", "minmax", "maxabs", "robust"], index=0)
else:
    normalization_method = None

# Opção para remover multicolinearidade
remove_multicollinearity = st.checkbox("Remove Multicollinearity", value=False)
if remove_multicollinearity:
    multicollinearity_threshold = st.slider('Multicollinearity Threshold:', 0.1, 1.0, step=0.1, value=0.9)
else:
    multicollinearity_threshold = None

# Opção de fold strategy
use_fold_strategy = st.checkbox("Use Fold Strategy", value=False)
if use_fold_strategy:
    fold_strategy = st.selectbox("Fold Strategy:", ["kfold", "stratifiedkfold", "groupkfold", "timeseries"], index=1)
    fold_number = st.slider('Fold Number:', 1, 20, step=1, value=10)
else:
    fold_strategy = None
    fold_number = None

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
        "fold_number": fold_number
    }

    save_configurations(config)
    st.session_state.setup_completed = True
    st.success("Setup completed! Now, you can proceed to train the models.")

# Se o setup foi completado, exibir os botões de ação
if st.session_state.setup_completed:
    st.write("---")  # Outro separador visual

    st.header("Action buttons")
    col1, col2, col3 = st.columns(3)
    with col1:
        train_button = st.button("Training the Models")
    with col2:
        hyperparam_button = st.button("Show the Best Model")
    with col3:
        predict_button = st.button("Prediction with the best model - Testing data")

    # Ações associadas aos botões
    if train_button:
        run_notebook()  # Executar o notebook com papermill

        # Verificar se o arquivo results.csv foi criado
        if os.path.exists('models/results.csv'):
            # Carregar e exibir os resultados
            results = pd.read_csv('models/results.csv')
            st.write("### Model Comparison Results")
            st.dataframe(results)
        else:
            st.warning("No results found. Please check if the training was successful.")

    if hyperparam_button:
        st.info("Showing hyperparameters... (To be implemented)")

    if predict_button:
        st.info("Predicting with the best model... (To be implemented)")
