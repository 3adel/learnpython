# Before we begin, let's load the libraries.
import numpy as np
import numpy.linalg as la
np.set_printoptions(suppress=True)

# Replace the ??? here with the probability of clicking a link to each website when leaving Website F (FaceSpace).
L = np.array([[0,   1/2, 1/3, 0, 0,   0 ],
              [1/3, 0,   0,   0, 1/2, 0 ],
              [1/3, 1/2, 0,   1, 0,   1/2 ],
              [1/3, 0,   1/3, 0, 1/2, 1/2 ],
              [0,   0,   0,   0, 0,   0 ],
              [0,   0,   1/3, 0, 0,   0 ]])


K = np.array([[0, 0, 0, 1],
              [1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0]])

KP = np.array([[.1, .1, .1, .7],
              [.7, .1, .1, .1],
              [.1, .7, .1, .1],
              [.1, .1, .7, .1]])

M4 = np.array([[0, 1, 0, 0],
              [1, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0]])

M4P = np.array([[0.1, .7, 0.1, 0.1],
              [.7, 0.1, 0.1, 0.1],
              [0.1, 0.1, 0.1, .7],
              [0.1, 0.1, .7, 0.1]])

def pageRank(linkMatrix, d) :
	n = linkMatrix.shape[0]
	M = d * linkMatrix + (1-d)/n * np.ones([n, n]) # np.ones() is the J matrix, with ones for each entry.

	r =100*np.ones(n)/n
	lastR = r
	r = M @ r

	i = 0
	while la.norm(lastR - r) > 0.01 :
		lastR = r
		r = M @ r
		i += 1
		print(i)

	return r




print(pageRank(M4P, 1))
