from numpy.random import seed
from numpy.random import randint
from numpy import mean

seed(1)

rolls = randint(1, 7, 50)
# [6 4 5 1 2 4 6 1 1 2 5 6 5 2 3 5 6 3 5 4 5 3 5 6 3 5 2 2 1 6 2 2 6 2 2 1 5
#  2 1 1 6 4 3 2 1 4 6 2 2 4]
print(rolls)
# 3.44
print(mean(rolls))
