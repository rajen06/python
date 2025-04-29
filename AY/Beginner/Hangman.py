import random

# List of words for the game
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", 
         "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon"]

def get_word():
    """Randomly selects a word from the list."""
    return random.choice(words)

def display_word(word, guesses):
    """Displays the word with guessed letters revealed and others hidden."""
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def main():
    word = get_word()  # Get a random word
    correct_guesses = []
    incorrect_guesses = []
    max_attempts = 6  # Maximum allowed incorrect guesses

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while True:
        # Display the current state of the word
        print("\n" + display_word(word, correct_guesses))
        
        # Display guessed letters and remaining attempts
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")
        print(f"Attempts remaining: {max_attempts - len(incorrect_guesses)}")
        
        # Check for win condition
        if set(correct_guesses) == set(word):
            print("Congratulations, you guessed the word!")
            break
        
        # Check for loss condition
        if len(incorrect_guesses) >= max_attempts:
            print("You lose! The word was:", word)
            break

        # Get user input
        guess = input("Enter a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in correct_guesses or guess in incorrect_guesses:
            print("You already guessed that letter.")
        elif guess in word:
            print("Correct!")
            correct_guesses.append(guess)
        else:
            print("Incorrect.")
            incorrect_guesses.append(guess)

if __name__ == "__main__":
    main()
