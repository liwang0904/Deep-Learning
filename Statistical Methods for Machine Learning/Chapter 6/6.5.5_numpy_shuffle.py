from numpy.random import seed
from numpy.random import shuffle

seed(1)

sequence = [i for i in range(20)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(sequence)

shuffle(sequence)
# [3, 16, 6, 10, 2, 14, 4, 17, 7, 1, 13, 0, 19, 18, 9, 15, 8, 12, 11, 5]
print(sequence)
