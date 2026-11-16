print("Masukan berat badan dan tinggi badan untuk mengetahui IMT")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (m): "))
imt = berat / (tinggi ** 2)

print(f"IMT Anda: {imt:.2f}")

if imt < 18.5:
    print("Kategori: Kurus")
elif imt >= 18.5 and imt < 24.9:
    print("Kategori: Normal")
elif imt >= 24.9 and imt < 29.9:
    print("Kategori: Gemuk")
else:
    print("Kategori: Obesitas")
