a = [1, 2, 3, 4]
b = '[1, 2, 3, 4]'

#the goal of __str__ is to be readable
print("str of a is:", str(a))
print("str of b is:", str(b))

#the goal of __repr__ is to be unambiguous
print("repr or a is:", repr(a))
print("repr or b is:", repr(b))
