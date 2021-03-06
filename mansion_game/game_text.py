"""
This are the text used in-game
"""


def print_intro():
    """
    The intro text for the game
    """
    intro = """You've been stranded in a forest for a long time. You can't even remember the last time you ate something besides berries.\n\
            The helicopter that crashed is way behind you, or at least you expected you haven't been walking in circles.
            Far, in the distance, you can see a mansion. Salvation! You sprint towards it, and you get excited as it gets bigger and bigger.\n\
            Immediately after you put your hand on the doorknob, you start hesitating. “What if I get trapped inside?”.\n\
            Your natural impulse doesn't allow you to keep waiting. And so, you enter the mansion.
            Now that you are inside, you want to go out.
            """
    return intro


def get_rooms():
    """
    Creates the dictionary where the game happens
    """
    rooms = {
        'entrance': ["""It doesn't look like this mansion is very big. You might as well call it a cottage. You can only see some stairs that lead to the upper floor.\n\
It also looks like there is a hallway that allows you to keep exploring the main floor.\n\
Looking more to your left there is a door, that it looks like it leads to the basement, but you can't tell from here.\n\
A thought comes to your mind “You might as well leave this place, is not worth it”. But do you really want to go back to the berries?""",
                     "Main Door", 'Upper Floor', 'Main Floor', 'Basement'],

        'upper floor': ["""There are three different rooms you can access from here:\n\
One of them looks to be the room where the owner of the mansion used to live.\n\
Next to that room, you can see the library.\n\
The last room seems to be another bedroom. Perhaps it was for the owner's child?""",
                        "Master's Bedroom", 'Library', "Child's Bedroom", 'Entrance'],

        'main floor': ["Well, this is very disappointing. You can only see two doors from here.",
                       'Bathroom', "Servant's quarters", 'Entrance'],

        "master's bedroom": ["""Just as you suspected, this is the owner's room. It looks like nobody's been living in this mansion for days.\n\
Why would someone build a mansion in the middle of the forest in the first place?\n\
There is nothing else to see here… oh, wait! Something is moving!""",
                             'Upper Floor', "Investigate"],

        'library': ["""There are a lot of dusty books. You pick up one of them, open it, but it's impossible to read.\n\
Dust scatters from the books you close it, confirming to you that it has been a long time since they've been used.\n\
This rooms connects with a hallway, that gives you the impression to go on eternally; there is another door leading to the child's bedroom, and another one connects to the entire upper floor.\n\
There also looks to be a big staircase, with multiple branches coming from it.""",
                    "Child's Bedroom", 'Hallway', 'Stairway', 'Upper Floor'],

        "child's bedroom": ["""This room doesn't give you the best vibes. You can see a cradle and a bed, but there's sign that only one person has lived here.\n\
“I would go crazy if I had to live on the same room my entire life” This room connects with the entire upper floor.\n\
There is also a passage to the library, and connects with some big staircase, with multiple branches coming from it.""",
                            'Library', 'Stairway', 'Upper Floor'],

        'stairway': ["""This stairway is crazy! It is very convenient, since it can connect rooms from both floors!""",
                     "Child's Bedroom", 'Library', "Servant's Quarters", "Hallway", "Kitchen"],

        'hallway': ["""This hallway is not as endless as you thought. But it is very long considering that you can only access the stairway and the library.\n\
It also looks like you can access the attic from here.""",
                    'Library', 'Stairway', "Attic"],

        'attic': ["""This is a very modest attic, with enough room to put Christmas decorations for the whole mansion.\n\
There seems to be access to the roof from here.""",
                  'Hallway', 'Rooftop'],

        'rooftop': ["""From here you can see that the forest is bigger than you thought. Looking down gives you a little bit of vertigo, but you can't stop thinking that you could probably make that jump.\n\
There's also a single horseshoe on the floor.""",
                    'Attic', 'Jump Out', "Grab Horseshoe"],

        "servant's quarters": ["Probably not a lot of servants served in this mansion. This room just has enough space for two people.\n\
But hey, at least it connects with the bathroom and a room where they could rest.",
                               'Main Floor', 'Bathroom', 'Break Room'],

        'break room': ["""Probably the place where the servants spent most of their time.\n\
The couches look wrecked, and the only bookshelf has tons of used books.\n\
You keep staring at the bookshelf. It looks suspicious. """,
                       "Servant's Quarters", 'Kitchen', 'Move Bookshelf'],

        'secret room': ["""You can't believe your eyes! This place can take you outside the mansion. When you were almost out, a giant turtle stops you. “If you wish to continue, you must give me a horseshoe”.\n\
“Why would a turtle want a horseshoe?” you wonder. But you keep forgetting the obvious:\n\
Do you have a horseshoe?""",
                        "Give item"],

        'bathroom':  ["""You can barely call this a bathroom. This small room has just enough space for the toilet and a trash can.\n\
It looks so uncomfortable to use it that the mere thought of someone trying to use it disturbs you. At least there is another door.""",
                      'Main Floor', "Servant's Quarters"],

        'kitchen': ["""First thing that you can see is a delicious cake. It looks a lot better than the berries you've been eating.\n\
This room also connects with the stairway and the break room.""",
                    "Eat", 'Stairway', 'Break Room'],

        'basement': """Opening that door that you thought it led to the basement, a chill wind brushes through your body.\n\
Suddenly, as if the whole room were a vacuum, you can feel a force trying to drag you inside. Without sufficient strength to overcome it, you enter the room, just to realize that you're falling.\n\
There is nothing but an infinite hole, and now you are eternally falling.""",

        'main door': """You try to open the door, ready to leave this creepy mansion. The door doesn't budge, so you start pulling the doorknob.\n\
You can't hold the doorknob with your sweaty hand, and you fall backwards, hitting your head. You die from brain damage.""",

        'investigate': """As you approach the moving object, you realize that it's not an object, but rather a raccoon.\n\
The racoon jumps straight at your face and grabs your face. Trying to frere yourself from the racoon, you trip and fall through the window.""",

        'eat': """"“You shouldn't eat strange food, you never know what could happen” You remember your mom's advice, but rather late.\n\
Laying on the floor hasn't been more comfortable before, specially now that you can feel how the air is leaving your lounges.\n\
It's starting to get cold and dark; you just want to take a nap. You see a tunnel, and there's light at the end. You go towards the light""",

        'jump out': """You tried to fly away, but gravity is stronger than your will.\n\
Did you expect something else to happen?""",

        'good ending': """You can go on. The turtle is nowhere to be found. You keep wondering why you entered in the first place.\n\
You start pondering about what you just experienced, and you can't stop but think that nothing that just happened made any sense.\n\
Maybe you are just a character from a game, made by a BYU Idaho student? Who knows, but if that were true, maybe there is another secret room somewhere inside this crazy mansion.\n\
Maybe that would make you go inside again, but who knows.\n\
You decide.""",

        'bad ending': "Without any attempts left, the room is now so close that you must crouch.\n\
Without compassion, the room continues collapsing. You make your last wish: To die painlessly.\n\
I hope your wish came true, my friend.",
    }
    return rooms
