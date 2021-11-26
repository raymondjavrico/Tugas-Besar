import pandas as pd
import os
df = pd.read_csv("earthquakes.csv")

print("Jumlah baris pada tabel data adalah, ", end="")
print(len(df))  # menampilkan jumlah baris pada tabel data

print("Jumlah kolom pada tabel data adalah, ", end="")
print(len(df.columns))  # menampilkan jumlah kolom pada tabel data

print("Jumlah data: " + str(len(df)))  # menampilkan jumlah data

file_path = "earthquakes.csv"
size = os.path.getsize(file_path)
print('Ukuran file: ' + str(size) + ' bytes')  # menampilkan ukuran file dalam bytes

# TIPE DATA
# 1) tahun = kategorikal data, nominal
# 2) bulan = kategorikal data, nominal
# 3) hari = kategorikal data, nominal
# 4) richter = kuantitatif data
# 5) area = kategorikal data, nominal
# 6) region = kategorikal data, nominal
# 7) deaths = kuantitatif data

# nilai minimum skala richter
col_min1 = df["richter"].min(axis=0)
print("Nilai minimum skala richter adalah, ", end="")
print(col_min1)

# nilai maksimum skala richter
col_max1 = df["richter"].max(axis=0)
print("Nilai maksimum skala richter adalah, ", end="")
print(col_max1)

# nilai minimum kematian
col_min2 = df["deaths"].min(axis=0)
print("jumlah kematian tersedikit adalah, ", end="")
print(int(col_min2))

# nilai maksimum kematian
col_max2 = df["deaths"].max(axis=0)
print("jumlah kematian terbanyak adalah, ", end="")
print(int(col_max2))

# standar deviasi richter
print("Standar deviasi skala richter adalah, ", end="")
print(df["richter"].std())

# standar deviasi kematian
print("Standar deviasi kematian adalah, ", end="")
print(df["deaths"].std())

# rata-rata skala richter
print("rata-rata skala richter adalah, ", end="")
print(df["richter"].mean())

# rata-rata kematian
print("rata-rata kematian adalah, ", end="")
print(df["deaths"].mean())

print("Nilai korelasi antara nilai skala richter dan jumlah kematian adalah " + str(df["richter"].corr(df["deaths"])))
# nilai korelasi antara skala richter dan jumlah kematian mendekati 0 yang artinya tidak berhubungan atau
# berhubungan tetapi kecil sekali
