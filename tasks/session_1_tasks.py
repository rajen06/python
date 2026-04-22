# Task : Session 1


### Q1 :- Print the given strings as per stated format.

# **Given strings**:
"""
```
"Data" "Science" "Mentorship" "Program"
"By" "CampusX"
```
**Output**:
```
Data-Science-Mentorship-Program-started-By-CampusX
```

Concept- [Seperator and End]
"""

# Write your code here
print("Data", "Science", "Mentorship", "Program", sep='-', end="-started-")
print( "By", "CampusX", sep="-")

"""### Q2:- Write a program that will convert celsius value to fahrenheit."""

# Write your code here
input_in_celcius = int(input('please enter celcius value '))
convert_to_fah =  int((input_in_celcius * 9/5) + 32)
print('Coverted to Fahrenheit', convert_to_fah)

"""fahrenheit### Q3:- Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax."""

# Write your code here
num1 = int(input('first number '))
num2 = int(input('Second number '))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After Swapping first number ", num1)
print('After swapping second number ', num2)

"""### Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input."""

# Write your code here
# √((x2 - x1)² + (y2 - y1)²)
coord1 = input("Enter first coordinate (x1,y1): ")
x1_str, y1_str = coord1.split(",")
x1 = float(x1_str)
y1 = float(y1_str)

coord2 = input("Enter second coordinate (x2,y2): ")
x2_str, y2_str = coord2.split(",")
x2 = float(x2_str)
y2 = float(y2_str)

dx = x2 - x1
dy = y2 - y1

euclidean_dist = (dx ** 2 + dy ** 2) ** 0.5
print('euclidean_dist ',round(euclidean_dist, 4))

"""### Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

"""

# Write your code here
# Input values
# Formuala interest = p * r * t / 100
principal = float(input("Enter principal amount (P): "))
rate = float(input("Enter annual interest rate in % (R): "))
time = float(input("Enter time in years (T): "))

interest = (principal * rate * time) / 100
print('Simple interest is ', round(interest, 2))

"""### Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2




"""

# Write your code here
# d + c = heads
# c = heads - d
# 4d + 2c = legs
# 4d + 2(heads - d) = legs
#  4d + 2*heads - 2d = legs
#  2d = legs- (2 * heads)
#  d = (legs - (2* heads)) / 2
heads = int(input('Enter value of heads'))
legs = int(input('Enter value of legs'))

dogs = int((legs - (2*heads))/ 2)
cats = heads - dogs

print('Total dogs ', dogs)
print('Total cats ', cats)

"""### Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user."""

# Write your code here
#  sum of squares natural numbers = n(n + 1) (2n+1) / 6

num = int(input('user input '))
result = (num * (num + 1) * (2 * num + 1)) // 6
print('Result is ', result)

"""### Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user."""

# Write your code here
#  formula nth_term_series = a + (n-1) * (b-a), Where a is first term and b is second term

a = int(input("Enter first term: "))
b = int(input("Enter second term: "))
n = int(input("Enter which term (n): "))

result = a + (n-1) * (b-a)
print('Result is ', result)

"""### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

# Write your code here
# assume we have a as numerator and b as denominator for fraction 1 and c as numerator and d as denominator for fraction 2
#  formula would be = (a*d + c*b) / (b *d)

a = int(input("Enter numerator of first fraction: "))
b = int(input("Enter denominator of first fraction: "))
c = int(input("Enter numerator of second fraction: "))
d = int(input("Enter denominator of second fraction: "))


result_numerator = (a*d + c*b)
result_denominator = b*d

print('Result is ', result_numerator, "/", result_denominator)

"""### Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.



Input:<br>
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
<br><br>
Dimensions of the glass<br>
h = 3cm, r = 1cm
"""

# Write your code here
# Tank is cuboid so voluma is H * L * B
# Glass is cylinderical so voumer is π*r**2*h

H = float(input("Enter height of the tank (in cm): "))
L = float(input("Enter length of the tank (in cm): "))
B = float(input("Enter breadth of the tank (in cm): "))

h = float(input("Enter height of the glass (in cm): "))
r = float(input("Enter radius of the glass (in cm): "))

tank_volume = H * L * B
pi = 3.1416
glass_volume = pi * (r ** 2) * h

num_glasses = round(tank_volume / glass_volume)

print('Result is ', num_glasses)