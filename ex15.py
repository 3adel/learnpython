from sys import argv

script, filename = argv

#txt = open(filename)

print(f"Here's your file: {filename}")
print(open(filename).read())

print("Type te filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())