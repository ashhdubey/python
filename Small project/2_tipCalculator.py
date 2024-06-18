print("Welcome to tip calculator!")

totalBill = float(input("What was your total bill ? :"))
percentage = int(input("What Percentage tip you would like to give ? 5 ,10, 15,20  ? :"))
people = int(input("How many people to split the bill ?"))
tip = round(((totalBill*percentage)/100)+totalBill,2)
split = tip/people

print(f"Your Total bill was {totalBill} Rs")
print(f"The {percentage} of the {totalBill} Rs is {tip}")
print(f"each should give {split} Rs")




