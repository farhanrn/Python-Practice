# belajar scope : global scope dan local scope 
# berguna untuk merubah variabel atau memproduksi variabel

#scope variable : local

namaKucing = 'cassandra'                                   # masukkan variabel
def rubahNamaKucing(namaBaru):                            # def argu(variabel)
    namaKucing = namaBaru                                     #ubah variabel
    print('Saya rubah nama kucing menjadi',namaKucing)      #print 1
rubahNamaKucing('ketie')                                       #argumen 2
print('Nama kucing saya menjadi',namaKucing)                   #print 2

#scope variable : global

namaKucing = 'cassandra'
def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru #variable global
    nama = namaBaru # variabel local
    print('Saya rubah nama kucing menjadi',namaKucing)
rubahNamaKucing('ketie')
print('Nama kucing saya menjadi',namaKucing)


namaKucing = 'cassandra'
makananKucing = 'royal canin'
def rubahNamaKucing(namaBaru):
    global namaKucing
    namaKucing = namaBaru
    print('Saya rubah nama kucing menjadi',namaKucing)

def kasihMakanKucing(makanan,nama):
    global namaKucing,makananKucing
    namaKucing = nama
    makananKucing = makanan

rubahNamaKucing('Ketie')

kasihMakanKucing('universal','alex')

print('Nama kucing saya menjadi',namaKucing,'dan makan',makananKucing)

# scope global sealalu di awali dengan global
#scope local  