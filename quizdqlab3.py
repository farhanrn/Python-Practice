

# Latihan oop dqlab > behaviour dalam class
'''
Selain dapat mendefinisikan atribut, dalam sebuah class,
 aku diperbolehkan untuk mendefinisikan fungsi-fungsi (behavior) dari sebuah class.
Dari potongan kode yang telah aku gunakan, aku dapat menambahkan fungsi-fungsi berkaitan 
dengan class Karyawan. Sebagai contoh, 
seorang karyawan tentunya mungkin saja memiliki pendapatan tambahan berdasarkan banyaknya kerja lembur
 dan jumlah proyek yang telah diselesaikan.
'''

# Definisikan class Karyawan berikut dengan attribut dan fungsinya
class Karyawan:
    nama_perusahaan = 'ABC'
    insentif_lembur = 250000
def __init__(self, nama, usia, pendapatan):
    self.nama = nama
    self.usia = usia
    self.pendapatan = pendapatan
    self.pendapatan_tambahan = 0
def lembur(self):
    self.pendapatan_tambahan += self.insentif_lembur
def tambahan_proyek(self, insentif_proyek):
    self.pendapatan_tambahan += insentif_proyek
def total_pendapatan(self):
    return self.pendapatan + self.pendapatan_tambahan
# Buat object dari karwayan bernama Aksara dan Senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)
# Aksara melaksanakan lembur
aksara.lembur()
# Senja memiliki proyek tambahan
senja.tambahan_proyek(2500000)
# Cetak pendapatan total Aksara dan Senja
print('Pendapatan Total Aksara: ' + str(aksara.total_pendapatan()))
print('Pendapatan Total Senja: ' +str(senja.total_pendapatan()))