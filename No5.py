import math

#membuat fungsi untuk mengjitung luas dan keliling lingkaran
def hitungLingkaran(r):
    #menghitung keliling
    keliling = 2 * math.pi * r
    #menghitung luas
    luas = math.pi * (r**2)
    return keliling, luas

#meminta input jari - jari dari pengguna
r = int(input("Masukkan nilai jari jari lingkaran: "))

#menghitungkeliling dan luas dengan memanggil fungsi
keliling, luas = hitungLingkaran(r)

#menampilkan hasil perhitungan
print(f"Keliling lingkaran = {keliling:.2f}")
print(f"Luas lingkaran = {luas:.2f}")