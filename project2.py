# program kasiiirr

print("Toko Saya")
print("Pilih Menu :")
print("1. Es Teh --> Rp. 7000")
print("2. Gurame --> Rp. 15000")
print("Beli 2 Dapat Diskon 20% ")
opsi = input("Pilih Menunya :")
if opsi == "1":
    jumlah = int(input("Jumlah :"))
    uang_kamu = int(input("Uang Kamu :"))
    harga = 7000
    diskon = 20/100
    if jumlah == 1:
        print("Kamu akan membeli es teh berjumlah :", jumlah,"dengan harga :", harga)
    elif jumlah == 2:
        print("Kamu Membeli Es teh berjumlah :", jumlah, "dengan harga :", harga, "dan mendapatkan diskon sebesar 20%")
        print("Total Diskon :", harga*jumlah*20/100)
