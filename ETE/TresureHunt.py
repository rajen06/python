print(
    "*******************************************************************************\n"
)
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")
print("You're at a cross road. Where do you want to go?\n")
choice = input('Type "left" or "right"\n').lower()
if choice == "left":
    print("You have come to a lake. There is an island in the middle of the lake.\n")
    choice = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice == "wait":
        print(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\n"
        )
        choice = input("Which colour do you choose?\n").lower()
        if choice == "red":
            print("It's a room full of fire. Game Over.")
        elif choice == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.\n")

else:
    print("You fell into a hole. Game Over.")
