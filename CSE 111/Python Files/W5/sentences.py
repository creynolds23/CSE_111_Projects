"""
Author: Conner Reynolds
Purpose: Use Pytest to check programs, created plural and singular sentences
Date: 10/11/22
"""
import random
from pyparsing import Word

def main():
    quantity = int(input('What is the quantity of your noun (Enter 1 for singular, 2+ for plural). '))
    tense = input("What is the tense of the scenario('past', 'present', or 'future')? ")
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    adjective = get_adjective()
    print(f'{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase}. ')
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ['bird','boy','car','cat','child','dog','girl','man','rabbit','woman']
    else:
        nouns = ['birds','boys','cars','cats','children','dogs','girls','men','rabbits','women']
    Word = random.choice(nouns)
    return Word

def get_verb(quantity, tense):
    if tense in'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense in 'present' and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif tense in 'present' and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    elif tense in 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    Word = random.choice(verbs)
    return Word
def get_adjective():
    adjectives = ['hairy', 'scary', 'sour', 'curly', 'funny', 'strong', 'weak', 'tall', 'short', 'big', 'small']
    word = random.choice(adjectives)
    return word

def get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    word = random.choice(prepositions)
    return word

def get_prepositional_phrase(quantity):
    if quantity == 1:
        phrase = get_preposition() + ' ' + get_determiner(1) + ' ' + get_noun(1)
    else:
        phrase = get_preposition() + ' ' + get_determiner(2) + ' ' + get_noun(2)
    return phrase
main()