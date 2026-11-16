nilai = float(input("Masukkan nilai akhir Anda (0-100): "))

if nilai >= 0 and nilai <= 100:
    if nilai >= 85:
        grade = "A"
    elif nilai >= 75:
        grade = "B"
    elif nilai >= 65:
        grade = "C"
    elif nilai >= 55:
        grade = "D"
    else:
        grade = "E"
    
    print(f"Grade Anda adalah: {grade}")
else:
    print("Nilai yang dimasukkan tidak valid!")