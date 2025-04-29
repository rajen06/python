# Guess Number Game
# Output:
# Welcome to the umber Guessing Game
# I'm thinking of a number between 1 and 100.
# Pssst, the correct answer is 45
# Choose a difficulty. Type 'easy' or 'hard': easy
# You have 10 attempts remaining to guess the number.
# Make a guess: 50
# Too high.
# You have 9 attempts remaining to guess the number.
# Make a guess: 40
# Too low.


import random

def set_difficulty():
    """Sets the number of attempts based on the difficulty level."""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return 10 if difficulty == "easy" else 5

def guess_number():
    """The main function to play the Number Guessing Game."""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    correct_answer = random.randint(1, 100)
    
    attempts = set_difficulty()
    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))
        if guess == correct_answer:
            print(f"Congratulations! The answer was {correct_answer}.")
            return
        elif guess > correct_answer:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

    print(f"Sorry, you've run out of attempts. The correct answer was {correct_answer}.")

guess_number()

