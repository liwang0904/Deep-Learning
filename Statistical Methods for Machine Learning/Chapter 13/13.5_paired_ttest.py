from numpy.random import seed
from numpy.random import randn
from scipy.stats import ttest_rel

seed(1)

data1 = 5 * randn(100) + 50
data2 = 5 * randn(100) + 51

stat, p = ttest_rel(data1, data2)
# Statistics=-2.372, p=0.020
print('Statistics=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
# Different distributions (reject H0)
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')
