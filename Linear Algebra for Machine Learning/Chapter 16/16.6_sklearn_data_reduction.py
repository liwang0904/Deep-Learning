from numpy import array
from sklearn.decomposition import TruncatedSVD

A = array([
	[1,2,3,4,5,6,7,8,9,10],
	[11,12,13,14,15,16,17,18,19,20],
	[21,22,23,24,25,26,27,28,29,30]])
# [[ 1  2  3  4  5  6  7  8  9 10]
#  [11 12 13 14 15 16 17 18 19 20]
#  [21 22 23 24 25 26 27 28 29 30]]
print(A)

svd = TruncatedSVD(n_components=2)

svd.fit(A)

result = svd.transform(A)
# [[18.52157747  6.47697214]
#  [49.81310011  1.91182038]
#  [81.10462276 -2.65333138]]
print(result)
