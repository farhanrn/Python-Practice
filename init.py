# init 
# bab sebelumnya = class
# urutannya dalah
# dalam kelas mahasiswa kita punya init, yg akan bekerja setelah kita panggil kelas baru
# contohnya otong itu kelas baru 
# bedanya smaa yang lain seperti belajar dan tidur itu adalah dia bakal bekerja pada saat dipanggil

class mahasiswa():
    # init = inisialization , membuat permulaan 
    # dijalankan saat inisialisasi objek
    def __init__(self, input_nama, input_nim ): # self = otong, nama = nama 
        self.nama = input_nama          # harus ada input
        self.nim = input_nim


    def belajar(self,kondisi):  
        print(self.nama,'sedang belajar',kondisi)
    def tidur(self):
        print(self.nama,'tidur dikelas')


# main program 

otong = mahasiswa("otong surotong",42220041) # disini __init__ dipanggil #disini juga harus ada inputnya
print(otong.nama)
# ucup = mahasiswa()
otong.belajar("dengan giat")
#otong.nama = 'otong surotong'
#ucup.nama = 'michael ucup'

