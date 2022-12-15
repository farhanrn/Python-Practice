# program quizz

print("Welcome to my computer quizz!")

playing = input("Do you want to play? (yes/no)  : ")
# perhatikan huruf besar dan kecilnya sobatt

if playing.lower() != "yes":
    quit()
# ingat .lower() fungsi nya untuk menjadikan yg ditampilkan jadi keciil
# jadi biarpun klo ada huruf besar diantaranya assala yes ji bacanya tetap diambil karena ada lower

print("Okay! Let's play :)")
score = 0 # --> untuk melacak berapa banyak pertanyaan benar dan berapa skor nya

answer = input("What does CPU stand for?  ")
if answer.lower() == "central processing unit":
#samaji kasusnya playing, jadi ini nanti huruf kecl semua
    print("Correct!")
    score += 1
else:
     print("Incorrect!!")

answer = input("What does GPU stand for?  ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
else:
     print("Incorrect!!")

answer = input("What does RAM stand for?  ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
     print("Incorrect!!")

answer = input("What does PSU stand for?  ")
if answer.lower() == "power supply":
    print("Correct!")
    score+=1
else:
     print("Incorrect!!"  )

print(" You got "  + str(score)+    " Questions correct! ")
# ingat penambahan striingg kalo score itu kan variabel operator
# makanya di casting ke string dengan cara str(score) supaya bisa disatukan
# score itu angkaa (integer)
# dengan string yang laiiin 
# mantaapp
print(" You got "  + str((score/4) + 100)+    " % ")