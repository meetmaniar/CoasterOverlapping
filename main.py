from scratch import *

from xml.etree.ElementTree import *


def f(a):  # Initiating the function
    a = Decimal(a)
    return a - scratch_sine(a) - (pi / 2)


# pdb.set_trace()        #comment it out to debug
alpha = bisection(f, 0, 10)  # Calling the Bisection method from scratch
print(alpha)  # Displaying the value of alpha
radius = UserInput()  # Getting the radius from the user
length = 2 * radius * (1 - (scratch_cosine(alpha / 2)))  # Computing the length
print(length)  # Displaying the length

#######---CODE FOR XML-DTD---#######
root = Element('Output')
tree = ElementTree(root)
alphaValue = Element('Alpha')
root.append(alphaValue)
lengthValue = Element('Length')
root.append(lengthValue)
alphaValue.text = 'Value of Alpha is: ' + str(alpha) + 'Radians'
lengthValue.text = 'Value of length is : ' + str(length)
tree.write(open('output.xml', 'wb'))

#######---CODE FOR TEXT FILE---#######
file_open = open("output.txt", "a")
file_open.write(alphaValue.text)
file_open.write("\n")
file_open.write(lengthValue.text)
