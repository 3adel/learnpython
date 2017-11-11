from sys import argv

#you need the file name, the encoding and error handling as parameters

script_name, file_name, file_encoding, error_handling =  argv

# recursive function to scan the file line by line
def lineScanner(file_Object,file_encoding, error_handling):
    line = file_Object.readline()
    if line:
        #print(line, end="")
        printLine(line, file_encoding, error_handling)
        return lineScanner(file_Object,file_encoding, error_handling)


def printLine(line, lineEncoding, error):
    encodedLine = line.strip().encode(lineEncoding, errors=error)
    decodedLine = encodedLine.decode(lineEncoding, errors=error)
    print(">>>> Encoded:", encodedLine, "Decoded: ", decodedLine)



file_Object = open(file_name, encoding = "utf-8")
#file_text = file_Object.read()

#call the main function now
lineScanner(file_Object, file_encoding, error_handling)









# You have a file called languages.txt
# 1 open the file and store in in a file object
# Now you opened the file, you need to start iterating on each line
# For each line, get the string, then encode it to binary, then decode it
# print
