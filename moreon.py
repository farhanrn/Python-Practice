barang = ['kunci','ember','jaket','ban','mobil']
print(barang)

#beberapa method untuk memanipulasi list
#method untu menambah data dalam list
barang.append('sepeda') # nambah sepeda dibelakang
print(barang)

barang.extend('dompet') #bakal ngeja per huruf
print(barang)

barang.insert(3,'sepeda') #menaroh string di tengah tengah list
print(barang)

# method untuk menghitung anggota 
jumlahSepeda = barang.count('sepeda')
print("jumlah sepeda adalah :",jumlahSepeda)

# meremove data 
barang.remove('sepeda') # cmn remove yg ketemu pertama kali
print(barang)

#memnbacaa dari belakang 
barang.reverse()
print(barang)

# 
print('='*100)
stuff = barang.copy() # auto buat list baru
stuff.append('gelas') # kalo ga pake.copy() stuff append bakal tampilkan juga data variabel
print(stuff)
print(barang)
