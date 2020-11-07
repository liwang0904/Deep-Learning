from statsmodels.stats.proportion import proportion_confint

lower, upper = proportion_confint(88, 100, 0.05)
# lower=0.816, upper=0.944
print('lower=%.3f, upper=%.3f' % (lower, upper))
