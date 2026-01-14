# 🏦 Loan Eligibility Prediction System
*End-to-End Classification Project using Machine Learning & Streamlit*

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk membantu perbankan mempercepat proses verifikasi kelayakan pinjaman secara otomatis. Dengan menggunakan data historis nasabah, model Machine Learning dikembangkan untuk memprediksi probabilitas persetujuan pinjaman berdasarkan profil risiko pemohon.

## 🛠️ Tech Stack
* **Modeling:** Logistic Regression (Scikit-Learn)
* **Processing:** Pandas, NumPy, Label Encoding
* **Interface:** Streamlit Dashboard

## 📊 Hasil Analisis
* **Model Accuracy:** ~80% (Dapat bervariasi tergantung data training).
* **Credit History**: Faktor penentu paling dominan. Nasabah dengan riwayat kredit yang baik memiliki peluang persetujuan hingga 8x lebih besar.
* **Education Level**: Kelompok Graduate menunjukkan stabilitas finansial yang lebih tinggi dalam dataset ini dibandingkan kelompok Non-Graduate.
* **Property Area**: Nasabah di area Semi-Urban cenderung memiliki tingkat persetujuan (approval rate) yang lebih tinggi dibandingkan area Rural atau Urban.
* **Model Accuracy**: Model mencapai akurasi sekitar 80%, yang menunjukkan performa yang cukup handal untuk tahap klasifikasi awal.

## 🚀 Cara Menjalankan
1. `pip install streamlit scikit-learn pandas`
2. `streamlit run app_loan.py`
