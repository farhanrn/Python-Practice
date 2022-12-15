# LIST

print("==List==")

Data = [1,4,9,16,25,36,49,64]

# Mengakses List
Subdata1 = Data[3]
Subdata2 = Data[-3]

# Memotong List
Subdata3 = Data[0:3]
Subdata4 = Data[:4]
print(Subdata4)


Data2 = [100,200,300,400,500,600,700,800]
# Menambah List
Data3 = Data + Data2
print(Data3)

# Merubah konten dari list .. numpy

print(Data)
#Data[4] = 87

# Mengcopy LIst Ke variabel baru
a = Data [:]
a[7] = 87

# merubah content lsit dengan menggunakan metode slicing

Data [3:5] = [11,12]
print(Data)

# List dalam List

x = [Data, Data2]
print(x)

# Mengakses list dalam multidimensional list

y = x[1][4]
print(x)
print(y)

# Method untuk lst

Data.append(30) #ditambahkan satu data dalam sebuah list

print(Data)

# Function yg bisa kita gunakan kepada list

panjang_list = len(Data)
print(panjang_list)

print("weee susahna")