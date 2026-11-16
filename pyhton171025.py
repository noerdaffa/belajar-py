print("1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Pangkat\n6. Akar Pangkat2")
pilihan = int(input("Masukkan pilihan (1-2-3-4-5-6): "))
if(pilihan == 1):
    operand1=int(input("Masukkan nilai operand 1: "))
    operand2=int(input("Masukkan nilai operand 2: "))
    hasil = operand1 + operand2
    print("Hasil dari: ", operand1," + ", operand2, " = ", hasil)
elif(pilihan == 2):
    operand1=int(input("Masukkan nilai operand 1: "))
    operand2=int(input("Masukkan nilai operand 2: "))
    hasil = operand1 - operand2
    print("Hasil dari: ", operand1," - ", operand2, " = ", hasil)
elif(pilihan == 3):
    operand1=int(input("Masukkan nilai operand 1: "))
    operand2=int(input("Masukkan nilai operand 2: "))
    hasil = operand1 * operand2
    print("Hasil dari: ", operand1," * ", operand2, " = ", hasil)
elif(pilihan == 4):
    operand1=int(input("Masukkan nilai operand 1: "))
    operand2=int(input("Masukkan nilai operand 2: "))
    hasil = operand1 / operand2
    print("Hasil dari: ", operand1," / ", operand2, " = ", hasil)
elif(pilihan == 5):
    operand1=int(input("Masukkan nilai operand 1: "))
    operand2=int(input("Masukkan nilai operand 2: "))
    hasil = operand1 ** operand2
    print("Hasil dari: ", operand1," ** ", operand2, " = ", hasil)
elif(pilihan == 6):
    operand1=int(input("Masukkan nilai operand 1: "))
    hasil = operand1 ** 0.5
    print("Hasil dari: ", operand1," ** 0.5", " = ", hasil)
else:
    print("Pilihan tidak tersedia")

