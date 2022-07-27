def get_stories():
    stories = {
    'home': "it's a normal day in life, nothing too special. Except there is something special.\nYou can feel the calling.\nYou accept the calling\n",
    'path': "You head outside, not knowing what awaits for you. You find on your path a sword and a bow with arrows.\nYou somehow know that you can't take both.\n",
    'woods': "Walking towards the woods, you find a wolf. He's sleeping, but you woke him up\n",
    'ogre': ("Leaving the woods you can see your objective loud and clear. Or at least that's what you thought.\n",
            "As you enter your destination, you notice a giant ogre, waiting for you. He's been waiting a long time for this.\nNow your final battle begins!\n"),
    'turtle': ("As you return home from your adventure, a wise turtle stops you.\n'Welcome back! Let's see how well did you do",
                "Let's see together what you just did:\n")
    }
    return stories


def get_prompts():
    prompts = {
    'path': "Which one will you take? Sword/Bow\n",
    'woods': "What do you do? Attack/Pet\n",
    'ogre': "What do you do? Fight/Flee\n"
    }
    return prompts


def get_decisions():
    decisions = {
    'sword' : "Picking up the sword, you know it can bring protection for your journey.\n",
    'bow' : "Even though you have never used one, it feels natural for you how to aim and reload at the speed of light.\n",
    'attack' : ("The wolf just stares at you as you unfold your sword and pierce his heart. The light inside his eyes vanishes as you remove the sword from his chest\n",
                "Aiming straight to his head, the wolf still doesn't move, he's just staring at you. You shoot and the wolf is no more.\n"),
    'pet' : "He starts to move his tails, he's very excited to meet you.\nThe wolf now joins in your adventure!\n", 
    'run' : "You were able to escape from the wolf, but apparently he wasn't a bad wolf anyways.\n",
    'fight_wolf' : ("You take the first step to start attacking, but suddenly, the wolf dashes towards the ogre. The ogre is too slow, so the wolf manages to avoid his attacks and jumps straight to his face.\nThe ogre, in his final attempt to free himself, slaps his face, leaving  flat as a paper.\nYou will always remember his courage, and you will always be friends.\n",
                "As you approach with the wolf, you notice that he's not breathing. Apparently he waited for so long that he ran out of food and died from starvation\n"),
    'fight' : ("After dodging his attacks, you strike his knee, allowing you to impulse to his chest. You pierce his heart, after which he only screams and then faints.\n",
                "Finding a high place, you take your bow and aim straight to one of his eyes. You take a deep breath, and then you shoot.\nDirect hit! The ogre faints.\n"),
    'flee' : ("You managed to escape, but only to turn around and see that the wolf is dead.\n",
                    "You managed to escape, but something feels wrong.\n"),
    }
    return decisions


def get_endings():
    endings = {
    'true': "You successfully conquered your fears by befriending the wolf and by fighting the ogre.\nCongratulations!",
    'sad': "You conquered some of your fears by befriending the wolf, but you ran on your final test, and the wolf died. I'm truly sorry for your loss.",
    'incomplete': "Oh poor wolf! He was just looking for a friend. You still conquered the ogre, but you missed a great opportunity to make a new friend.",
    'bad': "Your quest is over, but what did you earn? You have no experience because of your actions. You return home as if you never left.",
    }
    return endings