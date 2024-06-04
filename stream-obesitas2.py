import pickle
import streamlit as st

#obesitas model
obesitas_model = pickle.load(open('mp2_joblib'))

#judul web

st.title('Data Mining Prediksi Obesitas')
