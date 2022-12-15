# MATERI OPERASI DAN MANIPULASI STRING
# VIDEO 16
# SEMANGATTTT

# 1. Menyambung string (contantenate)
from typing import AsyncIterable


nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"
nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

nama_pertama = "Farhan"
nama_akhir = "Rahman"
nama_lengkap = nama_pertama + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# 3. Operator untuk sting

#mengecek apakah ada komponen char atau string di string ( in )

r ="R"
status = r in nama_lengkap
print(r + " ada di " + nama_lengkap + " = " + str(status))

r ="R"
status = r not in nama_lengkap
print(r + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# Indexing
print("==indexing==")
print("Index ke-0 :" + nama_lengkap[0])
print("Index ke-1 :" + nama_lengkap[1])
print("Index ke-(-1) :" + nama_lengkap[-1])
print("Index ke-(-2) :" + nama_lengkap[-2])
print("Index ke-[3:7] :" + nama_lengkap[3:8])
print("Index ke-[0:2:4:6:8:10] :" + nama_lengkap[0:10:2])
print("===============")

#item paling kecil
print("paling kecil :" + min(nama_lengkap))

#item paling besar (huruf terbanyak gitu gaess)
print("paling besar :" + max(nama_lengkap))

Ascii_code = ord(" ")
print("ASCII code untuk spasi adalah :" + str(Ascii_code))
data = 117
print("char untuk ASCII 117  adalah :" + chr(data))

Ascii_code = ord("'")
print("ASCII code untuk tanda petik satu adalah : " + str(Ascii_code))

# 4. Operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada" + data + "=" + str(jumlah))

Dear_Farhan = "SEMANGATTT"
semangat = input(str("Masukkan Nama :"))
print("Semangat woeieeee jadi programmer, ewakooo" , semangat)

