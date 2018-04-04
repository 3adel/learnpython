from sys import argv

script, filename = argv
target = open(filename,'r')
print(target.read())

#now let's try with with-as
