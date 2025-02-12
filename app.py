import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model

@st.cache_data() # Execute une fois et pas plus si le code ne change pas
def load():
    model_path = "drop_best_model.keras"
    model = load_model(model_path, compile=False)
    return model
# End def load

def predict():
    pass
# End def predict

# Chargement du modèle
model = load()

st.title("Détection de fraudes")

upload = st.file_uploader(
    "Chargez le dataset sous format csv:",
    type=['csv']
)

c1, c2 = st.columns(2)

if upload:
    prob_fraud = predict(upload)

    c2.write(f"Je suis certain à {prob_fraud*100:.2f}% que la transaction est frauduleuse")
    