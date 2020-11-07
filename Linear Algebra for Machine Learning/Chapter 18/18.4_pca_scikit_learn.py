from numpy import array
from sklearn.decomposition import PCA

A = array([
	[1, 2],
	[3, 4],
	[5, 6]])
# [[1 2]
#  [3 4]
#  [5 6]]
print(A)

pca = PCA(2)

pca.fit(A)

# [[ 0.70710678  0.70710678]
#  [ 0.70710678 -0.70710678]]
print(pca.components_)
# [8.00000000e+00 2.25080839e-33]
print(pca.explained_variance_)

B = pca.transform(A)
# [[-2.82842712e+00  2.22044605e-16]
#  [ 0.00000000e+00  0.00000000e+00]
#  [ 2.82842712e+00 -2.22044605e-16]]
print(B)
