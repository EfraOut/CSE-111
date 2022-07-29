"""
Author: Efrain Gomez Fajardo
Teacher: Comeau, Luc
Purpose: The Turing Test
Extra Mile:
1. Added get_adverb to add an adverb to the sentences
"""
from random import choice


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

    word = choice(words)
    return word


def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
    "gladly", "gently", "quietly", "safely", "truthfully", "warmly", 
    "wildly", "carefully", "wisely", "hard", "fast", "straight", "well",
    "angrily", "boldly", "daringly"

    Return: A randomly chosen adverb
    """
    adverbs = ["gladly", "gently", "quietly", "safely", "truthfully",
               "warmly", "wildly", "carefully", "wisely", "hard", "fast",
               "straight", "well", "angrily", "boldly", "daringly"]

    adverb = choice(adverbs)
    return adverb


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense.lower() == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense.lower() == 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]
    elif tense.lower() == 'present' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]
    else:
        verbs = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]

    verb = choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    preposition = choice(prepositions)
    return preposition


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are singular or plural.
    Return: a prepositional phrase.
    """
    if quantity == 1:
        prepositional_phrase = f"{get_preposition()}" \
            + f" {get_determiner(1)}" \
            + f" {get_noun(1)}"
    else:
        prepositional_phrase = f'{get_preposition()}' \
            + f' {get_determiner(2)}' \
            + f' {get_noun(2)}'

    return prepositional_phrase


def main():
    for i in range(2):
        # Past Tense
        print(f"{get_determiner(i).capitalize()} {get_noun(i)} {get_adverb()}",
              f"{get_verb(i, 'past')} {get_prepositional_phrase(i)}.")

    for i in range(2):
        # Present Tense
        print(f"{get_determiner(i).capitalize()} {get_noun(i)} {get_adverb()}",
              f"{get_verb(i, 'present')} {get_prepositional_phrase(i)}.")

    for i in range(2):
        # Future Tense
        print(f"{get_determiner(i).capitalize()} {get_noun(i)} {get_adverb()}",
              f"{get_verb(i, 'future')} {get_prepositional_phrase(i)}.")


# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
