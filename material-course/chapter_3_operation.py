pohon_tanam = 50
pohon_baru = 30
total_pohon = pohon_tanam + pohon_baru
nama = "Doni Wahyudi"
# print(f"{nama} tanam {total_pohon} pohon!")

sampah_awal = 100
sampah_daur_ulang = 40
sisa_sampah = sampah_awal - sampah_daur_ulang
# print(f"{nama} kurangi sampah jadi {sisa_sampah} kg!")

# Perhatikan pemdas nya, mana yang akan dikalkulasikan terlebih dahulu

lampu_per_rumah = 5
rumah = 10
total_lampu = lampu_per_rumah * rumah
# print(f"{nama} hemat {total_lampu} lampu!")

a = 5
b = 3
c = 1

formula = (((a**2)+c-b) % b)
formula_2 = a*(c+a)//(b+c)
'''
** => pangkat
% => modulus (sisa pembagian, bisa buat cari angka genap atau ganjil)
// => pembagian bulat kebawah
'''
print(formula, formula_2, sep="\n")