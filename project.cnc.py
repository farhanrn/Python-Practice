

'''
Project Open Recruitment Computer and Network Community PNUP
Program sederhana conversi 3 mata uang asing ke mata uang rupiah 
Kelompok 2 
Farhan Rahman
Maghfirah Amaliah Kasim 
Andi Faadiyah Sulfi
'''

# Program layanan konversi mata uang asing ke rupiah 

print("PROGRAM KONVERSI MATA UANG ASING KE MATA UANG RUPIAH")
print(" Kelompok 2 ")
print(20*"=")
print("Selamat datang di Program Kami!")

# Masukkan nama 
nama = str(input("Masukkan Nama anda :  "))
nama = nama.upper()
print("Halo", nama, "! Selamat menikmati layannan kami")

print("")

def list_mata_uang():
    print("Silahkan pilih jenis mata uang yang akan dikonversi")
    print(" 1. US Dollar ( Rp. 14.283,45 )")
    print(" 2. Riyal Arab ( Rp. 3.809,00 ) ")
    print(" 3. Yuan China ( Rp. 2.209,18) ")
    print(" 4. Berhenti ")

print("")

# Kondisi Awal Variabel 
ulang = "y"
# Kondisi while 
while ulang == "y":
    list_mata_uang()
    print("")
    pilihan = int(input("Masukkan Nomor pilihan untuk konversi mata uang anda :  "))

    if pilihan == 1:
        print("")
        print(" >> Format untuk memasukkan nominal tidak menggunakan titik dan koma <<")
        dollar = 14283
        dollar_ke_rupiah = int(input("Masukkan Nominal dalam US Dollar : "))
        print("")
        konversi_dollar = dollar_ke_rupiah*dollar
        print(f"{dollar_ke_rupiah} US Dollar senilai dengan {konversi_dollar} Rupiah" )
        print("")

    elif pilihan == 2:
            print("")
            print(">> Format untuk memasukkan nominal tidak menggunakan titik dan koma <<")
            riyal = 3809
            riyal_ke_rupiah = int(input("Masukkan Nominal dalam Riyal Arab : "))
            print("")
            konversi_riyal = riyal_ke_rupiah*riyal
            print(f"{riyal_ke_rupiah} Riyal Arab senilai dengan {konversi_riyal} Rupiah" )
            print("")

    elif pilihan == 3:
            print("")
            print(">> Format untuk memasukkan nominal tidak menggunakan titik dan koma <<")
            yuan = 2209
            yuan_ke_rupiah = int(input("Masukkan Nominal dalam Yuan China : "))
            print("")
            konversi_yuan = yuan_ke_rupiah*yuan
            print(f"{yuan_ke_rupiah} Yuan China senilai dengan {konversi_yuan} Rupiah" )
            print("")

    elif pilihan == 4:
            print("")
            print("Program Selesai")
            break
    else:
            print("Masukkan angka pilihan yang valid yaa sesuai daftar")
            print("")

    ulang = input(" Apakah masih ingin menggunakannya lagi? (y / t) : ")
    ulang = ulang.lower()

def akhir():
    print(100*"=")
    print("Terima Kasih Telah Menggunakan Layanan kami! Semoga bermanfaat ya!")

akhir()

