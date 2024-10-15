import json
import pandas as pd
from pycaret.classification import setup, compare_models, save_model, pull

# Carregar as configurações do arquivo config.json
try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    print("Arquivo config.json não encontrado.")
    raise

# Carregar o dataset
try:
    df = pd.read_csv(f'./datasets/{config["file"]}')
except pd.errors.EmptyDataError:
    print("Erro: Dataset está vazio ou mal formatado.")
    raise

# Verificar se o dataframe tem colunas e dados
if df.empty or len(df.columns) == 0:
    raise ValueError("Erro: O dataset está vazio ou sem colunas.")

# Verificar se a variável alvo está no dataset
if config["target"] not in df.columns:
    raise ValueError(f"A coluna alvo '{config['target']}' não está presente no dataset.")

# Verificar se a coluna de target contém valores válidos
if df[config["target"]].isnull().sum() > 0:
    raise ValueError(f"A coluna alvo '{config['target']}' contém valores nulos. Por favor, limpe ou preencha esses valores.")

# Verificações e ajustes de configuração
normalize = config.get("normalize", False)
normalize_method = config.get("normalization_method", None) if normalize else None

remove_multicollinearity = config.get("remove_multicollinearity", False)
multicollinearity_threshold = config.get("multicollinearity_threshold", False) if remove_multicollinearity else None

fold_strategy = config.get("fold_strategy", False)  # Se não for informado, usa None
fold_number = config.get("fold_number", 10) if fold_strategy else None  # Se fold_strategy não estiver marcado, ignoramos

# Setup do PyCaret
clf = setup(
    data=df,
    target=config["target"],
    session_id=config["session_id"],
    normalize=normalize,
    normalize_method=normalize_method,
    train_size=1 - config["test_size"],
    fold_strategy=fold_strategy,
    fold=fold_number,
    remove_multicollinearity=remove_multicollinearity,
    multicollinearity_threshold=multicollinearity_threshold
)

# Treinar os modelos e salvar o melhor
best_model = compare_models()

# Verificar se best_model foi retornado corretamente
if best_model is None or (isinstance(best_model, list) and len(best_model) == 0):
    raise ValueError("Nenhum modelo foi comparado ou retornado. Verifique as configurações.")

# Se best_model for uma lista, pegar o primeiro modelo
if isinstance(best_model, list):
    best_model = best_model[0]

# Salvar o melhor modelo
save_model(best_model, './models/best_model')

# Puxar os resultados
results = pull()

# Salvar os resultados em CSV
results.to_csv('./models/results.csv', index=False)

# Salvar os parâmetros do melhor modelo
with open('./models/best_model_params.json', 'w') as f:
    json.dump(best_model.get_params(), f)
