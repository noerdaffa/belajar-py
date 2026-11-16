import math

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi(sisi):
    return sisi ** 2

def volume_kubus(sisi):
    return sisi ** 3

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)

def luas_persegi_panjang(p, l):
    return p * l

def volume_balok(p, l, t):
    return p * l * t

def keliling_lingkaran(r):
    return 2 * math.pi * r

def luas_lingkaran(r):
    return math.pi * r ** 2

def volume_bola(r):
    return (4/3) * math.pi * r ** 3

while True:
    print("\n=== PROGRAM MENGHITUNG BANGUN DATAR DAN RUANG ===")
    print("1. Keliling Persegi")
    print("2. Luas Persegi")
    print("3. Volume Kubus")
    print("4. Keliling Persegi Panjang")
    print("5. Luas Persegi Panjang")
    print("6. Volume Balok")
    print("7. Keliling Lingkaran")
    print("8. Luas Lingkaran")
    print("9. Volume Bola")
    print("0. Keluar")
    
    pilihan = input("Masukkan pilihan (0-9): ")

    if pilihan == '1':
        sisi = float(input("Masukkan panjang sisi: "))
        print("Keliling persegi =", keliling_persegi(sisi))
    elif pilihan == '2':
        sisi = float(input("Masukkan panjang sisi: "))
        print("Luas persegi =", luas_persegi(sisi))
    elif pilihan == '3':
        sisi = float(input("Masukkan panjang sisi: "))
        print("Volume kubus =", volume_kubus(sisi))
    elif pilihan == '4':
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Keliling persegi panjang =", keliling_persegi_panjang(p, l))
    elif pilihan == '5':
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Luas persegi panjang =", luas_persegi_panjang(p, l))
    elif pilihan == '6':
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        t = float(input("Masukkan tinggi: "))
        print("Volume balok =", volume_balok(p, l, t))
    elif pilihan == '7':
        r = float(input("Masukkan jari-jari: "))
        print("Keliling lingkaran =", keliling_lingkaran(r))
    elif pilihan == '8':
        r = float(input("Masukkan jari-jari: "))
        print("Luas lingkaran =", luas_lingkaran(r))
    elif pilihan == '9':
        r = float(input("Masukkan jari-jari: "))
        print("Volume bola =", volume_bola(r))
    elif pilihan == '0':
        print("Terima kasih telah menggunakan program ini!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")