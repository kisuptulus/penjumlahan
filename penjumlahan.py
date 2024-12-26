# Program untuk menjumlahkan dua angka yang dimasukkan oleh pengguna

# Fungsi untuk menjumlahkan dua angka
def penjumlahan(angka1, angka2):
    return angka1 + angka2

# Meminta input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Menghitung hasil penjumlahan
hasil = penjumlahan(angka1, angka2)

# Menampilkan hasil penjumlahan
print(f"Hasil penjumlahan dari {angka1} dan {angka2} adalah {hasil}")