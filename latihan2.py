angka = int(input("Masukkan angka (0 untuk berhenti): "))
max_angka = angka

while angka != 0:
    angka = int(input("Masukkan angka (0 untuk berhenti): "))
    if angka > max_angka:
        max_angka = angka

print("Bilangan terbesar adalah:", max_angka)
