import random

random_numbers = [random.randint(0,49) for x in range(0,20)]
print(random_numbers)

squares = [x * x for x in random_numbers]
print(squares)
