# project menebak angka

import random # sudah ada di python dan memungkinkan anda menggunakan fitur di sini

#print(random.randrange(start,stop))
#r= random.randint(-5,11) # nda masuki nanti 11 batas ji
#print(r)

top_of_range = input("Type a number = ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

#random_number = random.radint(awal,akhir)
random_number = random.randint(0,top_of_range)
guesses = 0
#ingat awalnya ini angka berjalan, dari nol
print(random_number)

#while True:
    #print("Tim") ingatt ini bakal berjalan terruuus dan nda bakal berhenti karena kondisinya itu True, untuk kasi berhenti hanya diberhentikan secara manual
    #break --> inimi ada break, jadi klo misal sdh di jalankan program dibawah perintah while, maka satu baris akan na berhentikanki bgitue

while True:
    guesses +=1
    user_guess = input("Make a guess :")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
            print("You were above the number")
    else:
            print("You were below the number")
# we kdong klo minta terus ki guess ctrl+c saja biar kembli
    print("You got it in", guesses,"Guesses")