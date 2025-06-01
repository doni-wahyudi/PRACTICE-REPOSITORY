donatur = {
    "Doni": 100000,
    "Ihsan": 50000,
    "Ayi": 120000
}

cek_nama = input("Silahkan masukkan nama anda: ")

if cek_nama in donatur:
    print(f"\nSelamat datang Bapak/Ibu {cek_nama}!")
    
    while True:
        try:
            print("\nSilahkan pilih menu kegiatan:")
            print("1. Cek saldo donasi")
            print("2. Tambah donasi")
            print("3. Keluar")
            pilih_menu = input("Pilih (1/2/3): ")

            if pilih_menu == "1":
                print(f"\nSaldo donasi anda sebesar: Rp. {donatur[cek_nama]}")
            
            elif pilih_menu == "2":
                try:
                    tambah_donasi = int(input("Masukkan jumlah donasi yang ingin anda tambahkan: "))
                    donatur[cek_nama] += tambah_donasi
                    print(f"Terima kasih atas donasinya!")
                    print(f"Saldo donasi anda kini sebesar: Rp. {donatur[cek_nama]}")

                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")
            
            elif pilih_menu == "3":
                print(f"Terima kasih telah berpartisipasi, {cek_nama}!")
                break
            
            else:
                print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        except Exception as e:
            print(e)
else:
    print(f"\nMaaf, nama {cek_nama} tidak ditemukan dalam data donatur.")

    opsi_donasi = input(f"Apakah anda ingin ikut berpartisipasi? \nPilih (Y/N): ")

    if opsi_donasi.lower() == "y":
        jumlah_donasi = int(input(f"Masukkan jumlah donasi: Rp. "))
        donatur[cek_nama] = jumlah_donasi
        print(f"\nDonasi telah kami terima sebesar Rp. {donatur[cek_nama]}")
        print(f"Terimakasih telah berpartisipasi, {cek_nama}")

    else:
        print("Baik, Terimakasih atas kunjungannya.")