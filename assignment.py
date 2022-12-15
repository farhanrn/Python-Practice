# operasi yang dapat dilakukan dengan penyingkatan

#operasi ditambah dengan assignment

print("OPERASI ARITMATIKA")
a = 5 # adalah assignment
print("Nilai a =", a)

a += 1 #artinya adalah nilai a itu ditambah dengan 1
print("Nilai a +=1, nilai a menjadi", a)

a -= 2 #artinya adalah nilai a itu dikurangi dengan 2
print("Nilai a -=2, nilai a menjadi", a)

# pangkat atau eksponen 
a *= 5 #artinya adalah nilai a itu dikali dengan 5
print("Nilai a *=5 nilai a menjadi", a)

a /= 2 #artinya adalah nilai a itu dibagi dengan 2
print("Nilai a /=5 nilai a menjadi", a)

# operasi modulus dan floor divition
b = 10
print("Nilai b=", b)

b %= 3
print("Nilai b%=3 Nilai b menjadi", b)

b = 10
print("Nilai b=", b)

b //= 3
print("Nilai b//=3 Nilai b menjadi", b)


a = 5
print("Nilai a =", a)

a **= 3
print("Nilai a **=", a)

#OPERASI BITWISE
print("=================================")
print("OPERASI BITWISE")
c = True
print("\nNilai c =", c)

# operasi or
print ("Operasi OR")
c = False
print("\nNilai c =", c)
c |= False
print("Nilai c |= False, nilai c menjadi", c)

#Operasi and
print("Operasi And")
c = True
print("\nNilai c =", c)

c &= False
print("Nilai c &= False, nilai c menjadi", c)

c = True
print("nilai c&= True, Nilai C menjadi", c)
c &= True
print("nilai c&= False, Nilai c menjadi", c)

#Operasi XOR
print("\nOperasi XOR")
c = True
print("\nNilai c =", c)

c ^= False
print("Nilai c ^= False, nilai c menjadi", c)

c = True
print("nilai c^= True, Nilai C menjadi", c)
c ^= True
print("nilai c^= False, Nilai c menjadi", c)

# geser geser
d = 0b0100
print("\nnilai d =", format(d,'04b'))
d >>=2
print("nilai d>>= 2, nilai d menjadi", d)

