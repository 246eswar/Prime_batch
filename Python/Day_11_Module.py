#modules are collection of functions and classes
#1. buildin module
#2. Third party modules
#num files, pandas for better way of structure of data
#alias names
#package is a collection of modules

#import can be done in module,function or package

import math
print(math.sqrt(16))

def greet(name):
    return f"Hello, {name}"
print(greet("meenu"))

from math import pi,sqrt
#if perticular operation only need
print(sqrt(16))

import math as o
print(o.sqrt(16))
#2. pip install then do works
#3. two different files one file is created and import to another
'''in third import with file name
import math (in place of math file name)'''
