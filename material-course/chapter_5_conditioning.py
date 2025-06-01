berat_sampah = float(input("Masukkan berat sampah (kg): "))
daur_ulang = float(input("Masukkan jumlah sampah yang didaur ulang: "))
sisa_sampah = berat_sampah - daur_ulang
jasa_daur_ulang = 5000
if sisa_sampah == 0:
    print("\nKeren, kamu sudah daur ulang semua sampah!")
else:
    print(f"\nKamu masih punya sisa {sisa_sampah} kg sampah!")
    opsi_jasa = input("Apakah Kamu ingin kami bantu melalui jasa daur ulang sampah kami?(y/n): ").lower()
    if opsi_jasa == "y":
        print("\nBaik, kami akan menjemput sisa sampah nya ke rumahmu segera")
        print("Total biaya penjemputan sejumlah: Rp",sisa_sampah*jasa_daur_ulang,sep=".")
    else:
        print("\nBaik, mohon untuk mendaur ulang kembali sisa sampah nya ya")
print("Terimakasih!")

