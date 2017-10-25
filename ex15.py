#import the argv module so we can pass arguments through commandline
from sys import argv

script, filename = argv #define commandline arguments


#txt = open(filename) #open the file

#Show what's in the file object
print(">>>>>> File object: ",repr(open(filename)))


print(f"Here's your file: {filename}") #show the file name
print(open(filename).read()) #open the file, then read it and print it.

print("Type the filename again:") #acquire filename through the prompt
file_again = input("> ") #prompt the user to enter a file name

txt_again = open(file_again) #open the file again

print(txt_again.read()) #read the file, then print it.

