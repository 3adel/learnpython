#assign a formatted string to formatter with 4 placehorlders
formatter = "{} {} {} {}"

#print our formatter with numbers passed as arguments
print(formatter.format(1, 2, 3, 4))

#print out formatter with strings passed as arguments
print(formatter.format("one","two","three","four"))

#print out formatter with formatter passed as arguments
print(formatter.format(formatter, formatter, formatter, formatter))

#print out formatter with strings passed as arguments. Note that you can write on multiple lines
print(formatter.format(
    "Try your",
    "own text here",
    "maybe a poem",
    "or a song about fear"
))
