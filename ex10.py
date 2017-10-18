tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print (fat_cat)

#other escape characters
print("\n") #New line, line feed
print("\\") #backslach
print("\'") #single quote
print("\"") #double-quotes
print("\v") #vertical tab
print("\b") #backspace
print("\a") #BEL
print("\f") #form feed Form feed is a page-breaking ASCII control character. It forces the printer to eject the current page and to continue printing at the top of another. Often, it will also cause a carriage return.
print("\r") #carriage return
print("\t") #horizontal tap
print("\u3421") #character with 16-bit hex value xxxx
print ("\u43234334") #character with 32 hex value xxxxxxxx
print("\777") #character with an octal value ooo
print("\xAB") #hexadecimal character hh


#Why do you want to use ''' instead of """ or vice versa
weirdString = '''This string contains """ in it
and it looks really weird'''
print(weirdString)

weirdString2 = """This string contains ''' in it
and it looks really weird"""
print(weirdString2)

#combine escape sequence and format strings to create a more complex format
studentNumber1 = 1
studentName1 = "Saray"
studentNumber2 = 2
studentName2 = "Kamal"

print("This is the list of students participating in the fair:\n{} {}\n{} {}".format(studentNumber1,studentName1,studentNumber2,studentName2))

#a review of an f-string
myNumber = 3
print(f"This is an f string with a number: {myNumber}")
