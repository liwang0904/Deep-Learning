from numpy import array
from numpy import diag
from numpy import zeros
from scipy.linalg import svd

A = array([
	[1,2,3,4,5,6,7,8,9,10],
	[11,12,13,14,15,16,17,18,19,20],
	[21,22,23,24,25,26,27,28,29,30]])
# [[ 1  2  3  4  5  6  7  8  9 10]
#  [11 12 13 14 15 16 17 18 19 20]
#  [21 22 23 24 25 26 27 28 29 30]]
print(A)

U, s, VT = svd(A)

Sigma = zeros((A.shape[0], A.shape[1]))

Sigma[:A.shape[0], :A.shape[0]] = diag(s)

n_elements = 2
Sigma = Sigma[:, :n_elements]
VT = VT[:n_elements, :]

B = U.dot(Sigma.dot(VT))
# [[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
#  [11. 12. 13. 14. 15. 16. 17. 18. 19. 20.]
#  [21. 22. 23. 24. 25. 26. 27. 28. 29. 30.]]
print(B)

T = U.dot(Sigma)
# [[-18.52157747   6.47697214]
#  [-49.81310011   1.91182038]
#  [-81.10462276  -2.65333138]]
print(T)

T = A.dot(VT.T)
# [[-18.52157747   6.47697214]
#  [-49.81310011   1.91182038]
#  [-81.10462276  -2.65333138]]
print(T)
