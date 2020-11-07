from numpy import array
from numpy.linalg import eig

A = array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]])

values, vectors = eig(A)

B = A.dot(vectors[:, 0])
# [ -3.73863537  -8.46653421 -13.19443305]
print(B)

C = vectors[:, 0] * values[0]
# [ -3.73863537  -8.46653421 -13.19443305]
print(C)
