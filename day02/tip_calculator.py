print("Welcome to the tip calculator!")
bill = float(input("Enter the total bill: $ "))
tip = int(input("Enter what % of your bill you want to pay as tip (10, 12, 15): "))
people = int(input("Enter number of people sharing the bill: "))
bill_with_tip = bill * (1 + tip / 100)
pay = bill_with_tip / people
print(f"Share for each person is: {pay}")
