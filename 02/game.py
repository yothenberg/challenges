#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import random
import itertools
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters():
    return random.sample(POUCH, NUM_LETTERS)


def get_possible_dict_words(draw):
    """Get all possible words from draw which are valid dictionary words.
    Use the _get_permutations_draw helper and DICTIONARY constant"""
    permutations = [''.join(word).lower() for word in _get_permutations_draw(draw)]
    return set(permutations) & set(DICTIONARY)


def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""
    for r in range(1, len(draw) + 1):
        yield from list(itertools.permutations(draw, r))


def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""
    draw_copy = draw #list(draw)
    for char in word.upper():
        if char in draw_copy:
            draw_copy.remove(char)
        else:
          raise ValueError("{} is not a valid word!".format(word))
    if not word.lower() in DICTIONARY:
        raise ValueError('Not a valid dictionary word, try again')

    return word


def input_word(draw):
    """Ask player for a word.
    Validations: 1) only use letters of draw, 2) valid dictionary word"""
    while True:
        word = input('Form a valid word: ').upper()
        try:
            return _validation(word, draw)
        except ValueError as e:
            print(e)
            continue


def main():
    draw = draw_letters()
    print('Letters drawn: {}'.format(' '.join(draw)))
    
    word = input_word(draw)
    
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word.upper(), word_score))

    possible_words = get_possible_dict_words(draw)
    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(max_word.upper(), max_word_score))
    score = word_score / max_word_score * 100
    print('Your score: {:.1f}'.format(score))


if __name__ == "__main__":
    main()
