print('Hasil dari True and True   :', True and True)
print('Hasil dari True and False   :', True and False)
print('Hasil dari False and True   :', False and True)
print('Hasil dari False and False   :', False and False)

print('\n')

print('Hasil dari True or True   :', True or True)
print('Hasil dari True or False   :', True or False)
print('Hasil dari False or True   :', False or True)
print('Hasil dari False or False   :', False or False)

print('\n')

print('Hasil dari True not True   :', not True)
print('Hasil dari True not False  :', not False)

print('\n')

hasil = (5 > 6) and (10 <= 8)
print(hasil)

hasil = ('duniailkom' == 'duniailkom') or (10 <= 8)
print(hasil)

hasil = not (10 < 10)
print(hasil)

hasil = ('duniailkom' == 'duniailkom') and (10 <= 8) or (1 != 1)
print(hasil)

#and
x = 10
print(x > 5 and x < 15)

#or
x = 10
print(x > 5 or x < 2)


#not
x = 10
print(not(x > 5 and x < 15))
