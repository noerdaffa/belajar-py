import math
def luas_lingkaran(sisi):
    return (3,14) * sisi ** 2

def volume_bola(r):
    return (4/3) * math.pi * r ** 3

while True:
    print("\n=== PROGRAM MENGHITUNG BANGUN DATAR DAN RUANG ===")
    print("1. Lingkaran")
    print("2. bola")
    print("0. Keluar")
    pilihan = input("Masukkan pilihan (0-2): ")

    if pilihan == '1':
        sisi = float(input("Masukkan panjang sisi: "))
        print("Luas Lingkaran =", luas_lingkaran(sisi))
    elif pilihan == '2':
        sisi = float(input("Masukkan panjang sisi: "))
        print("Volume Bola =", volume_bola(sisi))
    elif pilihan == '0':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")