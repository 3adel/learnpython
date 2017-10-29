from sys import argv
from os.path import exists

script, from_file, to_file = argv


#we could do these two on one line how?

open(to_file, 'w').write(open(from_file).read())

print("Alright, all done.")


#Should always close files:
#open(to_file, 'w').close()
#open(from_file).close()
