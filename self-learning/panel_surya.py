# Membuat variabel dasar
jumlah_panel = 25  # jumlah panel surya
kapasitas_per_panel = 450  # kapasitas dalam watt
print("Jumlah panel:", jumlah_panel)
print(kapasitas_per_panel)
# jangan pake nama yang dimulai dengan angka (misalnya 1panel) atau pake spasi (misalnya jumlah panel)

# Menghitung total energi
total_energi = jumlah_panel * kapasitas_per_panel
print("Total energi yang dihasilkan:", total_energi, "watt")
# jangan lupa simpan hasil perhitungan ke variabel baru kalau mau dipake lagi nanti

# Menggunakan variabel untuk perhitungan dinamis
efisiensi = 0.85  # efisiensi panel 85%
total_energi = jumlah_panel * kapasitas_per_panel
energi_bersih = total_energi * efisiensi
print("Total energi:", total_energi, "watt")
print("Energi bersih setelah efisiensi:", energi_bersih, "watt")
# gunakan variabel untuk nilai yang bisa berubah-ubah, seperti efisiensi, biar gampang diupdate
# jangan hardcode nilai langsung di perhitungan (misalnya total_energi * 0.85) tanpa variabel, soalnya susah kalau mau ganti nilai

# Comments in python
# Proyek panel surya Eco Techno Leader
# jumlah_panel = 50
# kapasitas_per_panel = 300
# print("Jumlah panel:", jumlah_panel)
# tulis komentar yang jelas biar orang lain (atau kamu sendiri di masa depan) paham