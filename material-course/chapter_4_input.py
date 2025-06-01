# jumlah_pohon = input("Masukkan jumlah pohon: ")
jumlah_pohon = int(input("Masukkan jumlah pohon: "))
pohon_tambah = int(input("Masukkan jumlah pohon tambahan: "))
# berat_sampah = float(input("Masukkan berat sampah: "))
# Perhatikan tipe data pada inputan, jika tidak di define maka default nya ada lah string

total_pohon = jumlah_pohon + pohon_tambah

print("----------------------------")
print(f"Jumlah pohon yang ditanam sebanyak {jumlah_pohon} unit dan yang akan ditanam sebanyak {pohon_tambah} unit")
print(f"Total pohon semua nya sebanyak {total_pohon} unit")
# print(f"Berat sampah yang akan di daur ulang sebanyak {berat_sampah} kg")
print("----------------------------")

# print((jumlah_pohon) + 5)
# print(int(jumlah_pohon) + 5)
# print(type(berat_sampah))
