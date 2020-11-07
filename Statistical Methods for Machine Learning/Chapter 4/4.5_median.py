from numpy.random import seed
from numpy.random import randn
from numpy import median

seed(1)

data = 5 * randn(10000) + 50

result = median(data)
# Median: 50.042
print('Median: %.3f' % result)
