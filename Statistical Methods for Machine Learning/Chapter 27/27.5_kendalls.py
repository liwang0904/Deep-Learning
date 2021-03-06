from numpy.random import rand
from numpy.random import seed
from scipy.stats import kendalltau

seed(1)

data1 = rand(1000) * 20
data2 = data1 + (rand(1000) * 10)

coef, p = kendalltau(data1, data2)
# Kendall correlation coefficient: 0.709
print('Kendall correlation coefficient: %.3f' % coef)

alpha = 0.05
# Samples are correlated (reject H0) p=0.000
if p > alpha:
	print('Samples are uncorrelated (fail to reject H0) p=%.3f' % p)
else:
	print('Samples are correlated (reject H0) p=%.3f' % p)
