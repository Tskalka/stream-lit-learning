import streamlit as st
import joblib

st.title("Gender Prediction App")

# Load the model
@st.cache_resource
def load_model():
    return joblib.load("naive_bayes_gender_model_US.pkl")

model = load_model()

st.subheader("Enter measurements to predict")

col1, col2 = st.columns(2)

with col1:
    feet = st.number_input("Height (feet)", min_value=1.0, max_value=7.0, value=5.0, step=1.0)

with col2:
    inches = st.number_input("Inches", min_value=0.0, max_value=11.0, value=6.0, step=1.0)


height = feet + (12 /inches)
    
normalized_shoe_size = st.number_input("Shoe Size", min_value=1.0, max_value=20.0, value=10.0, step=0.5)
