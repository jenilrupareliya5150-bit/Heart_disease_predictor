import streamlit as st
import pandas as pd
import joblib

model=joblib.load("knn_heart.pkl")
scaler=joblib.load("scaler.pkl")
expected_columns=joblib.load("columns.pkl")

st.set_page_config(
    page_title="Heart Disease Predictor",
     page_icon="❤️",
    layout="centered"
)



st.title("HEART STROKE PREDICTION ❤️")
st.markdown("🩺 Enter Patient Medical Details")
st.divider()

col1, col2 = st.columns(2)
with col1:
 age=st.slider("AGE",18,100,40)
 sex=st.selectbox("👤 SEX",["M","F"])
 chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
 resting_bp = st.number_input("Resting BP", min_value=50, max_value=250, value=120, step=1)
 cholesterol = st.number_input("Cholesterol", min_value=100, max_value=600, value=200, step=1)
 fasting_bs = st.selectbox("🍬 Fasting Blood Sugar > 120 mg/dL", ["NO","YES" ])
 fasting_bs = 1 if fasting_bs == "YES" else 0

with col2:
 resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
 max_hr = st.slider("Max Heart Rate", 60, 220, 150)
 exercise_angina = st.selectbox("🏃Exercise-Induced Angina", ["Yes", "N0"])
 oldpeak = st.slider("📉ST Depression", 0.0, 6.0, 1.0)
 st_slope = st.selectbox("📊 ST Slope", ["Up", "Flat", "Down"])
st.divider()



# When Predict is clicked
if st.button("🔍 Predict Heart Disease"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")



