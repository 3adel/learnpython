#   Transpose a matrix with nested list comprehensions

#Transposing a matrix with traditional methods
def transposer(inputMatrix):

    #The length of the transpose matrix is equal to the length of any sub-matrix of the original matrix. In this case sub-matrices all have the same lenth for the transpose to work.
    transposed = [[] for x in range(len(inputMatrix[0]))]
    print(">>>Here's the main matrix:", inputMatrix)

    #we're traversing inputMatrix by columns, not by rows. Hence the idea of a transpose
    for col in range(len(transposed)):
        for row in range (len(inputMatrix)):
            transposed[col].append(inputMatrix[row][col])

    return transposed

#myMatrix = input("Enter any 2d matrix:")
myMatrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(">>>Here's the transposed matrix:",transposer(myMatrix))
