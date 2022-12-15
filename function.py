# function


print(90*'=')
print("Belajar Function")
print(85*'=')

# membuat fungsi sederhana
def suaraayam():
    print('kukuruyukk!!!')

def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp. 20.000')
suaraayam()


# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga',kg,'ayam adalah',hargaTotal)

hargaayam() #interpreted language 
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)
hargatotalayam(1000)
hargatotalayam(456320)

# kerjanya ini tuh berantai ki pada saaat di panggil satu fungsi maka bakal na panggil fungsi atasnya

