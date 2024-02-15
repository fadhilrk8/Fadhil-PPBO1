#membuat pengklasifikasian suhu
def klasifikasi(Suhu):
    if Suhu < 0:
        print("Membeku");
    elif Suhu < 10:
        print("Sangat dingin");
    elif Suhu < 20:
        print("Sejuk");
    elif Suhu < 30:
        print("Hangat");
    elif Suhu < 40:
        print("Panas");
    else:
        print("Sangat panas");

#membuat perulangan agar semua klasifikasi dapat terlihat outputnya
while True:
    #meminta input suhu dari user
    Suhu = int(input("Masukkan nilai suhu dalam celcius: "))
    #memanggil fungsi klasifikasi suhu
    klasifikasi(Suhu)