print("Welcome to my computer quiz")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    quit()

print("Alright!! Lets do this :)")
score = 0

answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource identifier":
    print('You got it right')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower == "random access memory":
    print('You got it right')
    score += 1
else:
    print("Incorrect!")

answer = input("What many Gigabytes are in a Terabyte? ")
if answer == "1000":
    print('You got it right')
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
    print('You got it right')
    score += 1


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%. ")







