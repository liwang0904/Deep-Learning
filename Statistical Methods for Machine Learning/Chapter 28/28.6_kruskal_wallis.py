from numpy.random import seed
from numpy.random import rand
from scipy.stats import kruskal

seed(1)

data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)
data3 = 52 + (rand(100) * 10)

stat, p = kruskal(data1, data2, data3)
# Statistics=34.747, p=0.000
print('Statistics=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
# Different distributions (reject H0)
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')
