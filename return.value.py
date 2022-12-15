print('Return Value')
print(70*'=')

#fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari', argumen, 'adalah =', total)
    return total

a = print(kuadrat(4))
print(a)

print('+'*100)

#funsgi dengan return value dan multiple arguments

def tambah(argumen1,argumen2):
    total = argumen1 + argumen2
    print(argumen1,'+',argumen2,'=',total)
    return total # bisa tipe data lain nda hanya number #bisa list juga anyway

def kali(argumen1,argumen2):
    total = argumen1 * argumen2
    print(argumen1,'x',argumen2,'=',total)
    return total # bisa tipe data lain nda hanya number 

b = kali(3,tambah(3,4))
print(b)