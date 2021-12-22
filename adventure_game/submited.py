"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: Adventure Game (practice if statements and decision making)
"""
print('--' * 40)
print("Hero's Journey\nGame inspired by Joseph Campbell's 'Hero's Journey'")
print('--' * 40)
print("it's a normal day in life, nothing too special. Except there is something special.\nYou can feel the calling.\nYou accept the calling ")
print("\nYou head outside, not knowing what awaits for you. You find on your path a sword and a bow with arrows.\nYou somehow know that you can't take both.")

# Choosing a weapon. Not a big of a deal since you can go empty-handed.
weapon = input("Which one will you take? Sword/Bow\n")
if weapon.lower() == 'sword':
    print('Even though you have never used it before, you feel confidente.')
    sword = True
    bow = False
elif weapon.lower() == 'bow':
    print('You can feel how your aiming abilities increased just by holding it.')
    bow = True
    sword = False
else:
    print("Well, I guess you're adventuring empty handed.")
    sword = False
    bow = False
print("\nWalking towards the woods, you find a wolf. He's sleeping, but you woke him up")

# Wolf encounter. You either befriend him or not
decision = input('What do you do? Attack/Pet/Run\n')
if decision.lower() == 'attack':
    if sword:
        print("The wolf just stares at you as you unfold your sword and pierce his heart. The light inside his eyes vanishes as you remove the sword from his chest")
    elif bow:
        print("Aiming straight to his head, the wolf still doesn't move, he's just staring at you. You shoot and the wolf is no more.")
    else:
        print("Since you didn't grab a weapon, you fist fight. The wolf runs away, meaning not harm to you.")
    wolf = False
elif decision.lower() == 'pet':
    print("He starts to move his tails, he's very excited to meet you.\nThe wolf now joins in your adventure!")
    wolf_name = input('Name the wolf: ')
    wolf = True
elif decision.lower() == 'run':
    print("You were able to escape from the wolf, but apperantly he wasn't a bad wolf anyways.")
    wolf = False
else:
    print("Being too late to decide now, your legs force you to run away, outside the woods.")
    wolf = False
print("\nLeaving the woods you can see your objective loud and clear. Or at least that's what you thought.")
"""
Final Battle where everything comes together.
Main Routes:
1. Fight with wolf
2. Fight without wolf
3. Run with wolf
4. Run without wolf 
5. else statement (Shouldn't happen)
"""
print("As you enter your destination, you notice a giant ogre, waiting for you. He's been waiting a long time for this.\nNow your final battle begins!")
battle = input("What do you do? Fight/Flee\n")
if battle.lower() == 'flee' and wolf: #1. Run w/ wolf
    print(f"You managed to escape, but only to turn around and see that {wolf_name.capitalize()} is dead.")
    courage = False
elif battle.lower() == 'flee' and not wolf: #2. Run w/o wolf
    print("You managed to escape, but something feels wrong.")
    courage = False
elif battle.lower() == 'fight' and not wolf: #3. Fight w/o wolf
    if sword:
        print("After dodging his attacks, you strike his knee, allowing you to impulse to his chest. You pierce his heart, after which he only screams and then faints. ")
    elif bow:
        print("Finding a high place, you take your bow and aim straight to one of his eyes. You take a deep breath, and then you shoot.\nDirect hit! The ogre faints.")
    else:
        print("You should've brought a weapon with you! Luckly, you remembered your acting classes.\nThe ogre is now scared by your bad performance, and now he runs away.")
    courage = True
elif battle.lower() == 'fight' and wolf: #4. Fight w/ wolf
    if sword:
        print(f"You take the first step to start attacking, but suddenly {wolf_name.capitalize()} dashes towards the ogre. The ogre is too slow, so {wolf_name.capitalize()} manages to avoid his attacks and jumps straight to his face.\nThe ogre, in his final attempt to free himself, slaps his face, leaving {wolf_name.capitalize()} flat as a paper.\nYou will always remember his courage, and you will always be friends. ")
    elif bow:
        print(f"As you approach with {wolf_name.capitalize()}, you notice that he's not breathing. Apperantly he waited for so long that he ran out of food and died from starvation")
    else:
        print(f"You are ready to face death. The lack of weapons is just too much for you. As you consider your last words, {wolf_name.capitalize()} jumps into battle. You scream, you don't want your friend to die.\nBut it's too late now. Both ogre and wolf are history, but your friendship with {wolf_name.capitalize()} will be forever.")
    courage = True
else: #5. else statement (Shouldn't happen)
    print("This text should never be displayed. If it does, there's something to be fixed somewhere")
    courage = False

# Checking if you get the true ending
if courage and wolf:
    friendship = True
else:
    friendship = False
"""
There are four different endings, depending on your actions
1. Befriend wolf and fight = True ending
2. Befriend wolf and run = Sad ending
3. Kill/Run wolf and fight = Incomplete ending
4. Kill/Run wolf and run = Bad ending
"""
# DIfferent endings
print("\nAs you return home from your adventure, a wise turtle stops you.\n'Welcome back! Let's see how well did you do'")
print("Let's see together what you just did:\n")
if friendship:
    print(f"You succesfully conquered your fears by befriending the wolf (by the way, I think {wolf_name.capitalize()} is an awesome name!) and by fighting the ogre.\nCongratulations!")
    ending = True
    ending_name = 'True Ending'
elif wolf and not courage:
    print(f"You conquered some of your fears by befriending the wolf, but you ran on your final test, and {wolf_name.capitalize()} died. I'm truly sorry for your loss.")
    ending = False
    ending_name = 'Sad Ending'
elif not wolf and courage:
    print("Oh poor wolf! He was just looking for a friend. You still conquered the ogre, but you missed a great opportunity to make a new friend.")
    ending = False
    ending_name = 'Incomplete Ending'
elif not wolf and not courage:
    print("Your quest is over, but what did you earn? You have no experience because of your actions. You return home as if you never left.")
    ending = False
    ending_name = 'Bad Ending'
else:
    print("If you're reading this, there's something wrong.")
    ending = False
    ending_name = "If you can read this, something's wrong"
print(f'\nYou just completed the {ending_name.upper()}!\nWhich other endings could you get?\n')
print('--' * 40)
print("'The cave you fear to enter holds the treasure you seek' Joseph Campbell")
print("What cave are you afraid of entering, but you know you should enter?")
print('--' * 40)