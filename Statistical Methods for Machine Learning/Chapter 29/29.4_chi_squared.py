from scipy.stats import chi2_contingency
from scipy.stats import chi2

table = [	[10, 20, 30],
			[6,  9,  17]]
# [[10, 20, 30], [6, 9, 17]]
print(table)
stat, p, dof, expected = chi2_contingency(table)
# dof=2
print('dof=%d' % dof)
# [[10.43478261 18.91304348 30.65217391]
#  [ 5.56521739 10.08695652 16.34782609]]
print(expected)

prob = 0.95
critical = chi2.ppf(prob, dof)
# probability=0.950, critical=5.991, stat=0.272
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
# Independent (fail to reject H0)
if abs(stat) >= critical:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')

alpha = 1.0 - prob
# significance=0.050, p=0.873
print('significance=%.3f, p=%.3f' % (alpha, p))
# Independent (fail to reject H0)
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')
