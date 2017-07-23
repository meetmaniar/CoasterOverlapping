from decimal import Decimal
from scratch import *
import math

def f(a):
        a = Decimal(a)
        return a-scratch_sine(a)-(pi/2)
    
a=bisection(f,1,3)
print(a)