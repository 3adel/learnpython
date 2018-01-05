a, b = 0, 1
while b < 10:
    print(">>> a before = ",a)
    print(">>> b before = ",b)
    #with simultaneous addition
    a, b = b, a+b
    
    #without simultaneous addition
    #a = b
    #b = a + b
    
    print(">>> a after = ",a)
    print(">>> b after = ",b,end='\n\n')
