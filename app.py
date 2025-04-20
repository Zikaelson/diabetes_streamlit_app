import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="Diabetes Prediction App", layout="centered")

# Title and intro
st.title("🔬 Diabetes Prediction App")
st.write("Enter your health details to predict the likelihood of diabetes.")

# Sidebar inputs
st.sidebar.header("User Input")

# Collect sidebar inputs
age = st.sidebar.slider("Age", 20, 90, 40)

# New: Add 'sex' field
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
sex = 1 if sex == "Male" else 0

bmi = st.sidebar.slider("BMI", 15.0, 45.0, 25.0)
bp = st.sidebar.slider("Blood Pressure", 50, 130, 80)
s1 = st.sidebar.slider("S1: Cholesterol", 100, 250, 170)
s2 = st.sidebar.slider("S2: LDL", 50, 200, 100)
s3 = st.sidebar.slider("S3: HDL", 30, 100, 50)
s4 = st.sidebar.slider("S4: TCH", 3.0, 7.0, 4.5)
s5 = st.sidebar.slider("S5: LTG", 4.0, 6.5, 5.0)
s6 = st.sidebar.slider("S6: Glucose", 70, 200, 100)

# Create DataFrame to feed model
input_df = pd.DataFrame({
    "age": [age],
    "sex": [sex],  # MUST match training columns!
    "bmi": [bmi],
    "bp": [bp],
    "s1": [s1],
    "s2": [s2],
    "s3": [s3],
    "s4": [s4],
    "s5": [s5],
    "s6": [s6]
})

# Show input data
st.subheader("Your Input")
st.write(input_df)

# Prediction button
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("🚨 High risk: You are likely to have diabetes.")
    else:
        st.success("✅ Low risk: You are unlikely to have diabetes.")
