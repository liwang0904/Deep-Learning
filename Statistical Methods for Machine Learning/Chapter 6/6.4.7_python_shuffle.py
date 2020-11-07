from random import seed
from random import shuffle

seed(1)

sequence = [i for i in range(20)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(sequence)

shuffle(sequence)
# [11, 5, 17, 19, 9, 0, 16, 1, 15, 6, 10, 13, 14, 12, 7, 3, 8, 2, 18, 4]
print(sequence)
