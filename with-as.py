from sys import argv

script, filename = argv

print(">>> Filename: ",filename)

target = open(filename,'r')
print(target.read())
