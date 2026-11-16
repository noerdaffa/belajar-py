total = float(input("Total Belanja : "))
konsumen = input("Apakah anda konsumen member ? (ya/tidak) ")

if 100000 < total <= 200000:
    diskon = 3/100
    if konsumen == "ya":
        diskon += 2/100
elif total > 200000:
    diskon = 4/100
    if konsumen == "ya":
        diskon += 2/100
elif total <= 100000:
    diskon = 0
    if konsumen == "ya":
        diskon += 2/100

total_bayar = total-(total*diskon)
print("Total diskon yang di dapatkan adalah ", diskon)
print("Total diskon yang di dapatkan adalah ", total_bayar)
