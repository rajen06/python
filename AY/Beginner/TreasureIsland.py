print("Welcome to Treasure island.\nYour mission is to find treasure.\n")
direction_chosen = input("You're at cross road. Where do you want to go?\n   Type \"left\" or \"right\"\n")
if direction_chosen == "left":
	option_taken = input("You've come o a lake. there is an island in the middle of the lake.\n   Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
	if option_taken == "wait":
		option_taken = input("You arrive at island unharmed. there is a house with 3 doors.\n   One red, one yellow and one blue. Which colour do you choose?\n")
		if option_taken == "red":
			print("Burned by fire. Game over!!")
		elif option_taken == "blue":
			print("Eaten by beasts. Game over!!")
		elif option_taken == "yellow":
			print("You Win!")
		else:
			print("Game over!!")	
	else:
		print("Attacked by trout. Game over")
else:
	print("Fall into a hole. Game Over!\n")
