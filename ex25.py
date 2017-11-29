def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words, reverse = False)

def print_first_word(words):
    """Prints the first  word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    print(">>>> sentence passed: ", sentence)
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    print(">>>> sentence broken: ", words)
    print(">>>> sentence sorted: ", sort_words(words))
    return sort_words(words)

def print_first_and_last(sentence):
    

print(sort_sentence("This is a long sentence"))
