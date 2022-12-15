print(30*'=')
print("Belajar Class")
print(30*'=')

#class HARUS DIATAS!
class mahasiswa(): # bisa buat sebanyak banyaknya dalam satu template
    nama = 'nama'
# method adalah fungsi yang nempel di dalam classsssss
    def belajar(self, kondisi): # self berfungsi mengidentifikasi siapa
        print(self.nama,'sedang belajar', kondisi)
        return

    def tidur(self):
        print(self.nama,'tidur dikelas')


# main program
otong = mahasiswa()
 # otong adalah instace dan mahasiswa class nya
ucup = mahasiswa()

otong.nama = "otong surotong"
ucup.nama = "Michael ucup"

#print(otong.nama)
#print(ucup.nama)

otong.belajar("dengan giat") # kondisi --> dengan giat 

ucup.tidur()

