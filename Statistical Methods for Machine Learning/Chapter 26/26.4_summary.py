from numpy import percentile
from numpy.random import seed
from numpy.random import rand

seed(1)

data = rand(1000)

quartiles = percentile(data, [25, 50, 75])

data_min, data_max = data.min(), data.max()

# Min: 0.000
print('Min: %.3f' % data_min)
# Q1: 0.252
print('Q1: %.3f' % quartiles[0])
# Median: 0.508
print('Median: %.3f' % quartiles[1])
# Q3: 0.751
print('Q3: %.3f' % quartiles[2])
# Max: 0.997
print('Max: %.3f' % data_max)
