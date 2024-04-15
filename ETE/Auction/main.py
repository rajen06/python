from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bids):
  highest_bid = 0
  highest_bidder = ""
  for bidder in bids:
    bid = bids[bidder]
    if bid > highest_bid:
      highest_bid = bid
      highest_bidder = bidder
  print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}.")


while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    continue