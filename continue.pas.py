print(85*'@')
print("PROGRAM CONTINUE DAN PASS")
print(85*'@')

for i in range (1,10):
    if i is 6:
        print("Nilai i adalah",6)
        # break : mengakhir for ; bisa pakai break, kalaau break dia melanjutkan sampai ke bawah nya 
        # bisa pakai fungsi continue dia melanjutkan dari atas sampenya bawah sampe habis 
        #  
        continue    
        print("cek bro 1")
    print('Nilai saat ini adalah',i)
    
else:
    print('akhir dari loop')

print('print diluar loop')

print(85*'@')
print("Program Pass")
print(85*"@")

for i in range (1,10):
    if i is 6:
        print("Nilai i adalah",6)
        pass #tidak melakukan apapun, melanjutkan saja sampe akhir
        print("cek bro 1")
    print('Nilai Saat ini adalh',i)
else:
    print('akhir dari loop')
