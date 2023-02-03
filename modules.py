# Python Modules

# Piece of software that delivers some sort of functionality

import os       # os = operating system, this module allows us to interact with os
import math, datetime, sys    # can import multiple by using commas

working_directory = os.getcwd()
print(working_directory)

# Module is referencing a single file whereas Libraries refer to a range of folders

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.name())

print(math.remainder(1, 5))
print(datetime.date.today())   # date is a class, today is a method
print((sys.path))

# When building a program, it is really important to think about whether you need to create your own class/object
# or simply a function. You may not even need to make a function yourself if there is a module that does so
# already.

# Build in Functions

# print()
# len()
# type()