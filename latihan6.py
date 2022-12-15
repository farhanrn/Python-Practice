# LATIHAN LOGIKA DAN KOMPARASI
#MEMBUAT GABUNGAN AREA RENTANG DARI ANGKA

#++++++++++++3----------10++++++++++

inputUser = float(input("masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10 :"))

# ++++++3---------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

#-------------10+++++++++++++
#Memeriksa angka lebih dari 10 
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

#++++++++3--------10+++++++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukan: ", isCorrect)


# ----------3++++++++++10-----------
#Kasus Irisan 
print(10*"=",)
inputUser = float(input("masukkan angka yang bernilai lebih dari 3 dan kurang dari 10 :"))




# --------3++++++++++
# lebih dari 3 
isLebihDari = inputUser > 3
print("Lebih Dari 3=", isLebihDari)


# +++++++++++10----------
# Kurang dari10
isKurangDari = inputUser < 10
print("Kurang Dari 10=", isKurangDari)


# --------3++++++++++
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan : ", isCorrect)









print("Jangan Menyerah!!!")
