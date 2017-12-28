print("Enter the pronoun:")
pronoun = input("->")
print("Enter the case:")
case = input("->")

def casePronoun(pronoun, case):
    if pronoun == "I" or "i":
        if case == "nom":
            return "ich"
        elif case == "akk":
            return "mich"
        elif case == "dat":
            return "mir"
        else:
            return "Invalid case Entered!"
    elif pronoun == "you":
        if case == "nom":
            return "du"
        elif case == "akk":
            return "dich"
        elif case == "dat":
            return "dir"
        else:
            return "Invalid case Entered!"
    else:
        print("no")

    return "Unknown"


print("The conjugation of [{}] in the [{}] case is [{}]".format(pronoun, case, casePronoun(pronoun, case)))
