
# Tipe data dalam python : Angka satuan (integer)
data_integer = 1100000
print(type(data_integer))
print("data : ", data_integer, ", bertipe :", type(data_integer))



#tipe kedua : float : angka dengan koma
data_float = 1.5
print("data : ", data_float, ", bertipe :", type(data_float))

#tipe data : string ( kumpulan karakter)
data_string = "ucup"
print("data : ", data_string, ", bertipe :", type(data_string))


#tipe data : boolean ( kumpulan biner) true/false
data_bool = True
print("data : ", data_bool, ", bertipe :", type(data_bool))

# tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex, ", bertipe :", type(data_complex))

#tipe data dari bahasa C

from ctypes import c_double 

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe :", type(data_c_double))
