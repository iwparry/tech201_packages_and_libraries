# Tech 201 Packages, Libraries and Modules

### What is a Module?
In Python a module is simple a file containing Python code that can be imported inside another program in Python.
We can consider a module to be a file that contains a set of functions that you want to include in your application.
```python
import module    # we use the keyword import to let Python know we wish to import a module  
import mod1, mod2, mod3    # can import multiple by using commas

module_function = module.module_method()
print(module_function)

def print_mod1_function():
    print(mod1.mod1_function())

def print_mod2_function():
    print(mod2.mod2_function())

print(mod3.mod3_function(arg)) # if the functions in modules require arguments they will still need to be provided
```
### What is a Library?
Module is referencing a single file whereas Libraries refer to a range of bundled files and folders.
Simply put Modules are just code you can use whilst Libraries are larger compilations of resources.
```python
from library import module # can specify modul, or use * to import everything contained in the library
# In the line above, from is the keyword we use when we wish to import something from a library
print(module())  # if we simple imported the library we would need to specify the library when making us of the module
```
### What are Packages?
A Python package usually consists of several modules.
A package is a hierarchical file directory structure that defines a single Python application environment that consist of modules and subpackages and so on.
Packages can also be found in Libraries.
```python

```

