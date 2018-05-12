#example of using list comprehensions to combine two lists

#traditional method:
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(">>> x",x)
print(">>> y", y)
print("Comb1",combs)

#with list comprehensions
combs2 = [(m,z) for m in [1,2,3] for z in [3,1,4] if m != z]
print(">>> m",x)
print(">>> z", y)
print("Comb2",combs2)
