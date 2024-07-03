import streamlit as st
import pandas as pd
from pycaret.classification import setup, compare_models, pull, predict_model, save_model
import os 

# Título e descrição da página inicial
st.title("Análise dos dados usando Modelos de Machine Learning")
st.subheader("Treinamento de modelos para a classificação de pacientes com a DP usando registros de voz")

# Buscando o arquivo enviado para análise
@st.cache_data
def carregar_dataframe():
    if os.path.exists("dados.csv"):
        df_data = pd.read_csv("dados.csv", index_col=None)
        st.session_state["data"] = df_data
        return df_data


df = carregar_dataframe()

# Variáveis a serem apresentadas à função PyCaret
with st.form("Basic Settings"):
    variavelTarget = st.selectbox("Selecione a variável alvo: ", df.columns, index=2)
    foldsNumber = st.number_input('Número de Folds', min_value=2, max_value=10, value=5)
    testing = st.slider('Escolha o percentual para os dados de teste:', min_value=0.05, max_value=1.00, step=0.05,
                        value=0.20)
    training = (1 - testing)
    # Botão para dar início à configuração e treinamento
    trainingModels = st.form_submit_button("Treinar os Modelos")

    if trainingModels:
        # PyCaret setup
        setup(data=df, target=variavelTarget, session_id=1245,
              normalize=True, remove_multicollinearity=True,
              multicollinearity_threshold=0.90, fold_strategy= 'kfold',
              fold=foldsNumber, train_size=training)
        setup_df = pull()
        st.info("Parâmetros utilizados para treinar os modelos")
        st.dataframe(setup_df, use_container_width=True)

        # Modelos Treinamento
        best_model = compare_models()
        compare_df = pull()
        st.info("Dataframe com o resultado para os modelos treinados")
        st.dataframe(compare_df, use_container_width=True)

        st.info("Os hiperparâmetros para o melhor modelo são dados a seguir:")
        st.json(best_model.get_params())

        # Salvando o melhor modelo
        save_model(best_model, 'best_model')

        # Realizando predição com o melhor modelo
        st.info("Realizando predições com o melhor modelo")
        test_predictions = predict_model(best_model)
        st.dataframe(test_predictions, use_container_width=True)

        metrics = pull()
        st.info("Métricas de avaliação do modelo nos dados de teste")
        st.dataframe(metrics)  # Exibindo todas as métricas disponíveis para inspeção