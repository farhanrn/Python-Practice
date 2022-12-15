# format string

# contoh generic

#sting
nama = "Ucup"
str = "Hello" 
format_str = f"hello {nama}"

print(format_str)

#boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

#angka 
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

#bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"  # tanda :d menandakan angka adalah bilangan bulat
print(format_str) 

#bilangan ribuan
angka = 2000
format_str = f"ribuan = {angka :,} " # tanda :, unuk memberikan koma atau titik pada angka sebelum nol
print(format_str)


#bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}" #tanda :.2f , :.3f menandakan berapa banyak angka dibelakang koma yang akan ditampilkan 
print(format_str)

# menampilkan leading zero (angka depannya )
angka = 2005.54321
format_str = f"desimal = {angka:9.3f}" #tanda :.2f , :.3f menandakan berapa banyak angka dibelakang koma yang akan ditampilkan 
print(format_str)
 
 # menampiljan tanda + atau -
angka_plus = 10
angka_minus = -10
format_plus = f"Plus = {angka_plus :+.2f}"
format_minus = f"Minus = {angka_minus :d}"

print(format_plus)
print(format_minus) 

#memformat persen
persentase = 0.045
format_persen = f"persen = {persentase :.2%}"
print(format_persen)

#d melakukan operasi aritmatika di dalam kurung kurawang / placeholder

harga = 10000
jumlah = 5

format_string = f"Harga total ={harga*jumlah}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)
