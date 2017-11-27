def ref_demo(x):
    print("x=",x,", id=",id(x))
    x = 5
    print("x=",x,", id=",id(x))


y = 8
print("y=",y,", id=",id(y))

ref_demo(y)
