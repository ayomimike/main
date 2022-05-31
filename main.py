import random

# Players
user = 0
computer = 0

options = ["R", "P", "S"]

while True:
    user_input = input("Type Rock, Paper, Scissors or Q to quit: ")
    if user_input == "Q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Rock: 0, Paper: 1, Scissors: 2

    computer_pick = options[random_number]
    print("Computer Picked", computer_pick + ".")

    if user_input == "R" and computer_pick == "R":
        print("You won!")
        user += 1
    elif user_input == "P" and computer_pick == "P":
        print("You won!")
        user += 1
    elif user_input == "S" and computer_pick == "S":
        print("You won!")
        user += 1
    else:
        print("You lost!")
        computer += 1

print("You won", user, "times.")
print("Computer Won", computer, "times.")
print("Thanks for playing and Goodbye")