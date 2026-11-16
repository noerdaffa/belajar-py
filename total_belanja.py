import math
def hitung_belanjaan():
    """
    Program untuk menghitung total pembayaran konsumen dengan diskon berdasarkan
    total belanja dan status member.
    """
    
    # 1. Input Konsumen
    # Menggunakan .lower() untuk memastikan input 'ya' atau 'tidak' dikenali
    jenis_konsumen_input = input("Apakah anda konsumen member? "
    "(ya/tidak): ").lower()
    
    try:
        total_belanja = float(input("Masukkan Total Belanja (Rp): "))
    except ValueError:
        print("Masukkan Total Belanja harus berupa angka yang valid.")
        return

    # Inisialisasi diskon persentase awal
    persen_diskon = 0.0

    # 2. Logika Diskon Berdasarkan Total Belanja (Poin b & c)
    if total_belanja > 100000:
        # Poin c: Diskon 3%
        persen_diskon = 3.0
    elif total_belanja > 200000:
        # Poin b: Diskon 4%
        persen_diskon = 4.0
    
    # 3. Logika Diskon Tambahan untuk Member (Poin d)
    is_member = jenis_konsumen_input == 'ya'
    diskon_member = 0.0
    
    if is_member:
        # Poin d: Diskon tambahan 2% untuk member
        diskon_member = 2.0
        persen_diskon += diskon_member

    # 4. Perhitungan Akhir
    
    # Hitung nilai diskon total (dalam Rupiah)
    nilai_diskon_total = total_belanja * (persen_diskon / 100)
    
    # Hitung total bayar akhir
    total_bayar = total_belanja - nilai_diskon_total

    # 5. Output Hasil
    print("\n--- Rincian Pembayaran ---")
    print(f"Status Konsumen: {'Member' if is_member else 'Non Member'}")
    print(f"Total Belanja Awal: Rp {total_belanja:,.2f}")
    print("----------")
    print(f"Diskon Belanja: {persen_diskon - diskon_member:.1f}%")
    if is_member:
         print(f"Diskon Member: {diskon_member:.1f}%")
    print(f"Total Diskon (%): {persen_diskon:.1f}%")
    print("--------------------------")
    print(f"TOTAL YANG HARUS DIBAYAR: Rp {total_bayar:,.2f}")

# Panggil fungsi untuk menjalankan program
hitung_belanjaan();