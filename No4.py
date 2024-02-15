#membuat fungsi untuk mengecek angka
def cekAngkaPrimer(angka):
    if angka == 1:
        print("Bukan bilangan primer");
    elif angka > 1:
        for i in range(2, angka):
            if (angka % i) == 0:
                print("Bukan bilangan primer");
        else:
            print("Bilangan primer")

#meminta user memberi input berupa integer
angka = int(input("Masukkan angka yang ingin di cek: "))
#memanggil fungsi pengecekan
cekAngkaPrimer(angka)