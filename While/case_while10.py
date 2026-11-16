data = [2, 5, -7, 4, 10, 12, 15, -10, -12, -4]
sum = 0
i = 0

while i < len(data):
    sum += data[i]
    i += 1

rata_rata = sum / len(data)
print ('Rata Rata data adalah :', rata_rata)