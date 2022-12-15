list = [1,2,3,4,]
tuple = (1,2,3,4)
set = {1,2,3,4}

print(type(list))
print(type(tuple))
print(type(set))

# dictionary = menggunakan mapping

print('belajar dictionary')

member1 = {"id" : 101,
          "Nama":"Farhan Rahman",
          "pekerjaan":"ML engineer",
          "Status Member":"Gold"
            }
print(member1["pekerjaan"])
print(member1.keys())
print(member1.values())

member2 = {"id":102,
           "nama":"Ujang Pintu",
           "pekerjaan":"reparasi pintu",
           "status member":"Berlian"}

memberlist = {101:member1,102:member2}

print(memberlist[101])