import random

n = int(input("Masukkan nilai n: "))
for _ in range(n):
    nilai_acak = random.random()
    if nilai_acak < 0.5:
        print(nilai_acak)
