from sys import argv

#you need the file name, the encoding and error handling as parameters

script_name, file_name, error_handling =  argv

# recursive function to scan the file line by line
def lineScanner(file_Object, error_handling):
    line = file_Object.readline()
    if line:
        #print(line, end="")
        printLine(line, error_handling)
        return lineScanner(file_Object, error_handling)


def printLine(line, error):
    decodedLine = line.strip()
    print("Decoded: ", decodedLine)



file_Object = open(file_name)
#file_text = file_Object.read()

#call the main function now
lineScanner(file_Object, error_handling)



# You have a file called languages.txt
# 1 open the file and store in in a file object
# Now you opened the file, you need to start iterating on each line
# For each line, get the string, then encode it to binary, then decode it
# print
