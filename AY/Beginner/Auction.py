# Secret Auction Program

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

print("Welcome to the secret auction program.")

bidders = {}

def get_bidder():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid


def find_winner(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while True:
    get_bidder()
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more_bidders == "no":
        break
    clear_screen()


find_winner(bidders)

