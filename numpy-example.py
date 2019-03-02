import numpy as np

A = [[1, 2, 3],
	 [4, 0, 6],
	 [7, 8, 9]]
Ainv = np.linalg.inv(A)
print(Ainv)