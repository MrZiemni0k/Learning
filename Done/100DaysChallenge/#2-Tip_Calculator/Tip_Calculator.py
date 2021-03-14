print("Welcome to the tip calculator.")
total = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give?\
 10%, 12%, 15%? "))
num_people = int(input("How many people to split the bill? "))
split_bill = "{:.2f}".format(round((total+(total*percentage))/num_people,2))
print(f"Each person should pay: ${split_bill}")