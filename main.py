





'''
Created on Jul 10, 2017

@author: M_ANIAR

'''
from scratch import *

from xml.etree.ElementTree import *
def f(a):
        a = Decimal(a)
        return a-scratch_sine(a)-(pi/2)
    


a=bisection(f,0,10)
print(a)
try:
    r=Decimal(input("Enter Radius: "))
    if(r<0): 
        raise ValueError
    l=2*r*(1-(scratch_cosine(a/2)))
    print(l)
    root=Element('Output')
    tree=ElementTree(root)
    alphaValue=Element('Alpha')
    root.append(alphaValue)
    lengthValue=Element('Length')
    root.append(lengthValue)
    alphaValue.text='Value of Alpha is: ' + str(a) + 'Radians'
    lengthValue.text='Value of length is : ' + str(l)
    tree.write(open('pojectoutput.xml', 'wb'))
except ValueError:
    print("Invalid Input")

