


'''
Created on Jul 22, 2017

@author: M_ANIAR

'''
from scratch import *

def f(a):
        a = Decimal(a)
        return a-scratch_sine(a)-(pi/2)
    

a=bisection(f,0,10)
print(a)
try:
    r=Decimal(input("Enter Radius: "))
    l=2*r*(1-(scratch_cosine(a/2)))
    print(l)
except ValueError:
    print("Invalid Input")
