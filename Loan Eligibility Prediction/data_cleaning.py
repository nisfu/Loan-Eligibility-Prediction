import pandas as pd

# Load data
#df = pd.read_csv('data_nasabah.csv')
df = pd.read_csv(r'C:\Users\aeni\portofolio\Loan Eligibility Prediction\data_nasabah.csv')

# Cek informasi dasar
print(df.info())

# Cek jumlah data kosong per kolom
print(df.isnull().sum())