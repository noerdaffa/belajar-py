print("Masukan setiap panjang segitiga")

a = float(input("Masukkan panjang sisi A: "))
b = float(input("Masukkan panjang sisi B: "))
c = float(input("Masukkan panjang sisi C: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Ketiga sisi sama besar, maka segitiga tersebut adalah segitiga sama sisi")
    elif a == b or b == c or a == c:
        print("Ada dua sisi yang sama, maka segitiga tersebut adalah segitiga sama kaki")
    else:
        print("Ketiga sisi berbeda, maka segitiga tersebut adalah segitiga sembarang")
else:
    print("Panjang sisi tidak dapat membentuk segitiga.")
 
