from numpy import array

data = array([[11, 22, 33],	[44, 55, 66], [77, 88, 99]])

split = 2
train, test = data[:split, :], data[split:, :]

# [[11 22 33]
#  [44 55 66]]
print(train)
# [[77 88 99]]
print(test)
