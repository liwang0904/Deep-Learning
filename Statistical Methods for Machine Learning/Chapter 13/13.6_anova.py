from numpy.random import seed
from numpy.random import randn
from scipy.stats import f_oneway

seed(1)

data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 50
data3 = 5 * randn(100) + 52

stat, p = f_oneway(data1, data2, data3)
# Statistics=3.655, p=0.027
print('Statistics=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
# Different distributions (reject H0)
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')
