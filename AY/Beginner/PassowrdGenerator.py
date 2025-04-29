import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Add random letters
for char in range(1, num_letters + 1):
    password_list.append(random.choice(letters))

# Add random symbols
for char in range(1, num_symbols + 1):
    password_list.append(random.choice(symbols))

# Add random numbers
for char in range(1, num_numbers + 1):
    password_list.append(random.choice(numbers))

# Shuffle the list for randomness
random.shuffle(password_list)

# Combine list into a string
password = "".join(password_list)

print(f"Your password is: {password}")
