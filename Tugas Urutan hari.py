print("Pilih urutan hari!")
angka = int(input("Masukkan angka (1-7) untuk menentukan hari: "))
if angka >= 1 and angka <= 7:
    if angka == 1:
        hari = "Senin"
    elif angka == 2:
        hari = "Selasa"
    elif angka == 3:
        hari = "Rabu"
    elif angka == 4:
        hari = "Kamis"
    elif angka == 5:
        hari = "Jumat"
    elif angka == 6:
        hari = "Sabtu"
    else:
        hari = "Minggu"
        
    print("Hari:", hari)

    if angka >= 1 and angka <= 5:
        print("Jenis Hari: Hari Kerja")
    else:
        print("Jenis Hari: Akhir Pekan")

else:
    print("Angka tidak valid! Masukkan angka 1-7.")
