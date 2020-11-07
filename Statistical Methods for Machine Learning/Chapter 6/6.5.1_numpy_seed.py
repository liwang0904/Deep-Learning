from numpy.random import seed
from numpy.random import rand

seed(1)

# [4.17022005e-01 7.20324493e-01 1.14374817e-04]
print(rand(3))

seed(1)

# [4.17022005e-01 7.20324493e-01 1.14374817e-04]
print(rand(3))
