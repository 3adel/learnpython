#import the argv module from the sys package
from sys import argv

#assign argv to script name and the name of the input file. This way you can pass them as arguments when you run the script
script, input_file = argv

#this function takes a file object and prints its content to the console
def print_all(f):
    print(f.read())

#this fucntion takes a file object and moves the cursor to its beginning
def rewind(f):
    f.seek(0)
#this function takes the line number and the file object as arguments, then prints the given line number and the content of the file at that specific line
def print_a_line(line_count, f):
    print(">>>> Passed line count is:", line_count)
    print(line_count, f.readline(), end = "")

#open the file and store the file object in the variable current_file
current_file = open(input_file)

print("First let's print the whole file:\n")

#invoke the print_all function, passing a file object
print_all(current_file)

print("Now  let's rewind, kind of like a tape.")

#invoke the rewind function
rewind(current_file)

print("Let's print three lines:")

#update the value of current file
current_line = 1
print_a_line(current_line, current_file)

#update the value of current file
current_line += 1
print_a_line(current_line, current_file)

#update the value of current file
current_line += 1
print_a_line(current_line, current_file)
