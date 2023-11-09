modal_awal = 100_000_000
total_labarugi = 0

for bulan in range(1, 9):
    if bulan <= 2:
        total_labarugi += 0  # Bulan pertama dan kedua tidak mendapatkan laba
    elif bulan == 3:
        total_labarugi += modal_awal * 0.01  # Bulan ketiga mendapatkan laba 1%
    elif bulan == 5:
        total_labarugi += modal_awal * 0.05  # Bulan kelima mendapatkan laba 5%
    elif bulan == 8:
        total_labarugi += modal_awal * 0.03  # Bulan kedelapan mendapatkan laba 3%

print("Total keuntungan selama 8 bulan adalah:", total_labarugi)
