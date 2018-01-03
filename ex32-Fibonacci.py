a, b = 0, 1
while b < 1000000:
    print(b, end='\n')
    a, b = b, a+b
