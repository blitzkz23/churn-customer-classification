import streamlit as st
import joblib
from PIL import Image
import requests
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd

def main():
    modeldir = 'model/logistic_regression-01.joblib'
    model = joblib.load(modeldir)
    img_url = "https://images.unsplash.com/photo-1611599281058-94426d0618a7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
    response = requests.get(img_url, stream=True)
    img = Image.open(response.raw)

    st.title("Customer Churn Classification")    
    st.image(img, use_column_width=True)
    st.write("Photo by [Sigmund](https://unsplash.com/@sigmund) on [Unsplash](https://unsplash.com/photos/r9PeXDCJyEw)")
    
    st.markdown('---')
    st.write("Please answer some question below in order for model to classify the customer.")
    # Create a dictionary to map "Yes" to 1 and "No" to 0
    yes_no_map = {"Yes": 1, "No": 0}
    
    seniorCitizen = yes_no_map[st.radio("Is the customer Senior citizen?", ["Yes", "No"])]
    partner = yes_no_map[st.radio("Do the customer have life partner?", ["Yes", "No"])]
    tenure = st.slider("How long has this customer been with us? (days)", 0, 1000)
    streamingTV = yes_no_map[st.radio("Do the customer subscribed to streaming TV service?", ["Yes", "No"])]
    internetService = yes_no_map[st.radio("Do the customer subscribed to internet service?", ["Yes", "No"])]
    paperlessBilling = yes_no_map[st.radio("Do the customer have paperless billing?", ["Yes", "No"])]
    monthlyCharges = st.number_input("How much is the monthly charge (1-120$)?", 0)
    totalCharges = st.number_input("How much is the monthly charge (1-10000$)?", 0)

    def predict():
        scaler = MinMaxScaler()
        scaled_tenure = scaler.fit_transform([[tenure]])[0][0]
        scaled_monthly_charges = scaler.fit_transform([[monthlyCharges]])[0][0]
        scaled_total_charges = scaler.fit_transform([[totalCharges]])[0][0]

        row = np.array([seniorCitizen, partner, scaled_tenure, streamingTV, internetService, paperlessBilling, scaled_monthly_charges, scaled_total_charges])
        columns = ['SeniorCitizen', 'Partner', 'tenure', 'StreamingTV', 'InternetService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges']
        X = pd.DataFrame([row], columns=columns)
        prediction = model.predict(X)[0]

        if prediction == 1:
            st.error("This customer will churn, we need to evaluate the cause and do a campaign in order to prevent it.")
        else:
            st.success("This customer won't churn, we can focus our attention to other one!")

    st.button('Predict', on_click=predict)

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass