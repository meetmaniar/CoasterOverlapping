'''
Created on Jul 10, 2017

@author: M_ANIAR
'''
from decimal import *
from future_builtins import *
import math



#Sets decimal to 50 digits of precision
getcontext().prec = 50

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def scratch_pi(n):   #plouffbig
    pi = Decimal(0)
    i = 0
    while i < n:
        pi += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
        i += 1
    return pi




for j in range(1,20):
    #print( j, " ", scratch_pi(j))
    pi=scratch_pi(19)
    




def scratch_sine(theta):
    x=theta
    m=0

    for k in range(0,10,1):
        y=((-1)**k)*(x**(1+2*k))/factorial(1+2*k)   #Taylor Expansion of Sine
        m+=y

    return Decimal(m)




def scratch_cosine(theta):
    x=theta
    m=0
    
    for k in range(0,10,1):
        y=((-1)**k)*(x**(2*k))/factorial(2*k)    #Taylor Expansion of Cosine
        m+=y
    return Decimal(m)

def checkSign(a, b):
        return a * b > 0

def bisection(function, negative, positive):
    

    assert not checkSign(function(negative), function(positive))

    for i in range(100):
        midpoint = (negative + positive) / 2.0
        if checkSign(function(negative), function(midpoint)):
            negative = midpoint
        else:
            positive = midpoint

    return midpoint
