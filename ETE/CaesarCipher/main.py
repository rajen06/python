from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(logo + "\n")


def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = index + shift_amount
            end_text += alphabet[new_index]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}\n")
    return end_text


# def encrypt(text, shift):
#     encrypted_text = ""
#     for letter in text:
#         if letter in alphabet:
#             index = alphabet.index(letter)
#             new_index = (index + shift) % 26
#             encrypted_text += alphabet[new_index]
#         else:
#             encrypted_text += letter
#     return encrypted_text

# def decrypt(text, shift):
#     decrypted_text = ""
#     for letter in text:
#         if letter in alphabet:
#             index = alphabet.index(letter)
#             new_index = (index - shift) % 26
#             decrypted_text += alphabet[new_index]
#         else:
#             decrypted_text += letter
#     return decrypted_text

end_program = False

while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in ["encode", "decode"]:
        print("Invalid input. Please try again.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caeser(text, shift, direction)
    run_again = input("Type 'yes' to run again, type 'no' to exit:\n")
    if run_again == "no":
        print("Goodbye!")
        end_program = True

