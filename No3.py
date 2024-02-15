def hitungNilaiAkhir(niu, nilai_tugas, nilai_laporan, nilai_ujian):

    #menghitung rata-rata nilai tugas dan laporan
    rerata_tugas_laporan = (nilai_tugas + nilai_laporan) / 2

    #menyelesaikan program apabila nilai kurang dari 40
    if rerata_tugas_laporan < 40:
        print(f"NIU: {niu}")
        print("Nilai akhir : K")
        return
    
    #menghitung nilai akhir
    nilai_akhir =  (nilai_tugas * 0.25) + (nilai_laporan * 0.25) + (nilai_ujian * 0.5)

    #menentukan nilai akhir huruf berdasarkan nilai akhir angka
    if nilai_akhir >= 80:
        nilai_huruf = "A";
    elif nilai_akhir >= 70:
        nilai_huruf = "B";
    elif nilai_akhir >= 60:
        nilai_huruf = "C";
    elif nilai_akhir >= 50:
        nilai_huruf = "D";
    else:
        nilai_huruf = "E"

    #menampilkan output berupa nilai huruf
    print(f"NIU : {niu}")
    print(f"Nilai akhir : {nilai_akhir:.2f}")
    print(f"Nilai akhir huruf : {nilai_huruf}")

print("Menghitung Nilai Akhir")
print("=============================")

#meminta user memasukkan input NIU
niu = int(input("Masukkan NIU anda: "))
#meminta user memasukkan input nilai tugas
nilai_tugas = float(input("Masukkan nilai tugas anda: "))
#meminta user memasukkan nilai laporan
nilai_laporan = float(input("Masukkan nilai laporan anda: "))
#meminta user memasukkan nilai ujian
nilai_ujian = int(input("Masukkan nilai ujian anda: "))

print("\nNilai Akhir Mahasiswa")
print("=============================")

#memanggil fungsi penghitungan nilai dan menampilkan nilai akhir
hitungNilaiAkhir(niu, nilai_tugas, nilai_laporan, nilai_ujian)