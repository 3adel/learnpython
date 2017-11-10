import sys
script, input_encoding, error = sys.argv


#Main function
def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print(">>>> Line is: ", line, end = "")
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

#This will encode strings, decode them again and then print them
def print_line(line, encoding, errors):
    print(">>>> Line in print_line is: ", line, end = "")
    next_lang = line.strip() #remove leading and trailing spaces
    print(">>>> Stripped line in print_line is: ", next_lang)

    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(">>>> Raw byte: ",raw_bytes)
    print(">>>> Cooked string: ",cooked_string, "\n")

#start
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
