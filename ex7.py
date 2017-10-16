print("Mary had a little lamb.")

#you can also use: print(f"Its fleece was white as {'snow'}")
print("Its fleece was white as {}".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) #What'd that do?

#The following lines assign characters to each variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# The "end" argument at the end specifies what the text ends with. You can change it to '\n' for example.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

#How to check if a string ends with a specific string
randomString = "just a text"
print(randomString.endswith('xt'))
