"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Calculate shopping cart
by loading from other files
Extra Mile:
1. Added dollar signs on the output
2. Added special character surrounding the 'thank you' message
3. Added a try, except block catching an IndexError
"""
import csv
from datetime import datetime


def read_products(filename):
    """
    Open the products.csv and create a dictionary based on its content
        return: a dictionary <product_index, (name, price)>
    """
    # Useful indexes from the products.csv file
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    products = {}

    try:
        with open(filename, 'rt') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            # Take all the information and make it into a dictionary
            # key: the product index
            # values: The corresponding name of the item (str) and
            # the price of that item (float)
            for row in reader:
                key = row[PRODUCT_INDEX]
                name = row[NAME_INDEX]
                price = float(row[PRICE_INDEX])
                products[key] = name, price
                
        # Return the dictionary     
        return products
        
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        print('Please select a valid file')
    except KeyError as key_err:
        print(key_err)


def read_request():
    """
    Opens the request.csv file and create a list based on
    its content
        returns: a list with tuples [(product_index, quantity)]
    """
    #Useful indexes for the request.csv fie
    PRODUCT_INDEX = 0
    QUANTITY = 1
    request = []

    try:
        with open('request.csv', 'rt') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                product = row[PRODUCT_INDEX]
                quantity = int(row[QUANTITY])
                request.append((product, quantity))

        return request
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        print('Please select a valid file') 


def compute_receipt():
    """
    Computes from both csv files the
    receipt can be created
        returns: a tuple
    """
    try:
        products = read_products('products.csv')
        requests = read_request()

        # Variables to compute the content for the receipt
        total_quantity = 0
        subtotal = 0
        total = 0
        current_date_and_time = datetime.now()
        for element in requests:
            request = element[0]
            quantity = int(element[1])
            product_name = products[request][0]
            price = float(products[request][1])
            print(f'{product_name}: {quantity} @ {price}')

            # Making the calculations
            total_quantity += quantity
            price *= quantity
            subtotal += price
            tax = subtotal * 0.06
            total = subtotal + tax
        items = (total_quantity, subtotal, tax, total, current_date_and_time)

        return items

    except (FileNotFoundError, PermissionError) as e:
        print(e)
        print('Please select a valid file') 
    except KeyError as key_err:
        print(key_err)


def print_receipt():
    """
    Prints the receipt by extracting all the 
    information from the compute_receipt function
        returns: nothing
    """
    try:
        # Useful indexes from products.csv
        QUANTITY_INDEX = 0
        SUBTOTAL_INDEX = 1
        TAX_INDEX = 2
        TOTAL_INDEX = 3
        DATE_INDEX = 4

        items = compute_receipt()

        # Create new variables from each
        # element in the tuple       
        quantity = items[QUANTITY_INDEX]
        subtotal = items[SUBTOTAL_INDEX]
        tax = items[TAX_INDEX]
        total = items[TOTAL_INDEX]
        current_date_and_time = items[DATE_INDEX]

        # Printing the receipt
        print()
        print(f'Total items: {quantity}')
        print(f'Subtotal: ${subtotal:.2f}')
        print(f'Sales tax: ${tax:.2f}')
        print(f'Total: ${total:.2f}')
        print()
        print('｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡')
        print('Thank you for shopping at The Store Name!')
        print(f"{current_date_and_time:%a %b %d %I:%M %p %Y}")
        print('｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡★｡+ﾟ☆ﾟ+｡')

    except IndexError as ind_err:
        print(f'Error: {ind_err}')


def main():
    print('The Store Name\n')
    print_receipt()


if __name__ == '__main__':
    main()