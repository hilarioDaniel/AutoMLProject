# Overview

**EDA and AutoML `version 1.0`** is a Python-based web application designed to streamline exploratory data analysis (EDA) and machine learning processes, with a focus on identifying patterns in audio and video datasets. The system is particularly suited for biomedical research, such as studies on Parkinson's disease. Built using Python and the Streamlit framework, it provides an intuitive interface for data analysis, visualization, and automated classification tasks. Its flexibility and user-friendly design make it an invaluable tool for researchers and healthcare professionals, enabling meaningful insights and driving advancements in biomedical research.

## Features
1. **Exploratory Data Analysis (EDA)**  
   The tool helps researchers summarize and understand the main characteristics of their datasets. Users can calculate descriptive statistics such as mean, median, standard deviation, and range with ease.  
   
2. **Preprocessing and AutoML**  
   - Offers data normalization options, including Min-Max scaling and Z-score normalization.  
   - Configurable training and testing dataset proportions.  
   - Fold strategy selection for cross-validation, with options to specify the number of folds.  
   - Fixes data imbalances and supports techniques like PCA (Principal Component Analysis) and feature selection.  

---

# Getting the Latest Code

To clone the repository using Git, run the following command:

```bash
git clone https://github.com/hilarioDaniel/AutoMLProject.git

```
---


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

---

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




