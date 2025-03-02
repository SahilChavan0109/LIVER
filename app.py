import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ... (other imports and functions)

# Streamlit UI components
st.title("Heart Disease Prediction")

# --- Input fields for your specific features ---
age = st.number_input("Age", min_value=0, max_value=100, value=3, step=1)
gender = st.number_input("Gender", min_value=0, max_value=200, value=148, step=1)  
total_bilirubin = st.number_input("Total Bilirubin", min_value=0, max_value=100, value=72, step=1)
direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0, max_value=100, value=35, step=1)
alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0, max_value=500, value=0, step=1) 
alanine_aminotransferase = st.number_input("Alanine Aminotransferase", min_value=0, max_value=500, value=336, step=1)
aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0.0, max_value=10.0, value=0.627, step=0.001)
total_proteins = st.number_input("Total Proteins", min_value=0, max_value=10, value=50, step=1)
albumin = st.number_input("Albumin", min_value=0, max_value=10, value=1, step=1)
albumin_and_globulin_ratio = st.number_input("Albumin and Globulin Ratio", min_value=0.0, max_value=10.0, value=3.1, step=0.1) 

# --- Create the input dictionary ---
input_data = {
    'Age': age,
    'Gender': gender,
    'Total_Bilirubin': total_bilirubin,
    'Direct_Bilirubin': direct_bilirubin,
    'Alkaline_Phosphotase': alkaline_phosphotase,
    'Alamine_Aminotransferase': alanine_aminotransferase, 
    'Aspartate_Aminotransferase': aspartate_aminotransferase,
    'Total_Protiens': total_proteins,
    'Albumin': albumin,
    'Albumin_and_Globulin_Ratio': albumin_and_globulin_ratio,
}

# When the user clicks the "Predict" button
if st.button("Predict"):
    with st.spinner('Making prediction...'):
        pred, prob = predict_diabetes(input_data)

        if pred == 1:
            st.error(f"Prediction: Diabetes with probability {prob:.2f}")
        else:
            st.success(f"Prediction: No Diabetes with probability {prob:.2f}")

