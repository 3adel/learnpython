import numpy as np

#solve the equation A x r = s
# r = [a,
# 	 b,
# 	 c]

A = [[4, 6, 2],
	 [3, 4, 1],
	 [2, 8, 13]]

#This represents t
s = [9,
	 7,
	 2]

Ainv = np.linalg.inv(A)
print(f"The inverse of\n{A}\nis\n{Ainv}")

Adet = np.linalg.det(A)
print(f"The determinant of\n{A}\nis\n{Adet}")


#now solve the equation

r = np.linalg.solve(A, s)
print(f"The solution of the equation is\n{r}")




