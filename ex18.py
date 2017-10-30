# this one is like your scripts with argv
def print_two(*args):
    #unpack the argument. save the list args  into variables
    arg1, arg2 = args
    # ok, that *args is actually pointless, it just takes the arguments and put them in a list
    print(">>>> args: ", repr(args))
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# without using args* now
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
    

# this just takes one argument
def print_one(arg1):
    print("arg1: {arg1}")
    
# this one takes no arguments
def print_none():
    print ("I got nothin'.")
    

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
