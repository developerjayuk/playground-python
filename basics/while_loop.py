import random

number = random.randint(1, 10)
user_input = input("Would you like to play? (Y/n) ")

while user_input != "n":
    user_number = int(input("Guess our number: "))

    if user_number == number:
        print("You are correct!!")
        break
    elif abs(number - user_number) == 1:
        print("You were so close!")
    else:
        print("Keep guessing...")
