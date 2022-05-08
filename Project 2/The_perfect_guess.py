import random
randNumber=random.randint(1, 100)
Userguess=None
guessess=0
while(Userguess!=randNumber):
    Userguess=int(input("Enter the number!"))
    guessess+=1
    if Userguess==randNumber:
        print("You are right!")
    elif(Userguess>randNumber):
        print("You are wrong! Please enter smaller number")
    else:
        print("You are wrong! Please enter larger number")
print(f"You have guessed in {guessess} guessess")

with open("another.txt") as f:
    highscore=int(f.read())
if highscore>guessess:
    print("You have broken the highscore")
    with open("another.txt","w") as f:
        f.write(str(guessess))



