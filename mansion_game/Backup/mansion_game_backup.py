"""
Filename: mansion_game.py
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
"""
import random

DESCRIPTION_INDEX = 0
inventory = []

def print_intro():
    print('Please enter the number of the room that you wish to enter.')
    print('Your mission: Leave the Mansion ALIVE')
    print('Good luck!')


def get_rooms():
    """
    Creates the dictionary where the game happens
    """
    rooms = {
        'entrance' : ['This is the entrance', "Main Door" ,'Upper Floor', 'Main Floor', 'Basement'],
        'upper floor' : ['This is the upper floor', "Master's Bedroom", 'Library', "Child's Bedroom", 'Entrance'],
        'main floor' : ['This is the main floor', 'Bathroom', "Servant's quarters", 'Entrance'],
        "master's bedroom" : ['This is the master\'s bedroom', 'Upper Floor', "Interact"],
        'library' : ['This is the library', "Child's Bedroom", 'Hallway', 'Stairway', 'Upper Floor'],
        "child's bedroom" : ['This is the child\'s bedroom', 'Library', 'Stairway', 'Upper Floor'],
        'stairway' : ['This is the stairway', "Child's Bedroom", 'Library', "Servant's Quarters", "Hallway", "Kitchen"],
        'hallway' : ['This is the hallway', 'Library', 'Stairway', "Attic"],
        'attic' : ['This is the attic', 'Hallway', 'Rooftop'],
        'rooftop' : ['This is the rooftop', 'Attic', 'Jump Out', "Grab Horseshoe"],
        "servant's quarters" : ['This is the servant\'s quarters', 'Main Floor', 'Bathroom', 'Break Room'],
        'break room': ['This is the break room', "Servant's Quarters", 'Kitchen', 'Move Bookshelf'],
        'secret room': ['This is the secret room', "Give item"],
        'bathroom':  ['This is the bathroom', 'Main Floor', "Servant's Quarters"],
        'kitchen' : ['This is the kitchen', "Eat", 'Stairway', 'Break Room'],
        'basement' : ["You fell to your dead", "You Died"],
        'main door' : ["The doornknob electrocuted you", "You Died"],
        'interact' : ["The person killed you", "You Died"],
        'eat' : ["The food was poisonus", "You Died"],
        'jump out' : ["You tried to fly, and failed", "You Died"],
        'good ending' : ['You escaped the mansion!'],
        'bad ending' : ['The room crushed you'],
        }
    return rooms


def explore_mansion(room_list):
    """
    Parameters:
        room_list : The list inside the room (dictionary values)
    Return: The key for the next room
    """
    print(room_list[DESCRIPTION_INDEX].upper())

    # Print all the available options for the current room
    for i in range(1, len(room_list)):
        print(f'{i}. {room_list[i]}')

    # Using the user's input as a key for the next room
    i = int(input('Where do you want to go?\n'))
    if i < 1 or i > len(room_list):
        raise IndexError
    room_key = room_list[i].lower()

    return room_key


def check_dead(room, rooms_dict):
    """
    Checks if the selected option leads to death
    Parameters:
        room: The current room (dictionary key)
        room_list : The list inside the room (dictionary values)
    Return: Whether the player is dead or not
    """
    alive = True

    if room in ('basement', 'main door', 'interact', 'eat', 'jump out'):
        for options in rooms_dict[room]:
            print(options)
        print('Maybe next time')
        alive = False

    return alive


def apply_special_conditions(room, room_list):
    """
    Since some "rooms" are not exactly rooms, this functions
    takes actions on those special rooms
    Parameters:
        room: The current room to check (the dictionary key)
        room_list : The list inside the room (dictionary values)
    Return: The room where the player should be after the special
            condition finishes
    """
    if room == 'move bookshelf': # Finding the Secret Room
        print('You found the secret room!')
        room_list.pop()
        room_list.append('Secret Room')
        room = 'break room'
    elif room == 'grab horseshoe': # Adding 'Horseshoe' to the inventory
        print('You grabbed the horseshoe!!!!!!!!!!!!!!!!!')
        inventory.append('Horseshoe')
        room_list.pop()
        room = 'rooftop'
    elif room == 'give item': # Giving the item
        print('Desciption text (you basically found someone and wants an item)')
        if inventory == ['Horseshoe']: # Guess My Number begins
            print('Well Done, you may continue')
            room = guess_number()
        else: # Allowing the player to find the item
            print('I WANT MY ITEM')
            room = 'break room'

    return room


def guess_number():
    """
    "Guess my number" game. This is the final room and it determines
    if the player wins or loses
    """
    print('Desciption text, maybe a villan rant or something like that')
    number = random.randint(1, 10)
    attempts = 0
    guess = int(input('Guess my number, I dare you!\nIt is between 1 and 10\nYou only have 3 attempts\n'))
    
    while attempts < 2:
        if guess < number:
            attempts += 1
            print("Higher")
            print('Used attempts:', attempts)
            guess = int(input('Can you guess my number?\n'))
        elif guess > number:
            attempts += 1
            print('Lower')
            print('Remaining attempts:', attempts)
            guess = int(input('Can you guess my number?\n'))
        else:
            print('You got it right!\nYou may continue')
            print('THE END')
            room = 'good ending'
            break
    if attempts == 2:
        room = 'bad ending'

    return room


def print_ending(room, rooms_dict):
        for options in rooms_dict[room]:
            print(options)


def main():
    print_intro()
    alive = True
    rooms = get_rooms() # This variable stores the dictionary
    room_list = rooms['entrance'] # You have to start somewhere, right?
    while alive:
        try:
            room_key = explore_mansion(room_list)

            # Cheking if the game is over
            alive = check_dead(room_key, rooms)
   
            # Some rooms have special conditions (grabbing an item, giving an item or moving something)
            # This function takes care of those conditions
            if room_key in ('grab horseshoe', 'move bookshelf', 'give item'):
                room_key = apply_special_conditions(room_key, room_list)
            if room_key in ('good ending', 'bad ending'):
                print_ending(room_key, rooms)
                alive = False

            # Get the item for the dictionary to be used continuing the loop           
            room_list = rooms[room_key]
            
        except KeyError as key_err:
            print(f'Room {key_err} does not exist')
            print('Maybe you should try to access an actual room?')
        except ValueError:
            print('Please type the number of the room')
        except IndexError:
            print('That is not a room, you know?')
            print('Maybe you should try to access an actual room?')

    print('Thank you for playing!')


if __name__ == '__main__':
    main()