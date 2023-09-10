import random

def roll_dice():
    return random.randint(1,6)
while True:
    user = input("Do you want to roll the dice?: ")
    if user == "yes":
        result  = roll_dice()
        print("You rolled ", result)
    elif user == "no":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Enter again please")