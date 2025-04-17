# to use random module we have to import random module

import my_module
print(my_module.pi)

#  randint will return random integer
import random

random_integer = random.randint(1,10)
print(random_integer)

# random no btw o and 1 ie float it will be give to 1 but not 1 ie upto 0.9999
random_float = random.random()
print(random_float)

# random no between 5 and float
random_integer5 = random.randint(5,10)
random_fint = random_integer5 + random_float
print(random_fint)

# or 

randomFloat = random.random() * 5
print(random_float)


