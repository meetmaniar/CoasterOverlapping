from decimal import *
from builtins import *


# Sets decimal to 50 digits of precision
getcontext().prec = 50


def factorial(n):  # Function to find the factorial of a number
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)  # Calling the same function recursively


def scratch_pi(n):  # Bailey–Borwein–Plouffe formula to calculate Pi
    pi = Decimal(0)
    i = 0
    while i < n:
        pi += (Decimal(1) / (16**i)) * ((Decimal(4) / (8 * i + 1)) - (Decimal(2) /
                                                                      (8 * i + 4)) - (Decimal(1) / (8 * i + 5)) - (Decimal(1) / (8 * i + 6)))
        i += 1
    return pi


for j in range(1, 20):
    #print( j, " ", scratch_pi(j))
    pi = scratch_pi(19)


def scratch_sine(theta):  # computing Sine of the theta (in radians) from scratch
    x = theta
    m = 0

    for k in range(0, 10, 1):
        y = ((-1)**k) * (x**(1 + 2 * k)) / \
            factorial(1 + 2 * k)  # Taylor Expansion of Sine
        m += y

    return Decimal(m)  # Returning Sine of theta


def scratch_cosine(theta):  # computing Cosine of the theta (in radians) from scratch
    x = theta
    m = 0

    for k in range(0, 10, 1):
        # Taylor Expansion of Cosine
        y = ((-1)**k) * (x**(2 * k)) / factorial(2 * k)
        m += y
    return Decimal(m)  # Returning Cosine of theta


def checkSign(a, b):  # This function is to check weather the two numbers have the same polarity
    return a * b > 0


def bisection(function, negative, positive):
        # This function calculates the midpoint by performing number of iterations of getting the midpoints.
        # of the two numbers with when substituted in the function, returns opposite polarity.
    assert not checkSign(function(negative), function(positive))

    for i in range(100):  # For 100 iterations
        midpoint = (negative + positive) / 2.0  # Getting the midpoint
        if checkSign(function(negative), function(midpoint)):  # Checking the polarity
            negative = midpoint  # setting the arguments for next iterations.
        else:
            positive = midpoint  # setting the arguments for next iterations.

    return midpoint  # Returning the midpoint which is most precise answer.


def UserInput():  # function for getting input from the user.
    try:
        # Getting float input from the user
        r = Decimal(input("Enter Radius: "))
        if(r < 0):  # Filtering out the negative number by raising the exception
            raise Exception
        return Decimal(r)
    except Exception:  # Filtering the string and special characters out
        print("Invalid Input")
        UserInput()  # Recursively calling the same function
