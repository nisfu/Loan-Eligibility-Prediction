import streamlit as st
import pickle
import pandas as pd
import os

# Mencari lokasi folder tempat file ini berada
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'loan_model.pkl')

# Mendapatkan alamat folder tempat file app_loan.py ini disimpan
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'loan_model.pkl')

# Load model
# Membuka file menggunakan alamat lengkap (absolute path)
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
else:
    st.error(f"File model tidak ditemukan di: {model_path}")
    st.stop()

st.set_page_config(page_title="Loan Prediction", layout="centered")
st.title("🏦 Sistem Prediksi Kelayakan Pinjaman")
st.write("Masukkan data nasabah untuk mengecek status kelayakan pinjaman.")

# Form Input
with st.form("loan_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.number_input("Dependents (Jumlah Tanggungan)", 0, 5)
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        
    with col2:
        income = st.number_input("Applicant Income", 0)
        co_income = st.number_input("Co-applicant Income", 0)
        loan_amt = st.number_input("Loan Amount", 0)
        term = st.number_input("Loan Term (Days)", 360)
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    submitted = st.form_submit_button("Cek Status Pinjaman")

if submitted:
    # Encoding manual sederhana untuk input
    g = 1 if gender == "Male" else 0
    m = 1 if married == "Yes" else 0
    e = 0 if education == "Graduate" else 1
    s = 1 if self_employed == "Yes" else 0
    p = 2 if property_area == "Urban" else (1 if property_area == "Semiurban" else 0)
    
    # Gabungkan semua input menjadi satu baris data
    data_input = [[g, m, dependents, e, s, income, co_income, loan_amt, term, credit_history, p]]
    
    # Prediksi
    prediction = model.predict(data_input)
    
    if prediction[0] == 1:
        st.success("✅ Pinjaman DISETUJUI (Eligible)")
    else:
        st.error("❌ Pinjaman DITOLAK (Not Eligible)")