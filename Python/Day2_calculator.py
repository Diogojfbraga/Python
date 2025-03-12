print("Click 'Run' to run the final project you will build")
print("Welcome to the Tip Calculator!")

# Get bill amount
bill = float(input("What was the total bill? $"))

# Get tip percentage
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? ")) / 100

# Get number of people splitting the bill
num_people = int(input("How many people to split the bill? "))

# Calculate total bill including tip
total_bill = bill + (bill * tip_percent)

# Calculate amount each person should pay
amount_per_person = total_bill / num_people

# Display the result formatted to 2 decimal places
print(f"Each person should pay: ${amount_per_person:.2f}")
