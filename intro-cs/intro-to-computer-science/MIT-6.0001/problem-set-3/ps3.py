# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by:    and Jenna Wiens <jwiens>
#
# Name          : eurodollarclub
# Collaborators : None
# Time spent    : <total time>

import math
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------


#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    word: string, the actual word
    n: int >= 0, the number of actual letters
    returns: int >= 0, product
    """
    assert isinstance(word, str), f"{word} not a str"
    assert isinstance(n, int) and n > 0, f"{n} not an int or {n} < 0"

    word = word.lower()
    first_component = 0
    for i in word:
        for k, v in SCRABBLE_LETTER_VALUES.items():
            if k == i:
                first_component += v
    second_component = 7 * len(word) - 3 * (n - len(word))
    if second_component < 0:
        second_component = 1
    return first_component * second_component


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for key in hand.keys():
        for _ in range(hand[key]):
            print(key, end=" ")
    print()


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int > 0
    returns: dictionary (string -> int)
    """
    assert n > 0, f"{n} <= 0"

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for _ in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for _ in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    * Do not assume that hand contains every letter in word at least as many times as the letter appears in word.
      hand might contain undefined, 0,1,2 letters
    * Letters in word that don't appear in hand should be ignored.

    * Letters that appear in word more times than in hand should never result in a negative count;
      instead, set the count in the returned hand to 0
      (or remove the letter from the dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    assert isinstance(hand, dict), f"type of {hand} not dict"
    assert isinstance(word, str), f"type of {word} not str"

    word = word.lower()
    new_hand = hand.copy()

    for i in range(len(word)):
        for k, v in new_hand.items():
            if k == word[i]:
                new_hand[k] = v - 1
                if new_hand[k] < 1:
                    new_hand[k] = 0
    return new_hand


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    """ 
    goal/understanding: 
    test if word is in wordlist and word consist entirely of letters in the hand

    strategy:
    check if word in wordlist 
    check if each letter of word is in hand
    if letter of word in hand then decrement it 
    
    evaluation:

    implimentation:
    """
    assert isinstance(word, str), f"{word} not a str"
    assert isinstance(hand, dict), f"{hand} not a dict"
    assert isinstance(word_list, list), f"{word_list} not a list"

    word = word.lower()
    new_hand = hand.copy()

    if word in word_list:
        for k in word:
            try:
                v = new_hand[k]
            except:
                pass
            if k not in new_hand:
                return False
            elif k in new_hand and v < 1:
                return False
            else:
                new_hand[k] = v - 1
        return True
    return False


#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    pass  # TO DO... Remove this line when you implement this function


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score

    # As long as there are still letters left in the hand:

    # Display the hand

    # Ask user for input

    # If the input is two exclamation points:

    # End the game (break out of the loop)

    # Otherwise (the input is not two exclamation points):

    # If the word is valid:

    # Tell the user how many points the word earned,
    # and the updated total score

    # Otherwise (the word is not valid):
    # Reject invalid word (print a message)

    # update the user's hand by removing the letters of their inputted word

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#


def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    pass  # TO DO... Remove this line when you implement this function


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    print(
        "play_game not implemented."
    )  # TO DO... Remove this line when you implement this function


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == "__main__":
    """word_list = load_words()
    play_game(word_list)"""
