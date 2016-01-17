"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    
    #Create a set of the characters in the input-string.
    character_set = set(input_string)
    letter_dict = {}

    #For each character in the character set, initialize its frequency at 0.
    #Each time the character appears in the input string the letter frequency
    # goes up 1. Add an entry to letter_dict, where the final letter frequency 
    # is the key and the character goes in a list of values. Repeat for each 
    # character, appending the letter to the value list if it appears the same
    # number of times as another character.
    for char in character_set:
        letter_frequency = 0
        for item in input_string:
            if item == char:
                letter_frequency +=1
        if char == " ":
            pass
        elif letter_dict.get(letter_frequency, False) == False:
            letter_dict[letter_frequency] = [char]
        else:
            letter_dict[letter_frequency].append(char)

    # Sort a list of key, value dictionary items and return the value(s) 
    # associated with the highest frequency key.
    return sorted(letter_dict.items())[-1][-1]
    



# FIXME: fix the "now try doing it with only one call to sort() or sorted()"
# Too hard.
def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    #Create blank dictionary and sort words so they are alphabetical
    letter_dict = {}
    words = sorted(words)

    #For each word create a dictionary entry using the lenght of the word as
    #the key and a list containing the word as the value. If a key cooresponding 
    #to a words length already exists, append the word to the list of values for
    # that key.
    for word in words:
        length = len(word)
        if letter_dict.get(length, False) == False:
            letter_dict[length] = [word]
        else:
            letter_dict[length].append(word)


    return letter_dict.items()


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
