# Blackjack game
# Output messages
# Your cards: [9,10]
# Computer's first choice: 8
# type 'y' to get another card, type 'n' to pass: n
# Your final hand: [9, 10]    
# Computer's final hand: [8, 10]
# You Win
# Do you want to play a game of Blackjack? Type 'y' or 'n': y

import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]  # 10 represents face cards; 11 represents an Ace
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of a given hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    """Compares the scores to determine the winner."""
    if user_score > 21 and computer_score > 21:
        return "You both went over. It's a draw!"
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"
    elif user_score == 0:
        return "You have Blackjack. You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_blackjack(start_immediately=True):
    """The main function to play a game of Blackjack."""
    if start_immediately:
        print("Welcome to Blackjack!\n")
    user_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand[:1])  # Only reveal one card of the computer

        print(f"Your cards: {user_hand}, current score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == "y":
                user_hand.append(deal_card())
            else:
                game_over = True

    while calculate_score(computer_hand) < 17:
        computer_hand.append(deal_card())

    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    # Ask for replay after the first game
    if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
        play_blackjack(False)

# Start the game directly without asking first
play_blackjack()
