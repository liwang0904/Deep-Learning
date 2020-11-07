from numpy.random import seed
from numpy.random import rand

seed(1)

values = rand(10)
# [4.17022005e-01 7.20324493e-01 1.14374817e-04 3.02332573e-01
#  1.46755891e-01 9.23385948e-02 1.86260211e-01 3.45560727e-01
#  3.96767474e-01 5.38816734e-01]
print(values)
