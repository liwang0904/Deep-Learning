from numpy.random import seed
from numpy.random import randn
from scipy.stats import normaltest

seed(1)

data = 5 * randn(100) + 50

stat, p = normaltest(data)
# Statistics=0.102, p=0.950
print('Statistics=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
# Sample looks Gaussian (fail to reject H0)
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')
