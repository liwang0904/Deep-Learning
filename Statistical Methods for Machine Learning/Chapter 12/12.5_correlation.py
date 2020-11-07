from numpy.random import randn
from numpy.random import seed
from scipy.stats import pearsonr

seed(1)

data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

corr, p = pearsonr(data1, data2)

# Pearsons correlation: 0.888
print('Pearsons correlation: %.3f' % corr)

alpha = 0.05
# Some correlation (reject H0)
if p > alpha:
	print('No correlation (fail to reject H0)')
else:
	print('Some correlation (reject H0)')
