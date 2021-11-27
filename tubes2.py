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

# frekuensi richter
print("tabel frekuensi richter adalah, ")
print(df["richter"].value_counts())

# persentase richter
print("Persentase richter adalah, ")
print(df["richter"].value_counts(normalize=True))


# frekuensi tahun
print("Tabel frekuensi tahun adalah, ")
print(df["year"].value_counts())


# persentase Tahun
print("persentase tahun adalah, ")
print(df["year"].value_counts(normalize=True))


# frekuensi bulan
print("Tabel frekuensi bulan adalah, ")
print(df["month"].value_counts())


# persentase bulan
print("Persentase Bulan adalah, ")
print(df["month"].value_counts(normalize=True))


# frekuensi hari
print("Tabel frekuensi hari adalah, ")
print(df["day"].value_counts())

# persentase hari
print("Persentase hari adalah, ")
print(df["day"].value_counts(normalize=True))

# frekuensi negara
print("Tabel frekuensi negara yang terkena gempa bumi adalah, ")
print(df["region"].value_counts())


# persentase negara
print("Persentase negara yang terkena gempa bumi adalah, ")
print(df["region"].value_counts(normalize=True))


# frekuensi wilayah
print("Tabel frekuensi wilayah yang terkena gempa bumi adalah, ")
print(df["area"].value_counts())

# persentase wilayah
print("Persentase wilayah yang terkena gempa bumi adalah, ")
print(df["area"].value_counts(normalize=True))

# frekuensi kematian
print("tabel frekuensi kematian adalah, ")
print(df["deaths"].value_counts())


# persentase kematian
print("Persentase kematian adalah, ")
print(df["deaths"].value_counts(normalize=True))


print("Nilai korelasi antara nilai skala richter dan jumlah kematian adalah " + str(df["richter"].corr(df["deaths"])))
# nilai korelasi antara skala richter dan jumlah kematian mendekati 0 yang artinya tidak berhubungan atau
# berhubungan tetapi kecil sekali
