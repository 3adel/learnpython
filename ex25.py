def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

print(sort_words(["Zdel", "Sami"]))
