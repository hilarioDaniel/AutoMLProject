# Overview

EDA and AutoML version 1.0 is a Python-based web application designed to streamline exploratory data analysis (EDA) and machine learning processes, with a focus on identifying patterns in audio and video datasets. The system is particularly suited to biomedical research, such as studies on Parkinson's disease. Built using Python and the Streamlit framework, it provides an intuitive interface for data analysis, visualization, and automated classification tasks. Its flexibility and user-friendly design make it an invaluable tool for researchers and healthcare professionals, facilitating meaningful insights and driving advancements in biomedical research.

The program offers:
1. Exploratory Data Analysis (EDA) - It's a key feature of the tool, designed to help researchers summarize and make sense of the main characteristics of their datasets. The tool enables users to calculate important descriptive statistics like mean, median, standard deviation, and range.
   
2.Preprocessing and AutoML - The tool provides the option for data normalization, allowing researchers to scale features to a standard range, typically [0, 1] or [-1, 1], with techniques like Min-Max scaling or Z-score normalization available. The tool also allows users to configure the dimensions of the training and testing datasets, select the fold strategy for cross-validation, number of folds, fix data imbalance, PCA (Principal Component Analysis), and feature selection.

# Getting the last code
To get the last code using git, simply type:
> git clone https://github.com/hilarioDaniel/AutoMLProject.git

# Requirements
O will need of the Python 3.10 or higher and some additional packages:
* Streamlit
* Pandas
* PyCaret
* os
* json
* papermill
* sklearn.metrics
* PIL
* and others.

> We created a requirements.txt to help the users.

# Installing
You can use `pip` to install the app:

> pip install requirements.txt

from the source directory. Maybe you need to be the administrator to install the program.

# Running the EDA and AutoML

Type the command below on the terminal to run the app.

> streamlit run main.py

After this step is just to select the options on the main menu.

# Support
If you encounter any issues or have questions, open an issue on GitHub or contact us at daniel.hilario@ufu.br




