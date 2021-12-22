"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Hero's Journey Game
"""
from dictionaries import *

stories = get_stories()
prompts = get_prompts()
decisions = get_decisions()
endings = get_endings()
SWORD_INDEX = 0
BOW_INDEX = 1


def print_intro():
    """
    The first message that the user will see when
    they execute the program
        return: nothing
    """
    print('--' * 40)
    print("Hero's Journey\nGame inspired by Joseph Campbell's \"Hero's Journey\"")
    print('--' * 40)
    print(stories['home'])


def create_path():
    """
    First scene from the game
    The player has to choose between a sword
    or a bow to continue on their adventure
        parameters: none
        return: The chosen weapon
    """
    print(stories['path'])
    weapon = input(prompts['path']).lower()

    while weapon not in ('sword', 'bow'):
        print('Please choose a correct weapon')
        weapon = input(prompts['path']).lower()

    print(decisions[weapon])

    return weapon


def create_woods(weapon):
    """
    Second scene from the game
    The player has to choose between
    attack, pet or run from a wolf
        parameters:
            weapon: The chosen weapon from
            create_path()
        return: The state of the wolf 
        (dead = False / alive = True)
    """
    wolf = True
    print(stories['woods'])
    decision = input(prompts['woods']).lower()
    while decision not in ('attack', 'pet', 'run'):
        print('Please enter a valid decision')
        decision = input(prompts['woods']).lower()

    if decision == 'attack':
        if weapon == 'sword':
            print(decisions[decision][SWORD_INDEX])
        else:
            print(decisions[decision][BOW_INDEX])
        wolf = False
    else:
        print(decisions[decision])

    return wolf


def create_battle(weapon, wolf):
    """
    Third and last scene from the game
    The player has to choose between figting or
    fleeing from an ogre
        parameters:
            weapon: The chosen weapon from
            create_path()
            wolf: The state of the wolf from
            create_woods()
        return: The corresponding ending 
    """
    print(stories['ogre'][SWORD_INDEX])
    print(stories['ogre'][BOW_INDEX])
    fight = input(prompts['ogre']).lower()
    while fight not in ('fight', 'flee'):
        print('Please enter a valid option')
        fight = input(prompts['ogre']).lower()

    if wolf:
        if weapon == 'sword' and fight == 'fight':
            print(decisions['fight_wolf'][SWORD_INDEX])
            ending = endings['true']
        elif weapon == 'bow' and fight == 'fight':
            print(decisions['fight_wolf'][BOW_INDEX])
            ending = endings['true']
        else:
            print(decisions['flee'][SWORD_INDEX])
            ending = endings['sad']
    elif not wolf:
        if weapon == 'sword' and fight == 'fight':
            print(decisions[fight][SWORD_INDEX])
            ending = endings['incomplete']
        elif weapon == 'bow' and fight == 'fight':
            print(decisions[fight][BOW_INDEX])
            ending = endings['incomplete']
        else:
            print(decisions['flee'][BOW_INDEX])
            ending = endings['bad']
            
    return ending


def print_ending(ending):
    """
    Final conversation with the turtle who anounces
    the reached ending.
        parameters:
            ending: The corresponding ending from
            create_battle() 
        returns: nothing
    """
    print(stories['turtle'][SWORD_INDEX])
    print(stories['turtle'][BOW_INDEX])
    print(ending)
    print()
    print('"The cave you fear to enter holds the treasure you seek" Joseph Campbell')
    print("What cave are you afraid of entering, but you know you should?")
    print('--' * 40)


def main():
    game_on = True
    while game_on:
        print_intro()
        weapon = create_path()
        wolf = create_woods(weapon)
        ending = create_battle(weapon, wolf)
        print_ending(ending)
        player = input('Do you want to play again? [YES/NO]\n').lower()
        print()
        if player == 'no':
            print('Thank you for playing!')
            game_on = False

if __name__ == '__main__':
    main()