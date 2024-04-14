import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n" ))
if your_choice not in [0,1,2]:
    print("Invalid choice!")
    exit()
print(game_images[your_choice])
computer_choice = random.randint(0,2)
print(f"Computer chose: \n {game_images[computer_choice]} \n")


if your_choice == computer_choice:
    print("It's a tie!")
elif your_choice == 0 and computer_choice == 2:
    print("You win!")
elif your_choice == 2 and computer_choice == 0:
    print("You lose!")
elif your_choice == 1 and computer_choice == 0:
    print("You win!")
elif your_choice == 0 and computer_choice == 1:
    print("You loose!")
elif your_choice == 1 and computer_choice == 2:
    print("You lose!")
elif your_choice == 2 and computer_choice == 1:
    print("You win!")