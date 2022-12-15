# fungsi dengan menggunakan argumen sederhana

def siswa(nama):
    print('siswa ini bernama : ', nama)
siswa('mario') # ini disebut dengan argumen #string yaa

# fungsi dengan menggunakan kewywords arguments

def guru(nama,pelajaran):
    print('guru ini bernama :', nama)
    print('Mengajar :', pelajaran)

guru(nama='popong',pelajaran='seni rupa') 
guru(pelajaran='olahraga',nama='endang')
#kywords nya nda harus berdasar kan urutan
#gunanya untuk akses argumen yang banyak dan panjang
guru('olahraga','raihan') # contoh salah :()

# fungsi dengan menggunakan default argumen 
def penjagaSekolah(nama,shift='siang', galak='tidak'): #dimasukkan memangmi shift dan galak nya sebagai string
    print('Penjaga sekolah ini bernama :', nama)
    print('Shiftnya :', shift)
    print('galak? :', galak)
    
penjagaSekolah('entis')
penjagaSekolah('Maman',shift='malam')
penjagaSekolah('Asep',galak='sangat') #tergantung settingannya 

#ini harus di isikan nama, karena nama sebagai default nya yg lain hanya opsional
