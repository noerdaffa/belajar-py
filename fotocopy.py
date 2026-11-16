def hitung_harga_fotocopy():
    print("--- Program Perhitungan Harga Fotocopy ---")
    status_langganan_input = input("Apakah anda 'langganan'? (ya/tidak): " \
    "").lower()
    is_langganan = (status_langganan_input == 'ya')
    try:
        jumlah_lembar = int(input("Masukkan jumlah lembar fotocopy: "))
        if jumlah_lembar <= 0:
            print("Jumlah lembar harus lebih dari 0.")
            return
    except ValueError:
        print("Jumlah lembar harus berupa angka bulat yang valid.")
        return
    harga_per_lembar = 0
    if is_langganan:
        harga_per_lembar = 75000
    else:
        if jumlah_lembar < 100:
            harga_per_lembar = 100000
        else:
            harga_per_lembar = 85000
    total_harga = jumlah_lembar * harga_per_lembar
    print("\n--- Rincian Pembayaran Fotocopy ---")
    print(f"Status Pelanggan: {'Langganan' if is_langganan else 'Bukan ' 
    'Langganan'}")
    print(f"Jumlah Lembar: {jumlah_lembar} lembar")
    print(f"Harga per Lembar: Rp {harga_per_lembar:,.2f}")
    print("-----------------------------------")
    print(f"**TOTAL HARGA YANG HARUS DIBAYAR: Rp {total_harga:,.2f}**")
hitung_harga_fotocopy()