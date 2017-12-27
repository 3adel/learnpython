print("Enter the pronoun:")
pronoun = input("->")
print("Enter the case:")
case = input("->")

if pronoun == "I":
    if case == "nom":
        print("ich")
    if case == "akk":
        print("mich")
    elif case == "dat":
        print("mir")
    else:
        print("Wrong case entry!")

elif pronoun == "You":
    if case == "nom":
        print("du")
    if case == "akk":
        print("dich")
    elif case == "dat":
        print("dir")
    else:
        print("Wrong case entry!")

else:
     print("Wrong pronoun entry!")
