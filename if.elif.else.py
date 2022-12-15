# Program if elif dan else

print(" Program If Elif Else")

nilai = 75 #variabel

if nilai == 75:
    print("nilai anda :", nilai)

if nilai == 80:
    print("nilai anda :", nilai)

# ini tergantung dari nilai berapa yang dimasukkan dalam variabel nya 
# misal nilai = 75 berti yg if nilai == 75 ji yg bekrja
# misal nilai = 80, berti yg if nilai == 80 ji yg bekerja jga


# program nasting if 
nilai1 = 75
nilai2 = 80

if nilai1 == 75:
    print("Nilai anda :", nilai1)
    print("Step 1")
    if nilai2 ==80:
        print("Nilai anda :", nilai2)
        print("Step 2")
    #if dalam if

print("=============")

nilai = 60
print("Nilainya adalah :", nilai)

if nilai == 75: #equal eksplisit
    print("Nilai Anda :", nilai)
if nilai is 60:  #equal
    # boleh pake is menggantikan ==
    print("Nilai Anda :", nilai)
if nilai is not 60: # not equal
    print("nilai anda bukan : 60 ", nilai)

print(100*"=")
print("elif")


nilai = 90
if 80 <= nilai <= 100:
    print("Nilai anda adalah A")
elif 70 <= nilai < 80:
    print("Nilai anda adalah B")
elif 60 <= nilai < 70:
    print("Nilai anda adalah C")
elif 50 <= nilai < 60:
    print("Nilai anda adalah T, lakukan perbaikan")
else :
    print("Maaf anda tidak lulus mata kuliah ini ")
   
print(100*"+")
print("Operator logika untuk list dan string")
print(" ")

ATK = ["pensil","pulpen","penggaris","penghapus","spidol"]
beli = "pulpen"

if beli in ATK:
    print('Mamang bilang," ya saya jual',beli,'"')
    if not beli in ATK:
        print('"saya gak jual',beli,'"')
    #program ini gak berjalan weh

karakter = "z"
if karakter in beli:
    print("ada ",karakter,"di",beli)
else:
    print("Tidak ada",karakter,"di",beli)
