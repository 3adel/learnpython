from sys import argv
from os.path import exists

script, from_file, to_file = argv

open(to_file, 'w').write(open(from_file).read())

print("Alright, all done.")


#Should always close files:
#open(to_file, 'w').close()
#open(from_file).close()
