# Shopping Discount System
#
# In this project, you will create a program that simulates a simple shopping discount system. The system
# will ask for the total purchase amount and determine the discount based on certain conditions.
# The program will then calculate and display the final amount
# after applying the discount.
#
# Project Requirements:
# Input:
# The user enters the total amount of their purchase.
# The user enters whether they are a member of the store (yes or no).
total_amount = int(input('Enter total purchase amount: '))
member = input('Are you a member? (yes/no): ')
print()
# Discount Rules:
# If the total purchase amount is greater than $500 and the user
# is a member, apply a 20% discount.
if total_amount > 500 and member == 'yes':
    discount = 0.2
# If the total purchase amount is greater than $500
# and the user is not a member, apply a 10% discount.
elif total_amount > 500 or member == 'no':
    discount = 0.1
# If the total purchase amount is between $200 and $500 (inclusive),
# apply a 5% discount regardless of membership.
elif 200 <= total_amount <= 500:
    discount = 0.05
# If the total purchase amount is less than $200, no discount is applied.
else:
    discount = 0
# Output:
# Display the original amount, the discount percentage applied, and the final amount after discount.
final_amount = total_amount * (1 - discount)
discount = int(discount * 100)
print(f'Original Amount: ${total_amount:.2f}')
print(f'Discount Applied: {discount:d}%')
print(f'Final Amount: ${final_amount:.2f}')
# Output Example:
#
# Enter total purchase amount: 550
# Are you a member? (yes/no): yes
#
# Original Amount: $550.00
# Discount Applied: 20%
# Final Amount: $440.00