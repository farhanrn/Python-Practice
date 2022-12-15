# program for loop

# List sebagai iterable >> bisa di iterasi

print("Program for loop")
print(5*"=")

gorengan = ['bakwan','cireng','tahu isi','tempe goreng','ubi goreng']


for g in gorengan: #si huruf g mengakses setiap isi dari listnya 
                    # si g merupakan variabel baru scope nya dalam for
    print(g)    #si g bakal ngambil komponen 'g' dalam gorengan / variabel
    print(len(g))
print(10*'=')

# string sebagai iterable

bakwan = 'bakwan' # tiap huruf bakal ditampilkan menurun
for i in bakwan:
    print(i)
print(10*'=')

# for di dalam for 
buah = ['semangka','jeruk','apel','anggur']
sayur = ['kangkung','wortel','tomat','kentang']

Daftar_Belanja = [gorengan,buah,sayur] #ditampilkan semuai
print(Daftar_Belanja) #ada tiga buah list 

for subDaftarBelanja in Daftar_Belanja:
    #dia akan mengambil tiap listnya
    print(subDaftarBelanja)
    for komponen in subDaftarBelanja:
        print(komponen)

print(90*"=")

print("Program For Else,, Range,, dan Break")
# lets begiiiiinnnnnnnn !!!!

#program range 
print("program range")
for i in range(10,40,5): 
    print(i)
print(90*'=')

# program for else
print('Program For...Else')
print(60*'@')

number = 25;

for i in range(0,40):
    print (i)
    if i is 25:
        print('angka ditemukan', i)

print ('Program break')
for i in range(0,40):
    print (i)
    if i is 25:
        print('angka ditemukan', i)
        break
# break is basically kasi berhenti sampe 25 sja jdi nda diteriskan mi sampe nya 39

number = 50;
for i in range(0,40):
    print (i)
    if i is 50:
        print('angka ditemukan', i)
        break
else:           #ngecek apakah for nya sampe di akhir ato nda
    print("angka tidak ditemukan")

print("space diluat for")




