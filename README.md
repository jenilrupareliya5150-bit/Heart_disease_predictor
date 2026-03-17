❤️ Heart Disease Prediction System

A Machine Learning-based web application that predicts the risk of heart disease using patient medical data. This project demonstrates end-to-end ML workflow including data analysis, preprocessing, model training, and deployment using Streamlit.

🚀 Project Overview

This project uses various classification algorithms to predict whether a person is at risk of heart disease based on clinical features like age, blood pressure, cholesterol, etc.

It includes:

📊 Exploratory Data Analysis (EDA)

⚙️ Data Preprocessing & Feature Engineering

🤖 Model Training & Evaluation

🌐 Web App using Streamlit
## 📁 Project Structure

```bash
HEART_DISEASE_PROJECT/
│
├── heart/
│   ├── heart.csv
│   ├── heartEDA.ipynb
│   ├── knn_heart.pkl
│   ├── scaler.pkl
│   ├── columns.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

📊 Dataset Information

The dataset contains 918 records with the following features:
```bash
Feature	Description
Age	Age of patient
Sex	Male / Female
ChestPainType	Type of chest pain
RestingBP	Resting blood pressure
Cholesterol	Serum cholesterol
FastingBS	Fasting blood sugar
RestingECG	ECG results
MaxHR	Maximum heart rate
ExerciseAngina	Exercise-induced angina
Oldpeak	ST depression
ST_Slope	Slope of peak exercise ST
HeartDisease	Target variable
```

⚙️ Technologies Used

Python 🐍

NumPy

Pandas

Matplotlib & Seaborn

Scikit-learn

Streamlit

Joblib

🤖 Machine Learning Models

The following models were trained and compared:

Logistic Regression

K-Nearest Neighbors (KNN) ✅ (Best Performing)

Decision Tree

Support Vector Machine (SVM)

📈 Model Performance
Model	Accuracy	F1 Score
Logistic Regression	~0.80	~0.80
Naive Bayes	~0.64	~0.64
KNN	~0.88	~0.88
SVM	~0.85	~0.84

👉 KNN was selected as final model

🧠 Key Features

Cleaned dataset (no missing values)

One-hot encoding for categorical variables

Feature scaling using StandardScaler

Model saving using Joblib

User-friendly UI with Streamlit

🌐 Web Application

The Streamlit app allows users to:

Input patient details

Predict heart disease risk instantly

Get clear result:

❌ High Risk

✅ Low Risk

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/jenilrupareliya5150-bit/Heart_disease_predictor
cd heart_disease_prediction
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the App
streamlit run app.py
📦 Requirements

Create a requirements.txt file:

numpy
pandas
matplotlib
seaborn
scikit-learn
streamlit
joblib
📌 Future Improvements

Add more advanced models (XGBoost, Random Forest)

Improve UI design

Deploy on cloud (Streamlit Cloud / Render)

Add real-time API integration

🙌 Acknowledgements

Dataset from UCI / Kaggle

Scikit-learn documentation

Streamlit documentation

👨‍💻 Author

Jenil Rupareliya <br>

Engineering Student (CSE)<br>
Aspiring AI Engineer 🚀

⭐ If you like this project

Give it a ⭐ on GitHub and share it!

🔥 Pro Tip (IMPORTANT)

Before pushing:
