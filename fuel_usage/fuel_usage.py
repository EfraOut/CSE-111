"""
Many vehicle owners record the fuel efficiency of their vehicles as
a way to track the health of the vehicle. If the fuel efficiency of
a vehicle suddenly drops, there is probably something wrong with the
engine or drive train of the vehicle. In the United States, fuel
efficiency for gasoline powered vehicles is calculated as miles per
gallon. In most other countries, fuel efficiency is calculated as
liters per 100 kilometers.
"""
def main():
    # Get an odometer value in U.S. miles from the user.
    start_odometer = int(input('Enter the first odometer reading',
    '(miles): '))

    # Get another odometer value in U.S. miles from the user.
    end_odometer = int(input('Enter the second odometer reading',
    '(miles): '))

    # Get a fuel amount in U.S. gallons from the user.
    fuel = float(input('Enter the amount of fuel used (gallons): '))

    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(start_odometer, end_odometer, fuel)

    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)

    # Round the miles per gallon to one digit after the decimal.
    print(f'{mpg:.1f} miles per gallon')

    # Round the liters per 100 km to two digits after the decimal.
    print(f'{lp100k:.2f} liters per 100 kilometers')


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    return (end_miles - start_miles) / amount_gallons


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    return 235.215 / mpg


main()