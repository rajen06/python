print("Welcome to Band Name Generator!!\n")
total_bill= int(input("Total Bill Amount!!\n"))
tip_percent= int(input("Tip Percentage!!\n"))
tip_amount= total_bill*tip_percent/100
people = int(input("How many people to split the bill!!\n"))
payable_amt = total_bill + tip_amount
split_amount = payable_amt/people
print("The total bill amount is: ",total_bill)
print("The tip amount is: ",tip_amount)
print("The split amount is: ",round(split_amount,2))