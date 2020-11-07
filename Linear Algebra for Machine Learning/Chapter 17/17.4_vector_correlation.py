from numpy import array
from numpy import corrcoef

x = array([1,2,3,4,5,6,7,8,9])
# [1 2 3 4 5 6 7 8 9]
print(x)

y = array([9,8,7,6,5,4,3,2,1])
# [9 8 7 6 5 4 3 2 1]
print(y)

corr = corrcoef(x,y)[0,1]
# -1.0
print(corr)
