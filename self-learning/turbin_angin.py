# Tipe data dasar (int, float, str, bool : benar/salah)
jumlah_turbin = 10
kapasitas_turbin = 2.5 
nama_proyek = "Turbin Angin Desa"
proyek_aktif = True 
print(jumlah_turbin)
print(kapasitas_turbin)
print(nama_proyek)
print(proyek_aktif)
# jangan campur tipe data yang gak cocok (misalnya, jumlah_turbin = "10" pake string untuk angka yang perlu dihitung)

# Menggunakan tipe data koleksi
lokasi_turbin = ["Desa A", "Desa B", "Desa C"]  # list: daftar yang bisa diubah
hari_operasi = ("Senin", "Rabu", "Jumat")  # tuple: daftar yang gak bisa diubah
tipe_turbin = {"vertikal", "horizontal"}  # set: kumpulan unik
data_proyek = {"nama": "Turbin Angin Desa", "kapasitas": 2.5}  # dict: pasangan kunci-nilai
print(lokasi_turbin)
print(hari_operasi)
print(tipe_turbin)
print(data_proyek)
# gunakan list kalau datanya bisa berubah, tuple kalau gak perlu diubah
# jangan pake set kalau urutan data penting, soalnya set gak urut

# Menggabungkan tipe data untuk bikin struktur data yang kompleks tapi terorganisir
lokasi_turbin = ["Desa A", "Desa B", "Desa C"]
total_kapasitas = jumlah_turbin * kapasitas_turbin
data_proyek = {"jumlah_turbin": jumlah_turbin, "total_kapasitas_mw": total_kapasitas, "lokasi": lokasi_turbin}
print("Data proyek:", data_proyek)
# jangan pake tipe data yang salah (misalnya, nyimpan daftar lokasi pake string, bukan list)