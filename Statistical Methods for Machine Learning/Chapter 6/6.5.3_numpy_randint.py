from numpy.random import seed
from numpy.random import randint

seed(1)

values = randint(0, 10, 20)
# [5 8 9 5 0 0 1 7 6 9 2 4 5 2 4 2 4 7 7 9]
print(values)
