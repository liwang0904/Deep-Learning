from numpy.random import seed
from numpy.random import randn
from numpy import mean

seed(1)

data = 5 * randn(10000) + 50

result = mean(data)
# Mean: 50.049
print('Mean: %.3f' % result)
