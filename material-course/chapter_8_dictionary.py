# donasi_pohon = {
#     "Pinus" : 15,
#     "Jati" : 23,
#     "Mahoni" : 41
# }

# print("Berikut donasi pohon yang diterima: ", donasi_pohon)

# print(f"Jumlah pohon Jati yang didonasikan: {donasi_pohon['Jati']}") #akses nilai dict

# donasi_pohon["Mahoni"] = 50 # untuk mengubah nilai di dict
# print("Berikut donasi pohon yang diterima: ", donasi_pohon)

# donasi_pohon["Mangga"] = 7 # menambahkan key value dict yg baru
# print("Berikut donasi pohon yang diterima: ", donasi_pohon)

# donasi_pohon = {}
# total_pohon = int(input("Masukkan jumlah pohon: "))
# for i in range(total_pohon):
#     pohon = input(f"Masukkan nama pohon ke {i+1}: ")
#     jumlah_pohon = int(input(f"Masukkan jumlah pohon {pohon}: "))
#     donasi_pohon[pohon] = jumlah_pohon
# print("Berikut donasi pohon yang diterima: ", donasi_pohon)

# for pohon, jumlah in donasi_pohon.items(): #untuk iterasi mengambil key value satu persatu
#     print(f"donasi pohon {pohon} sebanyak {jumlah} telah diterima")

# jenis_pohon = list(donasi_pohon.keys()) # keys buat ambil semua key dalam dict
# i = 0
# while i < len(jenis_pohon) :
#     pohon = jenis_pohon[i]
#     print(f"donasi pohon {pohon} sebanyak {donasi_pohon[pohon]} telah diterima")
#     i += 1



# jumlah_donasi = int(input("Masukkan jumlah pohon: "))
def donasi():
    donasi_pohon = {}
    for i in range(int(input("Masukkan jumlah pohon: "))):
        pohon = input(f"Masukkan nama pohon ke {i+1}: ")
        jumlah_pohon = int(input(f"Masukkan jumlah pohon {pohon}: "))
        donasi_pohon[pohon] = jumlah_pohon
    total_pohon = 0
    for jumlah_pohon in donasi_pohon.values(): #values untuk mengambil semua nilai di dict
        total_pohon += jumlah_pohon
    print(f"Total semua pohon yang terkumpul : {total_pohon} unit")

# donasi()