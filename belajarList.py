# listt

# kumpulan data numbers
data_angka = [1,5,2,3]
print(data_angka)

# kumpulan data sting 
data_string = ['ucup','otong','odah']
print(data_string)

#kumpulan data boolean 
data_boolean = [True,False,True,True]


# kumpulan campuran 
data_campuran = [1,'bala-bala','cireng','ucup',True,'otong',False]
print(data_campuran)

# cara alternatif bikin list 
data_range = range(0,10,2) # range (start, stop, step)
data_list = list(data_range)

print(data_list)

# membuat list dengan for loop comprehension 
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list pake for pake if

list_pake_for_if = [i for i in range (0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range (0,10) if i % 2 == 0]
print(list_pake_for_if)


# operasi list

# index 0       1       2 / (-1)
data = ["ucup","otong","Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0)= {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# panjang data 
panjang_data = len(data)
print(f"Panjang data= {panjang_data}")

# manipulasi data list


# menambahkan item pada list
print(f"data sebelum ditambah = {data}")

data.insert(1,'Asep')
print(f"data sesudah ditambah = {data}")

# menambah data diakhir
data.append("Jajang")
print(f"data ditambah lagi = \n{data}")

# menambah lis dengan list 
data_baru = ['Ujang','Usep','Dadang']
data.extend(data_baru)
print(f"data baru setelah menambahkan list data_baru = {data}")

# merubah data 
# mengubah data kedua jadi michael

data[2] = 'Michael'
print(f"data rubah = {data}")

# menghilangkan data

data.remove('Ujang')
print(f"data remove = \n{data}")

#Operasi pada list 

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]

print(f"data angka ={data_angka}")

# count data --> muncul berapa kali dalam data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3= data_angka.count(3)

print(f"jumlah angka 4 : {jumlah_data_4}")
print(f"jumlah angka 3 : {jumlah_data_3}")

# ambil posisi data (indexing)

data = ['farhan','rahman','james','scott']
print(f"data = {data}")

index_james = data.index("james")
print(f"index si james {index_james}")

# mengurut list
print(f"data sebelum di sort ={data_angka}")
data_angka.sort()
print(f"data yang telah di sort = {data_angka}")

# untuk sort data string
print(f"data = {data}")
data.sort()
print(f"data yang telah dis sort menggunakan string {data}")

# membalik list 
data_angka.reverse()
data.reverse()
print(f"data yang direverse=\{data_angka}\n{data}")


# copy list
# teknik duplikat list

a = ['farhan','rahman','aan']
print(f"a = {a}")

b = a # membuat lis dengan nama lain tapi address nya sama 
print(f"b = {b}")

# merubah member dari a

a[1] = 'james'
b.sort
print(f"a = {a}")
print(f"b = {b}")

# menduplikat list dgn copy
print("Membuat list c dengan a.copy()")
c = a.copy()


print("kita ubah data 0")
c[0] = 'semangat'
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

# nested list
data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,data_list_biasa,6,7]
print(f"list 2D = {list_2D} ")

# contoh penggunaan
peserta1 = ['Farhan', 19, 'Laki-laki']
peserta2 = ['Midoriya', 18, 'Laki-laki']
peserta3 = ['Sakura', 14, 'Perempuan']

list_peserta = [peserta1, peserta2, peserta3]
print(f"List peserta debat = {list_peserta}")

