import streamlit as st
from PIL import Image

# Título e descrição da página inicial
# Imagem
logoHome = Image.open("img/image1.png")
col1, col2, col3 = st.columns([3, 1, 3])
with col1:
    st.write("")
with col2:
    st.image(logoHome, use_column_width=True)
with col3:
    st.write("")

# Titulo de apresentacao
st.title("Auto Machine Learning Analysis")
st.subheader("Projeto criado para o curso de Extensão do IF Goiano - Campus Catalão")

# Marcação usando css e markdown
st.markdown("""
<style>
.big-font1 {
    font-size: 23px !important;
}
</style>
""", unsafe_allow_html = True)

st.markdown("""
<style>
.big-font2 {
    font-size: 21px !important;
}
</style>
""", unsafe_allow_html = True)

# Texto apresentando o cenário da ferramenta

st.markdown("<p class = 'big-font1'> Bem-vindo à nossa aplicação desenvolvida com Streamlit! Este projeto foi criado com o objetivo de facilitar"
                        "a análise do comportamento de modelos de machine learning, permitindo que você explore como a variação de parâmetros importantes"
                        "afeta o desempenho dos modelos. Na aba Home, você encontrará informações sobre a aplicação e seu propósito."
                        "Na aba Upload, você pode enviar arquivos CSV, que serão armazenados para análise posterior. Na aba ML, você terá a oportunidade" 
                        "de usar a biblioteca PyCaret para definir parâmetros essenciais, como o número de folds e a dimensão dos conjuntos de treinamento e teste."
                        "Em seguida, você poderá treinar e avaliar diferentes modelos de machine learning de maneira prática e intuitiva. </p>", unsafe_allow_html=True)

st.markdown("<p class = 'big-font2'> Navegue pelas abas para explorar todas as funcionalidades e aproveitar ao máximo esta ferramenta. </p>", unsafe_allow_html=True)
st.markdown("Desenvolvido para curso de Extensão do IF Goiano - Campus Catalão [Bacharelado em Sistemas de Informação](https://ifgoiano.edu.br/home/index.php/cursos-superiores-catalao/12730-sistemas-de-informacao.html)")