"""
Author: Conner Reynolds
Purpose: Test Sentences File
"""
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import pytest
import random

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # Test single nouns
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(11):
        word = get_noun(1)
        assert word in single_nouns
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(11):
        word = get_noun(2)
        assert word in plural_nouns
def test_get_verb():
    rq = [1,2]
    quantity = random.choice(rq)
    rt = ['past', 'present', 'future']
    tense = random.choice(rt)
    assert get_verb(quantity, tense)
def test_get_preposition():
    assert get_preposition()
def test_get_prepositional_phrase():
    rq = [1,2]
    quantity = random.choice(rq)
    assert get_prepositional_phrase(quantity)
def test_get_adjective():
    assert get_adjective()
pytest.main(["-v", "--tb=line", "-rN", __file__])