# set , himpunan
# tidak punya urutan


superhero = {'wiro sableng',
            'si buta dari gua hantu',
            'saras 008',
            'gundala',
            'gatotkaca'}
superhero.add('mak lampir') # himpunan urutannya ga penting
superhero.add('gundala')

print(superhero)

# cara menuliskan set

superhero = set()
superhero.add('wiro sableng')
superhero.add('gundala')
superhero.add('wiro sableng')
superhero.add('saras 008')
superhero.add(22455)

print(superhero)

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}
print(ganjil.union(genap)) 
print(ganjil.intersection(prima))
