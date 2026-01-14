import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#1.Mengubah Teks Menjadi Angka (Label Encoding)
#MUAT DATA (Langkah ini wajib agar 'df' terdefinisi)
df = pd.read_csv(r'C:\Users\aeni\portofolio\Loan Eligibility Prediction\data_nasabah.csv')

# Inisialisasi LabelEncoder
le = LabelEncoder()

# Daftar kolom kategori yang perlu diubah
category_cols = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status']

#2 Melakukan encoding untuk setiap kolom kategori
for col in category_cols:
    df[col] = le.fit_transform(df[col])

# Khusus untuk kolom 'Dependents', biasanya berisi string seperti '3+'
# Kita ubah menjadi angka 3 agar konsisten
df['Dependents'] = df['Dependents'].replace('3+', 3).astype(int)

#3 SPLITTING 
#memisahkan data yang menjadi "soal" (X) dan mana yang menjadi "jawaban/target" (y)
# Menghapus Customer_ID karena tidak berpengaruh pada prediksi
# Menghapus Loan_Status dari X karena itu adalah target yang ingin ditebak
X = df.drop(['Customer_ID', 'Loan_Status'], axis=1)
y = df['Loan_Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Proses Berhasil! Data 'df' sudah siap dan sudah dibagi.")
print(df.head())
#print("--- Hasil Encoding ---")
#print(df.head())

#menyimpan model di file training untuk AI
import pickle

#Latih Model (PASTIKAN NAMA VARIABEL ADALAH 'model')
model_loan = LogisticRegression(max_iter=1000)
model_loan.fit(X, y) # Di sini variabel 'model' dibuat

# 4. Simpan Model (Sekarang 'model' sudah terdefinisi)
with open('loan_model.pkl', 'wb') as file:
    pickle.dump(model_loan, file)

print("Berhasil! Model sekarang sudah tersimpan dalam file loan_model.pkl")