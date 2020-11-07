from random import seed
from random import randint

seed(1)

for _ in range(10):
	value = randint(0, 10)
    # 2
    # 9
    # 1
    # 4
    # 1
    # 7
    # 7
    # 7
    # 10
    # 6
	print(value)
