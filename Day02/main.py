print("Welcome to the tip calculator.")
bill = input("What was the total bill?\n")
percentage = input("What percentage tip would you like to give? 10, 12, or 15?\n")
people = input("How many people to split the bill?\n")

amount = round((float(bill) + (float(bill) * int(percentage) / 100)) / int(people),2)


print(f"Each person should pay: ${amount}")12