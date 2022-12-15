print(30*'=')
print("Private atteibute")
print(30*'=')
# berfungsi untuk menampilkan data dengan pemanggilan tertentu saja
# sehingga tidak mudah untuk di hack

# misal ada satu variabel yang ga ingin diubah
class mahasiswa():
    #nilai = 5 #gimana carany agar nilai ga bisa diakses dari program luar? kasi double underscore __
    jurusan = "Teknik tata boga"
    __nilai = 5 # private
    def __init__(self, input_nama, input_nim): #public
        self.nama = input_nama #public
        self.nim = input_nim #public
    
    def uts(self,input_nilai):
        self.__nilai += input_nilai
    
    def uas(self,input_nilai):
        self.__nilai+= input_nilai
    
    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, 'tidak lulus')
        else:
            print(self.nama,'Lulus')
    
otong = mahasiswa("Otong Surotong",42220090)
ucup = mahasiswa("Michael ucup",42220099)

otong.uts(10)
otong.uas(50)
otong.check_status()

ucup.uts(5)
ucup.uas(25)
ucup.check_status()

