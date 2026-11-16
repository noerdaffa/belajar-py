listKota = [
    'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo', 'Jogjakarta', 'Semarang', 'Makassar'
    ]

KotaYangDicari = input('Masukkan nama kota yang dicari : ')

i = 0
while i < len(listKota):
    if listKota[i].lower() == KotaYangDicari.lower():
     print('Ketemu di index', i)
     break

    print('Bukan', listKota[i])
    i += 1 
else:
    print('Maaf, kota yang anda cari tidak ditemukan.')

#fungsi lower semua huruf besar kecil di anggep sama