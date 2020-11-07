from scipy.stats import t

p = 0.95
df = 10

value = t.ppf(p, df)
# 1.8124611228107335
print(value)

p = t.cdf(value, df)
# 0.949999999999923
print(p)
