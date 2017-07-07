from decimal import *

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


print ("\t\t\t Plouff ")
for j in range(1,20):
    #print( j, " ", plouffBig(j))
    number=plouffBig(19)
    
print(number) 