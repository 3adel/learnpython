#   Transpose a matrix with nested list comprehensions



matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
transposed = [1,2,3,4]
print(">>>matrix: ", matrix)

for i in range(len(matrix[0])):
    for j in range (len(matrix)):
            #print("i",matrix[j][i],)
            transposed[i][j]=matrix[j][i]

print(transposed)
