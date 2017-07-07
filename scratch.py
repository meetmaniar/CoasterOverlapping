from decimal import *
from __builtin__ import input
import math

#Sets decimal to 25 digits of precision
getcontext().prec = 50

def factorial(n):
    if n<1:
        return 1
    else:
        return n * factorial(n-1)

def plouffBig(n): 
    pi = Decimal(0)
    i = 0
    while i < n:
        pi += (Decimal(1)/(16**i))*((Decimal(4)/(8*i+1))-(Decimal(2)/(8*i+4))-(Decimal(1)/(8*i+5))-(Decimal(1)/(8*i+6)))
        i += 1
    return pi



for j in range(1,20):
    #print( j, " ", plouffBig(j))
    pi=plouffBig(19)
    
print("Pi: ", pi)

a=input('Enter the value of Angle:-')
theta=a*pi/180

result1=math.sin(theta)
result2=math.cos(theta)
print(result1,result2)   # Just to compare the result with the scratch functions



def scratch_sine(theta):
    x=theta
    m=0

    for k in range(0,10,1):
        y=((-1)**k)*(x**(1+2*k))/factorial(1+2*k)   #Taylor Expansion of Sine
        m+=y

    return m

print("Sine of your angle is: ")
print(scratch_sine(theta))



def scratch_cosine(theta):
    x=theta
    m=0
    
    for k in range(0,10,1):
        y=((-1)**k)*(x**(2*k))/factorial(2*k)    #Taylor Expansion of Cosine
        m+=y
    return m

print("Cosine of your angle is: ")
print((scratch_cosine(theta)))
