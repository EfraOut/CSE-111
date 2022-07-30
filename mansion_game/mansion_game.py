"""
Filename: mansion_game.py
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
"""
import random
import sys
import time
from game_text import *

DESCRIPTION_INDEX = 0
inventory = []


def print_typewriter(message, time_delay_1, time_delay_2):
    """
    Prints the desired text similar to a typewriter, one letter at a time
    Parameters:
        message: The message to print
        time_delay_1: (In seconds) The time delay it will take to
        display each letter
        time_delay_2: (In seconds) the time delay between paragraphs
    Return: nothing
    Credits: Learn Learn Scratch Tutorial
    https://www.youtube.com/watch?v=2h8e0tXHfk0
    """
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != '\n':
            time.sleep(time_delay_1)
        else:
            time.sleep(time_delay_2)
    print()  # Returns pointer to the bottom


def explore_mansion(room_list):
    """
    Parameters:
        room_list : The list inside the room (dictionary values)'
        rooms_dict : The key ()
    Return: The key for the next room
    """
    print_typewriter(room_list[DESCRIPTION_INDEX], 0.01, 0.05)
    print()
    print_typewriter("Where do you want to go?", 0.1, 0.1)

    # Print all the available options for the current room
    for i in range(1, len(room_list)):
        print_typewriter(f'{i}. {room_list[i]}', 0.1, 0.1)

    # Using the user's input as a key for the next room
    i = int(input('Enter number: '))
    if i < 1 or i > len(room_list):
        raise IndexError
    room_key = room_list[i].lower()

    return room_key


def check_game_over(room, rooms_dict):
    """
    Checks if the selected option leads to death
    Parameters:
        room: The current room (dictionary key)
        room_list : The list inside the room (dictionary values)
    Return: Whether the player is dead or not
    """
    alive = True

    if room in (
        'basement', 'main door', 'investigate', 'eat', 'jump out',
        'good ending', 'bad ending'):
        print_typewriter(rooms_dict[room], 0.05, 0.05)
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

    # Finding the Secret Room
    if room == 'move bookshelf': 
        print_typewriter(
            'At the other side of the bookshelf, where a wall should be,'
             + 'there is now a secret room', 0.01, 0.05)
        room_list.pop()
        room_list.append('Secret Room')
        room_list[DESCRIPTION_INDEX] = "Aja! You knew there was something" \
                                + "weird with that bookshelf. But, what now?"
        room = 'break room'

    # Adding 'Horseshoe' to the inventory
    elif room == 'grab horseshoe':  
        print_typewriter('You grabbed the horseshoe', 0.1, 0.1)
        inventory.append('Horseshoe')
        room_list.pop()
        room_list[DESCRIPTION_INDEX] = "From here you can see that the forest" \
            + " is bigger than you thought.\n\ Looking down gives you a little bit" \
            + "of vertigo, but you can't stop thinking that you could probably make that jump."
        room = 'rooftop'

    # Giving the item for the final game to begin.
    elif room == 'give item':  
        if inventory == ['Horseshoe']:  # Guess My Number begins
            room = guess_number()
        else:  # Allowing the player to find the item
            print("Bring me the horseshoe, and then we can talk")
            room = 'break room'

    return room


def guess_number():
    """
    "Guess my number" game. This is the final room and it determines
    if the player wins or loses
    """
    while True:
        try:
            print_typewriter(
                'Alright, now that I have my horseshoe, try to guess my number.' \
                 + 'It is between 1 and 10', 0.01, 0.05)
            attempts = 1
            number = random.randint(1, 10)
            guess = int(input("Enter number "))
            while guess != number and attempts != 3:
                if guess > number:
                    print_typewriter("Try a lower number", 0.05, 0.05)
                    guess = int(input("Enter number "))
                    attempts += 1
                elif guess < number:
                    print_typewriter("Try a lower number", 0.05, 0.05)
                    guess = int(input("Enter number "))
                    attempts += 1
                elif guess == 42:
                    print_typewriter(
                        'Hi! My name is Efrain. Thank you for playing!', 0.5, 0.5)
            if guess == number:
                room = 'good ending'
                break
            elif attempts == 3:
                room = 'bad ending'
                break
        except ValueError:
            print('Enter valid number')

    return room


def main():
    print_typewriter(print_intro(), 0.01, 0.05)
    alive = True
    rooms = get_rooms()  # This variable stores the dictionary
    room_list = rooms['entrance']  # You have to start somewhere, right?
    while alive:
        try:
            room_key = explore_mansion(room_list)

            # Some rooms have special conditions, like grabbing an item,
            # giving an item or moving something.3
            # This algorithm takes care of those conditions.
            if room_key in ('grab horseshoe', 'move bookshelf', 'give item'):
                room_key = apply_special_conditions(room_key, room_list)

            # Get the item for the dictionary to be used continuing the loop
            room_list = rooms[room_key]

            # Checking if the game is over
            alive = check_game_over(room_key, rooms)

        except ValueError:
            print('Please type the number of the room')
        except IndexError:
            print('That is not a room, you know?')
            print('Maybe you should try to access an actual room?')

    print_typewriter('THE END', 1, 1)


if __name__ == '__main__':
    main()
