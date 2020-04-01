from random import shuffle

numbers = list(range(0, 101))
shuffle(numbers)
print(*numbers[:3])