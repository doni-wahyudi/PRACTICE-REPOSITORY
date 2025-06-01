# Operasi aritmetik 
energi_input = 1000  # energi input dalam kWh
energi_output = 850  # energi output dalam kWh
selisih = energi_input - energi_output
print("Selisih energi:", selisih, "kWh")
# jangan lupa simpan hasil perhitungan ke variabel kalau mau dipake lagi

# Assignment dan comparison
efisiensi = (energi_output / energi_input) * 100  # hitung efisiensi dalam persen
standar_efisiensi = 80
efisiensi += 5  # tambah efisiensi dengan 5% karena perbaikan
print("Efisiensi sistem:", efisiensi, "%")
print("Apakah efisiensi memenuhi standar?", efisiensi >= standar_efisiensi)
# jangan lupa urutan operasi (pake tanda kurung kalau perlu, misal (energi_output / energi_input) * 100)

# Boolean operator untuk analisis, dikombinasikan dengan and/or
is_operational = True
print("Apakah sistem efisien dan operasional?", efisiensi >= standar_efisiensi and is_operational)
print("Apakah sistem perlu perbaikan?", not (efisiensi >= standar_efisiensi))