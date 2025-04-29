import string

def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    shift %= 26  # Normalize shift
    alphabet = string.ascii_lowercase
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            new_position = (alphabet.index(char) + shift) % 26
            new_char = alphabet[new_position]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char
    return result

while True:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'exit' to quit:\n")
    if choice == "exit":
        break
    if choice not in ["encode", "decode"]:
        print("Invalid choice. Please type 'encode', 'decode', or 'exit'.")
        continue
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    print(f"Result: {caesar(text, shift, choice)}")
