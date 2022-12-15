# Operator String menggunakan method

print("Operator dalam Method")


## Merubah case dari string


# 1. merubah semua ke upper case

salam = "Bro!"
print("Normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case 
alay = "aKu KeCe AbieZzzzZZZzZZ"
print("Normal = " + alay)
alay = alay.lower()
print("Lower = " + alay)
alay = alay.upper()
print("Upper = " + alay )

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "sist" # hasilnya boolean
apakah_lower = salam.islower()
print( salam + " Is lower =" + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + "is upper = " + str(apakah_upper))

# isaalpha () <-- untuk mengecek semuanya huruf
# isalnum  () <-- huruf dan angka
# isdecimal () <-- angka saja
# isscpace () <-- spasi, tab, newline \n
# istitle () <-- semua kata dimulai dengan huruf besar 

    #isalpha()
nama = "Farhan"
cek_alpha = nama.isalpha()
print( nama + " is alpha = " + str(cek_alpha))
password = "farhan123"
cek_alpha = password.isalpha()
print( password + " is alpha = " + str(cek_alpha))

    #isalnum() --> artinya : is all number?
tl = "06012003"
print(tl)
cek_alnum = tl.isalnum()
print( tl + " is all number =" + str(cek_alnum))

tl = "AAU20RTK"
print(tl)
cek_alnum = tl.isalnum() 
print(tl + " is all number =" + str(cek_alnum))


# istitle()
judul = "it is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bakal bolean

print(judul + " is title = " + str(cek_judul))
        #disini tuh yg title semuanya garus berawalan huruf besar supaya teridentifikasi sebagai title
        #biarpun salah satunya huruf besar dn ada yang hur kecil bakal false hasilnya

## ngecek komponen startswith() endswith 
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start =" + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end =" + str(cek_end))

## Penggaungan komponen join() dan split()

pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))


#alokasi karakter = rjust() , ljust() center()

print(5*"=" + "data" + "="*5) #ini rumit shay

kanan = "kanan".rjust(10) 
print("'"+kanan+"'")

kanan = "surotong".rjust(10) 
print("'"+kanan+"'")

kiri = "kiri".ljust(10) 
print("'"+kiri+"'")

tengah = "tengah".center(20,"-") 
print("'"+tengah+"'")

## kebalikannya ->> strip
tengah = tengah.strip("-")
print("'"+tengah+"'")
