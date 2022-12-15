# program komparasiiii

# setiap hasil dari operasi komparasi adlah boolean

# >  <  >=  <=  ==  != is  is not

a = 4
b = 2

#lebih besar dari >
print("===== lebih besar dari >")
hasil = a > 3
print(a,'>',3,'=', hasil)

hasil = a > 7
print(a,'>',7,'=', hasil)

hasil = b > 3
print(b,'>',3,'=', hasil)

hasil = b > 2
print(b,'>',2,'=', hasil)

# kurang dari 
print("===== kurang dari <")
hasil = a < 9
print (a,'<',9,'=', hasil)
hasil = b < 5
print (b,'<',9,'=', hasil)
hasil = a < 3
print (a,'<',3,'=', hasil)
hasil = b < 1
print (b,'<',1,'=', hasil)

# lebih sama dengan 
print("===== lebih dari sama dengan =")
hasil = a>= 2
print(a,'>=',2,'=', hasil)
hasil = b>= 1
print(b,'>=',1,'=', hasil)
hasil = a>= 7
print (a,'>=',7,'=',hasil)
hasil = b>=2
print(b,'>=',2,'=', hasil)

# kurang dari sama dengan <=
print("===== kurang dari sama dengan =")
hasil = a <= 18
print(a,'<=', 18, '=', hasil)
hasil = b <= 100
print(b, '<=', 100, '=', hasil )
hasil = a <= -1
print (a,'<=', -1, '=', hasil)
hasil = b <= -20000
print (b, '<=', -2000, '=', hasil)

# sama dengan ==
print("===== sama dengan ==")
hasil = a == 4
print (a,'==', 4, '=', hasil)
hasil = b == 2
print (a,'==', 2, '=', hasil)
hasil = a == 5
print (a,'==', 5, '=', hasil)
hasil = b == 3
print (a, '==', 3, '=', hasil)


# tidak sama dengan !=
print("===== tidak sama dengan ==")
hasil = a != 6
print (a,'!=', 6, '=', hasil)
hasil = b != 7
print (a,'!=', 7, '=', hasil)
hasil = a != 4
print (a,'!=', 4, '=', hasil)
hasil = b != 2
print (a, '!=', 2 , '=', hasil)

# is sebagai komparasi object identity
x = 5 # ini adalah assignment membuat objek 
y = 5

hasil = x is y
print('x is y =', hasil)


