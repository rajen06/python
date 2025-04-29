import random

# Choices list for mapping
choices = ["Rock", "Paper", "Scissors"]

# Get user choice
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Ensure the user's choice is valid
if your_choice < 0 or your_choice >= 3:
    print("You typed an invalid number, you lose!\n")
else:
    # Get computer choice
    computer_choice = random.randint(0, 2)
    print(f"You chose: {choices[your_choice]}")
    print(f"Computer chose: {choices[computer_choice]}\n")

    # Game logic
    if your_choice == computer_choice:
        print("It's a draw!")
    elif (your_choice == 0 and computer_choice == 2) or \
         (your_choice == 1 and computer_choice == 0) or \
         (your_choice == 2 and computer_choice == 1):
        print("You Win!")
    else:
        print("You lose!")
