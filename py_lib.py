# Python Libraries

# import random      # with this we would have to specify random.tool_to_use_from_lib

from random import random    # specify what part of the library we want

import math

print(random())  # prints random float, without having to specify library

numfloat = 23.66

print(math.ceil(numfloat))  # prints the closest largest whole number (rounds up)
print((math.floor(numfloat))) # prints the closest smallest whole number (rounds down)
print(math.pi) # prints the value of pi:  3.141592653589793
