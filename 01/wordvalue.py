from data import DICTIONARY, LETTER_SCORES
from collections import namedtuple


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return [line.strip() for line in f.read().split()]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    # words = load_words()
    if words is None:
        words = load_words()

    return max(words, key=calc_word_value)


if __name__ == "__main__":
    pass # run unittests to validate
