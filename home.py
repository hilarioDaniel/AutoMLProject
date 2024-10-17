import streamlit as st
from PIL import Image

# Title and description of the initial page
# Image
logoHome = Image.open("./img/image1.png")
col1, col2, col3 = st.columns([4, 1, 4])
with col1:
    st.write("")
with col2:
    st.image(logoHome, use_column_width=True)
with col3:
    st.write("")

# Title
st.title("EDA and Auto Machine Learning")
st.subheader("Project created for use in the NIATS - UFU laboratory")

# Custom CSS for larger fonts
st.markdown("""
<style>
.big-font1 {
    font-size: 22px !important;
}
.big-font2 {
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

# Introduction text
st.markdown("<p class='big-font1'>Welcome to our Streamlit application! This project was developed to enable comprehensive exploratory data analysis and automated machine learning specifically for classification problems. You can delve into data statistics and understand how different parameters influence model performance.</p>", unsafe_allow_html=True)

st.markdown("<p class='big-font1'>On the Home tab, you'll find information about the application and its purpose. The Upload tab allows you to submit CSV or XLSX files for subsequent analysis. In the EDA tab, you can conduct exploratory data analysis with statistical summaries and visualizations to gain insights into your dataset. The Machine Learning tab enables you to use the PyCaret library to set essential parameters, such as the number of folds and the sizes of the training and test sets, among other options. You can then train and evaluate various machine learning models for classification in a practical and intuitive manner.</p>", unsafe_allow_html=True)

st.markdown("<p class='big-font2'>Navigate through the tabs to explore all features and maximize the potential of this tool.</p>", unsafe_allow_html=True)

st.markdown("This application is used in the NIATS laboratory, part of the [Graduate Program in Biomedical Engineering - UFU](http://www.ppgeb.feelt.ufu.br/pt-br/unidade/programa-de-pos-graduacao-em-engenharia-biomedica)")
