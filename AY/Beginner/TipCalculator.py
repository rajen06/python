print("Welcome to the tip calculator!\n")
total_bill = int(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split he bill?\n"))
individual_share = (total_bill + (total_bill * tip) / 100) / people
print(f"Each person should pay : ${individual_share:.2f}") 
