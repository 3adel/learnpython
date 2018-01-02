print("Enter the pronoun:")
pronoun = input("->")
print("Enter the case:")
case = input("->")

def casePronoun(pronoun, case):
    if pronoun == "I" or pronoun == "i":
        print(">>> first if met")
        if case == "nom":
            return "ich"
        elif case == "akk":
            return "mich"
        elif case == "dat":
            return "mir"
        else:
            return "Invalid case entered"
    elif pronoun == "you" or pronoun == "You":
        if case == "nom":
            return "du"
        elif case == "akk":
            return "dich"
        elif case == "dat":
            return "dir"
        else:
            return "Invalid case entered"

    elif pronoun == "he" or pronoun == "He":
        if case == "nom":
            return "er"
        elif case == "akk":
            return "ihn"
        elif case == "dat":
            return "ihm"
        else:
            return "Invalid case entered"

    elif pronoun == "she" or pronoun == "She":
        if case == "nom":
            return "sie"
        elif case == "akk":
            return "sie"
        elif case == "dat":
            return "ihr"
        else:
            return "Invalid case entered"

    elif pronoun == "it" or pronoun == "It":
        if case == "nom":
            return "es"
        elif case == "akk":
            return "es"
        elif case == "dat":
            return "ihm"
        else:
            return "Invalid case entered"

    elif pronoun == "we" or pronoun == "We":
        if case == "nom":
            return "wir"
        elif case == "akk":
            return "uns"
        elif case == "dat":
            return "uns"
        else:
            return "Invalid case entered"

    elif pronoun == "y'all" or pronoun == "Y'all":
        if case == "nom":
            return "ihr"
        elif case == "akk":
            return "euch"
        elif case == "dat":
            return "euch"
        else:
            return "Invalid case entered"

    elif pronoun == "they" or pronoun == "They":
        if case == "nom":
            return "sie"
        elif case == "akk":
            return "sie"
        elif case == "dat":
            return "ihnen"
        else:
            return "Invalid case entered"

    elif pronoun == "you f" or pronoun == "You f":
        if case == "nom":
            return "Sie"
        elif case == "akk":
            return "Sie"
        elif case == "dat":
            return "Ihnen"
        else:
            return "Invalid case entered"

    else:
        return "Invalid pronoun"

    return "Unknown error"


print("The conjugation of [{}] in the [{}] case is [{}]".format(pronoun, case, casePronoun(pronoun, case)))
