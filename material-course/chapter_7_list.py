jenis_sampah = ['organik','kertas','plastik']

# print("Berikut jenis sampah yang kami olah: ", jenis_sampah)

# print(jenis_sampah[2]) #index start dari 0

# jenis_sampah[2] = 'non-organik' #buat ganti isi sesuai index nya
# print("Berikut jenis sampah yang kami olah: ", jenis_sampah)

# jenis_sampah.append('non-organik') #append buat nambahin ke urutan paling akhir
# print(jenis_sampah)

# jenis_sampah = []
# jumlah_sampah = int(input("Masukkan jumlah sampah: "))
# for i in range(jumlah_sampah):
#     sampah = input(f"Masukkan jenis sampah ke-{i+1}: ")
#     jenis_sampah.append(sampah)
# print("Berikut jenis sampah yang akan diolah:", jenis_sampah)

# i = 0
# while i < len(jenis_sampah):
#     print(f"Berikut jenis sampah yang akan diolah: {jenis_sampah[i]}")
#     i = i + 1

berat_sampah = []
i = 0
while i<2:
    sampah = int(input(f"Masukkan berat sampah ke-{i+1}: "))
    berat_sampah.append(sampah)
    i+=1
total_berat = 0
for sampah in berat_sampah:
    total_berat += sampah
print(f"Kamu telah mendaur ulang sebanyak {total_berat} kg sampah!")