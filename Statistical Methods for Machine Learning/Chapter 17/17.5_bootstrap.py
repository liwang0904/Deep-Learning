from sklearn.utils import resample

data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

boot = resample(data, replace=True, n_samples=4, random_state=1)
# Bootstrap Sample: [0.6, 0.4, 0.5, 0.1]
print('Bootstrap Sample: %s' % boot)

oob = [x for x in data if x not in boot]
# OOB Sample: [0.2, 0.3]
print('OOB Sample: %s' % oob)
