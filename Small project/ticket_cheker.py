print("Welcome to Water Park !! ")
height = int(input("Enter your hieght here in cm ? "))
age = int(input("Enter your age here :  "))
bill =  0

if height >= 120 :
    print ("You can purchase a ticket ")
    if age < 10:
        bill = 100
        print("Ticket price should be  = 100Rs")
    elif age < 15:
        bill = 150
        print("Ticket price should be  = 150Rs")
    else:
        bill = 200
        print("Ticket Price should be = 200 Rs")

        want_photos = input("want photos if yes Enter Y if not then enter N ")
        if want_photos == "Y":
            totalBill= bill + 50
            print (f"You total bill is {totalBill}")

        else:
            print (f"Your total bill is {bill} ")
else :
    print("Sorry, you are not able to purchase a ticket ")


