"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days.
On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.
"""
from datetime import datetime as dt

# Looping until the user is done shopping
list1 = []
item = 0
quantity = 0
user_input = ''
print('When you\'re done shopping, type DONE')
while user_input.lower() != 'done':
    item = float(input('What is the price? '))
    quantity = float(input('How many? '))
    item *= quantity
    list1.append(item)
    user_input = input('Do you wanna keep shopping? ')

# Getting the subtotal and retrieving the weekday to see if the shop is on discount
subtotal = sum(list1)
current_date = dt.now()
weekday = current_date.weekday()

if subtotal >= 50 and (weekday == 1 or weekday == 2): #Discount applies and user buy enough to apply
    print(f'Subtotal: ${subtotal:.2f}') 
    discount = float((subtotal / 100) * 10)
    print(f'Discount amount: ${discount:.2f}')
    subtotal = float(subtotal - discount)
    sales_tax = float(subtotal / 100) * 6
    print(f'Sales Taxes: ${sales_tax:.2f}')
    print(f'Total: ${(subtotal + sales_tax):.2f}')
elif (subtotal <= 50 and weekday == 1) or (subtotal <= 50 and weekday == 2): # Discount applies but user didn't buy enough to apply
    print(f'Subtotal: ${subtotal:.2f}') 
    print(f'You need to buy ${(50 - subtotal):.2f} more if you want to get the discount')
    sales_tax = float(subtotal / 100) * 6
    print(f'Sales Taxes: ${sales_tax:.2f}')
    print(f'Total: ${(subtotal + sales_tax):.2f}')
else: #No Discount :(
    print(f'Subtotal: ${subtotal:.2f}') 
    sales_tax = float(subtotal / 100) * 6
    print(f'Sales Taxes: ${sales_tax:.2f}')
    print(f'Total: ${(subtotal + sales_tax):.2f}')