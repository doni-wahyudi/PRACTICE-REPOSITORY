#password

# saya ingin memastikan password yang dimasukkan sesuai dengan password yg telah saya buat yaitu "rahasia123"

""" 
password = input("Masukkan kata sandi: ")

if password == "rahasia123":
    print("Akses anda diterima! Selamat Datang!")
else:
    print("Akses ditolak! Kata Sandi salah!")
 """

# saya ingin mendeteksi angka ganjil atau genap
""" 
angka = int(input("Masukkan sebuah angka: "))

if angka % 2 == 0:
    print(f"angka {angka} merupakan angka genap")
else:
    print(f"angka {angka} merupakan angka ganjil")
 """

# saya punya nilai raport nilai adalah x, saya ingin tahun jika nilai saya a, b, c, dst, lulus nggak ya?

# rentang nilai antara 1 - 100, menjadi ABCDE, menentukan saya itu lulus atau tidak?
""" 
nilai = int(input("Tolong masukkan nilai (1-100): "))

# kalau kata dosen misal nilai kamu 80 atau lebih dari 80, kamu bisa dapat A
# operator AND nilai A dan dia lulus

if nilai >= 80:
    grade = "A"
    status = "Lulus"
elif nilai >= 70:
    grade = "B"
    status = "Lulus"
elif nilai >= 60:
    grade = "C"
    status = "Lulus"
elif nilai >= 50:
    grade = "D"
    status = "Tidak Lulus"
else:
    grade = "E"
    status = "Tidak Lulus"

print("------------------------------------")
print(f"Nilai anda: {nilai}\nGrade anda: {grade}\nAnda dinyatakan {status}")
 """


# operator AND
""" 
username = input("Masukkan nama pengguna: ")

password = input("Masukkan kata sandi: ")

if username == "admin" and password == "sistem123":
    print("Akses Anda diberikan! Selamat datang Doni Wahyudi sebagai Administrator!")
elif username == "admin":
    print("Kata Sandinya salah")
elif password == "sistem123":
    print("Username nya salah")
else:
    print("username dan password salah")
 """

# anda diminta oleh rekan, tolong bikin kalkulator 
# untuk mendeteksi hari ini hari apa 
# berdasarkan tanggal dan bulan, 
# serta saat ini apakah tahun kabisat

""" 
tanggal = int(input("Masukkan tanggal (1-31): "))
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

# tahun kabisat YYYY  / 4 (habis), tetapi kalau YYYY bisa dibagi 100 jadi bukan kabisat, atau kalau YYYY habis dibagi 400 merupakan tahun kabisat
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"Tahun {tahun} merupakan tahun kabisat")
else:
    print(f"Tahun {tahun} bukan merupakan tahun kabisat")
 """

""" 
perhitungan hari:
Matahari --> sunnadaeg : Sun-day
bulan --> monandaeg : Mon-day
merkurius --> Tiwedaeg (Dewa Tyr/ Tiw) : Tues-day
venus --> woodnesdaeg (Dewa Odin) : wednes-day
mars --> thorsdaeg (Dewa Thor)
jupyter --> frigedaeg (Dewi Frigg)
saturnus --> saternesdaeg (Dewa Saturnus)
 """

# while True:
#     try:
#         tanggal = int(input("Masukkan tanggal (1-31): "))
#         bulan = int(input("Masukkan bulan (1-12): "))
#         tahun = int(input("Masukkan tahun: "))

#         if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#             print(f"\nTahun {tahun} merupakan tahun kabisat\n")
#         else:
#             print(f"\nTahun {tahun} bukan merupakan tahun kabisat\n")
        
#         if tanggal < 1 or tanggal > 31 or bulan < 1 or bulan > 12:
#             print("Tanggal dan bulan tidak valid")
#         else:
#             q = tanggal

#             if bulan == 1 or bulan == 2:
#                 m = bulan + 12
#                 tahun_adj = tahun - 1
#             else:
#                 m = bulan
#                 tahun_adj = tahun

#             k = tahun_adj % 100
#             j = tahun_adj // 100

#             h = (q + ((13*(m+1))//5) + k + (k//4) + (j//4) - 2 * j) % 7

#             if h == 0:
#                 hari = "Sabtu"
#             elif h == 1:
#                 hari = "Minggu"
#             elif h == 2:
#                 hari = "Senin"
#             elif h == 3:
#                 hari = "Selasa"
#             elif h == 4:
#                 hari = "Rabu"
#             elif h == 5:
#                 hari = "Kamis"
#             else:
#                 hari = "Jumat"

#             if len(str(tanggal)) == 1:
#                 tanggal = "0"+str(tanggal)

#             if len(str(bulan)) == 1:
#                 bulan = "0"+str(bulan)

#             print(f"Berdasarkan perhitungan zeller's congruence: \ntanggal {tanggal}-{bulan}-{tahun} merupakan hari {hari}")
#             break

#     # except Exception as e:
#     #     print(f"Tolong di cek kembali terkait hal berikut:\n{e}")

#     except ValueError:
#         print("Tolong masukkan input yang valid!")


# for tahun in range(2020,2026):
#     if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
#         print(f"Tahun {tahun} merupakan tahun kabisat")
#     else:
#         print(f"Tahun {tahun} bukan merupakan tahun kabisat")

# tanggal = 0
# while tanggal<1 or tanggal > 31:
#     try:
#         tanggal = int(input("Masukkan Tanggal (1-31): "))

#         if tanggal <1 or tanggal >31:
#             print("Tanggal harus antara 1 s.d. 31, mohon input kembali")
        
#     except ValueError:
#         print("Tanggal nya harus dalam bentuk angka ya, mohon di input kembali")

# print(f"Tanggal anda valid yaitu: {tanggal}")    

# kalo udah pake while ga perlu lagi pake else, coba di efisiensiin codingannya


def validasi_input():
    while True:
        try:
            tanggal = int(input("Masukkan Tanggal (1-31): "))
            if tanggal <1 or tanggal>31:
                print("Tanggal harus diisi antara 1 s.d. 31, mohon diulangi")
                continue
            bulan = int(input("Masukkan Bulan (1-12): "))
            if bulan < 1 or bulan >12:
                print("Bulan harus diisi antara 1 s.d. 12, mohon diulangi")
                continue
            tahun = int(input("Masukkan Tahun: "))
            if tahun < 1:
                print("Tahun tidak boleh diisi dibawah 1, mohon diulangi")
                continue
            return (tanggal, bulan, tahun)
        except ValueError:
            print("Inputan tidak sesuai, mohon diulangi")


# print(f"input valid: {tanggal}/{bulan}/{tahun}")

# tugas : melatih bagaimana caranya anda menyatukan def validasi input dengan perhitungan zeller
# cek kabisat dan hitung hari dengan loop
# taro di github, jelasin detail kodingan nya
# konsep: buat 3 file penunjang, 1 buat validasi input, 1 buat perhitungan zeller, 1 buat perhitungan tahun kabisat
# pas perhitungan kabisat yg -2 +2 tahun, itu dibedain antara tahun sebelum, tahun ini, sama tahun setelah

tanggal, bulan, tahun = validasi_input()
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"\nTahun {tahun} merupakan tahun kabisat\n")
else:
    print(f"\nTahun {tahun} bukan merupakan tahun kabisat\n")

q = tanggal
if bulan == 1 or bulan == 2:
    m = bulan + 12
    tahun_adj = tahun - 1
else:
    m = bulan
    tahun_adj = tahun
k = tahun_adj % 100
j = tahun_adj // 100
h = (q + ((13*(m+1))//5) + k + (k//4) + (j//4) - 2 * j) % 7
if h == 0:
    hari = "Sabtu"
elif h == 1:
    hari = "Minggu"
elif h == 2:
    hari = "Senin"
elif h == 3:
    hari = "Selasa"
elif h == 4:
    hari = "Rabu"
elif h == 5:
    hari = "Kamis"
else:
    hari = "Jumat"

if len(str(tanggal)) == 1:
    tanggal = "0"+str(tanggal)
if len(str(bulan)) == 1:
    bulan = "0"+str(bulan)
print(f"Berdasarkan perhitungan zeller's congruence: \ntanggal {tanggal}-{bulan}-{tahun} merupakan hari {hari}")

