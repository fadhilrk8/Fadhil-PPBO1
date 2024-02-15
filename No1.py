#membuat fungsi untuk melakukan penghitungan mundur
def hitungMundur(angka):
    while angka >= 0:
        print(angka, end=" ")
        angka -= 1

#meminta input angka berupa integer
angka = int(input("Masukkan angka: "))
#memanggil fungsi penghitungan mundur
hitungMundur(angka)