import random

target = random.randint(1,100)

while True:
    UserChoice = input("Guess the Number or Quit(Q): ")
    if(UserChoice == "Q"):
        break
    UserChoice = int(UserChoice)
    if(UserChoice == target):
        print("Success You got the number.")
        break
    elif(UserChoice < target):
        print("Oops!! your number is too small...")
    else:
        print("Oops!! Your number is too big...")

print(" ---GAME OVER---")
