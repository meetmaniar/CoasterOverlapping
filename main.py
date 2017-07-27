'''
Created on Jul 10, 2017

@author: M_ANIAR

'''
from scratch import *

from xml.etree.ElementTree import *
def f(a):
        a = Decimal(a)
        return a-scratch_sine(a)-(pi/2)
    


alpha=bisection(f,0,10)
print(alpha)
radius=UserInput()

length=2*radius*(1-(scratch_cosine(alpha/2)))
print(length)
root=Element('Output')
tree=ElementTree(root)
alphaValue=Element('Alpha')
root.append(alphaValue)
lengthValue=Element('Length')
root.append(lengthValue)
alphaValue.text='Value of Alpha is: ' + str(alpha) + 'Radians'
lengthValue.text='Value of length is : ' + str(length)
tree.write(open('output.xml', 'wb'))
file_open=open("output.txt","a")
