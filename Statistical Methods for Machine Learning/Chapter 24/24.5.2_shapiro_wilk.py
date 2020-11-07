from numpy.random import seed
from numpy.random import randn
from scipy.stats import shapiro

seed(1)

data = 5 * randn(100) + 50

stat, p = shapiro(data)
# Statistics=0.992, p=0.822
print('Statistics=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
# Sample looks Gaussian (fail to reject H0)
if p > alpha:
	print('Sample looks Gaussian (fail to reject H0)')
else:
	print('Sample does not look Gaussian (reject H0)')
