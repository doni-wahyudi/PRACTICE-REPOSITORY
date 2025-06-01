# If untuk kondisi sederhana
kapasitas_sistem = 20000  # dalam watt
kapasitas_minimum = 15000
if kapasitas_sistem >= kapasitas_minimum:
    print("Kapasitas sistem cukup untuk operasi!")
else:
    print("Kapasitas sistem kurang, perlu ditambah.")
# perlu ada indentasi (4 spasi) dibawah if

# elif untuk kondisi bertingkat
efisiensi = 85  # dalam persen
if efisiensi >= 90:
    print("Efisiensi sangat baik!")
elif efisiensi >= 80:
    print("Efisiensi baik, tapi bisa ditingkatkan.")
else:
    print("Efisiensi rendah, perlu perbaikan.")
# lebih baik pakai elif untuk kondisi saling terkait dibanding pakai if yang banyak


# Kombinasi kondisi dengan and/or
efisiensi_minimum = 80
if kapasitas_sistem >= kapasitas_minimum and efisiensi >= efisiensi_minimum:
    print("Sistem siap beroperasi dengan baik!")
elif kapasitas_sistem < kapasitas_minimum or efisiensi < efisiensi_minimum:
    print("Sistem perlu perbaikan, cek kapasitas atau efisiensi.")