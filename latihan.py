num = int(input("Masukan Angka"))

if num > 20:
    if num % 2 == 0:
        print("Salah")
    elif num % 2 != 0:
        print("Benar")
else:
    print("Salah")
