
# STRING WIDTH AND ALLIGNMENT 

print("==WIDTH AND ALLIGNMENT==")

data_nama = "Ucup Sarucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

#string standard
data_string = f"nama ={data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, Nomor sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline <kasih enter> 
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nNomor sepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

#string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# kesimpulannya : pake mi saja yg f""" (enter) """ lebih efektif tgl di input saja string


# mengatur lebar
data_nama = "Farhan"
data_string = f"""
nama   = {data_nama}
nama   = {data_nama}
umur   = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu} 

nama   = {data_nama :>10}
nama   = {data_nama :>5}
umur   = {data_umur :>5}
tinggi = {data_tinggi :>5}
sepatu = {data_nomor_sepatu :>5} 
"""

# tanda :>5 , :.10 itu menandakan untuk rata kanan seberapa jauh//

print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

