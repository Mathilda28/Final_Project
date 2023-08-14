import streamlit as st
import pandas as pd
import numpy  as np
import joblib

st.header('Analisis Deposito Berjangka')
st.write("""
Predicting Customer Deposit
""")

@st.cache_data
def fetch_data():
    df = pd.read_csv("bank.csv")
    return df

df = fetch_data()

deposit = st.selectbox('deposit', df['deposit'].unique())
duration = st.number_input('duration', value=0)
housing = st.selectbox('housing', df['housing'].unique())
month = st.selectbox('month', df['month'].unique())
pdays = st.number_input('pdays', value=0)
day = st.number_input('day', value=0)
loan = st.number_input('loan', value=0)
poutcome = st.selectbox('poutcome', df['poutcome'].unique())
job = st.selectbox('job', df['job'].unique())
age = st.number_input('age', value=0)
campaign = st.number_input('campaign', value=0)

data = {
    'deposit': deposit,
    'duration': duration,
    'housing': housing,
    'month': month,
    'pdays': pdays,
    'day': day,
    'loan': loan,
    'poutcome': poutcome,
    'job': job,
    'age': age,
    'campaign': campaign,
}
input = pd.DataFrame(data, index=[0])

st.subheader('Deposit Berjangka')
st.write(input)

load_model = joblib.load("best_model.pkl")

# Mengonversi kategori menjadi nilai numerik
categorical_columns = ['housing', 'month', 'poutcome', 'job']
for col in categorical_columns:
    input[col] = df[col].astype('category').cat.codes
    
if st.button('Hasilnya'):
    prediction = load_model.predict(input)

    if prediction == 0:
        prediction = 'Deposit'
    else:
        prediction = 'Tidak Deposit'

    st.write('Berdasarkan data pelanggan, prediksi prioritas adalah:')
    st.write(prediction)