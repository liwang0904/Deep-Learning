from numpy import array

data = array([11, 22, 33, 44, 55])

# IndexError: index 5 is out of bounds for axis 0 with size 5
print(data[5])
