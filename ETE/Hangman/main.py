from hangman_art import logo, stages
from hangman_words import word_list
import random

chosen_word = random.choice(word_list).lower()
print("word is " +chosen_word)
display = ""

for letter in chosen_word:
    display += "_"

print(logo)
print(display + "\n")



lives = len(stages) -1 
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed letter {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display = display[:position] + guess + display[position+1:]
           

    if guess not in display:
        print(f"You guessed {guess}, that's not in word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lost!")
    
    print(display + "\n")
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You won!")

        




   
