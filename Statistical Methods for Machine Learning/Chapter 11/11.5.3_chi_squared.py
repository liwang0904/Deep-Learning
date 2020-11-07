from scipy.stats import chi2

p = 0.95
df = 10

value = chi2.ppf(p, df)
# 18.307038053275146
print(value)

p = chi2.cdf(value, df)
# 0.95
print(p)
