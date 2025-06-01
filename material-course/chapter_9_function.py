jumlah_pohon = int(input("Masukkan jumlah pohon yang ingin ditanam: "))

def hitung_area_kebun(jumlah):
    return jumlah * 9

luas_kebun = hitung_area_kebun(jumlah_pohon)

print(f"Total luas area kebun yang dibutuhkan untuk menanam {jumlah_pohon} pohon seluas {luas_kebun} m persegi")

def hitung_biaya_tanam(jumlah):
    if jumlah<100:
        return (jumlah*9)*1000000
    if 100<=jumlah<200:
        return (jumlah*9)*950000
    else:
        return (jumlah*9)*900000
    
total_biaya = hitung_biaya_tanam(jumlah_pohon)

print(f"Total biaya yang diperlukan untuk menanam {jumlah_pohon} sebanyak Rp {total_biaya:,}!".replace(",",".")) # :, dalam string formatting (f) untuk memisahkan ribuan menggunakan koma
