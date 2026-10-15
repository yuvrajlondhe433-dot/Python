age = int(input("Enter your age: "))

if age < 5:
    print("Ticket price: Free")
elif age < 18:
    print("Ticket price: Rs. 50")
elif age < 60:
    print("Ticket price: Rs. 100")
else:
    print("Ticket price: Rs. 70")
