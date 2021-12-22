"""
Teacher: Comeau, Luc
Purpose: Get the volume of a tire and append the inputs to a text file
Author: Efrain Gomez Fajardo
Extra Mile:
1, Appending phone number if user wants to buy tires
"""
from math import pi
from datetime import datetime

date = datetime.now()
# Getting the information from the user, calculating, and displaying it.
width = int(input('Please enter the width of the tire in mm (ex 205): '))
aspect_datio = int(input('Please enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Please enter diameter of the wheel in inches (ex 15): '))
volume = (pi * (width ** 2) * aspect_datio * (width * aspect_datio + (2540 * diameter))) / 10000000000
print(f'The aproximate volume of the tire is {volume:.2f} liters')
user_input = input('Do you want to buy tires with these dimentions? (Y/N) ')

# Opening and apending to an existing file
with open('volumes.txt', 'at') as data_file:
    if user_input.lower() == 'y':
        print(f'{date:%Y-%m-%d}', file=data_file,end=', ')
        print(f'{width}, {aspect_datio}, {diameter}, {volume:.2f}', file=data_file, end=', ')
        phone_number = input('What\'s your phone number? ')
        print(phone_number, file=data_file)
    else:
        print(f'{date:%Y-%m-%d}', file=data_file,end=', ')
        print(f'{width}, {aspect_datio}, {diameter}, {volume:.2f}', file=data_file)