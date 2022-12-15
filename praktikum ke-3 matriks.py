print (" Program matriks ke-3     ")
print ("==========================")
print (" Nama  : Nur Adnan Setiadi")
print (" Nim   : 32320025         ")
print (" Kelas : 2B Elektronika   ")
print ("========================= ")

m = int (input("Masukkan Jumlah Baris: "))
n = int (input("Masukkan Jumlah Kolom: "))
x = [0]*m
for i in range(m):
    x[i] = [1]*n
print (" ", x)