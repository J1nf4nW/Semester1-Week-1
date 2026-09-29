"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Jinfan Wang
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
monthly_savings = input("Please enter the monthly amount you want to save in £X.XX:")
try:
    monthly_savings = float(monthly_savings)
    if monthly_savings >= 0.00:
        yearly_savings = monthly_savings * 12
        print(f"By the end of the year you will have saved £{yearly_savings:.2f}")
        total_savings = 1.08 * yearly_savings
        print(f"With a 0.8% interest your total amount by the end of the year by saving £{monthly_savings:.2f} every month is £{total_savings:.2f}")
    else:
        print("Invalid amount")
except:
    print("Invalid amount")


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).
