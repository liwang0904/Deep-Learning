from random import seed
from random import sample

seed(1)

sequence = [i for i in range(20)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(sequence)

subset = sample(sequence, 5)
# [4, 18, 2, 8, 3]
print(subset)
