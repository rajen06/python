# list = [1, 2, 3, 4, 5]

# new_list = [n+1 for n in list]
# print(new_list)

# name = "Raj"

# new_list = [letter for letter in name]
# print(new_list)


# range_list = [n*2 for n in range(1, 5)]
# print(range_list)

# names = ["Raj", "John", "Jane", "Jim", "Jill"]
# new_list = [name.upper() for name in names if len(name) > 3]
# print(new_list)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [n for n in numbers if n % 2 == 0]
# print(result)


# with open("file1.txt") as file1:
#     file1_data = file1.readlines()
#     file1_data = [int(n) for n in file1_data]
#     print(file1_data)
    
# with open("file2.txt") as file2:
#     file2_data = file2.readlines()
#     file2_data = [int(n) for n in file2_data]
#     print(file2_data)

# result = [n for n in file1_data if n in file2_data]
# print(result)


# import random

# names = ["Raj", "John", "Jane", "Jim", "Jill"]

# student_scores = {student:random.randint(1, 100) for student in names}
# print(student_scores)

# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word:len(word) for word in sentence.split()}
# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# weather_f = {day:temp*9/5+32 for (day, temp) in weather_c.items()}
# print(weather_f)

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Loop through a data frame

# for (index, row) in student_data_frame.iterrows():
#     print(row.student)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in user_input]
print(output_list)


