from numpy.random import seed
from numpy.random import randn
from numpy import var

seed(1)

data = 5 * randn(10000) + 50

result = var(data)
# Variance: 24.939
print('Variance: %.3f' % result)
