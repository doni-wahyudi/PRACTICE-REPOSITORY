# String dasar
nama_proyek = "Proyek Panel Surya Desa"
lokasi = 'Desa Makmur'
print("Nama proyek:", nama_proyek)
print("Lokasi:", lokasi)
# pakai tanda kutip yg konsisten, jangan dicampur awal dan akhir nya antara ' dengan "

# F-String untuk memanggil variabel dan membuat format lebih rapi
jumlah_panel = 50
kapasitas_total = 15000
laporan = f"Laporan {nama_proyek} di {lokasi}: Jumlah panel = {jumlah_panel}, Kapasitas = {kapasitas_total} watt"
print(laporan)

# String methods
nama_proyek = "Proyek Panel Surya Desa"
lokasi_raw = "  desa makmur  "
lokasi_clean = lokasi_raw.strip().title()
laporan = f"Laporan {nama_proyek} di {lokasi_clean}: Jumlah panel = {jumlah_panel}, Kapasitas = {kapasitas_total} watt"
print(laporan)
print("Apakah 'Panel' ada di laporan?", "Panel" in laporan)
# strip untuk bersihkan data (buang spasi), title untuk format teks sebagai judul
# jangan ubah string langsung tanpa simpan ke variabel kalau mau dipake lagi (misalnya, lokasi.strip() tanpa simpan hasilnya)