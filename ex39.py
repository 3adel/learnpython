#to loop over a sequence in reverse

seq1 = ['name', 'age', 'height']

for i in reversed(seq1):
    print(i)


#in traditional methods

for k in seq1[::-1]:
    print(k)

#get the index:
for i in (seq1[::-1]):
    print(i, seq1.index(i))
