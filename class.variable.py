# class dan variable

print(30*'=')
print('Belajar class dan variabel')
print(30*'=')

class mahasiswa():

    Jumlah_Mahasiswa = 0

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim
        mahasiswa.Jumlah_Mahasiswa +=1

    

otong = mahasiswa("otong surotong",42220080)
ucup = mahasiswa("Michael Ucup",42220070)
cassandra = mahasiswa("Casandra aja",42220079)

print(mahasiswa.Jumlah_Mahasiswa)
