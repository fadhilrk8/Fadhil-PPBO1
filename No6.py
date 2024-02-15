num1 = int(input("Masukkan angka deret yang diinginkan: "))
if 0 <= num1 <= 10:
    num0 = 0
    total = 0

    while total < 10:
        print(num1, end=" ");
        n = num1 + num0
        num0 = num1
        num1 = n
        total += 1
else:
    print("Angka yang anda masukkan tidak valid")