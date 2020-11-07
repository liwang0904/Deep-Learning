from numpy.random import seed
from numpy.random import randn

seed(1)

values = randn(10)
# [ 1.62434536 -0.61175641 -0.52817175 -1.07296862  0.86540763 -2.3015387
#   1.74481176 -0.7612069   0.3190391  -0.24937038]
print(values)
