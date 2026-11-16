nilai = int(input('Masukkan nilai: '))
usia = int(input('Masukkan usia: '))

if nilai >= 75:
    if (usia < 15):
        print('Selamat dik, kamu lulus!')
    else:
        print('Selamat kak, kamu lulus!')
else:
    if (usia < 15):
        print('Mohon maaf dik, coba lagi ya!')
    else:
        print('Mohon maaf kak, coba lagi ya!')