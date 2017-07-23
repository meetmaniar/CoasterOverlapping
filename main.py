'''
Created on Jul 22, 2017

@author: M_ANIAR
'''
from scratch import *


def f(a):
        a = Decimal(a)
        return a-scratch_sine(a)-(pi/2)
    
a=bisection(f,1,3)
print(a)


