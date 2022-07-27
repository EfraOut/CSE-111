"""
Author: Efrain GOmez Fajardo
Teacher: Comeau, Luc
Purpose: Test functions from sentences.py
Extra Mile:
1. Added test_get_adverb to test the get_adverb function
"""
from sentences import *
import pytest


def test_get_determiner():
    # 1. Test the single determiners.
    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.
    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test singles nouns
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        noun = get_noun(1)

        assert noun in single_nouns

    # 2. Test plural nouns
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    for _ in range(4):
        noun = get_noun(2)

        assert noun in plural_nouns


def test_get_adverb():
    adverbs = ["gladly", "gently", "quietly", "safely", "truthfully",
        "warmly", "wildly", "carefully", "wisely", "hard", "fast", "straight",
        "well", "angrily", "boldly" "daringly"]

    for _ in range(4):
        adverb = get_adverb()

    assert adverb in adverbs


def test_get_verb():
    # 1. Test past verbs
    verbs_past = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        verb = get_verb(1, 'past')

        assert verb in verbs_past

    # 2. Test present and singles
    singles_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]

    for _ in range(4):
        verb = get_verb(1, 'present')

        assert verb in singles_verbs

    # 3. Test present and plural
    plural_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        verb = get_verb(2, 'present')

        assert verb in plural_verbs

    # 4. Test future verbs
    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        verb = get_verb(1, 'future')

        assert verb in future_verbs


def test_get_prepositional():
    # 1. Since there are no parameters, so only one test is necessary
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):
        preposition = get_preposition()

        assert preposition in prepositions


def test_get_prepositional_phrase():
    # 1.Singles
    for _ in range(4):
        preposition = get_prepositional_phrase(1)

    # Since the returned value should a sentence with 3 words
    # There should be two empty strings to separate the words
    assert preposition.count(' ') == 2

    # 2. Plurals
    for _ in range(4):
        preposition =  get_prepositional_phrase(2)

    # Since the returned value should a sentence with 3 words
    # There should be two empty strings to separate the words
    assert preposition.count(' ') == 2


pytest.main(["-v", "--tb=line", "-rN", __file__])