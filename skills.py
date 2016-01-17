"""Skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return the list with duplicates removed.

    For example:

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    non_dupe_list = []

    #add each unique word to the non_dupe_list 
    for word in words:
        if word not in non_dupe_list:
            non_dupe_list.append(word)
    
    # sort the non_duple_list
    non_dupe_list.sort()

    return non_dupe_list 


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not use 'if ___ in ___' or the method 'index'.

    This should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([4, 3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    """
    
    common_list = []

    #Go through each value in the first list, check if the value is in the 
    #second list, and if so check if its already in the common_list, if 
    #not add it. 
    
    for val in list1:
        if val in list2:
            if val not in common_list:
                common_list.append(val)

    common_list.sort()
    return common_list


    # #Alternate, using set to find unique values

    # common_list = []

    # for val in list1:
    #     if val in list2:
    #         common_list.append(val)

    # #Convert list to a set to remove any duplicates

    # common_set = set(common_list[:])
    # unique_common_list = []

    # #put items in set back into a list of unique items and sort
    # for val in common_set:
    #     unique_common_list.append(val)
    
    # unique_common_list.sort()
    # return unique_common_list
    

def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """

    split_string = input_string.split(" ")
    word_dict = {}

    for word in split_string:
        if word_dict.get(word, False) == False:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    pirate_dict = {
                    "sir" : "matey",
                    "hotel" : "fleabag inn",
                    "student" : "swabbie",
                    "boy" : "matey",
                    "madam" : "proud beauty",
                    "professor" : "foul blaggart",
                    "restaurant" : "galley",
                    "your" : "yer",
                    "excuse" : "arr",
                    "students" : "swabbies",
                    "are" : "be",
                    "lawyer" : "foul blaggart",
                    "the" : "th'",
                    "restroom" : "head",
                    "my" : "me",
                    "hello" : "avast",
                    "is" : "be",
                    "man" : "matey"
                    }

    # Split phrase into individual words
    split_phrase = phrase.split(" ")
    pirate_word_list = []

    # Check if each regular word has a value in the pirate dictionary
    # If it doesn't append the regular word to the pirate_word_list
    # If it does then append the pirate word to the pirate_word_list 
    for word in split_phrase:
        if pirate_dict.get(word, False) == False:
            pirate_word_list.append(word)
        else:
            pirate_word_list.append(pirate_dict[word])

    # Create a new phrase concatenating all the words in the pirate_word_list.
    new_phrase = "%s" % pirate_word_list[0]

    for pir_word in pirate_word_list[1:]:
        new_phrase = new_phrase + " " + pir_word

    return new_phrase


def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items---the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    
    word_dict = {}

    #Add each word to word_dict, with the key being the length of the word and
    #the value being a list containing the word. If a key of that length 
    # already exists, add the word to the list of values.
    for word in words:
        if word_dict.get(len(word), False) == False:
            word_dict[len(word)] = [word]
        else:
            word_dict[len(word)].append(word)

    #Return a list of the key value pairs in the dictionary. 
    return word_dict.items()


def get_sum_zero_pairs(input_list):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """
    
    # convert the list to a set to remove duplicate values
    unique_num_set  = set(input_list[:])
    abs_value_dict = {}
    zero_pair_list = []  

    #Check each number in the set, if it is a zero, append it to the zero_pair
    # list as its own pair. If the number is not a zero add it to the 
    # abs_value dictionary using the number's absolute value as the key and the
    # number as the value. If a key already exists for the absolute value of a 
    # given number, add the number to the list of values under that key. 
    for num in unique_num_set:
        if num == 0:
            zero_pair_list.append([num, num])
        else:
            if abs_value_dict.get(abs(num), False) == False:
                abs_value_dict[abs(num)] = [num]
            else:
                abs_value_dict[abs(num)].append(num)
    
    # Check each key in the abs_value dictionary to see if there is more than
    # one value associated with it. If so append a sorted list of values to the 
    # zero_pair list. 
    for item in abs_value_dict:
        if len(abs_value_dict[item]) > 1: 
            zero_pair_list.append(sorted(abs_value_dict[item]))

    return zero_pair_list


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
