# Getting input from the user
bill_before_tip = float(input("What is your total bill? "))
tip_percentage = float(input("How much do you want to tip (as a percentage)? "))
number_of_people = int(input("How many people are paying? "))

# Calculating the tip amount and the actual bill
tip_amount = bill_before_tip * (tip_percentage / 100)
actual_bill = tip_amount + bill_before_tip

# Splitting the bill
split_bill = actual_bill / number_of_people

# Displaying the result
print(f"Your bill before tip is ${bill_before_tip:.2f}, and you selected a tip percentage of {tip_percentage}%.")
print(f"This makes your total bill ${actual_bill:.2f}!")
print(f"Each person should pay: ${split_bill:.2f}")
